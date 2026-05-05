# Window Summary Prompt for LLM

## Recommended Prompt

```
You are analyzing window and door entries from an energy certificate XML file.

TASK: Create consolidated summary texts by grouping individual window/door entries by their BIClassification type.

INPUT FORMAT:
- Individual Status entries with Window BuildingUnit elements
- Each entry has: ShortText, LongText, Area, UValue, NumberOfWindows, Orientation, Inclination, glass type
- BIClassification codes like: 1-3-1-0 (windows), 1-3-2-0 (skylights), 1-3-3-0 (doors with glass)

OUTPUT FORMAT:
- One consolidated StatusText per BIClassification group
- Simple, descriptive Danish text
- Mention glass type (2-lag/3-lag energirude)
- Remove technical specifications (areas, U-values, orientations)
- Keep descriptions general and user-friendly

RULES:
1. Group all entries with the same BIClassification together
2. Write in present tense, factual style
3. Avoid listing individual measurements
4. Focus on what type of glazing is installed
5. If entries have different glass types within a group, mention both or use the predominant type

EXAMPLE:
Input: 6 window entries, all with "2 lags energirude med varm kant", U-value 1.4
Output: "Vinduerne er monteret med tolags energirude."

Now process the following window entries:
[paste your window Status entries here]
```

---

## Alternative: More Structured Prompt

```
Summarize these window entries for an energy certificate PDF report:

GROUPING CRITERIA:
- 1-3-1-0 = Standard windows → describe as "Vinduer"
- 1-3-2-0 = Skylights → describe as "Ovenlysvindue"
- 1-3-3-0 = Doors with glass → describe as "Terrassedør/Yderdør"

STYLE:
- Danish language
- 1-2 sentences per group
- Mention: window type + glass type (2-lag/3-lag energirude)
- Omit: measurements, U-values, orientations, counts

EXAMPLE OUTPUT:
"Vinduerne er monteret med tolags energirude."
"Ovenlysvindue er monteret med trelags energirude, efter BR15."
"Terrassedør og hoveddør med sideparti er monteret med tolags energiruder."

WINDOW ENTRIES TO SUMMARIZE:
[paste entries]
```

---

## BIClassification Reference

| Code | Type | Description |
|------|------|-------------|
| 1-3-1-0 | Standard Windows | Regular windows (Vinduer/Flerfagsvinduer) |
| 1-3-2-0 | Skylights | Roof windows (Ovenlysvindue) |
| 1-3-3-0 | Doors with Glass | Terrace/exterior doors with glazing (Terrassedør/Yderdør) |

---

## Usage Tips

1. **Provide examples** from existing PDFReportData
2. **Specify the language** (Danish for these energy certificates)
3. **Show the input format** clearly so the LLM knows what to expect
4. **Define grouping rules** explicitly (by BIClassification)
5. **Set constraints** (no technical specs, keep it simple)
6. **Include the actual window data** from the XML Status entries

---

## Expected Output Example

From 10 individual window entries → 3 grouped summaries:

**Text 1 (BIClassification 1-3-1-0):**
```
Vinduerne er monteret med tolags energirude.
```

**Text 2 (BIClassification 1-3-2-0):**
```
Ovenlysvindue er monteret med trelags energirude, efter BR15.
```

**Text 3 (BIClassification 1-3-3-0):**
```
Terrassedør og hoveddør med sideparti er monteret med tolags energiruder.
```

---

## Quality Checks

After generating summaries, verify:
- ✅ All window entries are covered in at least one group
- ✅ Glass type mentioned is accurate for the group
- ✅ No technical specifications (U-values, areas) included
- ✅ Text is in Danish and grammatically correct
- ✅ Style matches existing PDFReportData examples
- ⚠️ If mixed glass types in a group, ensure the most common or most accurate description is used
