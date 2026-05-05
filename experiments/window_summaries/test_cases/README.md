# Test cases (held-out)

These 5 projects are a **held-out** test set used to evaluate the window/door
summarizer prompt.

**Important:** the prompt in `summarize_windows.py` must NOT be tuned against
the outputs in this folder. The prompt was iteratively refined against the
projects in `problem/`, and `test_cases/` exists to gauge generalisation.

## Projects

| Project | Plans XML | Final XML (renamed from) | JSON (renamed from) |
|---|---|---|---|
| Januarvænget 62, 6000 Kolding | `Januarvænget_62_6000_Kolding.xml` | `report_311896587.xml` | `rbr-model-complete (56).json` |
| Vandmøllevej 65, 8723 Løsning | `Vandmøllevej_65_8723_Løsning.xml` | `report_311896148.xml` | `rbr-model-complete (57).json` |
| Gyvelvænget 10, 8543 Hornslet | `Gyvelvænget_10_8543_Hornslet.xml` | `report_311896098.xml` | `rbr-model-complete (58).json` |
| Lokesvej 40, 8660 Skanderborg | `Lokesvej_40_8660_Skanderborg.xml` | `report_311896389.xml` | `rbr-model-complete (59).json` |
| Lamdrup Møllevej 2, 5854 Gislev | `Lamdrup_Møllevej_2_5854_Gislev.xml` | `report_311896047.xml` | `rbr-model-complete (60).json` |

## Re-running the test set

From `experiments/window_summaries/`:

```bash
ANTHROPIC_API_KEY=sk-... python3 summarize_windows.py \
  --xml-dir test_cases \
  --output-dir test_cases
```

Outputs written to this folder:

- `window_summaries_output.json` — raw extraction + LLM summaries
- `window_summaries_report.md` — per-project, per-classification summaries
- `window_summaries_comparison.md` — 3-column comparison: PDFReportData vs Generated vs Individual Entries
