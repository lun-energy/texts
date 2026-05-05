"""
Comments Section Analysis: Plans XML vs Final XML

For each of the 10 projects in problem/, this script:
  1. Extracts <Comments> sub-fields from the Plans XML (boilerplate template
     with XXX placeholders and consultant instructions).
  2. Extracts the same fields from the Final XML (consultant-edited output).
  3. Diffs them line-by-line to isolate the consultant's edits.
  4. Pulls "structured facts" from the Plans XML (BBR, Zone) and the JSON
     room-by-room model (stories, rooms, heat source) that *could* be used
     to auto-populate parts of the consultant text.
  5. For each consultant-added phrase that mentions a measurement, year,
     building type, room name, or heat source, classifies whether the
     value is present in the structured data.
  6. Writes a markdown report to comments_analysis.md.

Output: experiments/comments_analysis/comments_analysis.md (+ .json dump)

Run from any cwd:
    python3 experiments/comments_analysis/analyze_comments.py
"""

from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from html import escape as html_escape
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple


# --- Constants ---------------------------------------------------------------

# This script now lives inside `problem/comments_analysis/`, so the
# project XML/JSON files are in the parent directory.
PROBLEM_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = PROBLEM_DIR.parent
OUTPUT_DIR = Path(__file__).resolve().parent

NS = "{http://www.ens.dk/EnergyLabel}"
NS_GLOBALS = "{http://www.ens.dk/Globals}"
NS_BU = "{http://www.ens.dk/BuildingUnits}"

COMMENT_FIELDS = [
    "Additional",
    "OnEnergyPrices",
    "OnBuildingDescription",
    "OnDestructiveInspections",
]

# Translation of BuildingType code -> Danish phrase commonly seen in comments.
BUILDING_TYPE_DA = {
    "DetachedBuilding": "fritliggende enfamilieshus",
    "TerracedHouse": "rækkehus",
    "SemiDetachedHouse": "dobbelthus",
    "ApartmentBuilding": "etagebolig",
    "Farm": "stuehus til landbrugsejendom",
    "FarmHouse": "stuehus",
}

STORY_TYPE_DA = {
    "ground": "stueetage",
    "first": "1. sal",
    "second": "2. sal",
    "third": "3. sal",
    "loft": "tagetage",
    "attic": "tagetage",
    "basement": "kælder",
    "halfbasement": "halvkælder",
}

# JSON heating source type (camelCase) -> Danish term used in PDF text.
HEAT_SOURCE_DA = {
    "districtHeating": "Fjernvarme",
    "naturalGas": "Naturgas",
    "oil": "Olie",
    "woodPellets": "Træpiller",
    "wood": "Brænde",
    "heatPump": "Varmepumpe",
    "airHeatPump": "Varmepumpe",
    "groundHeatPump": "Jordvarmepumpe",
    "electric": "Elvarme",
    "electricity": "Elvarme",
    "biofuel": "Biobrændsel",
    "strawBurner": "Halmfyr",
}

# JSON home.latestSnapshot.building.buildingType -> Danish phrase.
JSON_BUILDING_TYPE_DA = {
    "detachedHouse": "fritliggende enfamilieshus",
    "terracedHouse": "rækkehus",
    "semiDetachedHouse": "dobbelthus",
    "apartmentBuilding": "etagebolig",
    "farmHouse": "stuehus",
    "summerHouse": "sommerhus",
}


# --- Data containers ---------------------------------------------------------

@dataclass
class CommentsBlock:
    additional: str = ""
    on_energy_prices: str = ""
    on_building_description: str = ""
    on_destructive_inspections: str = ""

    def get(self, field_name: str) -> str:
        return {
            "Additional": self.additional,
            "OnEnergyPrices": self.on_energy_prices,
            "OnBuildingDescription": self.on_building_description,
            "OnDestructiveInspections": self.on_destructive_inspections,
        }[field_name]


@dataclass
class StructuredFacts:
    """Facts pulled from Plans XML / JSON that could populate comments text.
    
    Final XML is NOT a valid source: it is the consultant's output, so using
    it would be circular reasoning for an auto-population analysis.
    """
    # From Plans XML <Building><BBR>
    year_of_construction: Optional[str] = None
    year_of_renovation: Optional[str] = None
    dwelling_area: Optional[str] = None
    commercial_area: Optional[str] = None
    use_code: Optional[str] = None

    # From Plans XML <Zone>
    building_type: Optional[str] = None
    building_type_da: Optional[str] = None
    floor_count: Optional[str] = None
    housing_units: Optional[str] = None

    # From JSON home.latestSnapshot.building - rich building-level facts
    # that include the area fields the consultant typically writes.
    json_constructed_year: Optional[str] = None
    json_renovated_year: Optional[str] = None
    json_dwelling_area: Optional[str] = None
    json_heated_area: Optional[str] = None  # totalAreaSquareMeters / heatedAreaSquareMeters
    json_roof_stories_area: Optional[str] = None  # "udnyttet tagetage" m²
    json_regular_stories_area: Optional[str] = None
    json_basement_area: Optional[str] = None
    json_number_of_stories: Optional[str] = None
    json_building_type: Optional[str] = None  # "detachedHouse", etc.
    json_building_type_da: Optional[str] = None  # "fritliggende enfamilieshus"
    json_story_types: List[str] = field(default_factory=list)  # ["ground", "first", ...]

    # From JSON heating
    heat_source_raw: Optional[str] = None  # e.g. "districtHeating"
    heat_source_da: Optional[str] = None  # e.g. "Fjernvarme"

    # From JSON room-level walks
    json_stories_localised: List[str] = field(default_factory=list)
    json_room_count: int = 0
    json_room_types: List[str] = field(default_factory=list)
    json_has_loft: bool = False
    json_has_basement: bool = False
    json_has_garage: bool = False
    json_has_workshop: bool = False  # "værksted"


