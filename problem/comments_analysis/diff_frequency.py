"""
Comments diff frequency analysis.

For each of the 10 projects in `problem/`, compute the line-level diff
between the `<Comments>` block in the Plans XML (boilerplate template) and
the Final XML (consultant-edited output). Tally how often each individual
diff event (a single line added or removed) recurs across projects.

The output is sorted by frequency, so the dominant patterns surface
immediately:
  - lines the consultant *removes* in (almost) every project — i.e. dead
    boilerplate that should just be deleted from the template
  - lines the consultant *adds* in (almost) every project — i.e. canned
    phrases that should be promoted to the template / a pick-list

Output:
  problem/comments_analysis/diff_frequency.md (+ .json dump)

Run:
  python3 problem/comments_analysis/diff_frequency.py
"""

from __future__ import annotations

import json
from collections import defaultdict
from html import escape as html_escape
from pathlib import Path
from typing import Dict, List, Tuple

from analyze_comments import (
    COMMENT_FIELDS,
    PROBLEM_DIR,
    OUTPUT_DIR,
    _normalize_lines,
    _normalize_phrase,
    find_input_xml,
    parse_comments_block,
)


def _project_files() -> List[Tuple[str, Path, Path]]:
    triples: List[Tuple[str, Path, Path]] = []
    for final in sorted(PROBLEM_DIR.glob("*final.xml")):
        project_name = final.stem.replace(" final", "")
        plans = find_input_xml(project_name)
        if plans is None:
            continue
        triples.append((project_name, plans, final))
    return triples


def _diff_lines(plans: str, final: str) -> Tuple[List[str], List[str]]:
    plans_lines = _normalize_lines(plans)
    final_lines = _normalize_lines(final)
    plans_set = set(plans_lines)
    final_set = set(final_lines)
    removed = [ln for ln in plans_lines if ln not in final_set]
    added = [ln for ln in final_lines if ln not in plans_set]
    return removed, added


