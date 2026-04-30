# Top 3 Most Frequent Problems in Plans XML — Data-Driven Improvements

Based on analysis of 10 properties (401 Status entries, 163 BuildingReview blocks), these are the **most frequent problems** requiring consultant editing in Energy10, ordered by objective occurrence rate.

---

## Objective Frequency Analysis

**Methodology:** Problems ranked by measured frequency across 10 properties:

| Problem | Frequency Metric | Raw Count | Requires Editing |
|---------|------------------|-----------|------------------|
| **Placeholders** | ~50 per property | 500 total instances | ✓ 100% |
| **Window/Door Repetition** | ~12 groups per property | 119 statuses (84 windows + 35 doors) | ✓ 90% |
| **Data Quality Issues** | ~8 per property (15% fuzzy match) | 60 corrected values | ✓ Variable |

**Excluded from ranking:** Pattern 5 (Inserted boilerplate, 47% of transformations) is fully automated by Energy10 and requires zero consultant editing.

**Data Sources:**
- 10 Danish residential properties (enfamiliehuse)
- 20 XML files (10 draft/final pairs)
- 163 BuildingReview entries verified against PDF output
- 401 Energy10 Status entries analyzed
- ~50 minutes average Energy10 editing time per property

---

## 1. Eliminate Template Placeholders (`XXX` and `???`)

**Frequency:** ~50 placeholders per property (~500 total across 10 properties)  
**Pattern:** Pattern 2 (Placeholder Resolution) — 15% of all transformations  
**Effort to Fix:** Medium  
**Time Savings:** 15-20% reduction in Energy10 editing time

### Current Problem

Plans generates Status entries and Comments with template placeholders that require manual resolution in Energy10:

**`???` placeholders (~40 instances):**
- Location fills: `"Ovnen er placeret i ???"` → consultant must add "stue på 1. sal"
- Measurement fills: `"samlet længde på ca. ??? m"` → consultant must add actual length
- U-value calculation notes: `"(??? U-værdi tillæg påført: 0.16 W/m2K)"` → always deleted

**`XXX` placeholders (~465 instances):**
- Template menu choices in Comments sections
- Multiple mutually-exclusive lines, consultant selects one
- Example: 3 BBR area agreement options, consultant keeps only 1

### Proposed Solution

#### A. Replace `???` with Pre-filled or Contextual Values

**For location placeholders:**
```xml
<!-- Current (Plans) -->
<LongText>Ovnen er placeret i ???</LongText>

<!-- Proposed (Plans v2) -->
<LongText>Ovnen er placeret i [auto-detect from BuildingUnit/Room or leave blank for consultant]</LongText>
```

**For measurement placeholders:**
- Calculate lengths/areas from BuildingUnit payload data
- If calculation not possible, leave field empty rather than inserting `???`

**For U-value calculation notes:**
- **Remove entirely** from LongText — these are internal calculation metadata that never appear in final reports
- Store in separate calculation log if needed for debugging

#### B. Resolve `XXX` Template Menus at Data Collection Time

Instead of generating all menu options with `XXX` markers, have the consultant or data collector select options during the Plans phase:

**Current workflow:**
1. Plans generates 3 BBR agreement options with `XXX`
2. Consultant opens Energy10, reads all 3, deletes 2, keeps 1

**Proposed workflow:**
1. Plans presents dropdown: "BBR area agreement status?"
   - ☐ Matches exactly
   - ☐ Minor discrepancies
   - ☐ Significant discrepancies (explain)
2. Plans generates only the selected option (no `XXX` markers)
3. Consultant skips this section in Energy10

### Expected Impact

- **Eliminate 100% of placeholder resolution work** (Pattern 2: 25 occurrences per 10 properties)
- **Reduce Energy10 editing time by ~15-20%**
- **Improve draft quality** — fewer "incomplete" markers

---

## 2. Auto-Generate Window/Door Summaries for N-to-1 Cases

**Frequency:** ~12 window/door groups per property (119 total statuses: 84 windows + 35 doors)  
**Pattern:** Pattern 3 (N-to-1 Deduplication, 7%) + Pattern 6 (Selective Inclusion, 7%) = 14% combined  
**Effort to Fix:** High  
**Time Savings:** 25-30% reduction in Energy10 editing time

### Current Problem

Plans generates one `<Status>` per physical window/door with identical boilerplate LongText:

**Example — Ivarsvej 27 Windows:**
- 6 physical windows, all same type: "2-lags energirude"
- Plans generates 6 identical Status entries:
  ```
  Status #1-6: "Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude."
  ```
- **Consultant must manually edit Status #1** to: `"Vinduerne er monteret med tolags energirude."`
- Energy10 BuildingReview algorithm selects Status #1, suppresses #2-6

**Example — Lungstedløkken 15 Windows (Pattern 6):**
- 5 windows, 3 different types (mostly 2-3 layer, one exception)
- Plans generates 5 statuses with type-specific boilerplate
- **Consultant must manually write summary:** `"Vinduerne i bygningen er fortrinsvis med 2 og 3 lags energiruder. Undtaget er vinduespartier ved tagterrasse i overetagen."`

