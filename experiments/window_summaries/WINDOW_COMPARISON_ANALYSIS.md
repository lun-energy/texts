# Window Entries Comparison: InputData vs PDFReportData
## Project: Ivarsvej 27, 5200 Odense V

---

## Summary of Findings

The **InputData** section contains 10 individual window/door entries with detailed technical specifications, while the **PDFReportData** section consolidates these into 3 grouped summary texts based on window classification types.

---

## Detailed Window Entries from InputData

### All Window/Door Entries (Status elements with Window BuildingUnit)

| Status ID | ShortText | LongText | Area (m²) | U-value | Num | Orientation | Inclination | Glass Type |
|-----------|-----------|----------|-----------|---------|-----|-------------|-------------|------------|
| 6 | Terrassedør med sideparti - 2 lags energirude med varm kant | Terrassedør og hoveddør med sideparti er monteret med tolags energiruder. | 2.05 | 1.3 | 1 | 3° | 90° | 2-lag |
| 7 | Yderdør med sideparti - 3 lags energirude - energiklasse B | Yderdør med sideparti, monteret med trelags energiruder, energiklasse B. | 1.96 | 1.15 | 1 | 273° | 90° | 3-lag |
| 8 | Flerfagsvindue med gående rammer - 2 lags energirude med varm kant | Vinduerne er monteret med tolags energirude. | 2.26 | 1.4 | 1 | 93° | 90° | 2-lag |
| 9 | Flerfagsvindue med gående rammer - 2 lags energirude med varm kant | Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | 4.58 | 1.4 | 1 | 183° | 90° | 2-lag |
| 10 | Flerfagsvindue med gående rammer - 2 lags energirude med varm kant | Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | 2.41 | 1.4 | 2 | 183° | 90° | 2-lag |
| 11 | Flerfagsvindue med gående rammer - 2 lags energirude med varm kant | Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | 1.17 | 1.4 | 2 | 3° | 90° | 2-lag |
| 12 | Ovenlysvindue - 3 lags energirude - efter BR15 | Ovenlysvindue er monteret med trelags energirude | 1.12 | 1.6 | 1 | 273° | 42° | 3-lag |
| 13 | Flerfagsvindue med gående rammer - 2 lags energirude med varm kant | Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | 1.54 | 1.4 | 1 | 3° | 90° | 2-lag |
| 14 | Ovenlysvindue - 3 lags energirude - efter BR15 | Ovenlysvindue er monteret med trelags energirude, efter BR15. | 1.12 | 1.6 | 1 | 93° | 50° | 3-lag |
| 15 | Flerfagsvindue med gående rammer - 2 lags energirude med varm kant | Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | 2.15 | 1.4 | 1 | 183° | 90° | 2-lag |

**Total Window/Door Count:** 10 entries  
**Total Window/Door Area:** 20.36 m²  
**Total Individual Units:** 13 (counting NumberOfWindows)

---

## Summary from PDFReportData BuildingReview

The PDFReportData consolidates the 10 individual window entries into **3 grouped text blocks** based on BIClassification:

### Text ID 3 - BIClassification: 1-3-1-0 (Standard Windows)
**StatusText:**
> "Vinduerne er monteret med tolags energirude."

**Covers InputData Status IDs:** 8, 9, 10, 11, 13, 15  
**Individual entries:** 6 window entries  
**Physical units:** 8 windows (counting NumberOfWindows field)  
**Combined area:** ~14.11 m²  
**Glass type:** 2-lag energirude  
**U-value:** 1.4  

---

### Text ID 4 - BIClassification: 1-3-2-0 (Skylights)
**StatusText:**
> "Ovenlysvindue er monteret med trelags energirude"

**Covers InputData Status IDs:** 12, 14  
**Individual entries:** 2 window entries  
**Physical units:** 2 skylights  
**Combined area:** ~2.24 m²  
**Glass type:** 3-lag energirude (BR15)  
**U-value:** 1.6  
**Inclination:** 42° and 50° (sloped roof windows)  

---

### Text ID 5 - BIClassification: 1-3-3-0 (Doors with Side Panels)
**StatusText:**
> "Terrassedør og hoveddør med sideparti er monteret med tolags energiruder."

**Covers InputData Status IDs:** 6, 7  
**Individual entries:** 2 door entries  
**Physical units:** 2 doors with side panels  
**Combined area:** ~4.01 m²  
**Glass types:** Mixed (one 2-lag, one 3-lag)  
**U-values:** 1.3 and 1.15  

**Note:** The PDFReportData text says "tolags energiruder" (2-layer), but Status ID 7 actually has 3-layer glass with U-value 1.15. This is a **minor inconsistency** in the summary text.

---

## Key Transformation Observations

### 1. **Grouping by BIClassification**
- InputData: 10 individual Status entries with complete technical specs
- PDFReportData: 3 Text entries grouped by window type classification
  - `1-3-1-0` = Standard windows
  - `1-3-2-0` = Skylights/roof windows
  - `1-3-3-0` = Doors with glazing

### 2. **Level of Detail**
- **InputData:** Full technical specifications including:
  - Exact area per entry
  - U-value
  - Number of windows
  - Orientation (degrees)
  - Inclination
  - Glass share percentage
  - Solar heat transmittance
  - Shade/shadow parameters
  
- **PDFReportData:** Simplified summaries with:
  - General descriptions only
  - Glass type (2-lag or 3-lag)
  - No numerical specifications
  - No orientation or inclination data

### 3. **Text Consolidation**
- Multiple similar windows (e.g., "Flerfagsvindue med gående rammer - 2 lags energirude") are consolidated into a single statement
- Orientation-specific differences are removed
- Individual areas are not summed or mentioned

### 4. **Purpose Difference**
- **InputData:** Technical calculation input for energy modeling
- **PDFReportData:** User-facing descriptive summary for PDF report

### 5. **Minor Inconsistency Found**
Text ID 5 states both doors have "tolags energiruder" (2-layer glass), but Status ID 7 actually has "3 lags energirude - energiklasse B" (3-layer glass). The PDFReportData oversimplifies this distinction.

---

## Comparison Matrix

| Aspect | InputData | PDFReportData |
|--------|-----------|---------------|
| **Number of entries** | 10 distinct Status elements | 3 consolidated Text elements |
| **Detail level** | High (all technical specs) | Low (descriptive only) |
| **Target audience** | Calculation software | End user (PDF readers) |
| **Technical values** | Yes (Area, U-value, Orientation, etc.) | No |
| **Grouping method** | Individual per window/location | By BIClassification type |
| **Text style** | Technical/precise | General/simplified |
| **Completeness** | 100% of windows listed | 100% coverage through grouping |

---

## Validation

✅ **All 10 window entries from InputData are represented** in the PDFReportData through the 3 grouped texts  
✅ **Classification mapping is correct** (1-3-1-0, 1-3-2-0, 1-3-3-0)  
⚠️ **Minor text inconsistency** in Text ID 5 (states 2-lag for both doors, but one is 3-lag)  
✅ **No windows are missing** from the summary

---

## Conclusion

The transformation from InputData to PDFReportData follows a **detail-to-summary** pattern where:

1. Individual technical window entries are grouped by classification type
2. Technical specifications are removed for readability
3. Descriptive text is simplified for end-user consumption
4. The core information (glass type, general window types) is preserved
5. Minor simplifications may introduce small inaccuracies (e.g., the 3-lag door being described as 2-lag in the summary text)

This pattern is consistent with the purpose of PDFReportData: to provide a human-readable summary in the PDF energy certificate while maintaining all detailed technical data in the InputData section for calculations.