# --- XML parsing -------------------------------------------------------------

def _strip_ns(tag: str) -> str:
    if tag.startswith("{"):
        return tag.split("}", 1)[1]
    return tag


def _iter_local(root, localname: str):
    """Yield elements whose local-name equals `localname`, regardless of XML
    namespace. Plans XML uses `InputData` namespace while Final XML uses
    `EnergyLabel` namespace, so namespace-agnostic search keeps us robust."""
    for el in root.iter():
        if _strip_ns(el.tag) == localname:
            yield el


def parse_comments_block(xml_path: Path) -> CommentsBlock:
    """Extract the four <Comments> sub-fields from an EnergyLabel XML.

    The Plans XML places Comments under EnergyLabel/InputData/Label/Comments
    (InputData namespace). The Final XML places it under EnergyLabel/Comments
    (EnergyLabel namespace). We pick the first <Comments> element that
    actually contains the expected sub-fields.
    """
    block = CommentsBlock()
    try:
        tree = ET.parse(xml_path)
    except ET.ParseError as exc:
        print(f"  ⚠ Failed to parse {xml_path.name}: {exc}")
        return block

    root = tree.getroot()
    for comments in _iter_local(root, "Comments"):
        child_names = {_strip_ns(c.tag) for c in comments}
        if not child_names & set(COMMENT_FIELDS):
            continue
        for sub in comments:
            name = _strip_ns(sub.tag)
            text = (sub.text or "").strip()
            if name == "Additional":
                block.additional = text
            elif name == "OnEnergyPrices":
                block.on_energy_prices = text
            elif name == "OnBuildingDescription":
                block.on_building_description = text
            elif name == "OnDestructiveInspections":
                block.on_destructive_inspections = text
        break
    return block


def extract_structured_facts(plans_xml: Path,
                             json_path: Optional[Path]) -> StructuredFacts:
    """Pull structured facts from Plans XML and JSON only.
    
    The Final XML is intentionally NOT consulted: it is the consultant's
    output, so any field present only in Final cannot count as
    auto-populatable.
    """
    facts = StructuredFacts()

    # --- Plans XML: BBR + Zone (namespace-agnostic)
    if plans_xml.exists():
        try:
            tree = ET.parse(plans_xml)
            root = tree.getroot()
        except ET.ParseError:
            root = None
        if root is not None:
            for bbr in _iter_local(root, "BBR"):
                child_names = {_strip_ns(c.tag) for c in bbr}
                if not child_names & {
                    "YearOfConstruction", "DwellingArea", "UseCode",
                }:
                    continue
                for child in bbr:
                    name = _strip_ns(child.tag)
                    value = (child.text or "").strip()
                    if name == "YearOfConstruction" and value:
                        facts.year_of_construction = facts.year_of_construction or value
                    elif name == "YearOfRenovation" and value:
                        facts.year_of_renovation = facts.year_of_renovation or value
                    elif name == "DwellingArea" and value:
                        facts.dwelling_area = facts.dwelling_area or value
                    elif name == "CommercialArea" and value:
                        facts.commercial_area = facts.commercial_area or value
                    elif name == "UseCode" and value:
                        facts.use_code = facts.use_code or value
                break

            for zone in _iter_local(root, "Zone"):
                child_names = {_strip_ns(c.tag) for c in zone}
                if not child_names & {"BuildingType", "Usage", "FloorCount"}:
                    continue
                for child in zone:
                    name = _strip_ns(child.tag)
                    value = (child.text or "").strip()
                    if name == "BuildingType" and value and not facts.building_type:
                        facts.building_type = value
                        facts.building_type_da = BUILDING_TYPE_DA.get(value, value)
                    elif name == "FloorCount" and value:
                        facts.floor_count = facts.floor_count or value
                    elif name == "HousingUnits" and value:
                        facts.housing_units = facts.housing_units or value
                break

    # --- JSON: building, heating, stories, rooms
    if json_path and json_path.exists():
        try:
            data = json.loads(json_path.read_text(encoding="utf-8"))
        except Exception:
            data = None
        if isinstance(data, dict):
            home = (data.get("roomByRoomModel") or {}).get("home") or {}
            snapshot = home.get("latestSnapshot") or {}

            # Building-level facts (constructedYear, areas, type, ...)
            building = snapshot.get("building") or {}
            if building:
                if building.get("constructedYear"):
                    facts.json_constructed_year = str(building["constructedYear"])
                if building.get("renovatedYear"):
                    facts.json_renovated_year = str(building["renovatedYear"])
                if building.get("dwellingAreaSquareMeters") is not None:
                    facts.json_dwelling_area = str(building["dwellingAreaSquareMeters"])
                # Both totalAreaSquareMeters and heatedAreaSquareMeters tend
                # to be set; use heated if present, fall back to total.
                heated = building.get("heatedAreaSquareMeters")
                if heated is None:
                    heated = building.get("totalAreaSquareMeters")
                if heated is not None:
                    facts.json_heated_area = str(heated)
                if building.get("roofStoriesAreaSquareMeters") is not None:
                    facts.json_roof_stories_area = str(building["roofStoriesAreaSquareMeters"])
                if building.get("regularStoriesAreaSquareMeters") is not None:
                    facts.json_regular_stories_area = str(building["regularStoriesAreaSquareMeters"])
                if building.get("basementAreaSquareMeters") is not None:
                    facts.json_basement_area = str(building["basementAreaSquareMeters"])
                if building.get("numberOfStories") is not None:
                    facts.json_number_of_stories = str(building["numberOfStories"])
                btype = building.get("buildingType") or ""
                if btype:
                    facts.json_building_type = btype
                    facts.json_building_type_da = JSON_BUILDING_TYPE_DA.get(btype, btype)
                story_types = building.get("storyTypes") or []
                if isinstance(story_types, list):
                    facts.json_story_types = [str(s) for s in story_types]
                    for st in story_types:
                        if st in ("loft", "attic"):
                            facts.json_has_loft = True
                        if st in ("basement", "halfbasement"):
                            facts.json_has_basement = True

            # Heat source (primary)
            heating = snapshot.get("heating") or {}
            primary = heating.get("primarySource") or {}
            stype = (primary.get("sourceType") or "").strip()
            if stype:
                facts.heat_source_raw = stype
                facts.heat_source_da = HEAT_SOURCE_DA.get(stype, stype)

            # Story / room walk (room-by-room model)
            for story in (snapshot.get("stories") or []):
                stype = (story.get("storyType") or story.get("type") or "").lower()
                if stype:
                    da = STORY_TYPE_DA.get(stype, stype)
                    facts.json_stories_localised.append(da)
                    if stype in ("loft", "attic"):
                        facts.json_has_loft = True
                    if stype in ("basement", "halfbasement"):
                        facts.json_has_basement = True
                for room in story.get("rooms") or []:
                    facts.json_room_count += 1
                    rtype = (room.get("roomType") or room.get("type") or "").lower()
                    rname = (room.get("roomName") or room.get("name") or "").lower()
                    if rtype:
                        facts.json_room_types.append(rtype)
                    if "garage" in rtype or "garage" in rname:
                        facts.json_has_garage = True
                    if "workshop" in rtype or "værksted" in rname or "værksted" in rtype:
                        facts.json_has_workshop = True

    return facts