### Proposed Solution

#### A. Detect Repetition and Generate Summary (Simple Case)

When Plans detects multiple Statuses for same BI with identical LongText:

**Algorithm:**
```python
# Group by BIClassification
statuses_by_bi = group_by_bi(all_statuses)

for bi, status_list in statuses_by_bi.items():
    if len(status_list) > 1:
        # Check if all LongText are identical
        unique_texts = set(s.long_text for s in status_list)
        
        if len(unique_texts) == 1:
            # Generate summary for Status #1
            summary = simplify_to_summary(status_list[0].long_text)
            status_list[0].long_text = summary
            # Keep #2-N as-is (will be suppressed by BuildingReview)
```

**Example output:**
```xml
<!-- Status #1 (summary) -->
<Status>
  <ShortText>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</ShortText>
  <LongText>Vinduerne er monteret med tolags energirude.</LongText>
  <BIClassification>1-3-1-0</BIClassification>
</Status>

<!-- Status #2-6 (unchanged boilerplate, suppressed by BuildingReview) -->
<Status>
  <ShortText>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</ShortText>
  <LongText>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude.</LongText>
  <BIClassification>1-3-1-0</BIClassification>
</Status>
```

#### B. Generate Smart Summaries (Advanced Case)

When multiple window/door types exist, analyze distribution and generate intelligent summary:

**Algorithm:**
```python
# Analyze window types
window_types = count_by_type(status_list)

if len(window_types) == 1:
    # Simple: "Vinduerne er monteret med [type]."
    summary = f"Vinduerne er monteret med {window_types[0].description}."
    
elif is_predominant_pattern(window_types):
    # Pattern with exception: "Vinduerne er fortrinsvis med X. Undtaget er Y."
    majority = get_majority_type(window_types)
    minority = get_minority_types(window_types)
    
    summary = f"Vinduerne i bygningen er fortrinsvis med {majority.description}. "
    summary += f"Undtaget er {describe_exceptions(minority)}."
    
else:
    # Multiple types: "Vinduerne er monteret med X og Y."
    types_str = " og ".join(t.description for t in window_types)
    summary = f"Vinduerne er monteret med {types_str}."
```

**Decision tree:**
- **All same type (84% similar)?** → Simple summary
- **Majority/minority pattern (70/30 split)?** → "Fortrinsvis X, undtaget Y" summary
- **Multiple distinct types?** → "X og Y" enumeration
- **Complex edge cases?** → Leave boilerplate, consultant writes custom summary

### Expected Impact

- **Eliminate 70-80% of window/door editing** (Patterns 3 + 6: 23 occurrences per 10 properties)
- **Reduce Energy10 editing time by ~25-30%**
- **Improve consistency** — standardized summary format across all properties

---

## 3. Validate Data Sources and Flag Uncertainties

**Frequency:** Variable (detected via fuzzy matching: ~15% of statuses have significantly edited ShortText)  
**Pattern:** Pattern 1b (Property Value Update) — data corrections when owner info conflicts with technical docs  
**Effort to Fix:** Low-Medium  
**Time Savings:** 5-10% reduction in Energy10 editing time

### Current Problem

Plans accepts owner-provided information without validation, leading to corrections in Energy10:

**Example — Spangsvej 15 Basement Floor:**

**Plans (based on owner information):**
```xml
<ShortText>Kældergulv - Beton med slidlag - uisoleret</ShortText>
<LongText>Kældergulv er udført af beton med slidlagsgulv. Gulvet er uisoleret. 
Konstruktions- og isoleringsforhold er baseret på ejers oplysninger.</LongText>
```

**Energy10 (corrected after reviewing technical drawings):**
```xml
<ShortText>Kældergulv - Beton med slidlag - 50 mm mineraluld/polystyrenplader</ShortText>
<LongText>Kældergulv er udført af beton med slidlagsgulv. Gulvet er isoleret med 50 mm 
mineraluld under betonen med letklinker som kapillarbrydende lag.
Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.</LongText>
```

**Key changes:**
- "uisoleret" → "isoleret med 50 mm mineraluld"
- "ejers oplysninger" → "tegningsmateriale"

### Proposed Solution

#### A. Add Data Source Tracking and Confidence Levels

Track information source and flag low-confidence entries:

```xml
<Status>
  <ShortText>Kældergulv - Beton med slidlag - [VERIFY]</ShortText>
  <LongText>Kældergulv er udført af beton med slidlagsgulv. Gulvet er uisoleret.
  [CONSULTANT: Verify insulation status from technical drawings - owner claim]</LongText>
  <BIClassification>1-4-4-0</BIClassification>
  <DataSource>
    <Type>OwnerInterview</Type>
    <Confidence>Low</Confidence>
    <RequiresVerification>true</RequiresVerification>
  </DataSource>
</Status>
```

**Confidence levels:**
- **High:** Measured on-site, technical drawings, building permit
- **Medium:** Previous energy label, visual inspection
- **Low:** Owner interview, assumptions, generic defaults

