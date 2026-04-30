# Danish Energy Label XML Analysis

Analysis of transformation patterns between Plans (draft) and Energy10 (final) XML files for Danish energy labels.

## Overview

This analysis examined **10 properties** with **401 Status entries** and **163 BuildingReview blocks** to understand how data flows from the Plans software (consultant's draft) through Energy10 (final processing) to the BuildingReview (PDF report).

## Analysis Documents

### Problem Analysis (`problem/` folder)

1. **[ANALYSIS.md](problem/ANALYSIS.md)** — Main analysis document
   - 7 transformation patterns identified (Pattern 1-6 + Pattern 1b)
   - Detailed examples with XML snippets
   - BuildingReview generation algorithm
   - Placeholder resolution tracking
   - Window analysis deep-dive

2. **[ANALYSIS_BY_COMPONENT.md](problem/ANALYSIS_BY_COMPONENT.md)** — Component-focused analysis
   - Organized by building component (walls, windows, doors, floors, ceilings, technical systems)
   - Transformation profiles per component type
   - Concrete examples for each component
   - Pattern distribution by component

3. **[ANALYSIS_TRANSFORMATION_TABLE.md](problem/ANALYSIS_TRANSFORMATION_TABLE.md)** — Complete transformation tracking
   - **3-column table format**: BuildingReview | Plans Status | Energy10 Status
   - All 10 properties, all 163 BuildingReview entries
   - Fuzzy matching indicators (≥60% similarity)
   - BI reclassification tracking
   - Summary statistics and key insights

### Solution Recommendations (`solution/` folder)

4. **[RECOMMENDATIONS.md](solution/RECOMMENDATIONS.md)** — Top 3 most frequent problems (data-driven)
   - **#1:** Eliminate template placeholders (~50 per property, 15-20% time savings)
   - **#2:** Auto-generate window/door summaries (~12 groups per property, 25-30% time savings)
   - **#3:** Validate data sources (~8 corrections per property, 5-10% time savings)
   - **Ranking method:** Objective frequency analysis across 10 properties
   - **Combined impact:** 45-60% reduction in Energy10 editing time
   - Implementation roadmap (4 phases over 12 months)

5. **[PDF_VERIFICATION.md](solution/PDF_VERIFICATION.md)** — PDF vs XML validation
   - Confirms PDF energy certificates perfectly match XML PDFReportData/BuildingReview
   - Character-for-character verification across all 10 properties
   - Validates that our analysis captured the exact text end-users see
   - **Result:** 100% match rate (163 BuildingReview entries verified)

## Key Findings

### 7 Transformation Patterns

| Pattern | Description | Frequency |
|---------|-------------|-----------|
| **Pattern 1** | Unchanged (1:1 copy) | 10% |
| **Pattern 1b** | Property value update (data correction) | Variable |
| **Pattern 2** | Placeholder resolution | 15% |
| **Pattern 3** | N-to-1 deduplication | 7% |
| **Pattern 4** | Concatenation | 9% |
| **Pattern 5** | Inserted boilerplate | 47% |
| **Pattern 6** | Selective inclusion (consultant summary) | 7% |

### Component-Specific Insights

**Building Envelope (Walls, Windows, Doors, Floors, Ceilings):**
- Stable draft→final counts
- Patterns 1, 2, 3, 6 dominate
- Active consultant editing (especially windows/doors)
- Pattern 1b reveals data quality verification process

**Technical Systems (Heat, DHW, Ventilation, Solar):**
- Explosive growth (2-3x more entries in final)
- Pattern 5 (boilerplate insertion) dominates (47%)
- Energy10 auto-generates HB2023 compliance entries
- Minimal consultant editing

### Critical Discoveries

1. **Fuzzy matching essential** — 15% of matches have significantly edited ShortText
2. **Window summaries are manual** — Consultants write custom summaries for 84 window statuses
3. **Data source hierarchy matters** — Owner info → Technical drawings → Measured values
4. **BI reclassifications common** — Consultants review and correct element categorization
5. **Placeholders everywhere** — ~500 XXX/??? markers require manual resolution
6. **PDF matches XML perfectly** — BuildingReview content renders verbatim in PDF reports (100% verified)

## Data Sources

- **10 Danish properties** (residential buildings)
- **5 initial pairs** + **5 additional pairs** for validation
- **Plans software** (draft XML with placeholders, pretty-printed)
- **Energy10 software** (final XML with resolved data, minified)
- **BuildingReview** (PDF report section extracted from final XML)

## Methodology

1. **XML parsing** — ElementTree for structure analysis
2. **Fuzzy matching** — SequenceMatcher (≥60% threshold) for robust pairing
3. **Pattern classification** — Manual + algorithmic categorization
4. **Component grouping** — BI Classification-based organization
5. **Statistical analysis** — Frequency, distribution, and correlation analysis

## File Organization

```
/Users/ntindbaek/Cursor-repos/texts/
├── problem/
│   ├── ANALYSIS.md                           # Main pattern analysis
│   ├── ANALYSIS_BY_COMPONENT.md              # Component-focused view
│   ├── ANALYSIS_TRANSFORMATION_TABLE.md      # Complete transformation tracking
│   ├── *.xml                                  # 20 XML files (10 pairs)
│   └── *.pdf                                  # 10 PDF energy certificates
├── solution/
│   ├── RECOMMENDATIONS.md                     # Top 3 improvements
│   └── PDF_VERIFICATION.md                    # PDF vs XML validation
└── README.md                                  # This file
```

## Next Steps

1. **Review recommendations** — Prioritize implementation based on impact/effort
2. **Validate findings** — Test on additional property samples
3. **Implement Phase 1** — Quick wins (eliminate placeholders, add validation)
4. **Pilot Phase 2** — Template menu resolution in Plans UI
5. **Develop Phase 3** — Intelligent summary generation for windows/doors

---

**Analysis Date:** April 30, 2026  
**Data Quality:** ✓ All 10 properties successfully analyzed  
**Fuzzy Matching:** ✓ Enabled (≥60% similarity threshold)  
**Pattern Coverage:** ✓ 7 patterns identified and documented