# --- Diff utilities ----------------------------------------------------------

def _normalize_lines(text: str) -> List[str]:
    """Split into stripped non-empty lines for set-based diffing."""
    return [ln.strip() for ln in text.splitlines() if ln.strip()]


def diff_plans_vs_final(plans: str, final: str) -> Tuple[List[str], List[str]]:
    """Return (added_lines, removed_lines).

    added: lines in final but not in plans (consultant-added content)
    removed: lines in plans but not in final (boilerplate the consultant deleted)
    """
    plans_lines = _normalize_lines(plans)
    final_lines = _normalize_lines(final)
    plans_set = set(plans_lines)
    final_set = set(final_lines)
    added = [ln for ln in final_lines if ln not in plans_set]
    removed = [ln for ln in plans_lines if ln not in final_set]
    return added, removed


# --- Auto-populate scoring ---------------------------------------------------

YEAR_RE = re.compile(r"\b(1[89]\d{2}|20\d{2})\b")
AREA_RE = re.compile(r"(\d{1,4})\s*m\s*²")


def _to_float(value: Optional[str]) -> Optional[float]:
    if value is None or value == "":
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None
HEAT_KEYWORDS = [
    "fjernvarme", "naturgas", "olie", "træpiller", "varmepumpe",
    "elvarme", "biobrændsel", "halmfyr", "kondenserende",
]
BUILDING_TYPE_KEYWORDS = list(BUILDING_TYPE_DA.values()) + [
    "enfamilieshus", "rækkehus", "dobbelthus", "stuehus", "etagebolig",
    "fritliggende",
]
ROOM_KEYWORDS = [
    "kælder", "tagetage", "loft", "tagterrasse", "garage", "værksted",
    "carport", "udestue", "udhus", "anneks",
]