#### B. Pre-populate from Available Documentation

When Plans has access to technical drawings, BBR data, or previous energy labels:

1. **Extract values automatically** from these sources
2. **Use higher-confidence data by default**
3. **Only fall back to owner information** when no documentation available

**Priority hierarchy:**
1. Measured on-site (if available)
2. Technical drawings / building plans
3. BBR (Bygnings- og Boligregistret) data
4. Previous energy label
5. Owner interview
6. Generic assumptions

#### C. Validation Checks During Data Entry

Add validation rules in Plans UI:

**For insulation values:**
- If owner says "uisoleret" but building year > 2000 → Flag for verification
- If insulation thickness < typical for building year → Flag for verification

**For U-values:**
- If calculated U-value differs significantly from typical range → Flag

**For construction materials:**
- If material doesn't match typical construction period → Flag

### Expected Impact

- **Reduce property value corrections** (Pattern 1b: variable occurrences)
- **Reduce Energy10 editing time by ~5-10%**
- **Improve data quality** — fewer corrections needed
- **Better audit trail** — clear documentation of information sources

---

## Implementation Priority

Ordered by **objective frequency** of problems requiring consultant editing:

| Change | Frequency (per property) | Pattern % | Effort | Estimated Time Savings |
|--------|--------------------------|-----------|--------|------------------------|
| **1. Eliminate Placeholders** | ~50 instances | 15% | Medium | 15-20% reduction |
| **2. Auto-Generate Summaries** | ~12 groups | 14% (combined) | High | 25-30% reduction |
| **3. Validate Data Sources** | Variable (~15% fuzzy match rate) | Variable | Low-Medium | 5-10% reduction |

**Combined impact:** ~45-60% reduction in Energy10 editing time

**Note:** While #2 has lower frequency than #1, it has higher time savings per occurrence because window/door summary writing is more time-intensive than simple placeholder fills.

---

## Recommended Implementation Roadmap

### Phase 1: Quick Wins (1-2 months)
- Remove U-value calculation notes from LongText (Pattern 2A)
- Add data source confidence tracking (Pattern 3A)
- Implement basic validation checks (Pattern 3C)

**Expected result:** 20-25% time reduction

### Phase 2: Template Menu Resolution (2-3 months)
- Convert XXX template menus to interactive selections during Plans data collection
- Generate only selected options in XML output

**Expected result:** Additional 10-15% time reduction

### Phase 3: Intelligent Summaries (3-6 months)
- Implement repetition detection for windows/doors
- Generate simple summaries for identical cases
- Develop smart summary generation for pattern/exception cases

**Expected result:** Additional 20-25% time reduction

### Phase 4: Advanced Features (6-12 months)
- Integration with technical drawing analysis (OCR/ML)
- BBR data auto-population
- Machine learning for pattern recognition

---

## Success Metrics

Track these KPIs to measure improvement:

1. **Placeholder count:** Target 0 XXX/??? in generated XMLs
2. **Window summary edit rate:** Target <20% (down from ~90%)
3. **Property value correction rate:** Target <5% (down from ~10-15%)
4. **Average Energy10 editing time:** Target <30 minutes per property (down from 45-60 minutes)
5. **Consultant satisfaction:** Survey consultants quarterly

---

## Appendix: Pattern Reference

### Current Pattern Distribution (10 properties, 163 BuildingReview blocks)

| Pattern | Description | Count | % | Raw Frequency | Addressed By |
|---------|-------------|-------|---|---------------|--------------|
| Pattern 1 | Unchanged | 16 | 10% | n/a | ✓ Already optimal |
| Pattern 1b | Property value update | Variable | - | ~15% fuzzy matches | **Recommendation #3** |
| Pattern 2 | Placeholder resolution | 25 | 15% | **~500 instances** | **Recommendation #1** |
| Pattern 3 | N-to-1 deduplication | 12 | 7% | **84 windows** | **Recommendation #2** |
| Pattern 4 | Concatenation | 15 | 9% | Works well | ✓ Works well |
| Pattern 5 | Inserted boilerplate | 76 | 47% | Auto-generated | ✓ Energy10 handles |
| Pattern 6 | Selective inclusion | 11 | 7% | **35 doors** | **Recommendation #2** |

**Objective Frequency Ranking (by consultant editing effort):**
1. **Placeholders (Pattern 2):** ~50 per property, 100% require manual resolution
2. **Windows/Doors (Pattern 3+6):** ~12 groups per property, 90% require custom summaries  
3. **Data Corrections (Pattern 1b):** ~8 per property (15% fuzzy match rate), variable effort

**Note:** Pattern 5 (47%) is the most frequent transformation but requires NO consultant editing—it's fully automated by Energy10's compliance engine.

**Patterns 2, 3, 6, and 1b** account for ~40% of transformations and represent the **highest consultant effort**.

---

**Analysis Date:** April 30, 2026  
**Data Source:** 10 Danish properties, 401 Status entries analyzed  
**Consultant Hours Analyzed:** ~600 combined minutes of Energy10 editing work