def _bucket(events: List[Tuple[str, str, str, str]]):
    """Group diff events by (field, action, normalized_line).
    
    events is a list of (project, field, action, raw_line)
    Returns: { (field, action, normalized): {projects: set, examples: list[(proj,raw)], count: int} }
    """
    buckets: Dict[Tuple[str, str, str], Dict] = defaultdict(
        lambda: {"projects": set(), "examples": [], "count": 0}
    )
    for project, field, action, raw in events:
        key = (field, action, _normalize_phrase(raw))
        if not key[2]:
            continue
        bucket = buckets[key]
        bucket["projects"].add(project)
        bucket["examples"].append((project, raw))
        bucket["count"] += 1
    return buckets


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    triples = _project_files()
    print(f"Found {len(triples)} projects.\n")

    events: List[Tuple[str, str, str, str]] = []
    per_project: Dict[str, Dict] = {}

    for project, plans, final in triples:
        plans_block = parse_comments_block(plans)
        final_block = parse_comments_block(final)
        proj_summary: Dict[str, Dict[str, List[str]]] = {}
        for fname in COMMENT_FIELDS:
            removed, added = _diff_lines(
                plans_block.get(fname), final_block.get(fname)
            )
            for ln in removed:
                events.append((project, fname, "removed", ln))
            for ln in added:
                events.append((project, fname, "added", ln))
            proj_summary[fname] = {"removed": removed, "added": added}
        per_project[project] = proj_summary

    buckets = _bucket(events)

    # Build per (field, action) frequency tables.
    grouped: Dict[Tuple[str, str], List[Dict]] = defaultdict(list)
    for (field, action, normalized), bucket in buckets.items():
        grouped[(field, action)].append({
            "normalized": normalized,
            "count": bucket["count"],
            "project_count": len(bucket["projects"]),
            "projects": sorted(bucket["projects"]),
            "examples": bucket["examples"],
        })
    for items in grouped.values():
        items.sort(key=lambda d: (-d["project_count"], -d["count"]))

    # --- Markdown report ---
    lines: List[str] = [
        "# Comments diff frequency",
        "",
        "Each row below is a single line that was either **removed from "
        "the boilerplate** or **added by the consultant** when comparing "
        "the Plans XML's `<Comments>` block to the Final XML's "
        "`<Comments>` block. Lines are grouped by their normalised text "
        "(years/numbers/dates/IDs masked as `<YEAR>`, `<NUM>`, `<DATE>`, "
        "`<ID>`) so near-duplicate edits collapse into a single entry.",
        "",
        "Sorted by **# projects** (highest reach first), then by total "
        "occurrences. Click a row to see the per-project raw text.",
        "",
        "**Reading guide:**",
        "- High-frequency `removed` rows = dead boilerplate / "
        "instructions the consultant always strips → delete from "
        "template.",
        "- High-frequency `added` rows = canned phrases the consultant "
        "always types → promote to template.",
        "",
        "---",
        "",
    ]

    # Aggregate scoreboard.
    total_events = len(events)
    total_unique = len(buckets)
    repeated_unique = sum(1 for b in buckets.values() if len(b["projects"]) >= 2)
    repeated_events = sum(b["count"] for b in buckets.values() if len(b["projects"]) >= 2)
    universal_unique = sum(1 for b in buckets.values() if len(b["projects"]) == len(triples))

    lines.extend([
        "## Aggregate",
        "",
        f"- Total diff events: **{total_events}** "
        f"(across {len(triples)} projects, 4 Comments sub-fields)",
        f"- Unique normalised diffs: **{total_unique}**",
        f"- Diffs that recur in ≥2 projects: **{repeated_unique}** "
        f"(covering **{repeated_events}** events, "
        f"{round(100 * repeated_events / total_events) if total_events else 0}% of all diffs)",
        f"- Diffs occurring in **all {len(triples)} projects**: "
        f"**{universal_unique}**",
        "",
        "---",
        "",
    ])

    for fname in COMMENT_FIELDS:
        for action in ("removed", "added"):
            items = grouped.get((fname, action), [])
            if not items:
                continue
            lines.append(f"## `{fname}` — {action}")
            lines.append("")
            lines.append(
                "| # projects | Total | Normalised line |"
            )
            lines.append("|---|---|---|")
            for item in items:
                short = item["normalized"]
                if len(short) > 220:
                    short = short[:217] + "…"
                lines.append(
                    f"| **{item['project_count']}/{len(triples)}** "
                    f"| {item['count']} | {html_escape(short)} |"
                )
            lines.append("")
            for item in items:
                short = item["normalized"]
                if len(short) > 100:
                    short = short[:97] + "…"
                lines.append(
                    f"<details><summary><code>{html_escape(short)}</code> "
                    f"— {item['project_count']}/{len(triples)} "
                    f"({', '.join(item['projects'])})</summary>\n"
                )
                seen_raw = set()
                for proj, raw in item["examples"]:
                    if raw in seen_raw:
                        continue
                    seen_raw.add(raw)
                    lines.append(
                        f"- _{html_escape(proj)}_: {html_escape(raw)}"
                    )
                lines.append("\n</details>\n")
            lines.append("---\n")

    md_path = OUTPUT_DIR / "diff_frequency.md"
    md_path.write_text("\n".join(lines), encoding="utf-8")

    # --- JSON dump (for tooling) ---
    json_dump = {
        "projects": [t[0] for t in triples],
        "summary": {
            "total_events": total_events,
            "total_unique": total_unique,
            "repeated_unique": repeated_unique,
            "repeated_events": repeated_events,
            "universal_unique": universal_unique,
        },
        "by_field_action": {
            f"{f}|{a}": [
                {
                    "normalized": item["normalized"],
                    "count": item["count"],
                    "project_count": item["project_count"],
                    "projects": item["projects"],
                    "examples": [
                        {"project": p, "raw": r} for p, r in item["examples"]
                    ],
                }
                for item in items
            ]
            for (f, a), items in grouped.items()
        },
    }
    json_path = OUTPUT_DIR / "diff_frequency.json"
    json_path.write_text(json.dumps(json_dump, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"✓ Markdown report saved to: {md_path}")
    print(f"✓ Raw frequency dump saved to: {json_path}")
    print()
    print(f"Diff events: {total_events} | unique: {total_unique} | "
          f"recurring: {repeated_unique} | universal: {universal_unique}")


if __name__ == "__main__":
    main()