def classify_added_line(line: str, facts: StructuredFacts) -> Dict[str, object]:
    """For a consultant-added line, identify auto-populatable hooks.

    Returns a dict of hits, each with the category and a note about whether
    the value is present in `facts`.
    """
    line_l = line.lower()
    hits: List[Dict[str, str]] = []

    # Years — auto-populatable from Plans XML BBR or JSON building.
    for m in YEAR_RE.finditer(line):
        year = m.group(1)
        source = "?"
        present = False
        if year == facts.year_of_construction or year == facts.json_constructed_year:
            present = True
            source = "Plans BBR.YearOfConstruction / JSON building.constructedYear"
        elif year == facts.year_of_renovation or year == facts.json_renovated_year:
            present = True
            source = "Plans BBR.YearOfRenovation / JSON building.renovatedYear"
        hits.append({
            "category": "year",
            "value": year,
            "auto": "yes" if present else "no",
            "source": source,
        })

    # Areas — Plans XML BBR has DwellingArea/CommercialArea only; the JSON
    # building snapshot has heatedArea, roofStoriesArea, regularStoriesArea
    # and basementArea which cover the consultant's typical phrasing.
    for m in AREA_RE.finditer(line):
        area = m.group(1)
        candidates = [
            (facts.dwelling_area, "Plans BBR.DwellingArea"),
            (facts.commercial_area, "Plans BBR.CommercialArea"),
            (facts.json_dwelling_area, "JSON building.dwellingAreaSquareMeters"),
            (facts.json_heated_area, "JSON building.heatedAreaSquareMeters"),
            (facts.json_roof_stories_area, "JSON building.roofStoriesAreaSquareMeters"),
            (facts.json_regular_stories_area, "JSON building.regularStoriesAreaSquareMeters"),
            (facts.json_basement_area, "JSON building.basementAreaSquareMeters"),
        ]
        match_source = None
        for key, src in candidates:
            if key and area == str(key).split(".")[0]:  # tolerate "177.0"
                match_source = src
                break
        hits.append({
            "category": "area",
            "value": f"{area} m²",
            "auto": "yes" if match_source else "no",
            "source": match_source or "?",
        })

    # Building type
    for kw in BUILDING_TYPE_KEYWORDS:
        if kw and kw.lower() in line_l:
            present = False
            source = "?"
            if facts.building_type_da and kw.lower() in facts.building_type_da.lower():
                present = True
                source = "Plans Zone.BuildingType"
            elif facts.json_building_type_da and kw.lower() in facts.json_building_type_da.lower():
                present = True
                source = "JSON building.buildingType"
            hits.append({
                "category": "building_type",
                "value": kw,
                "auto": "yes" if present else "no",
                "source": source,
            })
            break

    # Heat source — derive from JSON heating.sources[].sourceType.
    for kw in HEAT_KEYWORDS:
        if kw in line_l:
            present = bool(
                facts.heat_source_da
                and kw in facts.heat_source_da.lower()
            )
            hits.append({
                "category": "heat_source",
                "value": kw,
                "auto": "yes" if present else "no",
                "source": "JSON.heating.primarySource.sourceType",
            })
            break

    # Rooms / story features — derive from JSON only.
    for kw in ROOM_KEYWORDS:
        if kw in line_l:
            present = False
            source = "?"
            roof_area = _to_float(facts.json_roof_stories_area)
            basement_area = _to_float(facts.json_basement_area)
            if kw in ("tagetage", "loft"):
                if facts.json_has_loft:
                    present = True
                    source = "JSON building.storyTypes (loft/attic)"
                elif roof_area and roof_area > 0:
                    present = True
                    source = "JSON building.roofStoriesAreaSquareMeters>0"
            elif kw == "kælder":
                if facts.json_has_basement:
                    present = True
                    source = "JSON building.storyTypes (basement)"
                elif basement_area and basement_area > 0:
                    present = True
                    source = "JSON building.basementAreaSquareMeters>0"
            elif kw == "garage" and facts.json_has_garage:
                present = True
                source = "JSON.rooms[garage]"
            elif kw == "værksted" and facts.json_has_workshop:
                present = True
                source = "JSON.rooms[workshop]"
            hits.append({
                "category": "room_feature",
                "value": kw,
                "auto": "yes" if present else "no",
                "source": source,
            })

    return {
        "line": line,
        "hits": hits,
    }


# --- Project iteration -------------------------------------------------------

def find_input_xml(project_name: str) -> Optional[Path]:
    candidates = [
        PROBLEM_DIR / f"{project_name}.xml",
        PROBLEM_DIR / f"{project_name} plans.xml",
    ]
    for path in candidates:
        if path.exists():
            return path
    return None


def find_json(project_name: str) -> Optional[Path]:
    path = PROBLEM_DIR / f"{project_name}.json"
    return path if path.exists() else None


def analyse_project(project_name: str,
                    plans_xml: Path,
                    final_xml: Path,
                    json_path: Optional[Path]) -> Dict:
    plans_comments = parse_comments_block(plans_xml)
    final_comments = parse_comments_block(final_xml)
    # Facts pulled from Plans XML + JSON only (Final XML is the consultant's
    # output, so it cannot count as an auto-populate source).
    facts = extract_structured_facts(plans_xml, json_path)

    fields_analysis = {}
    for fname in COMMENT_FIELDS:
        plans_text = plans_comments.get(fname)
        final_text = final_comments.get(fname)
        added, removed = diff_plans_vs_final(plans_text, final_text)
        classified = [classify_added_line(line, facts) for line in added]
        fields_analysis[fname] = {
            "plans_text": plans_text,
            "final_text": final_text,
            "plans_chars": len(plans_text),
            "final_chars": len(final_text),
            "added_lines": added,
            "removed_lines": removed,
            "classified_added_lines": classified,
        }

    return {
        "project": project_name,
        "plans_xml": plans_xml.name,
        "final_xml": final_xml.name,
        "json_path": json_path.name if json_path else None,
        "facts": facts.__dict__,
        "fields": fields_analysis,
    }


# --- Reporting ---------------------------------------------------------------

CATEGORY_LABEL = {
    "year": "Year",
    "area": "Area (m²)",
    "building_type": "Building type",
    "heat_source": "Heat source",
    "room_feature": "Room/story feature",
}


def _pct(num: int, denom: int) -> str:
    if denom <= 0:
        return "—"
    return f"{round(100 * num / denom)}%"


def render_facts_table(facts_dict: Dict) -> str:
    rows = []
    items = [
        ("Year of construction (Plans BBR)", "year_of_construction"),
        ("Year of construction (JSON)", "json_constructed_year"),
        ("Year of renovation (Plans BBR)", "year_of_renovation"),
        ("Year of renovation (JSON)", "json_renovated_year"),
        ("Dwelling area (Plans BBR)", "dwelling_area"),
        ("Dwelling area (JSON)", "json_dwelling_area"),
        ("Heated area (JSON)", "json_heated_area"),
        ("Roof stories area (JSON)", "json_roof_stories_area"),
        ("Regular stories area (JSON)", "json_regular_stories_area"),
        ("Basement area (JSON)", "json_basement_area"),
        ("Number of stories (JSON)", "json_number_of_stories"),
        ("Floor count (Plans Zone)", "floor_count"),
        ("Building type (Plans Zone)", "building_type_da"),
        ("Building type (JSON)", "json_building_type_da"),
        ("Heat source (JSON)", "heat_source_da"),
        ("Story types (JSON building)", "json_story_types"),
        ("Stories localised (JSON walk)", "json_stories_localised"),
        ("# rooms (JSON walk)", "json_room_count"),
        ("Has loft (JSON)", "json_has_loft"),
        ("Has basement (JSON)", "json_has_basement"),
        ("Has workshop (JSON)", "json_has_workshop"),
        ("Has garage (JSON)", "json_has_garage"),
    ]
    rows.append("| Fact | Value | Source |")
    rows.append("|---|---|---|")
    for label, key in items:
        value = facts_dict.get(key)
        if value in (None, "", [], 0, False):
            value_display = "_(missing)_"
        elif isinstance(value, list):
            value_display = ", ".join(str(v) for v in value) or "_(empty)_"
        else:
            value_display = str(value)
        rows.append(f"| {label} | {value_display} | {_fact_source(key)} |")
    return "\n".join(rows)


def _fact_source(key: str) -> str:
    return {
        "year_of_construction": "Plans XML BBR.YearOfConstruction",
        "year_of_renovation": "Plans XML BBR.YearOfRenovation",
        "dwelling_area": "Plans XML BBR.DwellingArea",
        "commercial_area": "Plans XML BBR.CommercialArea",
        "floor_count": "Plans XML Zone.FloorCount",
        "housing_units": "Plans XML Zone.HousingUnits",
        "building_type": "Plans XML Zone.BuildingType",
        "building_type_da": "Mapped from Plans Zone.BuildingType",
        "json_constructed_year": "JSON building.constructedYear",
        "json_renovated_year": "JSON building.renovatedYear",
        "json_dwelling_area": "JSON building.dwellingAreaSquareMeters",
        "json_heated_area": "JSON building.heatedAreaSquareMeters",
        "json_roof_stories_area": "JSON building.roofStoriesAreaSquareMeters",
        "json_regular_stories_area": "JSON building.regularStoriesAreaSquareMeters",
        "json_basement_area": "JSON building.basementAreaSquareMeters",
        "json_number_of_stories": "JSON building.numberOfStories",
        "json_building_type": "JSON building.buildingType",
        "json_building_type_da": "Mapped from JSON building.buildingType",
        "heat_source_raw": "JSON heating.primarySource.sourceType",
        "heat_source_da": "Mapped from JSON heat source",
        "json_story_types": "JSON building.storyTypes",
        "json_stories_localised": "JSON model.stories[].storyType",
        "json_room_count": "JSON model.stories[].rooms[]",
        "json_has_loft": "JSON building.storyTypes (loft/attic)",
        "json_has_basement": "JSON building.storyTypes (basement)",
        "json_has_workshop": "JSON rooms with workshop/værksted",
        "json_has_garage": "JSON rooms with garage",
    }.get(key, "?")


def render_classified_lines(lines: List[Dict]) -> str:
    if not lines:
        return "_(no consultant-added lines)_"
    out = []
    for entry in lines:
        line_text = entry["line"]
        hits = entry["hits"]
        if not hits:
            out.append(f"- {html_escape(line_text)}\n  - _no auto-populatable values detected_")
            continue
        bullets = []
        for hit in hits:
            mark = "✅" if hit["auto"] == "yes" else "❌"
            bullets.append(
                f"  - {mark} **{CATEGORY_LABEL.get(hit['category'], hit['category'])}**: "
                f"`{html_escape(str(hit['value']))}` "
                f"(source: `{html_escape(hit['source'])}`)"
            )
        out.append(f"- {html_escape(line_text)}\n" + "\n".join(bullets))
    return "\n".join(out)


def _normalize_phrase(line: str) -> str:
    """Normalize a phrase for repeat detection.
    
    Strategy: lowercase, collapse whitespace, mask things that vary by
    project (years, dates, area numbers, energy-label IDs) so that
    differing-only-in-numbers phrases are recognised as the same template.
    """
    s = line.strip().lower()
    # Mask 4-digit years and integer/decimal numbers (areas, IDs).
    s = re.sub(r"\b(1[89]\d{2}|20\d{2})\b", "<YEAR>", s)
    # Date forms like 22-03-16, 18-10-2007, 11. maj 2022, 22.03.2016.
    s = re.sub(
        r"\b\d{1,2}[-./\s][a-zæøå]{3,}[-./\s]\d{2,4}\b",
        "<DATE>",
        s,
    )
    s = re.sub(r"\b\d{1,2}[-./]\d{1,2}[-./]\d{2,4}\b", "<DATE>", s)
    # Energy label IDs (long digit strings) and similar.
    s = re.sub(r"\b\d{6,}\b", "<ID>", s)
    # Generic numbers (e.g. areas, counts).
    s = re.sub(r"\b\d+(?:[.,]\d+)?\b", "<NUM>", s)
    # Collapse whitespace.
    s = re.sub(r"\s+", " ", s).strip()
    return s


def find_repeated_phrases(results: List[Dict],
                          min_projects: int = 2) -> Dict[str, List[Dict]]:
    """Group consultant-added lines by normalized phrase, per field.
    
    Returns a dict keyed by Comments sub-field, each value is a list of
    {"normalized": ..., "examples": [...], "projects": [...], "count": N}
    sorted by count descending. Only phrases appearing in >= min_projects
    distinct projects are returned.
    """
    output: Dict[str, List[Dict]] = {}
    for fname in COMMENT_FIELDS:
        # Map normalized -> {"projects": set, "examples": list[(project, raw_line)], "auto_yes_count": int, "any_hit_count": int, "total": int}
        grouped: Dict[str, Dict] = {}
        for proj in results:
            project_name = proj["project"]
            for entry in proj["fields"][fname]["classified_added_lines"]:
                line = entry["line"]
                key = _normalize_phrase(line)
                if not key or key in {"<num>", "<year>", "<date>", "<id>"}:
                    continue
                bucket = grouped.setdefault(
                    key,
                    {
                        "projects": set(),
                        "examples": [],
                        "auto_yes_count": 0,
                        "any_hit_count": 0,
                        "total": 0,
                    },
                )
                bucket["projects"].add(project_name)
                bucket["examples"].append((project_name, line))
                bucket["total"] += 1
                if entry["hits"]:
                    bucket["any_hit_count"] += 1
                    if all(h["auto"] == "yes" for h in entry["hits"]):
                        bucket["auto_yes_count"] += 1
        items = []
        for key, bucket in grouped.items():
            if len(bucket["projects"]) >= min_projects:
                items.append({
                    "normalized": key,
                    "count": bucket["total"],
                    "project_count": len(bucket["projects"]),
                    "projects": sorted(bucket["projects"]),
                    "examples": bucket["examples"],
                    "auto_yes_count": bucket["auto_yes_count"],
                    "any_hit_count": bucket["any_hit_count"],
                })
        items.sort(key=lambda d: (-d["project_count"], -d["count"]))
        output[fname] = items
    return output


def aggregate_scoreboard(results: List[Dict]) -> Dict:
    totals = {
        "added_lines": 0,
        "lines_with_any_hit": 0,
        "hits_total": 0,
        "hits_auto_yes": 0,
        "by_category": {},
        "by_field": {},
    }
    for fname in COMMENT_FIELDS:
        totals["by_field"][fname] = {
            "added_lines": 0,
            "added_chars_total": 0,
            "removed_lines": 0,
            "hits_total": 0,
            "hits_auto_yes": 0,
            "projects_with_changes": 0,
        }
    for proj in results:
        for fname, fdata in proj["fields"].items():
            field_stats = totals["by_field"][fname]
            if fdata["added_lines"] or fdata["removed_lines"]:
                field_stats["projects_with_changes"] += 1
            field_stats["removed_lines"] += len(fdata["removed_lines"])
            for entry in fdata["classified_added_lines"]:
                totals["added_lines"] += 1
                field_stats["added_lines"] += 1
                field_stats["added_chars_total"] += len(entry["line"])
                hits = entry["hits"]
                if hits:
                    totals["lines_with_any_hit"] += 1
                for hit in hits:
                    totals["hits_total"] += 1
                    field_stats["hits_total"] += 1
                    if hit["auto"] == "yes":
                        totals["hits_auto_yes"] += 1
                        field_stats["hits_auto_yes"] += 1
                    cat = hit["category"]
                    cat_stats = totals["by_category"].setdefault(
                        cat, {"total": 0, "auto_yes": 0}
                    )
                    cat_stats["total"] += 1
                    if hit["auto"] == "yes":
                        cat_stats["auto_yes"] += 1
    return totals


def write_markdown_report(results: List[Dict], output_path: Path) -> None:
    lines = [
        "# Plans XML vs Final XML — Comments Section Analysis",
        "",
        "This report compares the four `<Comments>` sub-fields between each "
        "project's **Plans XML** (boilerplate template the consultant starts "
        "from) and its **Final XML** (after the consultant has filled it "
        "in). For every consultant-added line we look at whether its facts "
        "(years, areas, building type, heat source, room/story features) "
        "are already present in **upstream structured data** and could "
        "therefore be auto-populated.",
        "",
        "**Valid auto-populate sources** (upstream of the consultant):",
        "- **Plans XML** — `BBR.YearOfConstruction`, `BBR.YearOfRenovation`, "
        "  `BBR.DwellingArea`, `BBR.CommercialArea`, `Zone.BuildingType`, "
        "  `Zone.FloorCount`, `Zone.HousingUnits`",
        "- **JSON room-by-room model** — `heating.sources[].sourceType`, "
        "  `stories[].storyType`, `stories[].rooms[].roomType` / `roomName`",
        "",
        "Final XML is **not** used as a source: it is the consultant's "
        "output, so any field present only in Final cannot count as "
        "auto-populatable.",
        "",
        "**Comment fields analysed:**",
        "- `Additional` — general legal/explanatory text",
        "- `OnEnergyPrices` — text about energy price assumptions",
        "- `OnBuildingDescription` — building summary, areas, year, accessed rooms",
        "- `OnDestructiveInspections` — destructive inspection text",
        "",
        "**Legend for hits inside added lines:**",
        "- ✅ value present in Plans XML or JSON (auto-populatable today)",
        "- ❌ value detected but not found in upstream data (would need extra source or consultant input)",
        "",
        "---",
        "",
    ]

    scoreboard = aggregate_scoreboard(results)
    lines.extend([
        "## Aggregate scoreboard (10 projects)",
        "",
        f"- Consultant-added lines analysed: **{scoreboard['added_lines']}**",
        f"- Lines with at least one auto-populatable token: **{scoreboard['lines_with_any_hit']}**",
        f"- Tokens detected: **{scoreboard['hits_total']}**",
        f"- Tokens already covered by structured data: **{scoreboard['hits_auto_yes']}** "
        f"({_pct(scoreboard['hits_auto_yes'], scoreboard['hits_total'])})",
        "",
        "### Hits by category",
        "",
        "| Category | Detected | Auto-populatable | Coverage |",
        "|---|---|---|---|",
    ])
    for cat, stats in scoreboard["by_category"].items():
        lines.append(
            f"| {CATEGORY_LABEL.get(cat, cat)} "
            f"| {stats['total']} | {stats['auto_yes']} "
            f"| {_pct(stats['auto_yes'], stats['total'])} |"
        )
    lines.extend([
        "",
        "### Activity by Comments sub-field",
        "",
        "| Field | Projects with edits | Lines added | Lines removed | "
        "Tokens detected | Auto-populatable | Coverage |",
        "|---|---|---|---|---|---|---|",
    ])
    for fname in COMMENT_FIELDS:
        stats = scoreboard["by_field"][fname]
        lines.append(
            f"| `{fname}` | {stats['projects_with_changes']}/10 "
            f"| {stats['added_lines']} | {stats['removed_lines']} "
            f"| {stats['hits_total']} | {stats['hits_auto_yes']} "
            f"| {_pct(stats['hits_auto_yes'], stats['hits_total'])} |"
        )
    lines.extend([
        "",
        "### Takeaways",
        "",
        "- `OnBuildingDescription` is where the consultant cites the most "
        "facts. The JSON `home.latestSnapshot.building` block already "
        "contains **everything** that goes into the typical opening "
        "sentence — `constructedYear`, `renovatedYear`, "
        "`dwellingAreaSquareMeters`, `heatedAreaSquareMeters`, "
        "`roofStoriesAreaSquareMeters` (\"udnyttet tagetage\"), "
        "`regularStoriesAreaSquareMeters`, `basementAreaSquareMeters`, "
        "`buildingType`, `numberOfStories`, `storyTypes`. So the entire "
        "phrase *\"Bygningen er et fritliggende enfamilieshus med X m² "
        "udnyttet tagetage, opført i Y, med et opvarmet areal på Z m²\"* "
        "is **fully auto-populatable from JSON**.",
        "- `OnEnergyPrices` is dominated by heat-source mentions "
        "(`fjernvarme`, `træpiller`, …) which are derivable from "
        "`JSON.heating.primarySource.sourceType`. The specific supplier "
        "name (e.g. *\"Fjernvarme Fyn\"*) is NOT in our data and would "
        "need an external address-based lookup.",
        "- `Additional` edits are mostly **boilerplate placeholder "
        "removals** (`XXX`-cleanup) plus small free-text references to "
        "previous energy reports. Reference numbers and dates are not in "
        "upstream data, but the placeholder cleanup itself is "
        "deterministic.",
        "- `OnDestructiveInspections` is empty in every project.",
        "- Free-text room features (e.g. `tagterrasse`, `udestue`, "
        "`udhus`) are NOT consistently in the JSON model. JSON would "
        "need richer room-type metadata to cover those.",
        "- Several **standard phrases** are pasted verbatim across "
        "many projects (see _Repeated standard phrases_ section "
        "below). Promoting them to the Plans XML template — or at "
        "least to a pick-list — would remove the bulk of the "
        "consultant's manual editing in `Additional` and "
        "`OnBuildingDescription`.",
        "",
        "---",
        "",
    ])
    
    # --- Repeated/standard phrases used by the consultant ---
    repeats_by_field = find_repeated_phrases(results, min_projects=2)
    repeated_total_unique = sum(len(items) for items in repeats_by_field.values())
    repeated_total_lines = sum(
        item["count"]
        for items in repeats_by_field.values()
        for item in items
    )
    repeated_share = _pct(repeated_total_lines, scoreboard["added_lines"])

    lines.extend([
        "## Repeated standard phrases",
        "",
        f"**{repeated_total_unique} distinct phrases** are reused across "
        f"≥2 projects, accounting for **{repeated_total_lines} of "
        f"{scoreboard['added_lines']}** consultant-added lines "
        f"({repeated_share}). These are strong candidates for direct "
        "inclusion in the Plans XML boilerplate or a pick-list — the "
        "consultant is effectively copy-pasting them today.",
        "",
        "Numbers/years/dates are masked as `<NUM>`, `<YEAR>`, `<DATE>`, "
        "`<ID>` so that lines differing only in those values group "
        "together. Click each phrase to see the per-project raw text.",
        "",
    ])
    grand_total_repeats = 0
    for fname in COMMENT_FIELDS:
        items = repeats_by_field[fname]
        if not items:
            continue
        lines.append(f"### `{fname}`")
        lines.append("")
        lines.append(
            "| # projects | Total occurrences | Auto-populatable | "
            "Normalized phrase |"
        )
        lines.append("|---|---|---|---|")
        for item in items:
            grand_total_repeats += 1
            auto = (
                "✅ all" if item["auto_yes_count"] == item["count"]
                and item["count"] > 0 and item["any_hit_count"] > 0
                else (f"partial ({item['auto_yes_count']}/{item['count']})"
                      if item["any_hit_count"]
                      else "—")
            )
            short = item["normalized"]
            if len(short) > 200:
                short = short[:197] + "…"
            lines.append(
                f"| **{item['project_count']}/10** | {item['count']} "
                f"| {auto} | {html_escape(short)} |"
            )
        lines.append("")
        # Detailed expandable list with raw examples.
        for item in items:
            short = item["normalized"]
            if len(short) > 100:
                short = short[:97] + "…"
            lines.append(
                f"<details><summary><code>{html_escape(short)}</code> "
                f"— {item['project_count']} projects "
                f"({', '.join(item['projects'])})</summary>\n"
            )
            seen_lines = set()
            for proj_name, raw in item["examples"]:
                if raw in seen_lines:
                    continue
                seen_lines.add(raw)
                lines.append(
                    f"- _{html_escape(proj_name)}_: {html_escape(raw)}"
                )
            lines.append("\n</details>\n")
        lines.append("---\n")
    if grand_total_repeats == 0:
        lines.append("_No phrases repeat across ≥2 projects._\n\n---\n")

    for proj in results:
        lines.append(f"## {proj['project']}")
        lines.append("")
        lines.append(f"- Plans XML: `{proj['plans_xml']}`")
        lines.append(f"- Final XML: `{proj['final_xml']}`")
        lines.append(f"- JSON model: `{proj['json_path'] or 'n/a'}`")
        lines.append("")
        lines.append("### Structured facts")
        lines.append("")
        lines.append(render_facts_table(proj["facts"]))
        lines.append("")
        for fname in COMMENT_FIELDS:
            fdata = proj["fields"][fname]
            plans_chars = fdata["plans_chars"]
            final_chars = fdata["final_chars"]
            added_count = len(fdata["added_lines"])
            removed_count = len(fdata["removed_lines"])
            lines.append(
                f"### `{fname}` "
                f"(Plans: {plans_chars} chars → Final: {final_chars} chars · "
                f"+{added_count}/-{removed_count} lines)"
            )
            lines.append("")
            lines.append("**Consultant-added lines & auto-populate analysis:**")
            lines.append("")
            lines.append(render_classified_lines(fdata["classified_added_lines"]))
            lines.append("")
            if fdata["removed_lines"]:
                preview = fdata["removed_lines"][:4]
                lines.append(
                    "<details><summary>Lines removed from boilerplate "
                    f"({removed_count})</summary>\n"
                )
                for ln in preview:
                    lines.append(f"- {html_escape(ln)}")
                if removed_count > len(preview):
                    lines.append(f"- _(…{removed_count - len(preview)} more…)_")
                lines.append("\n</details>\n")
        lines.append("---\n")

    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"✓ Markdown report saved to: {output_path}")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    final_files = sorted(PROBLEM_DIR.glob("*final.xml"))
    print(f"Found {len(final_files)} projects with final XMLs.\n")

    results: List[Dict] = []
    for final in final_files:
        project_name = final.stem.replace(" final", "")
        plans = find_input_xml(project_name)
        if plans is None:
            print(f"  ⚠ No plans XML for {project_name}, skipping.")
            continue
        json_path = find_json(project_name)
        print(f"Analyzing: {project_name}")
        print(f"  Plans : {plans.name}")
        print(f"  Final : {final.name}")
        print(f"  JSON  : {json_path.name if json_path else '(none)'}")
        analysis = analyse_project(project_name, plans, final, json_path)
        results.append(analysis)
        print()

    json_out = OUTPUT_DIR / "comments_analysis.json"
    json_out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✓ Raw analysis saved to: {json_out}")
    write_markdown_report(results, OUTPUT_DIR / "comments_analysis.md")


if __name__ == "__main__":
    main()
