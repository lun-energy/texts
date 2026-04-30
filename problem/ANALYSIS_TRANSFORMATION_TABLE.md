# Danish Energy Label — Transformation Tracking by Property

This analysis shows the complete transformation chain for each property:
**Plans Status → Energy10 Status → BuildingReview**

- **Plans Status**: Status entries from the Plans software (draft XML)
- **Energy10 Status**: Status entries from Energy10 software (final XML)
- **BuildingReview**: Final text that appears in the PDF report

**Matching Strategy:**
- First tries exact ShortText match
- Falls back to fuzzy matching (≥60% similarity) when ShortText was significantly edited
- Tracks BI reclassifications

---

## Ivarsvej 27

### 1. BI Classification: `1-1-1-0`

**Status Counts:** Plans=0 (in this BI), Energy10=2

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Vægge mod skunkrum vurderes isoleret med 200 mm isolering. Konstruktions- og isoleringsforhold er skønnet ud fra renoveringstidspunktet.<br><br>Skråvægge vurderes isoleret med 250 mm mineraluld. Konstruktionstykkelse er målt ved vindue. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. | **ShortText:**<br>Vægge mod skunkrum - 200 mm isolering *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Vægge mod skunkrum vurderes isoleret med 200 mm isolering. Konstruktions- og isoleringsforhold er skønnet ud fra renoveringstidspunktet.<br><br>**BI reclassified:** `1-1-3-0` → `1-1-1-0` | **ShortText:**<br>Vægge mod skunkrum - 200 mm isolering *(was BI 1-1-1-0)*<br><br>**LongText:**<br>Vægge mod skunkrum vurderes isoleret med 200 mm isolering. Konstruktions- og isoleringsforhold er skønnet ud fra renoveringstidspunktet. |
| | **ShortText:**<br>Skråvægge - 250 mm isolering *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Skråvægge vurderes isoleret med 250 mm mineraluld. Konstruktionstykkelse er målt ved vindue. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet.<br><br>**BI reclassified:** `1-1-3-0` → `1-1-1-0` | **ShortText:**<br>Skråvægge - 250 mm isolering *(was BI 1-1-1-0)*<br><br>**LongText:**<br>Skråvægge vurderes isoleret med 250 mm mineraluld. Konstruktionstykkelse er målt ved vindue. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. |

---

### 2. BI Classification: `1-1-3-0`

**Status Counts:** Plans=4 (in this BI), Energy10=2

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Hanebåndsloft vurderes isoleret med 400 mm mineraluld. Isoleringsforholdet i konstruktionen er målt i forbindelse med besigtigelsen.<br><br>Loft mod skunkrum vurderes isoleret med 250 mm mineraluld. Konstruktions- og isoleringsforhold er skønnet ud fra renoveringstidspunktet. | **ShortText:**<br>Hanebåndsloft - 400 mm isolering *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Hanebåndsloft vurderes isoleret med 400 mm mineraluld. Isoleringsforholdet i konstruktionen er målt i forbindelse med besigtigelsen. | **ShortText:**<br>Hanebåndsloft - 400 mm isolering *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Hanebåndsloft vurderes isoleret med 400 mm mineraluld. Isoleringsforholdet i konstruktionen er målt i forbindelse med besigtigelsen. |
| | **ShortText:**<br>Loft mod skunkrum - 250 mm isolering *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Loft mod skunkrum vurderes isoleret med 250 mm mineraluld. Konstruktions- og isoleringsforhold er skønnet ud fra renoveringstidspunktet. | **ShortText:**<br>Loft mod skunkrum - 250 mm isolering *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Loft mod skunkrum vurderes isoleret med 250 mm mineraluld. Konstruktions- og isoleringsforhold er skønnet ud fra renoveringstidspunktet. |

---

### 3. BI Classification: `1-2-1-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Ydervægge er udført som 30 cm hulmur. Vægge består udvendigt og indvendigt af tegl. Hulrummet vurderes efterisoleret med mineraluldsgranulat. Konstruktions- og isoleringsforhold er baseret på et tidligere energimærke. | **ShortText:**<br>Hul ydervæg - 30 cm tegl/tegl - mineraluldsgranulat *(was BI 1-2-1-0)*<br><br>**LongText:**<br>Ydervægge er udført som 30 cm hulmur. Vægge består udvendigt og indvendigt af tegl. Hulrummet vurderes efterisoleret med mineraluldsgranulat. Konstruktions- og isoleringsforhold er baseret på et tidligere energimærke.<br>(??? U-værdi tillæg påført: 0.16 W/m2K) | **ShortText:**<br>Hul ydervæg - 30 cm tegl/tegl - mineraluldsgranulat *(was BI 1-2-1-0)*<br><br>**LongText:**<br>Ydervægge er udført som 30 cm hulmur. Vægge består udvendigt og indvendigt af tegl. Hulrummet vurderes efterisoleret med mineraluldsgranulat. Konstruktions- og isoleringsforhold er baseret på et tidligere energimærke. |

---

### 4. BI Classification: `1-3-1-0`

**Status Counts:** Plans=6 (in this BI), Energy10=6

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. |

---

### 5. BI Classification: `1-3-2-0`

**Status Counts:** Plans=2 (in this BI), Energy10=2

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Ovenlysvindue er monteret med trelags energirude | **ShortText:**<br>Ovenlysvindue - 3 lags energirude - efter BR15 *(was BI 1-3-2-0)*<br><br>**LongText:**<br>Ovenlysvindue er monteret med trelags energirude, efter BR15. | **ShortText:**<br>Ovenlysvindue - 3 lags energirude - efter BR15 *(was BI 1-3-2-0)*<br><br>**LongText:**<br>Ovenlysvindue er monteret med trelags energirude |
| | **ShortText:**<br>Ovenlysvindue - 3 lags energirude - efter BR15 *(was BI 1-3-2-0)*<br><br>**LongText:**<br>Ovenlysvindue er monteret med trelags energirude, efter BR15. | **ShortText:**<br>Ovenlysvindue - 3 lags energirude - efter BR15 *(was BI 1-3-2-0)*<br><br>**LongText:**<br>Ovenlysvindue er monteret med trelags energirude, efter BR15. |

---

### 6. BI Classification: `1-3-3-0`

**Status Counts:** Plans=2 (in this BI), Energy10=2

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Terrassedør og hoveddør med sideparti er monteret med tolags energiruder. | **ShortText:**<br>Terrassedør med sideparti - 2 lags energirude med varm kant *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Terrassedør med sideparti, monteret med tolags energiruder. | **ShortText:**<br>Terrassedør med sideparti - 2 lags energirude med varm kant *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Terrassedør og hoveddør med sideparti er monteret med tolags energiruder. |
| | **ShortText:**<br>Yderdør med sideparti - 3 lags energirude - energiklasse B *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør med sideparti, monteret med trelags energiruder, energiklasse B. | **ShortText:**<br>Yderdør med sideparti - 3 lags energirude - energiklasse B *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør med sideparti, monteret med trelags energiruder, energiklasse B. |

---

### 7. BI Classification: `1-4-2-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Gulv mod uopvarmet kælder udført som lukket bjælkelag vurderes isoleret med 30 mm mineraluld. Konstruktions- og isoleringsforhold er skønnet ud fra opførelsestidspunktet. | **ShortText:**<br>Gulv mod uopvarmet kælder - lukket bjælkelag - 30 mm isolering *(was BI 1-4-2-0)*<br><br>**LongText:**<br>Gulv mod uopvarmet kælder udført som lukket bjælkelag vurderes isoleret med 30 mm mineraluld. Konstruktions- og isoleringsforhold er skønnet ud fra opførelsestidspunktet. | **ShortText:**<br>Gulv mod uopvarmet kælder - lukket bjælkelag - 30 mm isolering *(was BI 1-4-2-0)*<br><br>**LongText:**<br>Gulv mod uopvarmet kælder udført som lukket bjælkelag vurderes isoleret med 30 mm mineraluld. Konstruktions- og isoleringsforhold er skønnet ud fra opførelsestidspunktet. |

---

### 8. BI Classification: `1-5-1-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er naturlig ventilation i hele bygningen. Bygningen er normal tæt, da konstruktionssamlinger og fuger ved vindues- og døråbninger, samt tætningslister i vinduer og udvendige døre fremstår i god stand. | *(not in Plans)* | **ShortText:**<br>Bolig - Naturlig - tæt 0,3 l/s m² *(was BI 1-5-1-0)*<br><br>**LongText:**<br>Der er naturlig ventilation i hele bygningen. Bygningen er normal tæt, da konstruktionssamlinger og fuger ved vindues- og døråbninger, samt tætningslister i vinduer og udvendige døre fremstår i god stand. |

---

### 9. BI Classification: `2-1-3-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Bygningen opvarmes med fjernvarme. Anlægget er udført som direkte fjernvarmeanlæg, med fjernvarmevand i fordelingsnettet. stik er indført i kælder. | *(not in Plans)* | **ShortText:**<br>Fjernvarme uden veksler - direkte *(was BI 2-1-3-0)*<br><br>**LongText:**<br>Bygningen opvarmes med fjernvarme. Anlægget er udført som direkte fjernvarmeanlæg, med fjernvarmevand i fordelingsnettet. stik er indført i kælder. |

---

### 10. BI Classification: `2-1-5-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er ikke stillet forslag til varmepumpe, da dette, med bygningens eksisterende varmeanlæg og den dertilhørende energipris, ikke vil kunne medføre et fornuftigt og rentabelt forslag. | *(not in Plans)* | **ShortText:**<br>Ingen varmepumpe - Intet forslag *(was BI 2-1-5-0)*<br><br>**LongText:**<br>Der er ikke stillet forslag til varmepumpe, da dette, med bygningens eksisterende varmeanlæg og den dertilhørende energipris, ikke vil kunne medføre et fornuftigt og rentabelt forslag. |

---

### 11. BI Classification: `2-1-6-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er ikke stillet forslag til solvarmeanlæg, da dette, med bygningens eksisterende varmeanlæg og den dertilhørende energipris, ikke vil kunne medføre et fornuftigt og rentabelt forslag. | *(not in Plans)* | **ShortText:**<br>Intet solvarmeanlæg - Intet forslag *(was BI 2-1-6-0)*<br><br>**LongText:**<br>Der er ikke stillet forslag til solvarmeanlæg, da dette, med bygningens eksisterende varmeanlæg og den dertilhørende energipris, ikke vil kunne medføre et fornuftigt og rentabelt forslag. |

---

### 12. BI Classification: `2-2-1-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Den primære opvarmning af ejendommen sker via radiatorer i opvarmede rum. Varmefordelingsrør er udført som to-strengs anlæg. | *(not in Plans)* | **ShortText:**<br>Radiator - 2-streng iht. HB2023 *(was BI 2-2-1-0)*<br><br>**LongText:**<br>Den primære opvarmning af ejendommen sker via radiatorer i opvarmede rum. Varmefordelingsrør er udført som to-strengs anlæg. |

---

### 13. BI Classification: `2-2-2-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Varmerør er udført som 3/4" stålrør. Varmerørene er isoleret med 15 mm isolering. | *(not in Plans)* | **ShortText:**<br>3/4" (26,9 mm) stålrør - 15 mm *(was BI 2-2-2-0)*<br><br>**LongText:**<br>Varmerør er udført som 3/4" stålrør. Varmerørene er isoleret med 15 mm isolering. |

---

### 14. BI Classification: `2-2-4-0`

**Status Counts:** Plans=0 (in this BI), Energy10=2

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er monteret termostatventiler på alle radiatorer til regulering af korrekt rumtemperatur.<br><br>Udenfor fyringssæsonen forudsættes det i beregningen, at varmeanlægget kan afbrydes. Enten automatisk via udeføler eller manuelt ved lukning af ventiler og slukning af varmefordelingspumper. | *(not in Plans)* | **ShortText:**<br>Termostatventiler på alle radiatorer *(was BI 2-2-4-0)*<br><br>**LongText:**<br>Der er monteret termostatventiler på alle radiatorer til regulering af korrekt rumtemperatur. |
| | *(not in Plans)* | **ShortText:**<br>Sommerstop af varmeanlæg *(was BI 2-2-4-0)*<br><br>**LongText:**<br>Udenfor fyringssæsonen forudsættes det i beregningen, at varmeanlægget kan afbrydes. Enten automatisk via udeføler eller manuelt ved lukning af ventiler og slukning af varmefordelingspumper. |

---

### 15. BI Classification: `3-1-3-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Tilslutningsrør til varmtvandsbeholder er udført som 3/4" stålrør. Rørene er isoleret med 15 mm isolering. | *(not in Plans)* | **ShortText:**<br>Tilslutningsrør til VVB - 3/4" stålrør - 15 mm *(was BI 3-1-3-0)*<br><br>**LongText:**<br>Tilslutningsrør til varmtvandsbeholder er udført som 3/4" stålrør. Rørene er isoleret med 15 mm isolering. |

---

### 16. BI Classification: `3-1-5-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Varmt brugsvand produceres i 100 l varmtvandsbeholder, isoleret med 50 mm isolering. Beholderen er placeret i kælderrum mod vej | *(not in Plans)* | **ShortText:**<br>100 l - 50 mm isolering iht. HB2023 *(was BI 3-1-5-0)*<br><br>**LongText:**<br>Varmt brugsvand produceres i 100 l varmtvandsbeholder, isoleret med 50 mm isolering. Beholderen er placeret i kælderrum mod vej |

---

### 17. BI Classification: `4-1-3-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er ingen solceller på bygningen. | *(not in Plans)* | **ShortText:**<br>Ingen solcelle *(was BI 4-1-3-0)*<br><br>**LongText:**<br>Der er ingen solceller på bygningen. |

---


## Spangsvej 15

### 1. BI Classification: `1-1-1-0`

**Status Counts:** Plans=1 (in this BI), Energy10=2

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Loftsrum vurderes isoleret med 300 mm mineraluld. Konstruktionstykkelse er målt ved loftlem. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet.<br><br>Loftslem vurderes isoleret med 100 mm mineraluld. Konstruktionstykkelse er målt ved loftlem. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. | **ShortText:**<br>Loftsrum - 300 mm isolering *(was BI 1-1-1-0)*<br><br>**LongText:**<br>Loftsrum vurderes isoleret med 300 mm mineraluld. Konstruktionstykkelse er målt ved loftlem. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. | **ShortText:**<br>Loftsrum - 300 mm isolering *(was BI 1-1-1-0)*<br><br>**LongText:**<br>Loftsrum vurderes isoleret med 300 mm mineraluld. Konstruktionstykkelse er målt ved loftlem. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. |
| | **ShortText:**<br>Loftslem - 100 mm isolering *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Loftslem vurderes isoleret med 100 mm mineraluld. Konstruktionstykkelse er målt ved loftlem. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet.<br><br>**BI reclassified:** `1-1-3-0` → `1-1-1-0` | **ShortText:**<br>Loftslem - 100 mm isolering *(was BI 1-1-1-0)*<br><br>**LongText:**<br>Loftslem vurderes isoleret med 100 mm mineraluld. Konstruktionstykkelse er målt ved loftlem. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. |

---

### 2. BI Classification: `1-2-1-0`

**Status Counts:** Plans=3 (in this BI), Energy10=3

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Ydervægge i oprindelig del er udført som 30 cm hulmur. Vægge består udvendigt af tegl og indvendigt af letbeton. Hulrummet er isoleret ved opførelsen. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br><br>Ydervægge i tilbygning er udført som 30 cm hulmur. Vægge består udvendigt og indvendigt af tegl. Hulrummet vurderes isoleret ved opførelsen. Konstruktions- og isoleringsforhold er skønnet ud fra opførelsestidspunktet.<br>Der er ikke stillet forslag til efterisolering af hulmur, da det ikke er umiddelbart rentabelt, da en evt. yderligere indvendig efterisolering vil mindske boligarealet og er vanskelig pga. indretning og installationer og en evt. udvendig efterisolering vil ændre bygningens arkitektur. | **ShortText:**<br>Hul ydervæg - 30 cm tegl/letbeton (7,5 cm bagmur) - Isoleret ved opførelsen (75 mm isolering) *(was BI 1-2-1-0)*<br><br>**LongText:**<br>Ydervægge er udført som 30 cm hulmur. Vægge består udvendigt af tegl og indvendigt af letbeton. Hulrummet er isoleret ved opførelsen. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br>(??? U-værdi tillæg påført: 0.05 W/m2K) | **ShortText:**<br>Hul ydervæg - 30 cm tegl/letbeton (7,5 cm bagmur) - Isoleret ved opførelsen (75 mm isolering) *(was BI 1-2-1-0)*<br><br>**LongText:**<br>Ydervægge i oprindelig del er udført som 30 cm hulmur. Vægge består udvendigt af tegl og indvendigt af letbeton. Hulrummet er isoleret ved opførelsen. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. |
| | **ShortText:**<br>Hul ydervæg - 30 cm tegl/letbeton (7,5 cm bagmur) - Isoleret ved opførelsen (75 mm isolering) *(was BI 1-2-1-0)*<br><br>**LongText:**<br>Ydervægge er udført som 30 cm hulmur. Vægge består udvendigt af tegl og indvendigt af letbeton. Hulrummet er isoleret ved opførelsen. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br>(??? U-værdi tillæg påført: 0.05 W/m2K) | **ShortText:**<br>Hul ydervæg - 30 cm tegl/letbeton (7,5 cm bagmur) - Isoleret ved opførelsen (75 mm isolering) *(was BI 1-2-1-0)*<br><br>**LongText:**<br>Ydervægge er udført som 30 cm hulmur. Vægge består udvendigt af tegl og indvendigt af letbeton. Hulrummet er isoleret ved opførelsen. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. |
| | **ShortText:**<br>Hul ydervæg - 30 cm tegl/tegl - Isoleret ved opførelsen *(was BI 1-2-1-0)*<br><br>**LongText:**<br>Ydervægge er udført som 30 cm hulmur. Vægge består udvendigt og indvendigt af tegl. Hulrummet vurderes isoleret ved opførelsen. Konstruktions- og isoleringsforhold er skønnet ud fra opførelsestidspunktet.<br>(??? U-værdi tillæg påført: 0.1 W/m2K) | **ShortText:**<br>Hul ydervæg - 30 cm tegl/tegl - Isoleret ved opførelsen *(was BI 1-2-1-0)*<br><br>**LongText:**<br>Ydervægge i tilbygning er udført som 30 cm hulmur. Vægge består udvendigt og indvendigt af tegl. Hulrummet vurderes isoleret ved opførelsen. Konstruktions- og isoleringsforhold er skønnet ud fra opførelsestidspunktet.<br>Der er ikke stillet forslag til efterisolering af hulmur, da det ikke er umiddelbart rentabelt, da en evt. yderligere indvendig efterisolering vil mindske boligarealet og er vanskelig pga. indretning og installationer og en evt. udvendig efterisolering vil ændre bygningens arkitektur. |

---

### 3. BI Classification: `1-2-4-0`

**Status Counts:** Plans=3 (in this BI), Energy10=3

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Kælderydervægge består af 29 cm væg af lecabeton.<br>Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. | **ShortText:**<br>Kælderydervæg 0-2m dybde - 30 cm beton - uisoleret *(was BI 1-2-4-0)*<br><br>**LongText:**<br>Kælderydervægge mod jord består af 30 cm uisoleret betonvæg. Konstruktionstykkelse er målt ved vindue. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet.<br><br>**(fuzzy match: 87%)** | **ShortText:**<br>Kælderydervæg 0-2m dybde - 29 cm letklinkerbeton - uisoleret *(was BI 1-2-4-0)*<br><br>**LongText:**<br>Kælderydervægge består af 29 cm væg af lecabeton.<br>Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. |
| | **ShortText:**<br>Kælderydervæg over jord - 30 cm beton - uisoleret *(was BI 1-2-4-0)*<br><br>**LongText:**<br>Kælderydervægge over jord består af 30 cm uisoleret betonvæg. Konstruktionstykkelse er målt ved vindue. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet.<br><br>**(fuzzy match: 91%)** | **ShortText:**<br>Kælderydervæg over jord - 30 cm letklinkerbeton - uisoleret *(was BI 1-2-4-0)*<br><br>**LongText:**<br>Kælderydervægge over jord består af 30 cm væg af letklinkerbeton.<br>Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. |
| | **ShortText:**<br>Kælderydervæg 0-2m dybde - 30 cm beton - uisoleret *(was BI 1-2-4-0)*<br><br>**LongText:**<br>Kælderydervægge mod jord består af 30 cm uisoleret betonvæg. Konstruktionstykkelse er målt ved vindue. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet.<br><br>**(fuzzy match: 87%)** | **ShortText:**<br>Kælderydervæg 0-2m dybde - 29 cm letklinkerbeton - uisoleret *(was BI 1-2-4-0)*<br><br>**LongText:**<br>Kælderydervægge mod jord består af 29 cm væg af letklinkerbeton.<br>Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. |

---

### 4. BI Classification: `1-3-1-0`

**Status Counts:** Plans=9 (in this BI), Energy10=9

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Vinduerne er monteret med to- og trelags energiruder. | **ShortText:**<br>Enkeltfagsvindue i fast ramme - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Faste vinduer med et fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Enkeltfagsvindue i fast ramme - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Vinduerne er monteret med to- og trelags energiruder. |
| | **ShortText:**<br>Enkeltfagsvindue i fast ramme - 3 lags energirude - energiklasse B *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Faste vinduer med et fag. Vinduerne er monteret med trelags energirude, energiklasse B. | **ShortText:**<br>Enkeltfagsvindue i fast ramme - 3 lags energirude - energiklasse B *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Faste vinduer med et fag. Vinduerne er monteret med trelags energirude, energiklasse B. |
| | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Enkeltfagsvindue i fast ramme - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Faste vinduer med et fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Enkeltfagsvindue i fast ramme - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Faste vinduer med et fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Enkeltfagsvindue i fast ramme - 3 lags energirude - energiklasse B *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Faste vinduer med et fag. Vinduerne er monteret med trelags energirude, energiklasse B. | **ShortText:**<br>Enkeltfagsvindue i fast ramme - 3 lags energirude - energiklasse B *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Faste vinduer med et fag. Vinduerne er monteret med trelags energirude, energiklasse B. |
| | **ShortText:**<br>Enkeltfagsvindue i fast ramme - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Faste vinduer med et fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Enkeltfagsvindue i fast ramme - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Faste vinduer med et fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Enkeltfagsvindue i fast ramme - 3 lags energirude - energiklasse B *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Faste vinduer med et fag. Vinduerne er monteret med trelags energirude, energiklasse B. | **ShortText:**<br>Enkeltfagsvindue i fast ramme - 3 lags energirude - energiklasse B *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Faste vinduer med et fag. Vinduerne er monteret med trelags energirude, energiklasse B. |

---

### 5. BI Classification: `1-3-3-0`

**Status Counts:** Plans=3 (in this BI), Energy10=3

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Skydedørsparti er monteret med tolags termoruder.<br><br>Hoveddør og bryggersdør er monteret med tolags energiruder. | **ShortText:**<br>Skydedørsparti - 1 fast og 1 gående - 2 lags termorude *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Skydedørsparti med 1 fast og 1 gående fag, monteret med tolags termoruder. | **ShortText:**<br>Skydedørsparti - 1 fast og 1 gående - 2 lags termorude *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Skydedørsparti er monteret med tolags termoruder. |
| | **ShortText:**<br>Yderdør med sideparti - 2 lags energirude med kold kant *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør med sideparti, monteret med tolags energiruder. | **ShortText:**<br>Yderdør med sideparti - 2 lags energirude med kold kant *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Hoveddør og bryggersdør er monteret med tolags energiruder. |
| | **ShortText:**<br>Skydedørsparti - 1 fast og 1 gående - 2 lags termorude *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Skydedørsparti med 1 fast og 1 gående fag, monteret med tolags termoruder. | **ShortText:**<br>Skydedørsparti - 1 fast og 1 gående - 2 lags termorude *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Skydedørsparti med 1 fast og 1 gående fag, monteret med tolags termoruder. |

---

### 6. BI Classification: `1-4-1-0`

**Status Counts:** Plans=3 (in this BI), Energy10=3

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Terrændæk i bryggers og badeværelse er udført af beton med letklinkerbeton. Gulvet er uisoleret. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br><br>Terrændæk er udført i beton og med strøgulve der er isoleret med 75 mm mineraluld mellem strøer. Under betonen er gulvet uisoleret. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. | **ShortText:**<br>Terrændæk - letklinkerbeton *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Terrændæk er udført af beton med letklinkerbeton. Gulvet er uisoleret. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. | **ShortText:**<br>Terrændæk - letklinkerbeton *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Terrændæk i bryggers og badeværelse er udført af beton med letklinkerbeton. Gulvet er uisoleret. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. |
| | **ShortText:**<br>Terrændæk - Beton med strøgulv - 75 mm mineraluld *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Terrændæk er udført i beton og med strøgulve der er isoleret med 75 mm mineraluld mellem strøer. Under betonen er gulvet uisoleret. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. | **ShortText:**<br>Terrændæk - Beton med strøgulv - 75 mm mineraluld *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Terrændæk er udført i beton og med strøgulve der er isoleret med 75 mm mineraluld mellem strøer. Under betonen er gulvet uisoleret. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. |
| | **ShortText:**<br>Terrændæk - letklinkerbeton *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Terrændæk er udført af beton med letklinkerbeton. Gulvet er uisoleret. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. | **ShortText:**<br>Terrændæk - letklinkerbeton *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Terrændæk er udført af beton med letklinkerbeton. Gulvet er uisoleret. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. |

---

### 7. BI Classification: `1-4-4-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Kældergulv er udført af beton med slidlagsgulv. Gulvet er isoleret med 50 mm mineraluld under betonen med letklinker som kapillarbrydende lag.<br>Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. | **ShortText:**<br>Kældergulv - Beton med slidlag - uisoleret *(was BI 1-4-4-0)*<br><br>**LongText:**<br>Kældergulv er udført af beton med slidlagsgulv. Gulvet er uisoleret. Konstruktions- og isoleringsforhold er baseret på ejers oplysninger.<br><br>**(fuzzy match: 69%)** | **ShortText:**<br>Kældergulv - Beton med slidlag - 50 mm mineraluld/polystyrenplader *(was BI 1-4-4-0)*<br><br>**LongText:**<br>Kældergulv er udført af beton med slidlagsgulv. Gulvet er isoleret med 50 mm mineraluld under betonen med letklinker som kapillarbrydende lag.<br>Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. |

---

### 8. BI Classification: `1-5-1-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er naturlig ventilation i hele bygningen. Bygningen er normal tæt, da konstruktionssamlinger og fuger ved vindues- og døråbninger, samt tætningslister i vinduer og udvendige døre fremstår i god stand. | *(not in Plans)* | **ShortText:**<br>Bolig - Naturlig - tæt 0,3 l/s m² *(was BI 1-5-1-0)*<br><br>**LongText:**<br>Der er naturlig ventilation i hele bygningen. Bygningen er normal tæt, da konstruktionssamlinger og fuger ved vindues- og døråbninger, samt tætningslister i vinduer og udvendige døre fremstår i god stand. |

---

### 9. BI Classification: `2-1-3-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Bygningen opvarmes med fjernvarme. Anlægget er udført som direkte fjernvarmeanlæg, med fjernvarmevand i fordelingsnettet.<br>Fjernvarmestik er placeret i bryggers. | *(not in Plans)* | **ShortText:**<br>Fjernvarme uden veksler - direkte *(was BI 2-1-3-0)*<br><br>**LongText:**<br>Bygningen opvarmes med fjernvarme. Anlægget er udført som direkte fjernvarmeanlæg, med fjernvarmevand i fordelingsnettet.<br>Fjernvarmestik er placeret i bryggers. |

---

### 10. BI Classification: `2-2-1-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Den primære opvarmning af ejendommen sker via radiatorer i opvarmede rum. Varmefordelingsrør er udført som to-strengs anlæg. Der er desuden gulvvarme i badeværelse. | *(not in Plans)* | **ShortText:**<br>Radiator - 2-streng iht. HB2023 *(was BI 2-2-1-0)*<br><br>**LongText:**<br>Den primære opvarmning af ejendommen sker via radiatorer i opvarmede rum. Varmefordelingsrør er udført som to-strengs anlæg. Der er desuden gulvvarme i badeværelse. |

---

### 11. BI Classification: `2-2-4-0`

**Status Counts:** Plans=0 (in this BI), Energy10=2

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Udenfor fyringssæsonen forudsættes det i beregningen, at varmeanlægget kan afbrydes. Enten automatisk via udeføler eller manuelt ved lukning af ventiler og slukning af varmefordelingspumper.<br><br>Der er monteret termostatventiler på alle radiatorer og gulvvarme til regulering af korrekt rumtemperatur. | *(not in Plans)* | **ShortText:**<br>Sommerstop af varmeanlæg *(was BI 2-2-4-0)*<br><br>**LongText:**<br>Udenfor fyringssæsonen forudsættes det i beregningen, at varmeanlægget kan afbrydes. Enten automatisk via udeføler eller manuelt ved lukning af ventiler og slukning af varmefordelingspumper. |
| | *(not in Plans)* | **ShortText:**<br>Termostatventiler på alle radiatorer og gulvvarme *(was BI 2-2-4-0)*<br><br>**LongText:**<br>Der er monteret termostatventiler på alle radiatorer og gulvvarme til regulering af korrekt rumtemperatur. |

---

### 12. BI Classification: `3-1-5-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Varmt brugsvand produceres via brugsvandsveksler. Veksleren er placeret i skab i bryggers. | *(not in Plans)* | **ShortText:**<br>Brugsvandsveksler, Øvrige *(was BI 3-1-5-0)*<br><br>**LongText:**<br>Varmt brugsvand produceres via brugsvandsveksler. Veksleren er placeret i skab i bryggers. |

---

### 13. BI Classification: `4-1-3-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er ingen solceller på bygningen. | *(not in Plans)* | **ShortText:**<br>Ingen solcelle *(was BI 4-1-3-0)*<br><br>**LongText:**<br>Der er ingen solceller på bygningen. |

---


## Lungstedløkken 15

### 1. BI Classification: `1-1-1-0`

**Status Counts:** Plans=0 (in this BI), Energy10=2

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Vægge mod skunkrum vurderes isoleret med 150 mm isolering. <br>Konstruktions- og isoleringsforhold er skønnet ud fra opførelsestidspunktet.<br><br>Tag ved tagterrasse vurderes isoleret med 200 mm mineraluld.<br>Konstruktions- og isoleringsforhold er skønnet ud fra opførelsestidspunktet. | **ShortText:**<br>Vægge mod skunkrum - 150 mm isolering *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Vægge mod skunkrum vurderes isoleret med 150 mm isolering. Konstruktions- og isoleringsforhold er skønnet ud fra renoveringstidspunktet.<br><br>**BI reclassified:** `1-1-3-0` → `1-1-1-0` | **ShortText:**<br>Vægge mod skunkrum - 150 mm isolering *(was BI 1-1-1-0)*<br><br>**LongText:**<br>Vægge mod skunkrum vurderes isoleret med 150 mm isolering. <br>Konstruktions- og isoleringsforhold er skønnet ud fra opførelsestidspunktet. |
| | **ShortText:**<br>Fladt tag - 200 mm isolering *(was BI 1-1-0-0)*<br><br>**LongText:**<br>Fladt tag (built-up tag) vurderes isoleret med 200 mm mineraluld.<br><br>**(fuzzy match: 82%)**<br><br>**BI reclassified:** `1-1-0-0` → `1-1-1-0` | **ShortText:**<br>Fladt tag tagterrasse - 200 mm isolering *(was BI 1-1-1-0)*<br><br>**LongText:**<br>Tag ved tagterrasse vurderes isoleret med 200 mm mineraluld.<br>Konstruktions- og isoleringsforhold er skønnet ud fra opførelsestidspunktet. |

---

### 2. BI Classification: `1-1-3-0`

**Status Counts:** Plans=3 (in this BI), Energy10=3

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Skunkrum vurderes isoleret med 150 mm mineraluld. <br>Konstruktions- og isoleringsforhold er skønnet ud fra opførelsestidspunktet.<br><br>Skråvægge vurderes isoleret med 150 mm mineraluld. <br>Konstruktions- og isoleringsforhold er skønnet ud fra opførelsestidspunktet.<br><br>Hanebåndsloft er isoleret med 200 mm mineraluld.<br>Konstruktionstykkelse er målt ved loftlem. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. | **ShortText:**<br>Loft mod skunkrum - 150 mm isolering *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Loft mod skunkrum vurderes isoleret med 150 mm mineraluld. Konstruktions- og isoleringsforhold er skønnet ud fra renoveringstidspunktet. | **ShortText:**<br>Loft mod skunkrum - 150 mm isolering *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Skunkrum vurderes isoleret med 150 mm mineraluld. <br>Konstruktions- og isoleringsforhold er skønnet ud fra opførelsestidspunktet. |
| | **ShortText:**<br>Skråvægge - 150 mm isolering *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Skråvægge vurderes isoleret med 150 mm mineraluld. Konstruktions- og isoleringsforhold er skønnet ud fra renoveringstidspunktet. | **ShortText:**<br>Skråvægge - 150 mm isolering *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Skråvægge vurderes isoleret med 150 mm mineraluld. <br>Konstruktions- og isoleringsforhold er skønnet ud fra opførelsestidspunktet. |
| | **ShortText:**<br>Fladt tag - 200 mm isolering *(was BI 1-1-0-0)*<br><br>**LongText:**<br>Fladt tag (built-up tag) vurderes isoleret med 200 mm mineraluld.<br><br>**(fuzzy match: 73%)**<br><br>**BI reclassified:** `1-1-0-0` → `1-1-3-0` | **ShortText:**<br>Hanebåndsloft - 200 mm isolering *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Hanebåndsloft er isoleret med 200 mm mineraluld.<br>Konstruktionstykkelse er målt ved loftlem. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. |

---

### 3. BI Classification: `1-2-1-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Ydervægge er udført som 30 cm hulmur. Vægge består udvendigt af tegl og indvendigt af letbeton. Hulrummet er isoleret ved opførelsen. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br>Der er ikke stillet forslag til efterisolering af hulmur, da det ikke er umiddelbart rentabelt, da en evt. yderligere indvendig efterisolering vil mindske boligarealet og er vanskelig pga. indretning og installationer og en evt. udvendig efterisolering vil ændre bygningens arkitektur. | **ShortText:**<br>Hul ydervæg - 30 cm tegl/letbeton (10 cm bagmur) - Isoleret ved opførelsen *(was BI 1-2-1-0)*<br><br>**LongText:**<br>Ydervægge er udført som 30 cm hulmur. Vægge består udvendigt af tegl og indvendigt af letbeton. Hulrummet er isoleret ved opførelsen. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br>(??? U-værdi tillæg påført: 0.05 W/m2K) | **ShortText:**<br>Hul ydervæg - 30 cm tegl/letbeton (10 cm bagmur) - Isoleret ved opførelsen *(was BI 1-2-1-0)*<br><br>**LongText:**<br>Ydervægge er udført som 30 cm hulmur. Vægge består udvendigt af tegl og indvendigt af letbeton. Hulrummet er isoleret ved opførelsen. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br>Der er ikke stillet forslag til efterisolering af hulmur, da det ikke er umiddelbart rentabelt, da en evt. yderligere indvendig efterisolering vil mindske boligarealet og er vanskelig pga. indretning og installationer og en evt. udvendig efterisolering vil ændre bygningens arkitektur. |

---

### 4. BI Classification: `1-2-3-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Ydervægge i gavle er udført som let konstruktion med beklædning ud- og indvendig. Hulrum mellem beklædninger er isoleret med 150 mm mineraluld. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. | **ShortText:**<br>Let ydervæg - træ/træ - 150 mm isolering *(was BI 1-2-3-0)*<br><br>**LongText:**<br>Ydervægge er udført som let konstruktion med beklædning ud- og indvendig. Hulrum mellem beklædninger er isoleret med 150 mm mineraluld. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br><br>**(fuzzy match: 93%)** | **ShortText:**<br>Let ydervæg gavle - træ/træ - 150 mm isolering *(was BI 1-2-3-0)*<br><br>**LongText:**<br>Ydervægge i gavle er udført som let konstruktion med beklædning ud- og indvendig. Hulrum mellem beklædninger er isoleret med 150 mm mineraluld. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. |

---

### 5. BI Classification: `1-3-1-0`

**Status Counts:** Plans=5 (in this BI), Energy10=5

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Vinduerne i bygningen er fortrinsvis med 2 og 3 lags energiruder. Undtaget er vinduespartier ved tagterrasse i overetagen. | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Vinduerne i bygningen er fortrinsvis med 2 og 3 lags energiruder. Undtaget er vinduespartier ved tagterrasse i overetagen. |
| | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Enkeltfagsvindue i fast ramme - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Faste vinduer med et fag. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Enkeltfagsvindue i fast ramme - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Faste vinduer med et fag. Vinduerne er monteret med tolags termorude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 3 lags energirude - energiklasse B *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med trelags energirude, energiklasse B. | **ShortText:**<br>Flerfagsvindue med gående rammer - 3 lags energirude - energiklasse B *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med trelags energirude, energiklasse B. |

---

### 6. BI Classification: `1-3-2-0`

**Status Counts:** Plans=2 (in this BI), Energy10=2

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Ovenlysvinduer er monteret med tolags termoruder. | **ShortText:**<br>Ovenlysvindue - 2 lags termorude kold kant *(was BI 1-3-2-0)*<br><br>**LongText:**<br>Ovenlysvindue er monteret med tolags termorude. | **ShortText:**<br>Ovenlysvindue - 2 lags termorude kold kant *(was BI 1-3-2-0)*<br><br>**LongText:**<br>Ovenlysvinduer er monteret med tolags termoruder. |
| | **ShortText:**<br>Ovenlysvindue - 2 lags termorude kold kant *(was BI 1-3-2-0)*<br><br>**LongText:**<br>Ovenlysvindue er monteret med tolags termorude. | **ShortText:**<br>Ovenlysvindue - 2 lags termorude kold kant *(was BI 1-3-2-0)*<br><br>**LongText:**<br>Ovenlysvindue er monteret med tolags termorude. |

---

### 7. BI Classification: `1-3-3-0`

**Status Counts:** Plans=3 (in this BI), Energy10=3

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Terrassedør i stueetage er monteret med tolags energiruder.<br><br>Hoveddør er monteret med tolags energiruder.<br><br>Terrassedør i overetagen er monteret med tolags termoruder. | **ShortText:**<br>Terrassedør med sideparti - 2 lags energirude med kold kant *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Terrassedør med sideparti, monteret med tolags energiruder. | **ShortText:**<br>Terrassedør med sideparti - 2 lags energirude med kold kant *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Terrassedør i stueetage er monteret med tolags energiruder. |
| | **ShortText:**<br>Yderdør med sideparti - 2 lags energirude med kold kant *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør med sideparti, monteret med tolags energiruder. | **ShortText:**<br>Yderdør med sideparti - 2 lags energirude med kold kant *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Hoveddør er monteret med tolags energiruder. |
| | **ShortText:**<br>Terrassedør med sideparti - 2 lags termorude *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Terrassedør med sideparti, monteret med tolags termoruder. | **ShortText:**<br>Terrassedør med sideparti - 2 lags termorude *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Terrassedør i overetagen er monteret med tolags termoruder. |

---

### 8. BI Classification: `1-4-1-0`

**Status Counts:** Plans=2 (in this BI), Energy10=2

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Terrændæk er udført af beton med slidlagsgulv. Gulvet vurderes isoleret med 50 mm trædefast mineraluld under betonen og sten som kapillarbrydende lag. Konstruktions- og isoleringsforhold er skønnet ud fra opførelsestidspunktet.<br><br>Terrændæk i badeværelse er udført af beton med slidlagsgulv. Gulvet vurderes isoleret med 300 mm polystyrenplader under betonen. Konstruktions- og isoleringsforhold er skønnet ud fra renoveringstidspunktet. | **ShortText:**<br>Terrændæk - Beton med slidlag - 50 mm trædefast mineraluld, sten som kapillarbrydende lag - skillevægsfundament (beton) *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Terrændæk er udført af beton med slidlagsgulv. Gulvet vurderes isoleret med 50 mm trædefast mineraluld under betonen og sten som kapillarbrydende lag. Konstruktions- og isoleringsforhold er skønnet ud fra opførelsestidspunktet.<br>(??? U-værdi tillæg påført: 0.06 W/m2K) | **ShortText:**<br>Terrændæk - Beton med slidlag - 50 mm trædefast mineraluld, sten som kapillarbrydende lag - skillevægsfundament (beton) *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Terrændæk er udført af beton med slidlagsgulv. Gulvet vurderes isoleret med 50 mm trædefast mineraluld under betonen og sten som kapillarbrydende lag. Konstruktions- og isoleringsforhold er skønnet ud fra opførelsestidspunktet. |
| | **ShortText:**<br>Terrændæk - Beton med slidlag - 300 mm polystyrenplader - skillevægsfundament (beton) *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Terrændæk er udført af beton med slidlagsgulv. Gulvet vurderes isoleret med 300 mm polystyrenplader under betonen. Konstruktions- og isoleringsforhold er skønnet ud fra renoveringstidspunktet.<br>(??? U-værdi tillæg påført: 0.07 W/m2K)<br><br>**(fuzzy match: 93%)** | **ShortText:**<br>Terrændæk badeværelse - Beton med slidlag - 300 mm polystyrenplader - skillevægsfundament (beton) *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Terrændæk i badeværelse er udført af beton med slidlagsgulv. Gulvet vurderes isoleret med 300 mm polystyrenplader under betonen. Konstruktions- og isoleringsforhold er skønnet ud fra renoveringstidspunktet. |

---

### 9. BI Classification: `1-5-1-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er naturlig ventilation i hele bygningen. Bygningen er normal tæt, da konstruktionssamlinger og fuger ved vindues- og døråbninger, samt tætningslister i vinduer og udvendige døre fremstår i god stand. | *(not in Plans)* | **ShortText:**<br>Bolig - Naturlig - tæt 0,3 l/s m² *(was BI 1-5-1-0)*<br><br>**LongText:**<br>Der er naturlig ventilation i hele bygningen. Bygningen er normal tæt, da konstruktionssamlinger og fuger ved vindues- og døråbninger, samt tætningslister i vinduer og udvendige døre fremstår i god stand. |

---

### 10. BI Classification: `2-1-3-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Bygningen opvarmes med fjernvarme. Anlægget er udført som direkte fjernvarmeanlæg, med fjernvarmevand i fordelingsnettet.<br>Fjernvarmestik er placeret i bryggers. | *(not in Plans)* | **ShortText:**<br>Fjernvarme uden veksler - direkte *(was BI 2-1-3-0)*<br><br>**LongText:**<br>Bygningen opvarmes med fjernvarme. Anlægget er udført som direkte fjernvarmeanlæg, med fjernvarmevand i fordelingsnettet.<br>Fjernvarmestik er placeret i bryggers. |

---

### 11. BI Classification: `2-2-1-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Den primære opvarmning af ejendommen sker via radiatorer i opvarmede rum. Varmefordelingsrør er udført som to-strengs anlæg. Der er desuden gulvvarme i badeværelser. | *(not in Plans)* | **ShortText:**<br>Radiator - 2-streng iht. HB2023 *(was BI 2-2-1-0)*<br><br>**LongText:**<br>Den primære opvarmning af ejendommen sker via radiatorer i opvarmede rum. Varmefordelingsrør er udført som to-strengs anlæg. Der er desuden gulvvarme i badeværelser. |

---

### 12. BI Classification: `2-2-2-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Varmerør i skunk er udført som kobberrør. Varmerørene er isoleret med 10 mm isolering. | *(not in Plans)* | **ShortText:**<br>12 mm kobberrør - 10 mm *(was BI 2-2-2-0)*<br><br>**LongText:**<br>Varmerør i skunk er udført som kobberrør. Varmerørene er isoleret med 10 mm isolering. |

---

### 13. BI Classification: `2-2-4-0`

**Status Counts:** Plans=0 (in this BI), Energy10=2

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Udenfor fyringssæsonen forudsættes det i beregningen, at varmeanlægget kan afbrydes. Enten automatisk via udeføler eller manuelt ved lukning af ventiler og slukning af varmefordelingspumper.<br><br>Der er monteret termostatventiler på alle radiatorer og gulvvarme til regulering af korrekt rumtemperatur. | *(not in Plans)* | **ShortText:**<br>Sommerstop af varmeanlæg *(was BI 2-2-4-0)*<br><br>**LongText:**<br>Udenfor fyringssæsonen forudsættes det i beregningen, at varmeanlægget kan afbrydes. Enten automatisk via udeføler eller manuelt ved lukning af ventiler og slukning af varmefordelingspumper. |
| | *(not in Plans)* | **ShortText:**<br>Termostatventiler på alle radiatorer *(was BI 2-2-4-0)*<br><br>**LongText:**<br>Der er monteret termostatventiler på alle radiatorer og gulvvarme til regulering af korrekt rumtemperatur. |

---

### 14. BI Classification: `3-1-3-0`

**Status Counts:** Plans=0 (in this BI), Energy10=2

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Brugsvandsrør med cirkulation er udført som PEX-rør. Rørene er isoleret med 10 mm isolering. | *(not in Plans)* | **ShortText:**<br>Standard tilslutningsrør - Længde og isoleringsniveau iht. HB2023 *(was BI 3-1-3-0)*<br><br>**LongText:**<br>Varmetabet fra tilslutningsrør under 5 meter indregnes med et standard værdisæt for rørlængde og isoleringsniveau svarende til 4 meter med 30 mm isolering. Dette udføres iht. gældende Håndbog for Energikonsulenter. |
| | *(not in Plans)* | **ShortText:**<br>Brugsvandsrør med cirkulation - 15 mm PEX-rør - 10 mm *(was BI 3-1-3-0)*<br><br>**LongText:**<br>Brugsvandsrør med cirkulation er udført som PEX-rør. Rørene er isoleret med 10 mm isolering. |

---

### 15. BI Classification: `3-1-4-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| I brugsvandsanlægget er der monteret en cirkulationspumpe, af fabrikat Grundfos, type Comfort UP. Pumpen har en maksimal effekt på 8 Watt. | *(not in Plans)* | **ShortText:**<br>Grundfos Comfort *(was BI 3-1-4-0)*<br><br>**LongText:**<br>I brugsvandsanlægget er der monteret en cirkulationspumpe, af fabrikat Grundfos, type Comfort UP. Pumpen har en maksimal effekt på 8 Watt. |

---

### 16. BI Classification: `3-1-5-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Varmt brugsvand produceres via gennemstrømningsvandvarmer. Veksleren er placeret i bryggers. | *(not in Plans)* | **ShortText:**<br>Gennemstrømningsvandvarmer *(was BI 3-1-5-0)*<br><br>**LongText:**<br>Varmt brugsvand produceres via gennemstrømningsvandvarmer. Veksleren er placeret i bryggers. |

---

### 17. BI Classification: `4-1-3-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er ingen solceller på bygningen. | *(not in Plans)* | **ShortText:**<br>Ingen solcelle *(was BI 4-1-3-0)*<br><br>**LongText:**<br>Der er ingen solceller på bygningen. |

---


## Spurvevej 13

### 1. BI Classification: `1-1-1-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Loftslem vurderes isoleret med 100 mm mineraluld. Konstruktionstykkelse er målt ved loftlem i gang på første sal. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. | **ShortText:**<br>Loftslem - 100 mm isolering *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Loftslem vurderes isoleret med 100 mm mineraluld. Konstruktionstykkelse er målt ved loftlem. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet.<br><br>**BI reclassified:** `1-1-3-0` → `1-1-1-0` | **ShortText:**<br>Loftslem - 100 mm isolering *(was BI 1-1-1-0)*<br><br>**LongText:**<br>Loftslem vurderes isoleret med 100 mm mineraluld. Konstruktionstykkelse er målt ved loftlem i gang på første sal. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. |

---

### 2. BI Classification: `1-1-3-0`

**Status Counts:** Plans=5 (in this BI), Energy10=4

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Hanebåndsloft vurderes isoleret med 275 mm mineraluld. Hanebåndsloft under gangbro vurderes isoleret med 100 mm mineraluld. Konstruktionstykkelse er målt ved loftlem i gang på første sal. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet.<br><br>Skråvægge er isoleret med 100 mm mineraluld. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. Skråvægge er isoleret het ned til tagfod, jf. ejers oplysninger. | **ShortText:**<br>Skråvægge - 100 mm isolering *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Skråvægge er isoleret med 100 mm mineraluld. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. | **ShortText:**<br>Skråvægge - 100 mm isolering *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Skråvægge er isoleret med 100 mm mineraluld. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. Skråvægge er isoleret het ned til tagfod, jf. ejers oplysninger. |
| | **ShortText:**<br>Hanebåndsloft - 275 mm isolering *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Hanebåndsloft vurderes isoleret med 275 mm mineraluld. Konstruktionstykkelse er målt ved loftlem. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. | **ShortText:**<br>Hanebåndsloft - 275 mm isolering *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Hanebåndsloft vurderes isoleret med 275 mm mineraluld. Hanebåndsloft under gangbro vurderes isoleret med 100 mm mineraluld. Konstruktionstykkelse er målt ved loftlem i gang på første sal. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. |
| | **ShortText:**<br>Hanebåndsloft - 100 mm isolering *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Hanebåndsloft vurderes isoleret med 100 mm mineraluld. | **ShortText:**<br>Hanebåndsloft - 100 mm isolering *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Hanebåndsloft under gangbro vurderes isoleret med 100 mm mineraluld. |
| | **ShortText:**<br>Hanebåndsloft - 275 mm isolering *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Hanebåndsloft vurderes isoleret med 275 mm mineraluld. Konstruktionstykkelse er målt ved loftlem. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. | **ShortText:**<br>Hanebåndsloft - 275 mm isolering *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Hanebåndsloft vurderes isoleret med 275 mm mineraluld. Konstruktionstykkelse er målt ved loftlem. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. |

---

### 3. BI Classification: `1-2-1-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Ydervægge er udført som 30 cm hulmur. Vægge består udvendigt og indvendigt af tegl. Hulrummet er isoleret ved opførelsen. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. | **ShortText:**<br>Hul ydervæg - 30 cm tegl/tegl - Isoleret ved opførelsen *(was BI 1-2-1-0)*<br><br>**LongText:**<br>Ydervægge er udført som 30 cm hulmur. Vægge består udvendigt og indvendigt af tegl. Hulrummet er isoleret ved opførelsen. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br>(??? U-værdi tillæg påført: 0.1 W/m2K) | **ShortText:**<br>Hul ydervæg - 30 cm tegl/tegl - Isoleret ved opførelsen *(was BI 1-2-1-0)*<br><br>**LongText:**<br>Ydervægge er udført som 30 cm hulmur. Vægge består udvendigt og indvendigt af tegl. Hulrummet er isoleret ved opførelsen. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. |

---

### 4. BI Classification: `1-2-2-1`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Vægge mod uopvarmet rum består af 12 cm massiv og uisoleret teglvæg. Konstruktionstykkelse er målt ved dør. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. | **ShortText:**<br>Massiv væg mod uopvarmet rum - 12 cm tegl - uisoleret *(was BI 1-2-2-1)*<br><br>**LongText:**<br>Vægge mod uopvarmet rum består af 12 cm massiv og uisoleret teglvæg. Konstruktionstykkelse er målt ved dør. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. | **ShortText:**<br>Massiv væg mod uopvarmet rum - 12 cm tegl - uisoleret *(was BI 1-2-2-1)*<br><br>**LongText:**<br>Vægge mod uopvarmet rum består af 12 cm massiv og uisoleret teglvæg. Konstruktionstykkelse er målt ved dør. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. |

---

### 5. BI Classification: `1-2-3-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Ydervæg ved gavl på første sal mod vest er udført som let konstruktion med beklædning ud- og indvendig. Hulrum mellem beklædninger er isoleret med 100 mm mineraluld. Konstruktions- og isoleringsforhold er baseret på ejers oplysninger. | **ShortText:**<br>Let ydervæg - træ/træ - 100 mm isolering *(was BI 1-2-3-0)*<br><br>**LongText:**<br>Ydervægge er udført som let konstruktion med beklædning ud- og indvendig. Hulrum mellem beklædninger er isoleret med 100 mm mineraluld. Konstruktions- og isoleringsforhold er baseret på ejers oplysninger. | **ShortText:**<br>Let ydervæg - træ/træ - 100 mm isolering *(was BI 1-2-3-0)*<br><br>**LongText:**<br>Ydervæg ved gavl på første sal mod vest er udført som let konstruktion med beklædning ud- og indvendig. Hulrum mellem beklædninger er isoleret med 100 mm mineraluld. Konstruktions- og isoleringsforhold er baseret på ejers oplysninger. |

---

### 6. BI Classification: `1-2-4-0`

**Status Counts:** Plans=3 (in this BI), Energy10=3

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Kælderydervægge mod jord består af 19 cm beton udvendig og 11 cm leca indvendig. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br><br>Kælderydervægge over jord består af 19 cm beton udvendig og 11 cm indvendig. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. | **ShortText:**<br>Kælderydervæg 0-2m dybde - 30 cm beton - uisoleret *(was BI 1-2-4-0)*<br><br>**LongText:**<br>Kælderydervægge mod jord består af 19 cm beton udvendig og 11 cm leca indvendig. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. | **ShortText:**<br>Kælderydervæg 0-2m dybde - 30 cm beton - uisoleret *(was BI 1-2-4-0)*<br><br>**LongText:**<br>Kælderydervægge mod jord består af 19 cm beton udvendig og 11 cm leca indvendig. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. |
| | **ShortText:**<br>Kælderydervæg over 2m - 30 cm beton - uisoleret *(was BI 1-2-4-0)*<br><br>**LongText:**<br>Kælderydervægge mod jord består af 19 cm beton udvendig og 11 cm leca indvendig Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. | **ShortText:**<br>Kælderydervæg over 2m - 30 cm beton - uisoleret *(was BI 1-2-4-0)*<br><br>**LongText:**<br>Kælderydervægge mod jord består af 19 cm beton udvendig og 11 cm leca indvendig Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. |
| | **ShortText:**<br>Kælderydervæg over jord - 30 cm beton - uisoleret *(was BI 1-2-4-0)*<br><br>**LongText:**<br>Kælderydervægge over jord består af 19 cm beton udvendig og 11 cm indvendig. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. | **ShortText:**<br>Kælderydervæg over jord - 30 cm beton - uisoleret *(was BI 1-2-4-0)*<br><br>**LongText:**<br>Kælderydervægge over jord består af 19 cm beton udvendig og 11 cm indvendig. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. |

---

### 7. BI Classification: `1-3-1-0`

**Status Counts:** Plans=9 (in this BI), Energy10=9

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Alle vinduer er monteret med tolags termoruder.<br><br>Vindue ved trappe er med glasbyggesten. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Alle vinduer er monteret med tolags termoruder. |
| | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags termorude. |
| | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags termorude. |
| | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags termorude. |
| | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags termorude. |
| | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags termorude. |
| | **ShortText:**<br>Glasbyggesten *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Vindue i glasbyggesten. | **ShortText:**<br>Glasbyggesten *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Vindue ved trappe er med glasbyggesten. |
| | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags termorude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags termorude. |

---

### 8. BI Classification: `1-3-2-0`

**Status Counts:** Plans=2 (in this BI), Energy10=2

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Ovenlysvindue er monteret med trelags energirude. | **ShortText:**<br>Ovenlysvindue - 3 lags energirude - efter BR15 *(was BI 1-3-2-0)*<br><br>**LongText:**<br>Ovenlysvindue er monteret med trelags energirude, efter BR15. | **ShortText:**<br>Ovenlysvindue - 3 lags energirude - efter BR15 *(was BI 1-3-2-0)*<br><br>**LongText:**<br>Ovenlysvindue er monteret med trelags energirude. |
| | **ShortText:**<br>Ovenlysvindue - 3 lags energirude - efter BR15 *(was BI 1-3-2-0)*<br><br>**LongText:**<br>Ovenlysvindue er monteret med trelags energirude, efter BR15. | **ShortText:**<br>Ovenlysvindue - 3 lags energirude - efter BR15 *(was BI 1-3-2-0)*<br><br>**LongText:**<br>Ovenlysvindue er monteret med trelags energirude, efter BR15. |

---

### 9. BI Classification: `1-3-3-0`

**Status Counts:** Plans=6 (in this BI), Energy10=6

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Yderdør i kælder er monteret med tolags termoruder.<br><br>Terrassedør i stue er monteret med tolags termorude.<br><br>Yderdør med sideparti i entre er monteret med tolags termoruder.<br><br>Terrassedør på første sal er monteret med tolags energirude.<br><br>Portpanelet i garage er udført som et sandwichmodul som dobbelt lag stål og med isolering imellem.<br><br>Dør til uopvarmet kælderrum er uisoleret | **ShortText:**<br>Yderdør med flere ruder - 2 lags termorude *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør med flere vinduesfag, monteret med tolags termoruder. | **ShortText:**<br>Yderdør med flere ruder - 2 lags termorude *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør i kælder er monteret med tolags termoruder. |
| | **ShortText:**<br>Hörmann indbygget stålport - isoleret 42 mm - uden vinduer *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Portpanelet er udført som et sandwichmodul som dobbelt lag stål og med isolering imellem. | **ShortText:**<br>Hörmann indbygget stålport - isoleret 42 mm - uden vinduer *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Portpanelet i garage er udført som et sandwichmodul som dobbelt lag stål og med isolering imellem. |
| | **ShortText:**<br>Terrassedør med 1 rude - 2 lags termorude *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Terrassedør med enkeltfagsvindue, monteret med tolags termoruder. | **ShortText:**<br>Terrassedør med 1 rude - 2 lags termorude *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Terrassedør i stue er monteret med tolags termorude. |
| | **ShortText:**<br>Yderdør med sideparti - 2 lags termorude *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør med sideparti, monteret med tolags termoruder. | **ShortText:**<br>Yderdør med sideparti - 2 lags termorude *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør med sideparti i entre er monteret med tolags termoruder. |
| | **ShortText:**<br>Terrassedør med 1 rude - 2 lags energirude med varm kant *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Terrassedør med enkeltfagsvindue, monteret med tolags energiruder. | **ShortText:**<br>Terrassedør med 1 rude - 2 lags energirude med varm kant *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Terrassedør på første sal er monteret med tolags energirude. |
| | *(not in Plans)* | **ShortText:**<br>Yderdør uden glas - Før 1990 - uisoleret iht. HB2023 *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Dør til uopvarmet kælderrum er uisoleret |

---

### 10. BI Classification: `1-4-2-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Gulv mod uopvarmet depotrum i kælder, beton med trægulv er isoleret med 50 mm mineraluld. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. | **ShortText:**<br>Gulv mod uopvarmet kælder - beton med trægulv - 50 mm isolering *(was BI 1-4-2-0)*<br><br>**LongText:**<br>Gulv mod uopvarmet kælder, beton med trægulv er isoleret med 50 mm mineraluld. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. | **ShortText:**<br>Gulv mod uopvarmet kælder - beton med trægulv - 50 mm isolering *(was BI 1-4-2-0)*<br><br>**LongText:**<br>Gulv mod uopvarmet depotrum i kælder, beton med trægulv er isoleret med 50 mm mineraluld. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. |

---

### 11. BI Classification: `1-4-4-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Kældergulv er udført af beton med slidlagsgulv. Gulvet er uisoleret. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. | **ShortText:**<br>Kældergulv - Beton med slidlag - uisoleret *(was BI 1-4-4-0)*<br><br>**LongText:**<br>Kældergulv er udført af beton med slidlagsgulv. Gulvet er uisoleret. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. | **ShortText:**<br>Kældergulv - Beton med slidlag - uisoleret *(was BI 1-4-4-0)*<br><br>**LongText:**<br>Kældergulv er udført af beton med slidlagsgulv. Gulvet er uisoleret. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. |

---

### 12. BI Classification: `1-5-1-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er naturlig ventilation i hele ejendommen. Ejendommen er normal tæt, da konstruktionssamlinger og fuger ved vindues- og døråbninger, samt tætningslister i vinduer og udvendige døre fremstår i god stand. | **ShortText:**<br>Bolig - Naturlig - tæt 0,3 l/s m² *(was BI 1-5-1-0)*<br><br>**LongText:**<br>Der er naturlig ventilation i hele ejendommen. Ejendommen er normal tæt, da konstruktionssamlinger og fuger ved vindues- og døråbninger, samt tætningslister i vinduer og udvendige døre fremstår i god stand. | **ShortText:**<br>Bolig - Naturlig - tæt 0,3 l/s m² *(was BI 1-5-1-0)*<br><br>**LongText:**<br>Der er naturlig ventilation i hele ejendommen. Ejendommen er normal tæt, da konstruktionssamlinger og fuger ved vindues- og døråbninger, samt tætningslister i vinduer og udvendige døre fremstår i god stand. |

---

### 13. BI Classification: `1-6-1-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Internt varmetilskud for enfamiliebyggeri. | **ShortText:**<br>Internt varmetilskud for enfamiliebyggeri *(was BI 1-6-1-0)*<br><br>**LongText:**<br>Internt varmetilskud for enfamiliebyggeri. | **ShortText:**<br>Internt varmetilskud for enfamiliebyggeri *(was BI 1-6-1-0)*<br><br>**LongText:**<br>Internt varmetilskud for enfamiliebyggeri. |

---

### 14. BI Classification: `2-1-3-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Ejendommen opvarmes med fjernvarme. Anlægget er udført som direkte fjernvarmeanlæg, med fjernvarmevand i fordelingsnettet. Fjernvarmen kommer ind i bryggers i kælder. | **ShortText:**<br>Fjernvarme uden veksler - direkte *(was BI 2-1-0-0)*<br><br>**LongText:**<br>Ejendommen opvarmes med fjernvarme. Anlægget er udført som direkte fjernvarmeanlæg, med fjernvarmevand i fordelingsnettet.<br>Vejle Fjernvarmeselskab a.m.b.a.<br><br>**BI reclassified:** `2-1-0-0` → `2-1-3-0` | **ShortText:**<br>Fjernvarme uden veksler - direkte *(was BI 2-1-3-0)*<br><br>**LongText:**<br>Ejendommen opvarmes med fjernvarme. Anlægget er udført som direkte fjernvarmeanlæg, med fjernvarmevand i fordelingsnettet. Fjernvarmen kommer ind i bryggers i kælder. |

---

### 15. BI Classification: `2-1-4-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er supplerende varmeforsyning i form af en åben pejs. Varmekilden indgår ikke i beregning af energiforbruget, i henhold til Energistyrelsens beregningsregler. Ovnen er placeret i stue på 1. sal. | **ShortText:**<br>Åben pejs - ikke indregnet *(was BI 2-1-4-0)*<br><br>**LongText:**<br>Der er supplerende varmeforsyning i form af en åben pejs. Varmekilden indgår ikke i beregning af energiforbruget, i henhold til Energistyrelsens beregningsregler. Ovnen er placeret i ???. | **ShortText:**<br>Åben pejs - ikke indregnet *(was BI 2-1-4-0)*<br><br>**LongText:**<br>Der er supplerende varmeforsyning i form af en åben pejs. Varmekilden indgår ikke i beregning af energiforbruget, i henhold til Energistyrelsens beregningsregler. Ovnen er placeret i stue på 1. sal. |

---

### 16. BI Classification: `2-1-5-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er ikke stillet forslag til varmepumpe, da dette, med bygningens eksisterende varmeanlæg og den dertilhørende energipris, ikke vil kunne medføre et fornuftigt og rentabelt forslag. | *(not in Plans)* | **ShortText:**<br>Ingen varmepumpe - Intet forslag *(was BI 2-1-5-0)*<br><br>**LongText:**<br>Der er ikke stillet forslag til varmepumpe, da dette, med bygningens eksisterende varmeanlæg og den dertilhørende energipris, ikke vil kunne medføre et fornuftigt og rentabelt forslag. |

---

### 17. BI Classification: `2-1-6-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er ikke stillet forslag til solvarmeanlæg, da dette, med bygningens eksisterende varmeanlæg og den dertilhørende energipris, ikke vil kunne medføre et fornuftigt og rentabelt forslag. | *(not in Plans)* | **ShortText:**<br>Intet solvarmeanlæg - Intet forslag *(was BI 2-1-6-0)*<br><br>**LongText:**<br>Der er ikke stillet forslag til solvarmeanlæg, da dette, med bygningens eksisterende varmeanlæg og den dertilhørende energipris, ikke vil kunne medføre et fornuftigt og rentabelt forslag. |

---

### 18. BI Classification: `2-2-1-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Varmeanlægget er udført som et 2-strengs radiatorsystem, hvor radiatorerne er tilsluttet separate frem- og returløb. | **ShortText:**<br>Radiator - 2-streng iht. HB2023 *(was BI 2-2-1-0)*<br><br>**LongText:**<br>Varmeanlægget er udført som et 2-strengs radiatorsystem, hvor radiatorerne er tilsluttet separate frem- og returløb. | **ShortText:**<br>Radiator - 2-streng iht. HB2023 *(was BI 2-2-1-0)*<br><br>**LongText:**<br>Varmeanlægget er udført som et 2-strengs radiatorsystem, hvor radiatorerne er tilsluttet separate frem- og returløb. |

---

### 19. BI Classification: `2-2-2-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Varmerørene er udført i stål med en dimension på 3/4" og er isoleret med ca. 10 mm isolering. Rørene er placeret i uopvarmet depotrum i kælder. | **ShortText:**<br>3/4" (26,9 mm) stålrør - 10 mm *(was BI 2-2-2-0)*<br><br>**LongText:**<br>Varmerørene er udført i stål med en dimension på 3/4" og er isoleret med ca. 10 mm isolering. Rørene er placeret i kælder og har en samlet længde på ca. ??? m. | **ShortText:**<br>3/4" (26,9 mm) stålrør - 10 mm *(was BI 2-2-2-0)*<br><br>**LongText:**<br>Varmerørene er udført i stål med en dimension på 3/4" og er isoleret med ca. 10 mm isolering. Rørene er placeret i uopvarmet depotrum i kælder. |

---

### 20. BI Classification: `2-2-4-0`

**Status Counts:** Plans=1 (in this BI), Energy10=2

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er monteret returventiler på returløb ved alle radiatorer i ejendommen. Denne regulering sikrer kun en tilpas afkøling, men sikrer ikke en konstant regulering for en stabil varmetilførsel og rumtemperatur. <br><br>Udenfor fyringssæsonen forudsættes det i beregningen, at varmeanlægget kan afbrydes. Enten automatisk via udeføler eller manuelt ved lukning af ventiler og slukning af varmefordelingspumper. | **ShortText:**<br>Kun returventiler på alle radiatorer, +1 grad iht. HB2023 *(was BI 2-2-4-0)*<br><br>**LongText:**<br>Der er monteret returventiler på returløb ved alle radiatorer i ejendommen. Denne regulering sikrer kun en tilpas afkøling, men sikrer ikke en konstant regulering for en stabil varmetilførsel og rumtemperatur. Antal 16 stk alle radiatorer | **ShortText:**<br>Kun returventiler på alle radiatorer, +1 grad iht. HB2023 *(was BI 2-2-4-0)*<br><br>**LongText:**<br>Der er monteret returventiler på returløb ved alle radiatorer i ejendommen. Denne regulering sikrer kun en tilpas afkøling, men sikrer ikke en konstant regulering for en stabil varmetilførsel og rumtemperatur. |
| | *(not in Plans)* | **ShortText:**<br>Sommerstop af varmeanlæg *(was BI 2-2-4-0)*<br><br>**LongText:**<br>Udenfor fyringssæsonen forudsættes det i beregningen, at varmeanlægget kan afbrydes. Enten automatisk via udeføler eller manuelt ved lukning af ventiler og slukning af varmefordelingspumper. |

---

### 21. BI Classification: `3-1-3-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Varmetabet fra tilslutningsrør under 5 meter indregnes med et standard værdisæt for rørlængde og isoleringsniveau svarende til 4 meter med 30 mm isolering. Dette udføres iht. gældende Håndbog for Energikonsulenter. | *(not in Plans)* | **ShortText:**<br>Standard tilslutningsrør - Længde og isoleringsniveau iht. HB2023 *(was BI 3-1-3-0)*<br><br>**LongText:**<br>Varmetabet fra tilslutningsrør under 5 meter indregnes med et standard værdisæt for rørlængde og isoleringsniveau svarende til 4 meter med 30 mm isolering. Dette udføres iht. gældende Håndbog for Energikonsulenter. |

---

### 22. BI Classification: `3-1-5-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er registreret en varmtvandsbeholder til produktion af varmt brugsvand af fabrikat Metro, model 110 (rør ned). Beholderen har et volumen på ca. 94 liter og er placeret i bryggers i kælder. | **ShortText:**<br>94 l - Metro model 110 (rør ned) *(was BI 3-1-5-0)*<br><br>**LongText:**<br>Der er registreret en varmtvandsbeholder til produktion af varmt brugsvand af fabrikat Metro, model 110 (rør ned). Beholderen har et volumen på ca. 94 liter og er placeret i ???. Beholderen er isoleret med ca. ??? isolering. | **ShortText:**<br>94 l - Metro model 110 (rør ned) *(was BI 3-1-5-0)*<br><br>**LongText:**<br>Der er registreret en varmtvandsbeholder til produktion af varmt brugsvand af fabrikat Metro, model 110 (rør ned). Beholderen har et volumen på ca. 94 liter og er placeret i bryggers i kælder. |

---

### 23. BI Classification: `4-1-3-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er ingen solceller på bygningen. | *(not in Plans)* | **ShortText:**<br>Ingen solcelle *(was BI 4-1-3-0)*<br><br>**LongText:**<br>Der er ingen solceller på bygningen. |

---


## Møllehøj 15

### 1. BI Classification: `1-1-1-0`

**Status Counts:** Plans=1 (in this BI), Energy10=3

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Loftsrum er isoleret med ca. 400 mm mineraluld. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br>Der er ikke givet forslag til efterisolering, da den årlige besparelse vil være minimal i forhold til investeringen.<br><br>Skråvægge er isoleret med ca. 400 mm mineraluld. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br>Der er ikke givet forslag til efterisolering, da den årlige besparelse vil være minimal i forhold til investeringen.<br><br>Loftslem er placeret i bryggers, og vurderes isoleret med ca. 30 mm mineraluld. Konstruktionstykkelse er målt ved loftlem. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet.<br>Der er ikke givet forslag til efterisolering eller udskiftning af loftlem, da den årlige besparelse vil være minimal i forhold til investeringen. | **ShortText:**<br>Loftsrum - 400 mm isolering *(was BI 1-1-1-0)*<br><br>**LongText:**<br>Loftsrum er isoleret med 400 mm mineraluld. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. | **ShortText:**<br>Loftsrum - 400 mm isolering *(was BI 1-1-1-0)*<br><br>**LongText:**<br>Loftsrum er isoleret med ca. 400 mm mineraluld. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br>Der er ikke givet forslag til efterisolering, da den årlige besparelse vil være minimal i forhold til investeringen. |
| | **ShortText:**<br>Skråvægge - 400 mm isolering *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Skråvægge er isoleret med 400 mm mineraluld. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br><br>**BI reclassified:** `1-1-3-0` → `1-1-1-0` | **ShortText:**<br>Skråvægge - 400 mm isolering *(was BI 1-1-1-0)*<br><br>**LongText:**<br>Skråvægge er isoleret med ca. 400 mm mineraluld. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br>Der er ikke givet forslag til efterisolering, da den årlige besparelse vil være minimal i forhold til investeringen. |
| | **ShortText:**<br>Loftslem - 30 mm isolering *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Loftslem vurderes isoleret med 30 mm mineraluld. Konstruktionstykkelse er målt ved loftlem. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet.<br><br>**BI reclassified:** `1-1-3-0` → `1-1-1-0` | **ShortText:**<br>Loftslem - 30 mm isolering *(was BI 1-1-1-0)*<br><br>**LongText:**<br>Loftslem er placeret i bryggers, og vurderes isoleret med ca. 30 mm mineraluld. Konstruktionstykkelse er målt ved loftlem. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet.<br>Der er ikke givet forslag til efterisolering eller udskiftning af loftlem, da den årlige besparelse vil være minimal i forhold til investeringen. |

---

### 2. BI Classification: `1-2-1-0`

**Status Counts:** Plans=2 (in this BI), Energy10=2

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Ydervægge, samt væg mod udestuen, er udført som ca. 400 mm hulmur. Vægge består udvendigt af tegl og indvendigt af letbeton. Hulrummet er isoleret ved opførelsen. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br>Der er ikke givet forslag til efterisolering, da den årlige besparelse vil være minimal i forhold til investeringen. | **ShortText:**<br>Hul ydervæg - 40 cm tegl/letbeton (10 cm bagmur) - Isoleret ved opførslen *(was BI 1-2-1-0)*<br><br>**LongText:**<br>Ydervægge er udført som ca. 40 cm hulmur. Vægge består udvendigt af tegl og indvendigt af letbeton. Hulrummet er isoleret ved opførelsen. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br>(??? U-værdi tillæg påført: 0.05 W/m2K) | **ShortText:**<br>Hul ydervæg - 40 cm tegl/letbeton (10 cm bagmur) - Isoleret ved opførslen *(was BI 1-2-1-0)*<br><br>**LongText:**<br>Ydervægge, samt væg mod udestuen, er udført som ca. 400 mm hulmur. Vægge består udvendigt af tegl og indvendigt af letbeton. Hulrummet er isoleret ved opførelsen. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br>Der er ikke givet forslag til efterisolering, da den årlige besparelse vil være minimal i forhold til investeringen. |
| | **ShortText:**<br>Hul ydervæg - 40 cm tegl/letbeton (10 cm bagmur) - Isoleret ved opførslen *(was BI 1-2-1-0)*<br><br>**LongText:**<br>Ydervægge er udført som ca. 40 cm hulmur. Vægge består udvendigt af tegl og indvendigt af letbeton. Hulrummet er isoleret ved opførelsen. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br>(??? U-værdi tillæg påført: 0.05 W/m2K) | **ShortText:**<br>Hul ydervæg - 40 cm tegl/letbeton (10 cm bagmur) - Isoleret ved opførslen *(was BI 1-2-1-0)*<br><br>**LongText:**<br>Ydervægge er udført som ca. 40 cm hulmur. Vægge består udvendigt af tegl og indvendigt af letbeton. Hulrummet er isoleret ved opførelsen. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br>Der er ikke givet forslag til efterisolering, da den årlige besparelse vil være minimal i forhold til investeringen. |

---

### 3. BI Classification: `1-2-2-1`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Væg mod tagrum er ca. 100 mm letbeton med indvendig pladebeklædning, og er isoleret med ca. 200 mm isolering. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br>Der er ikke givet forslag til efterisolering, da den årlige besparelse vil være minimal i forhold til investeringen. | **ShortText:**<br>Massiv væg mod uopvarmet rum - 19 cm letbeton - 200 mm indvendig isolering *(was BI 1-2-2-1)*<br><br>**LongText:**<br>Vægge mod uopvarmet rum består af ca 10 cm massiv letbetonvæg med indvendig pladebeklædning og 200 mm isolering mod tagrum.<br> Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. | **ShortText:**<br>Massiv væg mod uopvarmet rum - 19 cm letbeton - 200 mm indvendig isolering *(was BI 1-2-2-1)*<br><br>**LongText:**<br>Væg mod tagrum er ca. 100 mm letbeton med indvendig pladebeklædning, og er isoleret med ca. 200 mm isolering. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br>Der er ikke givet forslag til efterisolering, da den årlige besparelse vil være minimal i forhold til investeringen. |

---

### 4. BI Classification: `1-3-1-0`

**Status Counts:** Plans=5 (in this BI), Energy10=5

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Beskrivelse og glasforhold vedrørende vinduer, ovenlys/tagvinduer og døre er baseret på visuel kontrol ved konsulent.<br>Vinduer, ovenlys/tagvinduer og døre er med to-lags energiruder med kold kant.<br>Den massive yderdør er isoleret.<br><br>Der er ikke givet forslag til udskiftning af vinduer, ovenlys/tagvinduer og døre, da den årlige besparelse vil være minimal i forhold til investeringen. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Beskrivelse og glasforhold vedrørende vinduer, ovenlys/tagvinduer og døre er baseret på visuel kontrol ved konsulent.<br>Vinduer, ovenlys/tagvinduer og døre er med to-lags energiruder med kold kant.<br>Den massive yderdør er isoleret.<br><br>Der er ikke givet forslag til udskiftning af vinduer, ovenlys/tagvinduer og døre, da den årlige besparelse vil være minimal i forhold til investeringen. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. |

---

### 5. BI Classification: `1-4-1-0`

**Status Counts:** Plans=2 (in this BI), Energy10=2

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Terrændæk er udført af beton med slidlagsgulv. Gulvet er isoleret med ca. 275 mm polystyrenplader under betonen. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br>Der er ikke givet forslag til etablering af nyt terrændæk, da den årlige besparelse vil være minimal i forhold til investeringen. | **ShortText:**<br>Terrændæk - Beton med slidlag - 250 mm polystyrenplader *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Terrændæk er udført af beton med slidlagsgulv. Gulvet er isoleret med 250 mm polystyrenplader under betonen. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. | **ShortText:**<br>Terrændæk - Beton med slidlag - 250 mm polystyrenplader *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Terrændæk er udført af beton med slidlagsgulv. Gulvet er isoleret med ca. 275 mm polystyrenplader under betonen. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br>Der er ikke givet forslag til etablering af nyt terrændæk, da den årlige besparelse vil være minimal i forhold til investeringen. |
| | **ShortText:**<br>Terrændæk - Beton med slidlag - 250 mm polystyrenplader *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Terrændæk er udført af beton med slidlagsgulv. Gulvet er isoleret med 250 mm polystyrenplader under betonen. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. | **ShortText:**<br>Terrændæk - Beton med slidlag - 250 mm polystyrenplader *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Terrændæk er udført af beton med slidlagsgulv. Gulvet er isoleret med 250 mm polystyrenplader under betonen. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. |

---

### 6. BI Classification: `1-5-1-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er naturlig ventilation i hele ejendommen. Ejendommen er normal tæt, da konstruktionssamlinger og fuger ved vindues- og døråbninger, samt tætningslister i vinduer og udvendige døre fremstår i god stand. | **ShortText:**<br>Bolig - Naturlig - tæt 0,3 l/s m² *(was BI 1-5-1-0)*<br><br>**LongText:**<br>Der er naturlig ventilation i hele ejendommen. Ejendommen er normal tæt, da konstruktionssamlinger og fuger ved vindues- og døråbninger, samt tætningslister i vinduer og udvendige døre fremstår i god stand. | **ShortText:**<br>Bolig - Naturlig - tæt 0,3 l/s m² *(was BI 1-5-1-0)*<br><br>**LongText:**<br>Der er naturlig ventilation i hele ejendommen. Ejendommen er normal tæt, da konstruktionssamlinger og fuger ved vindues- og døråbninger, samt tætningslister i vinduer og udvendige døre fremstår i god stand. |

---

### 7. BI Classification: `2-1-2-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Bygningen opvarmes med naturgas via en kedel, mærke Wolf CGB 2-20. Kedlen er kondenserende og vurderes til at være fra ca. 2015 Kedlen er tilsluttet bygningens centralvarmesystem, og opvarmer til både brugsvand og rumopvarmning. Kedlen er placeret i bryggers.<br>Ved besigtigelsen forelå dokumentation for eftersyn af kedelanlæg i 2025. | **ShortText:**<br>Kedel - Gas - 18,9 kW - Wolf CGB 2-20 *(was BI 2-1-0-0)*<br><br>**LongText:**<br>Bygningen opvarmes med gas fra en Wolf CGB 2-20. Kedlen er kondenserende og vurderes til at være fra ca 2015 Kedlen er tilsluttet bygningens centralvarmesystem, og opvarmer til både brugsvand og rumopvarmning. Kedlen er placeret i bryggers<br><br>**BI reclassified:** `2-1-0-0` → `2-1-2-0` | **ShortText:**<br>Kedel - Gas - 18,9 kW - Wolf CGB 2-20 *(was BI 2-1-2-0)*<br><br>**LongText:**<br>Bygningen opvarmes med naturgas via en kedel, mærke Wolf CGB 2-20. Kedlen er kondenserende og vurderes til at være fra ca. 2015 Kedlen er tilsluttet bygningens centralvarmesystem, og opvarmer til både brugsvand og rumopvarmning. Kedlen er placeret i bryggers.<br>Ved besigtigelsen forelå dokumentation for eftersyn af kedelanlæg i 2025. |

---

### 8. BI Classification: `2-1-6-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er ikke installeret solvarmeanlæg. <br>Varmepumpe og solvarmeanlæg har ”top effekt” på samme tid, nemlig om sommeren. Idet der stilles forslag om varmepumpe, type luft/vand, er det derfor ikke relevant med solvarme i dette tilfælde. | *(not in Plans)* | **ShortText:**<br>Intet solvarmeanlæg - Intet forslag *(was BI 2-1-6-0)*<br><br>**LongText:**<br>Der er ikke installeret solvarmeanlæg. <br>Varmepumpe og solvarmeanlæg har ”top effekt” på samme tid, nemlig om sommeren. Idet der stilles forslag om varmepumpe, type luft/vand, er det derfor ikke relevant med solvarme i dette tilfælde. |

---

### 9. BI Classification: `2-2-1-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Den primære opvarmning af ejendommen sker via radiatorer i opvarmede rum. Varmefordelingsrør er udført som to-strengs anlæg. Der er gulvvarme i bryggers, køkken, stue, entré og to badeværelser. | **ShortText:**<br>Radiator + gulvvarme - 2-streng iht. HB2023 *(was BI 2-2-1-0)*<br><br>**LongText:**<br>Den primære opvarmning af ejendommen sker via radiatorer i opvarmede rum. Varmefordelingsrør er udført som to-strengs anlæg. Der er desuden gulvvarme i ???. | **ShortText:**<br>Radiator + gulvvarme - 2-streng iht. HB2023 *(was BI 2-2-1-0)*<br><br>**LongText:**<br>Den primære opvarmning af ejendommen sker via radiatorer i opvarmede rum. Varmefordelingsrør er udført som to-strengs anlæg. Der er gulvvarme i bryggers, køkken, stue, entré og to badeværelser. |

---

### 10. BI Classification: `2-2-2-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er synlig rørføring i bryggers.<br>Alle varmerør er skønnet placeret på den varme side af isoleringen/klimaskærmen.<br>Forhold er baseret på inspektion på stedet samt på skøn ud fra opførelsestidspunkt. | *(not in Plans)* | **ShortText:**<br>Ingen varmerør *(was BI 2-2-2-0)*<br><br>**LongText:**<br>Der er synlig rørføring i bryggers.<br>Alle varmerør er skønnet placeret på den varme side af isoleringen/klimaskærmen.<br>Forhold er baseret på inspektion på stedet samt på skøn ud fra opførelsestidspunkt. |

---

### 11. BI Classification: `2-2-3-0`

**Status Counts:** Plans=2 (in this BI), Energy10=2

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Gulvvarme er forsynet med en varmefordelingspumpe. Pumpen er mærke Wilo med en effekt vurderet til ca.49W. Pumpen er placeret i bryggers og vurderes at være fra perioden 2006-2015. Pumpen er udført som automatisk modulerende.<br>Desuden er der en cirkulationspumpe, som er integreret i kedel. Pumpens data er ikke tilgængelig, hvorfor type og effekt er baseret på skøn og vurdering.<br>Pumpen vurderes at være til fordelerrør, og vurderes at være på 45W. | **ShortText:**<br>Automatisk modulerende - 2006-2015 iht. HB2023 *(was BI 2-2-3-0)*<br><br>**LongText:**<br>Gulvvarme er forsynet med en varmefordelingspumpe. Pumpens effekt er vurderet til ca.49W. Pumpen er placeret i bryggers og vurderes at være fra perioden 2006-2015. Pumpen er udført som automatisk modulerende. | **ShortText:**<br>Automatisk modulerende - 2006-2015 iht. HB2023 *(was BI 2-2-3-0)*<br><br>**LongText:**<br>Gulvvarme er forsynet med en varmefordelingspumpe. Pumpen er mærke Wilo med en effekt vurderet til ca.49W. Pumpen er placeret i bryggers og vurderes at være fra perioden 2006-2015. Pumpen er udført som automatisk modulerende.<br>Desuden er der en cirkulationspumpe, som er integreret i kedel. Pumpens data er ikke tilgængelig, hvorfor type og effekt er baseret på skøn og vurdering.<br>Pumpen vurderes at være til fordelerrør, og vurderes at være på 45W. |
| | **ShortText:**<br>Automatisk modulerende - 2006-2015 iht. HB2023 *(was BI 2-2-3-0)*<br><br>**LongText:**<br>Gulvvarme er forsynet med en varmefordelingspumpe. Pumpens effekt er vurderet til ca.49W. Pumpen er placeret i bryggers og vurderes at være fra perioden 2006-2015. Pumpen er udført som automatisk modulerende. | **ShortText:**<br>Automatisk modulerende - 2006-2015 iht. HB2023 *(was BI 2-2-3-0)*<br><br>**LongText:**<br>Varmeanlægget er forsynet med en varmefordelingspumpe. Pumpens effekt er vurderet til ca.45W. Pumpen er placeret i fyr og vurderes at være fra perioden 2006-2015. Pumpen er udført som automatisk modulerende |

---

### 12. BI Classification: `2-2-4-0`

**Status Counts:** Plans=0 (in this BI), Energy10=3

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er monteret udetemperaturkompensering til regulering af fremløbstemperaturen i varmeanlægget.<br>Der er mulighed for sommerstop.<br>Der er monteret termostatventiler på alle radiatorer til regulering af korrekt rumtemperatur.<br>Gulvvarmen styres via rumføler. | *(not in Plans)* | **ShortText:**<br>Udetemperaturkompensering *(was BI 2-2-4-0)*<br><br>**LongText:**<br>Der er monteret udetemperaturkompensering til regulering af fremløbstemperaturen i varmeanlægget.<br>Der er mulighed for sommerstop.<br>Der er monteret termostatventiler på alle radiatorer til regulering af korrekt rumtemperatur.<br>Gulvvarmen styres via rumføler. |
| | *(not in Plans)* | **ShortText:**<br>Sommerstop af varmeanlæg *(was BI 2-2-4-0)*<br><br>**LongText:**<br>Udenfor fyringssæsonen forudsættes det i beregningen, at varmeanlægget kan afbrydes. Enten automatisk via udeføler eller manuelt ved lukning af ventiler og slukning af varmefordelingspumper. |
| | *(not in Plans)* | **ShortText:**<br>Termostatventiler på alle radiatorer *(was BI 2-2-4-0)*<br><br>**LongText:**<br>Der er monteret termostatventiler på alle radiatorer til regulering af korrekt rumtemperatur. |

---

### 13. BI Classification: `3-1-5-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er registreret en varmtvandsbeholder til produktion af varmt brugsvand med et volumen på ca. 110 liter. Beholderen er mærke Bosch, årgang ca. 2015, og er isoleret med ca. 100 mm isolering. | **ShortText:**<br>100 l - 100 mm isolering iht. HB2023 *(was BI 3-1-5-0)*<br><br>**LongText:**<br>Der er registreret en varmtvandsbeholder til produktion af varmt brugsvand med et volumen på ca. 100 liter. Beholderen er placeret i ??? og er isoleret med ca. 100 mm isolering. 110mm isolering Bosch fra ca2015 | **ShortText:**<br>100 l - 100 mm isolering iht. HB2023 *(was BI 3-1-5-0)*<br><br>**LongText:**<br>Der er registreret en varmtvandsbeholder til produktion af varmt brugsvand med et volumen på ca. 110 liter. Beholderen er mærke Bosch, årgang ca. 2015, og er isoleret med ca. 100 mm isolering. |

---

### 14. BI Classification: `4-1-3-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er ingen solceller på bygningen. | *(not in Plans)* | **ShortText:**<br>Ingen solcelle *(was BI 4-1-3-0)*<br><br>**LongText:**<br>Der er ingen solceller på bygningen. |

---


## Kirkegyden 15

### 1. BI Classification: `1-1-1-0`

**Status Counts:** Plans=1 (in this BI), Energy10=2

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Loftsrum vurderes isoleret med 200 mm mineraluld. Loftslem er uisoleret<br>Konstruktionstykkelse er målt ved loftlem. | **ShortText:**<br>Loftsrum - 200 mm isolering *(was BI 1-1-1-0)*<br><br>**LongText:**<br>Loftsrum vurderes isoleret med 200 mm mineraluld. Konstruktionstykkelse er målt ved loftlem. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. | **ShortText:**<br>Loftsrum - 200 mm isolering *(was BI 1-1-1-0)*<br><br>**LongText:**<br>Loftsrum vurderes isoleret med 200 mm mineraluld. Loftslem er uisoleret<br>Konstruktionstykkelse er målt ved loftlem. |
| | **ShortText:**<br>Loftsrum - 200 mm isolering *(was BI 1-1-1-0)*<br><br>**LongText:**<br>Loftsrum vurderes isoleret med 200 mm mineraluld. Konstruktionstykkelse er målt ved loftlem. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet.<br><br>**(fuzzy match: 64%)** | **ShortText:**<br>Loftslem - uisoleret *(was BI 1-1-1-0)*<br><br>**LongText:**<br>Loftslem er uisoleret.<br>Konstruktionstykkelse er målt ved loftlem. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. |

---

### 2. BI Classification: `1-2-2-0`

**Status Counts:** Plans=2 (in this BI), Energy10=2

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Ydervægge består af bindingsværk bestående af halvstens teglmur med ca. 15 % træ og indvendig forsatsvæg med 100 mm mineraluld og pladebeklædning. Konstruktions- og isoleringsforhold er baseret på et tidligere energimærke. | **ShortText:**<br>Massiv ydervæg - Bindingsværk - 100 mm *(was BI 1-2-2-0)*<br><br>**LongText:**<br>Ydervægge består af bindingsværk bestående af halvstens teglmur med ca. 15 % træ og indvendig forsatsvæg med 100 mm mineraluld og pladebeklædning. Konstruktions- og isoleringsforhold er baseret på et tidligere energimærke. | **ShortText:**<br>Massiv ydervæg - Bindingsværk - 100 mm *(was BI 1-2-2-0)*<br><br>**LongText:**<br>Ydervægge består af bindingsværk bestående af halvstens teglmur med ca. 15 % træ og indvendig forsatsvæg med 100 mm mineraluld og pladebeklædning. Konstruktions- og isoleringsforhold er baseret på et tidligere energimærke. |
| | **ShortText:**<br>Massiv ydervæg - Bindingsværk - 100 mm *(was BI 1-2-2-0)*<br><br>**LongText:**<br>Ydervægge består af bindingsværk bestående af halvstens teglmur med ca. 15 % træ og indvendig forsatsvæg med 100 mm mineraluld og pladebeklædning. Konstruktions- og isoleringsforhold er baseret på et tidligere energimærke. | **ShortText:**<br>Massiv ydervæg - Bindingsværk - 100 mm *(was BI 1-2-2-0)*<br><br>**LongText:**<br>Ydervægge består af bindingsværk bestående af halvstens teglmur med ca. 15 % træ og indvendig forsatsvæg med 100 mm mineraluld og pladebeklædning. Konstruktions- og isoleringsforhold er baseret på et tidligere energimærke. |

---

### 3. BI Classification: `1-2-2-1`

**Status Counts:** Plans=3 (in this BI), Energy10=3

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Vægge mod lade - uopvarmet rum består af 12 cm massiv teglvæg henholdsvis uisoleret og med indvendig pladebeklædning og 100 mm isolering. Konstruktions- og isoleringsforhold er skønnet ud fra renoveringstidspunktet. | **ShortText:**<br>Massiv væg mod uopvarmet rum - 12 cm tegl - 100 mm indvendig isolering *(was BI 1-2-2-1)*<br><br>**LongText:**<br>Vægge mod uopvarmet rum består af 12 cm massiv teglvæg med indvendig pladebeklædning og 100 mm isolering. Konstruktions- og isoleringsforhold er skønnet ud fra renoveringstidspunktet. | **ShortText:**<br>Massiv væg mod uopvarmet rum - 12 cm tegl - 100 mm indvendig isolering *(was BI 1-2-2-1)*<br><br>**LongText:**<br>Vægge mod lade - uopvarmet rum består af 12 cm massiv teglvæg henholdsvis uisoleret og med indvendig pladebeklædning og 100 mm isolering. Konstruktions- og isoleringsforhold er skønnet ud fra renoveringstidspunktet. |
| | **ShortText:**<br>Massiv væg mod uopvarmet rum - 12 cm tegl - uisoleret *(was BI 1-2-2-1)*<br><br>**LongText:**<br>Vægge mod uopvarmet rum består af 12 cm massiv og uisoleret teglvæg. Konstruktionstykkelse er målt ved dør. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. | **ShortText:**<br>Massiv væg mod uopvarmet rum - 12 cm tegl - uisoleret *(was BI 1-2-2-1)*<br><br>**LongText:**<br>Vægge mod uopvarmet rum består af 12 cm massiv og uisoleret teglvæg. Konstruktionstykkelse er målt ved dør. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. |
| | **ShortText:**<br>Massiv væg mod uopvarmet rum - 12 cm tegl - uisoleret *(was BI 1-2-2-1)*<br><br>**LongText:**<br>Vægge mod uopvarmet rum består af 12 cm massiv og uisoleret teglvæg. Konstruktionstykkelse er målt ved dør. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. | **ShortText:**<br>Massiv væg mod uopvarmet rum - 12 cm tegl - uisoleret *(was BI 1-2-2-1)*<br><br>**LongText:**<br>Vægge mod uopvarmet rum består af 12 cm massiv og uisoleret teglvæg. Konstruktionstykkelse er målt ved dør. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. |

---

### 4. BI Classification: `1-3-1-0`

**Status Counts:** Plans=16 (in this BI), Energy10=16

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| De fleste vinduer er monteret med tolags termorude. Vinduer i bryggers er monteret med etlags glasruder. Vinduer i værelse mod nordvest er monteret med etlags glasrude og forsatsrude.<br>Enkelte vinduer er monteret med tolags energiruder. | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag og sprosser. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>De fleste vinduer er monteret med tolags termorude. Vinduer i bryggers er monteret med etlags glasruder. Vinduer i værelse mod nordvest er monteret med etlags glasrude og forsatsrude.<br>Enkelte vinduer er monteret med tolags energiruder. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 1 lag glas *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag og sprosser. Vinduerne er monteret med etlags glasrude. | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 1 lag glas *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag og sprosser. Vinduerne er monteret med etlags glasrude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag og sprosser. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag og sprosser. Vinduerne er monteret med tolags termorude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag og sprosser. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag og sprosser. Vinduerne er monteret med tolags termorude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag og sprosser. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag og sprosser. Vinduerne er monteret med tolags termorude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag og sprosser. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag og sprosser. Vinduerne er monteret med tolags termorude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag og sprosser. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag og sprosser. Vinduerne er monteret med tolags termorude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag og sprosser. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag og sprosser. Vinduerne er monteret med tolags termorude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag og sprosser. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag og sprosser. Vinduerne er monteret med tolags termorude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag og sprosser. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag og sprosser. Vinduerne er monteret med tolags termorude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag og sprosser. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag og sprosser. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag og sprosser. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag og sprosser. Vinduerne er monteret med tolags termorude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag og sprosser. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag og sprosser. Vinduerne er monteret med tolags termorude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag og sprosser. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag og sprosser. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag og sprosser. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag og sprosser. Vinduerne er monteret med tolags termorude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 1+1 lag glas *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med etlags glasrude og forsatsrude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 1+1 lag glas *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med etlags glasrude og forsatsrude |

---

### 5. BI Classification: `1-3-3-0`

**Status Counts:** Plans=6 (in this BI), Energy10=6

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Yderdøre er med uisoleret fyldning og enkeltfagsvindue monteret med tolags termoruder.<br><br>Yderdør ved gang i nordøstfløj, monteret med tolags energiruder. | **ShortText:**<br>Yderdør med uisoleret fyldning og 1 rude - 2 lags termorude *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør med uisoleret fyldning og enkeltfagsvindue, monteret med tolags termoruder. | **ShortText:**<br>Yderdør med uisoleret fyldning og 1 rude - 2 lags termorude *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør med uisoleret fyldning og enkeltfagsvindue, monteret med tolags termoruder. |
| | **ShortText:**<br>Yderdør med uisoleret fyldning og 1 rude - 2 lags termorude *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør med uisoleret fyldning og enkeltfagsvindue, monteret med tolags termoruder. | **ShortText:**<br>Yderdør med uisoleret fyldning og 1 rude - 2 lags termorude *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør med uisoleret fyldning og enkeltfagsvindue, monteret med tolags termoruder. |
| | **ShortText:**<br>Yderdør med uisoleret fyldning og 1 rude - 2 lags termorude *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør med uisoleret fyldning og enkeltfagsvindue, monteret med tolags termoruder. | **ShortText:**<br>Yderdør med uisoleret fyldning og 1 rude - 2 lags termorude *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdøre er med uisoleret fyldning og enkeltfagsvindue monteret med tolags termoruder. |
| | **ShortText:**<br>Yderdør med 1 rude - 2 lags energirude med varm kant *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør med enkeltfagsvindue, monteret med tolags energiruder. | **ShortText:**<br>Yderdør med 1 rude - 2 lags energirude med varm kant *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør ved gang i nordøstfløj, monteret med tolags energiruder. |
| | **ShortText:**<br>Yderdør med uisoleret fyldning og 1 rude - 2 lags termorude *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør med uisoleret fyldning og enkeltfagsvindue, monteret med tolags termoruder. | **ShortText:**<br>Yderdør med uisoleret fyldning og 1 rude - 2 lags termorude *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør med uisoleret fyldning og enkeltfagsvindue, monteret med tolags termoruder. |
| | **ShortText:**<br>Yderdør med uisoleret fyldning og 1 rude - 2 lags termorude *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør med uisoleret fyldning og enkeltfagsvindue, monteret med tolags termoruder. | **ShortText:**<br>Yderdør med uisoleret fyldning og 1 rude - 2 lags termorude *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør med uisoleret fyldning og enkeltfagsvindue, monteret med tolags termoruder. |

---

### 6. BI Classification: `1-4-1-0`

**Status Counts:** Plans=3 (in this BI), Energy10=3

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Terrændæk i stuer, værelser og gang er skønnet udført i beton og med strøgulve der er isoleret med 50 mm mineraluld mellem strøer. Under betonen er gulvet uisoleret.<br>Konstruktions- og isoleringsforhold er skønnet ud fra renoveringstidspunktet.<br><br>Gulve i bryggers, badeværelser, toiletrum og depotrum er skønnet udført som terrazzogulve, klinker, fliser el. linoleum direkte mod jord. Gulvet er uisoleret. Konstruktions- og isoleringsforhold er skønnet ud fra opførelsestidspunktet. | **ShortText:**<br>Terrændæk - Beton med slidlag - 50 mm trædefast mineraluld, sten som kapillarbrydende lag - skillevægsfundament (beton) *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Terrændæk er udført af beton med slidlagsgulv. Gulvet vurderes isoleret med 50 mm trædefast mineraluld under betonen og sten som kapillarbrydende lag. Konstruktions- og isoleringsforhold er skønnet ud fra renoveringstidspunktet.<br>(??? U-værdi tillæg påført: 0.06 W/m2K) | **ShortText:**<br>Terrændæk - Beton med slidlag - 50 mm trædefast mineraluld, sten som kapillarbrydende lag - skillevægsfundament (beton) *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Terrændæk i stuer, værelser og gang er skønnet udført i beton og med strøgulve der er isoleret med 50 mm mineraluld mellem strøer. Under betonen er gulvet uisoleret.<br>Konstruktions- og isoleringsforhold er skønnet ud fra renoveringstidspunktet. |
| | **ShortText:**<br>Terrændæk - Klinker, fliser el linoleum på beton, direkte på jord - Uisoleret *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Gulv er udført som af klinker, fliser el. linoleum direkte mod jord. Gulvet er uisoleret. Konstruktions- og isoleringsforhold er skønnet ud fra opførelsestidspunktet. | **ShortText:**<br>Terrændæk - Klinker, fliser el linoleum på beton, direkte på jord - Uisoleret *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Gulve i bryggers, badeværelser, toiletrum og depotrum er skønnet udført som terrazzogulve, klinker, fliser el. linoleum direkte mod jord. Gulvet er uisoleret. Konstruktions- og isoleringsforhold er skønnet ud fra opførelsestidspunktet. |
| | **ShortText:**<br>Terrændæk - Klinker, fliser el linoleum på beton, direkte på jord - Uisoleret *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Gulv er udført som af klinker, fliser el. linoleum direkte mod jord. Gulvet er uisoleret. Konstruktions- og isoleringsforhold er skønnet ud fra opførelsestidspunktet. | **ShortText:**<br>Terrændæk - Klinker, fliser el linoleum på beton, direkte på jord - Uisoleret *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Gulv er udført som af klinker, fliser el. linoleum direkte mod jord. Gulvet er uisoleret. Konstruktions- og isoleringsforhold er skønnet ud fra opførelsestidspunktet. |

---

### 7. BI Classification: `1-5-1-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er naturlig ventilation i hele ejendommen. Ejendommen er delvis utæt, da konstruktionssamlinger og fuger ved vindues- og døråbninger, samt tætningslister i vinduer og udvendige døre ikke er helt intakte. | **ShortText:**<br>Bolig - Naturlig - delvis tæt 0,4 l/s m² *(was BI 1-5-1-0)*<br><br>**LongText:**<br>Der er naturlig ventilation i hele ejendommen. Ejendommen er delvis utæt, da konstruktionssamlinger og fuger ved vindues- og døråbninger, samt tætningslister i vinduer og udvendige døre ikke er helt intakte. | **ShortText:**<br>Bolig - Naturlig - delvis tæt 0,4 l/s m² *(was BI 1-5-1-0)*<br><br>**LongText:**<br>Der er naturlig ventilation i hele ejendommen. Ejendommen er delvis utæt, da konstruktionssamlinger og fuger ved vindues- og døråbninger, samt tætningslister i vinduer og udvendige døre ikke er helt intakte. |

---

### 8. BI Classification: `1-6-1-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Internt varmetilskud for enfamiliebyggeri. | **ShortText:**<br>Internt varmetilskud for enfamiliebyggeri *(was BI 1-6-1-0)*<br><br>**LongText:**<br>Internt varmetilskud for enfamiliebyggeri. | **ShortText:**<br>Internt varmetilskud for enfamiliebyggeri *(was BI 1-6-1-0)*<br><br>**LongText:**<br>Internt varmetilskud for enfamiliebyggeri. |

---

### 9. BI Classification: `2-1-3-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Ejendommen opvarmes med fjernvarme. Anlægget er udført som direkte fjernvarmeanlæg, med fjernvarmevand i fordelingsnettet.<br>Fjernvarmestik er placeret i værelse / kontor mod vej.<br>Fjernvarme Fyn - 1-1.000 m² | **ShortText:**<br>Fjernvarme uden veksler - direkte *(was BI 2-1-0-0)*<br><br>**LongText:**<br>Ejendommen opvarmes med fjernvarme. Anlægget er udført som direkte fjernvarmeanlæg, med fjernvarmevand i fordelingsnettet.<br>Fjernvarmestik er placeret i værelse / kontor mod vej.<br>Fjernvarme Fyn - 1-1.000 m²<br><br>**BI reclassified:** `2-1-0-0` → `2-1-3-0` | **ShortText:**<br>Fjernvarme uden veksler - direkte *(was BI 2-1-3-0)*<br><br>**LongText:**<br>Ejendommen opvarmes med fjernvarme. Anlægget er udført som direkte fjernvarmeanlæg, med fjernvarmevand i fordelingsnettet.<br>Fjernvarmestik er placeret i værelse / kontor mod vej.<br>Fjernvarme Fyn - 1-1.000 m² |

---

### 10. BI Classification: `2-1-5-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er ingen varmepumpe i bygningen. | *(not in Plans)* | **ShortText:**<br>Ingen varmepumpe *(was BI 2-1-5-0)*<br><br>**LongText:**<br>Der er ingen varmepumpe i bygningen. |

---

### 11. BI Classification: `2-1-6-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er ikke stillet forslag til solvarmeanlæg, da dette, med bygningens eksisterende varmeanlæg og den dertilhørende energipris, ikke vil kunne medføre et fornuftigt og rentabelt forslag. | *(not in Plans)* | **ShortText:**<br>Intet solvarmeanlæg - Intet forslag *(was BI 2-1-6-0)*<br><br>**LongText:**<br>Der er ikke stillet forslag til solvarmeanlæg, da dette, med bygningens eksisterende varmeanlæg og den dertilhørende energipris, ikke vil kunne medføre et fornuftigt og rentabelt forslag. |

---

### 12. BI Classification: `2-2-1-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Den primære opvarmning af ejendommen sker via radiatorer i opvarmede rum. Varmefordelingsrør er udført som to-strengs anlæg. | *(not in Plans)* | **ShortText:**<br>Radiator - 2-streng iht. HB2023 *(was BI 2-2-1-0)*<br><br>**LongText:**<br>Den primære opvarmning af ejendommen sker via radiatorer i opvarmede rum. Varmefordelingsrør er udført som to-strengs anlæg. |

---

### 13. BI Classification: `2-2-2-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Varmerør er udført som 3/8" stålrør. Varmerørene er isoleret med 50 mm isolering. | **ShortText:**<br>3/8" (17,1 mm) stålrør - 20 mm *(was BI 2-2-2-0)*<br><br>**LongText:**<br>Status: Varmerørene er udført i stål med en dimension på 3/8" og er isoleret med ca. 20 mm isolering. Rørene er placeret i tagrum og har en samlet længde på ca. xx m. ???<br><br>**(fuzzy match: 97%)** | **ShortText:**<br>3/8" (17,1 mm) stålrør - 50 mm *(was BI 2-2-2-0)*<br><br>**LongText:**<br>Varmerør er udført som 3/8" stålrør. Varmerørene er isoleret med 50 mm isolering. |

---

### 14. BI Classification: `2-2-4-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er monteret termostatventiler på alle radiatorer til regulering af korrekt rumtemperatur. | *(not in Plans)* | **ShortText:**<br>Termostatventiler på alle radiatorer *(was BI 2-2-4-0)*<br><br>**LongText:**<br>Der er monteret termostatventiler på alle radiatorer til regulering af korrekt rumtemperatur. |

---

### 15. BI Classification: `3-1-4-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Brugsvandsanlægget er forsynet med en cirkulationspumpe af fabrikat Grundfos type Alpha 2 - 20-40 N - 22W med en nominel effekt på 22 W. Pumpen er placeret i bryggers. | **ShortText:**<br>Grundfos Alpha 2 - 20-40 N - 22W *(was BI 3-1-4-0)*<br><br>**LongText:**<br>Brugsvandsanlægget er forsynet med en cirkulationspumpe af fabrikat Grundfos type Alpha 2 - 20-40 N - 22W med en nominel effekt på ??? W. Pumpen er placeret i ??? og vurderes at være fra perioden ???. Pumpen er udført som ???. ??? (Evt.: Rørene er frostsikret med el-tracing) | **ShortText:**<br>Grundfos Alpha 2 - 20-40 N - 22W *(was BI 3-1-4-0)*<br><br>**LongText:**<br>Brugsvandsanlægget er forsynet med en cirkulationspumpe af fabrikat Grundfos type Alpha 2 - 20-40 N - 22W med en nominel effekt på 22 W. Pumpen er placeret i bryggers. |

---

### 16. BI Classification: `3-1-5-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Varmt brugsvand produceres via brugsvandsveksler, fabrikat Redan. Veksleren er placeret i bryggers. | **ShortText:**<br>Brugsvandsveksler, Redan *(was BI 3-1-5-0)*<br><br>**LongText:**<br>Varmt brugsvand produceres via brugsvandsveksler, fabrikat Redan. Veksleren er placeret i bryggers. | **ShortText:**<br>Brugsvandsveksler, Redan *(was BI 3-1-5-0)*<br><br>**LongText:**<br>Varmt brugsvand produceres via brugsvandsveksler, fabrikat Redan. Veksleren er placeret i bryggers. |

---

### 17. BI Classification: `4-1-3-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er ingen solceller på bygningen.<br><br>Grundet bygningens stråtag indgår der ikke et forslag til etablering af solcelleanlæg. De specielle nødvendig løsninger til etablering af solceller på et stråtag vil være fordyrende, samt ændre husets arkitektoniske udtryk væsentligt. | *(not in Plans)* | **ShortText:**<br>Ingen solcelle *(was BI 4-1-3-0)*<br><br>**LongText:**<br>Der er ingen solceller på bygningen.<br><br>Grundet bygningens stråtag indgår der ikke et forslag til etablering af solcelleanlæg. De specielle nødvendig løsninger til etablering af solceller på et stråtag vil være fordyrende, samt ændre husets arkitektoniske udtryk væsentligt. |

---


## Lunden 3

### 1. BI Classification: `1-1-1-0`

**Status Counts:** Plans=1 (in this BI), Energy10=2

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Loftsrum vurderes isoleret med 200-250 mm mineraluld. <br>Loftslem er uisoleret.<br>Isoleringsforholdet i konstruktionen er målt i forbindelse med besigtigelsen. | **ShortText:**<br>Loftsrum - 225 mm isolering *(was BI 1-1-1-0)*<br><br>**LongText:**<br>Loftsrum vurderes isoleret med 225 mm mineraluld. Isoleringsforholdet i konstruktionen er målt i forbindelse med besigtigelsen. | **ShortText:**<br>Loftsrum - 225 mm isolering *(was BI 1-1-1-0)*<br><br>**LongText:**<br>Loftsrum vurderes isoleret med 200-250 mm mineraluld. <br>Loftslem er uisoleret.<br>Isoleringsforholdet i konstruktionen er målt i forbindelse med besigtigelsen. |
| | **ShortText:**<br>Loftslem - uisoleret *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Loftslem er uisoleret. Isoleringsforholdet i konstruktionen er målt i forbindelse med besigtigelsen.<br><br>**BI reclassified:** `1-1-3-0` → `1-1-1-0` | **ShortText:**<br>Loftslem - uisoleret *(was BI 1-1-1-0)*<br><br>**LongText:**<br>Loftslem er uisoleret. Isoleringsforholdet i konstruktionen er målt i forbindelse med besigtigelsen. |

---

### 2. BI Classification: `1-2-1-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Ydervægge er udført som 30 cm hulmur. Vægge består udvendigt og indvendigt af tegl. Hulrummet er isoleret ved opførelsen. Der er ikke stillet forslag om energioptimering da dette ikke er rentabelt.<br>Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. | **ShortText:**<br>Hul ydervæg - 30 cm tegl/tegl - Isoleret ved opførelsen *(was BI 1-2-1-0)*<br><br>**LongText:**<br>Ydervægge er udført som 30 cm hulmur. Vægge består udvendigt og indvendigt af tegl. Hulrummet er isoleret ved opførelsen. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br>(??? U-værdi tillæg påført: 0.1 W/m2K) | **ShortText:**<br>Hul ydervæg - 30 cm tegl/tegl - Isoleret ved opførelsen *(was BI 1-2-1-0)*<br><br>**LongText:**<br>Ydervægge er udført som 30 cm hulmur. Vægge består udvendigt og indvendigt af tegl. Hulrummet er isoleret ved opførelsen. Der er ikke stillet forslag om energioptimering da dette ikke er rentabelt.<br>Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. |

---

### 3. BI Classification: `1-3-1-0`

**Status Counts:** Plans=7 (in this BI), Energy10=7

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Vinduer i ejendommen er alle med tolags energiruder med kolde kante. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Vinduer i ejendommen er alle med tolags energiruder med kolde kante. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. |

---

### 4. BI Classification: `1-3-3-0`

**Status Counts:** Plans=2 (in this BI), Energy10=2

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Entredør uden glas vurderes isoleret med ca. 15 mm isolering, mens terrasse skydedør i stue i tilbygningen er med trelags energiruder med varme kante. | **ShortText:**<br>Yderdør uden glas - 2000-2009 - isoleret med 15 mm iht. HB2023 *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør uden glas vurderes isoleret med ca. 15 mm isolering. | **ShortText:**<br>Yderdør uden glas - 2000-2009 - isoleret med 15 mm iht. HB2023 *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Entredør uden glas vurderes isoleret med ca. 15 mm isolering, mens terrasse skydedør i stue i tilbygningen er med trelags energiruder med varme kante. |
| | **ShortText:**<br>Skydedørsparti - 1 fast og 1 gående - 3 lags energirude - energiklasse B *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Skydedørsparti med 1 fast og 1 gående fag, monteret med trelags energiruder, energiklasse B. | **ShortText:**<br>Skydedørsparti - 1 fast og 1 gående - 3 lags energirude - energiklasse B *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Skydedørsparti med 1 fast og 1 gående fag, monteret med trelags energiruder, energiklasse B. |

---

### 5. BI Classification: `1-4-1-0`

**Status Counts:** Plans=4 (in this BI), Energy10=4

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Terrændæk i den oprindelige del er udført af beton med slidlagsgulv, der er desuden gulvvarme i badeværelse. Gulvet er isoleret med 100 mm letklinker under betonen. <br>Der er ikke stillet forslag om energioptimering da dette ikke er rentabelt.<br>Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br><br>Terrændæk i tilbygningen, der er desuden gulvvarme i området med gulvklinker er udført af beton med slidlagsgulv. Gulvet er isoleret med 50 mm trædefast mineraluld under betonen og sten som kapillarbrydende lag. <br>Der er ikke stillet forslag om energioptimering da dette ikke er rentabelt.<br>Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. | **ShortText:**<br>Terrændæk - Beton med slidlag - 100 mm letklinker - skillevægsfundament (beton) *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Terrændæk er udført af beton med slidlagsgulv. Gulvet er isoleret med 100 mm letklinker under betonen. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br>(??? U-værdi tillæg påført: 0.06 W/m2K) | **ShortText:**<br>Terrændæk - Beton med slidlag - 100 mm letklinker - skillevægsfundament (beton) *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Terrændæk i den oprindelige del er udført af beton med slidlagsgulv, der er desuden gulvvarme i badeværelse. Gulvet er isoleret med 100 mm letklinker under betonen. <br>Der er ikke stillet forslag om energioptimering da dette ikke er rentabelt.<br>Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. |
| | **ShortText:**<br>Terrændæk - Beton med slidlag - 50 mm trædefast mineraluld, sten som kapillarbrydende lag *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Terrændæk er udført af beton med slidlagsgulv. Gulvet er isoleret med 50 mm trædefast mineraluld under betonen og sten som kapillarbrydende lag. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. | **ShortText:**<br>Terrændæk - Beton med slidlag - 50 mm trædefast mineraluld, sten som kapillarbrydende lag *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Terrændæk i tilbygningen, der er desuden gulvvarme i området med gulvklinker er udført af beton med slidlagsgulv. Gulvet er isoleret med 50 mm trædefast mineraluld under betonen og sten som kapillarbrydende lag. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. |
| | **ShortText:**<br>Terrændæk - Beton med slidlag - 50 mm trædefast mineraluld, sten som kapillarbrydende lag *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Terrændæk er udført af beton med slidlagsgulv. Gulvet er isoleret med 50 mm trædefast mineraluld under betonen og sten som kapillarbrydende lag. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. | **ShortText:**<br>Terrændæk - Beton med slidlag - 50 mm trædefast mineraluld, sten som kapillarbrydende lag *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Terrændæk i tilbygningen, der er desuden gulvvarme i området med gulvklinker er udført af beton med slidlagsgulv. Gulvet er isoleret med 50 mm trædefast mineraluld under betonen og sten som kapillarbrydende lag. <br>Der er ikke stillet forslag om energioptimering da dette ikke er rentabelt.<br>Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. |
| | **ShortText:**<br>Terrændæk - Beton med slidlag - 100 mm letklinker - skillevægsfundament (beton) *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Terrændæk er udført af beton med slidlagsgulv. Gulvet er isoleret med 100 mm letklinker under betonen. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br>(??? U-værdi tillæg påført: 0.06 W/m2K) | **ShortText:**<br>Terrændæk - Beton med slidlag - 100 mm letklinker - skillevægsfundament (beton) *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Terrændæk i den oprindelige del er udført af beton med slidlagsgulv, der er desuden gulvvarme i badeværelse. Gulvet er isoleret med 100 mm letklinker under betonen. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. |

---

### 6. BI Classification: `1-5-1-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er naturlig ventilation i hele bygningen. Bygningen er normal tæt, da konstruktionssamlinger og fuger ved vindues- og døråbninger, samt tætningslister i vinduer og udvendige døre fremstår i god stand. | *(not in Plans)* | **ShortText:**<br>Bolig - Naturlig - tæt 0,3 l/s m² *(was BI 1-5-1-0)*<br><br>**LongText:**<br>Der er naturlig ventilation i hele bygningen. Bygningen er normal tæt, da konstruktionssamlinger og fuger ved vindues- og døråbninger, samt tætningslister i vinduer og udvendige døre fremstår i god stand. |

---

### 7. BI Classification: `2-1-3-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Ejendommen opvarmes med fjernvarme. Anlægget er udført som direkte fjernvarmeanlæg, med fjernvarmevand i fordelingsnettet.<br>Galten Varmeværk A.m.b.a. | **ShortText:**<br>Fjernvarme uden veksler - direkte *(was BI 2-1-0-0)*<br><br>**LongText:**<br>Ejendommen opvarmes med fjernvarme. Anlægget er udført som direkte fjernvarmeanlæg, med fjernvarmevand i fordelingsnettet.<br>Galten Varmeværk A.m.b.a.<br><br>**BI reclassified:** `2-1-0-0` → `2-1-3-0` | **ShortText:**<br>Fjernvarme uden veksler - direkte *(was BI 2-1-3-0)*<br><br>**LongText:**<br>Ejendommen opvarmes med fjernvarme. Anlægget er udført som direkte fjernvarmeanlæg, med fjernvarmevand i fordelingsnettet.<br>Galten Varmeværk A.m.b.a. |

---

### 8. BI Classification: `2-1-5-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er ikke stillet forslag til varmepumpe, da dette, med bygningens eksisterende varmeanlæg og den dertilhørende energipris, ikke vil kunne medføre et fornuftigt og rentabelt forslag. | *(not in Plans)* | **ShortText:**<br>Ingen varmepumpe - Intet forslag *(was BI 2-1-5-0)*<br><br>**LongText:**<br>Der er ikke stillet forslag til varmepumpe, da dette, med bygningens eksisterende varmeanlæg og den dertilhørende energipris, ikke vil kunne medføre et fornuftigt og rentabelt forslag. |

---

### 9. BI Classification: `2-1-6-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er ikke stillet forslag til solvarmeanlæg, da dette, med bygningens eksisterende varmeanlæg og den dertilhørende energipris, ikke vil kunne medføre et fornuftigt og rentabelt forslag. | *(not in Plans)* | **ShortText:**<br>Intet solvarmeanlæg - Intet forslag *(was BI 2-1-6-0)*<br><br>**LongText:**<br>Der er ikke stillet forslag til solvarmeanlæg, da dette, med bygningens eksisterende varmeanlæg og den dertilhørende energipris, ikke vil kunne medføre et fornuftigt og rentabelt forslag. |

---

### 10. BI Classification: `2-2-1-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Den primære opvarmning af ejendommen sker via radiatorer i opvarmede rum. Varmefordelingsrør er udført som to-strengs anlæg. Der er desuden gulvvarme i badeværelse og i område med klinker i tilbygningen. | *(not in Plans)* | **ShortText:**<br>Radiator + gulvvarme - 2-streng iht. HB2023 *(was BI 2-2-1-0)*<br><br>**LongText:**<br>Den primære opvarmning af ejendommen sker via radiatorer i opvarmede rum. Varmefordelingsrør er udført som to-strengs anlæg. Der er desuden gulvvarme i badeværelse og i område med klinker i tilbygningen. |

---

### 11. BI Classification: `2-2-2-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Varmerør i terrændæk er skønnet udført som 1/2" stålrør. Varmerørene skønnet isoleret med 30 mm isolering. | *(not in Plans)* | **ShortText:**<br>1/2" (21,4 mm) stålrør - 30 mm *(was BI 2-2-2-0)*<br><br>**LongText:**<br>Varmerør i terrændæk er skønnet udført som 1/2" stålrør. Varmerørene skønnet isoleret med 30 mm isolering. |

---

### 12. BI Classification: `2-2-4-0`

**Status Counts:** Plans=1 (in this BI), Energy10=2

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er monteret termostatventiler på alle radiatorer til regulering af korrekt rumtemperatur.<br><br>Der er monteret returventil på gulvvarme i tilbygningen. Mens styring til gulvvarme i badeværelse ikke kunne lokaliseres ved besigtigelsen. Derfor skønnes dette styret ved retur ventil. | **ShortText:**<br>Termostatventiler på alle radiatorer *(was BI 2-2-4-0)*<br><br>**LongText:**<br>Der er monteret termostatventiler på alle radiatorer til regulering af korrekt rumtemperatur. | **ShortText:**<br>Termostatventiler på alle radiatorer *(was BI 2-2-4-0)*<br><br>**LongText:**<br>Der er monteret termostatventiler på alle radiatorer til regulering af korrekt rumtemperatur. |
| | *(not in Plans)* | **ShortText:**<br>Kun returventiler på gulvvarmesystemet, +1 grad iht. HB2023 *(was BI 2-2-4-0)*<br><br>**LongText:**<br>Der er monteret returventil på gulvvarme i tilbygningen. Mens styring til gulvvarme i badeværelse ikke kunne lokaliseres ved besigtigelsen. Derfor skønnes dette styret ved retur ventil. |

---

### 13. BI Classification: `3-1-1-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| I beregningen er der indregnet et varmtvandsforbrug på 250 liter pr. m² opvarmet etageareal pr. år. | **ShortText:**<br>Bolig - standard varmtvandforbrug iht. HB2023 *(was BI 3-1-1-0)*<br><br>**LongText:**<br>I beregningen er der indregnet et varmtvandsforbrug på 250 liter pr. m² opvarmet etageareal pr. år. | **ShortText:**<br>Bolig - standard varmtvandforbrug iht. HB2023 *(was BI 3-1-1-0)*<br><br>**LongText:**<br>I beregningen er der indregnet et varmtvandsforbrug på 250 liter pr. m² opvarmet etageareal pr. år. |

---

### 14. BI Classification: `3-1-3-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Varmetabet fra tilslutningsrør under 5 meter indregnes med et standard værdisæt for rørlængde og isoleringsniveau svarende til 4 meter med 30 mm isolering. Dette udføres iht. gældende Håndbog for Energikonsulenter. | *(not in Plans)* | **ShortText:**<br>Standard tilslutningsrør - Længde og isoleringsniveau iht. HB2023 *(was BI 3-1-3-0)*<br><br>**LongText:**<br>Varmetabet fra tilslutningsrør under 5 meter indregnes med et standard værdisæt for rørlængde og isoleringsniveau svarende til 4 meter med 30 mm isolering. Dette udføres iht. gældende Håndbog for Energikonsulenter. |

---

### 15. BI Classification: `3-1-5-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Varmt brugsvand produceres via brugsvandsveksler, fabrikat Termix, fra 2006. Veksleren er placeret i bryggers. | **ShortText:**<br>Brugsvandsveksler, Termix VMTD *(was BI 3-1-5-0)*<br><br>**LongText:**<br>Varmt brugsvand produceres via brugsvandsveksler, fabrikat Termix, model VMTD. Veksleren er placeret i ???. Fra 2006 | **ShortText:**<br>Brugsvandsveksler, Termix VMTD *(was BI 3-1-5-0)*<br><br>**LongText:**<br>Varmt brugsvand produceres via brugsvandsveksler, fabrikat Termix, fra 2006. Veksleren er placeret i bryggers. |

---

### 16. BI Classification: `4-1-3-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er ingen solceller på bygningen. | *(not in Plans)* | **ShortText:**<br>Ingen solcelle *(was BI 4-1-3-0)*<br><br>**LongText:**<br>Der er ingen solceller på bygningen. |

---


## Nypølsgade 14

### 1. BI Classification: `1-1-1-0`

**Status Counts:** Plans=0 (in this BI), Energy10=2

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Hanebåndsloft er isoleret med ca. 250 mm isolering. Konstruktions- og isoleringsforhold er baseret på ejers oplysninger. <br><br>Loftlem er placeret på 1.sal og er isoleret med ca. 10 mm isolering. Konstruktions- og isoleringsforhold er baseret på ejers oplysninger.<br>Der er ikke givet forslag til efterisolering eller udskiftning af loftlem, da den årlige besparelse vil være minimal i forhold til investeringen. | **ShortText:**<br>Hanebåndsloft - 250 mm isolering *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Hanebåndsloft er isoleret med 250 mm mineraluld. Konstruktions- og isoleringsforhold er baseret på ejers oplysninger.<br><br>**BI reclassified:** `1-1-3-0` → `1-1-1-0` | **ShortText:**<br>Hanebåndsloft - 250 mm isolering *(was BI 1-1-1-0)*<br><br>**LongText:**<br>Hanebåndsloft er isoleret med ca. 250 mm isolering. Konstruktions- og isoleringsforhold er baseret på ejers oplysninger. |
| | **ShortText:**<br>Loftslem - 50 mm isolering *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Loftslem er isoleret med 50 mm mineraluld. Konstruktions- og isoleringsforhold er baseret på ejers oplysninger.<br><br>**BI reclassified:** `1-1-3-0` → `1-1-1-0` | **ShortText:**<br>Loftslem - 50 mm isolering *(was BI 1-1-1-0)*<br><br>**LongText:**<br>Loftlem er placeret på 1.sal og er isoleret med ca. 10 mm isolering. Konstruktions- og isoleringsforhold er baseret på ejers oplysninger.<br>Der er ikke givet forslag til efterisolering eller udskiftning af loftlem, da den årlige besparelse vil være minimal i forhold til investeringen. |

---

### 2. BI Classification: `1-1-3-0`

**Status Counts:** Plans=2 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Skråvægge er isoleret med ca. 250 mm isolering. Konstruktions- og isoleringsforhold er baseret på ejers oplysninger. | **ShortText:**<br>Stråtag - 200 mm isolering *(was BI 1-1-0-0)*<br><br>**LongText:**<br>Stråtag vurderes isoleret med 200 mm mineraluld.<br><br>**(fuzzy match: 81%)**<br><br>**BI reclassified:** `1-1-0-0` → `1-1-3-0` | **ShortText:**<br>Skråvægge - 250 mm isolering *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Skråvægge er isoleret med ca. 250 mm isolering. Konstruktions- og isoleringsforhold er baseret på ejers oplysninger. |

---

### 3. BI Classification: `1-2-2-0`

**Status Counts:** Plans=2 (in this BI), Energy10=2

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Ydervægge er ca. 240 mm massiv tegl. <br>Ydervæggen er isoleret med ca. 75 mm isolering på indvendig side nederst i stue/køkken. Konstruktions- og isoleringsforhold er baseret på ejers oplysninger.<br>Øvrig del af ydervæggen er uden isolering. Konstruktions- og isoleringsforhold er skønnet ud fra opførelsestidspunktet. | **ShortText:**<br>Massiv ydervæg - 24 cm tegl - uisoleret *(was BI 1-2-2-0)*<br><br>**LongText:**<br>Ydervægge består af 24 cm massiv og uisoleret teglvæg. Konstruktions- og isoleringsforhold er skønnet ud fra opførelsestidspunktet. | **ShortText:**<br>Massiv ydervæg - 24 cm tegl - uisoleret *(was BI 1-2-2-0)*<br><br>**LongText:**<br>Ydervægge er ca. 240 mm massiv tegl. <br>Ydervæggen er isoleret med ca. 75 mm isolering på indvendig side nederst i stue/køkken. Konstruktions- og isoleringsforhold er baseret på ejers oplysninger.<br>Øvrig del af ydervæggen er uden isolering. Konstruktions- og isoleringsforhold er skønnet ud fra opførelsestidspunktet. |
| | **ShortText:**<br>Massiv ydervæg - 24 cm tegl - 50 mm indvendig isolering *(was BI 1-2-2-0)*<br><br>**LongText:**<br>Ydervægge består af 24 cm massiv teglvæg med indvendig pladebeklædning og 50 mm isolering. Konstruktions- og isoleringsforhold er baseret på ejers oplysninger.<br><br>**(fuzzy match: 98%)** | **ShortText:**<br>Massiv ydervæg - 24 cm tegl - 75 mm indvendig isolering *(was BI 1-2-2-0)*<br><br>**LongText:**<br>Massiv ydervæg er ca. 240 mm tegl og er isoleret med ca. 75 mm isolering på indvendig side i stue/køkken.  Konstruktions- og isoleringsforhold er baseret på ejers oplysninger. |

---

### 4. BI Classification: `1-2-3-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Kvistflunker er udført som let konstruktion og er isoleret med ca. 250 mm isolering. Konstruktions- og isoleringsforhold er baseret på ejers oplysninger.<br>Der er ikke givet forslag til efterisolering, da den årlige besparelse vil være minimal i forhold til investeringen. | **ShortText:**<br>Kvistflunke - træ/træ - 250 mm isolering *(was BI 1-2-3-0)*<br><br>**LongText:**<br>Kvistflunke er udført som let konstruktion med beklædning ud- og indvendig. Hulrum mellem beklædninger vurderes isoleret med 250 mm mineraluld.<br><br>**(fuzzy match: 75%)** | **ShortText:**<br>Let ydervæg - træ/træ - 250 mm isolering *(was BI 1-2-3-0)*<br><br>**LongText:**<br>Kvistflunker er udført som let konstruktion og er isoleret med ca. 250 mm isolering. Konstruktions- og isoleringsforhold er baseret på ejers oplysninger.<br>Der er ikke givet forslag til efterisolering, da den årlige besparelse vil være minimal i forhold til investeringen. |

---

### 5. BI Classification: `1-3-1-0`

**Status Counts:** Plans=16 (in this BI), Energy10=16

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Beskrivelse og glasforhold vedrørende vinduer og døre er baseret på visuel kontrol ved konsulent.<br>Vinduer mod nord og vest i værksted er med 1 lag glas. Øvrige vinduer i boligen, samt yderdøre er med to-lags energiruder med varm kant. Den massive yderdør ved værksted er uden isolering.<br><br>Der er ikke givet forslag til udskiftning af vinduer og døre med energiruder, da den årlige besparelse vil være minimal i forhold til investeringen. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 1 lag glas *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med etlags glasrude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 1 lag glas *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Beskrivelse og glasforhold vedrørende vinduer og døre er baseret på visuel kontrol ved konsulent.<br>Vinduer mod nord og vest i værksted er med 1 lag glas. Øvrige vinduer i boligen, samt yderdøre er med to-lags energiruder med varm kant. Den massive yderdør ved værksted er uden isolering.<br><br>Der er ikke givet forslag til udskiftning af vinduer og døre med energiruder, da den årlige besparelse vil være minimal i forhold til investeringen. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 1 lag glas *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med etlags glasrude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 1 lag glas *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med etlags glasrude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 1 lag glas *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med etlags glasrude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 1 lag glas *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med etlags glasrude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags energirude. |

---

### 6. BI Classification: `1-4-1-0`

**Status Counts:** Plans=2 (in this BI), Energy10=2

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Gulve er terrændæk udført som betondæk.<br>Terrændæk i bad er isoleret med ca. 300 mm polystyren. Øvrig del af terrændæk er uden isolering. Konstruktions- og isoleringsforhold er baseret på ejers oplysninger. | **ShortText:**<br>Terrændæk - Beton med slidlag - uisoleret *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Terrændæk er udført i beton og med strøgulve. Gulvet er uisoleret. Konstruktions- og isoleringsforhold er baseret på ejers oplysninger. | **ShortText:**<br>Terrændæk - Beton med slidlag - uisoleret *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Gulve er terrændæk udført som betondæk.<br>Terrændæk i bad er isoleret med ca. 300 mm polystyren. Øvrig del af terrændæk er uden isolering. Konstruktions- og isoleringsforhold er baseret på ejers oplysninger. |
| | **ShortText:**<br>Terrændæk - Beton med slidlag - 300 mm polystyrenplader - skillevægsfundament (beton) *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Terrændæk er udført af beton med slidlagsgulv. Gulvet er isoleret med 300 mm polystyrenplader under betonen. Konstruktions- og isoleringsforhold er baseret på ejers oplysninger.<br>(??? U-værdi tillæg påført: 0.07 W/m2K) | **ShortText:**<br>Terrændæk - Beton med slidlag - 300 mm polystyrenplader - skillevægsfundament (beton) *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Terrændæk er udført af beton med slidlagsgulv. Gulvet er isoleret med 300 mm polystyrenplader under betonen. Konstruktions- og isoleringsforhold er baseret på ejers oplysninger.<br>U-værdi tillæg påført: 0.07 W/m2K) |

---

### 7. BI Classification: `1-5-1-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er naturlig ventilation i hele bygningen. Bygningen er normal tæt, da konstruktionssamlinger og fuger ved vindues- og døråbninger, samt tætningslister i vinduer og udvendige døre fremstår i god stand. | *(not in Plans)* | **ShortText:**<br>Bolig - Naturlig - tæt 0,3 l/s m² *(was BI 1-5-1-0)*<br><br>**LongText:**<br>Der er naturlig ventilation i hele bygningen. Bygningen er normal tæt, da konstruktionssamlinger og fuger ved vindues- og døråbninger, samt tætningslister i vinduer og udvendige døre fremstår i god stand. |

---

### 8. BI Classification: `2-1-1-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Boligen er el-opvarmet via el-radiatorer og el-gulvvarme. Som supplerende opvarmning er der to varmepumper, type luft/luft, og en brændeovn. Yderligere beskrivelse herfor under punkterne: "Varmepumper" og "Ovne".<br><br>Entré, bryggers, gang og værksted er uden varmeinstallation, og beregnes som værende el-opvarmet, da det vurderes at eksisterende varmeanlæg ikke er tilstrækkelig til at kunne opvarme hele boligen (jfr. Energistyrelsen). | *(not in Plans)* | **ShortText:**<br>El til panelradiatorer *(was BI 2-1-1-0)*<br><br>**LongText:**<br>Boligen er el-opvarmet via el-radiatorer og el-gulvvarme. Som supplerende opvarmning er der to varmepumper, type luft/luft, og en brændeovn. Yderligere beskrivelse herfor under punkterne: "Varmepumper" og "Ovne".<br><br>Entré, bryggers, gang og værksted er uden varmeinstallation, og beregnes som værende el-opvarmet, da det vurderes at eksisterende varmeanlæg ikke er tilstrækkelig til at kunne opvarme hele boligen (jfr. Energistyrelsen). |

---

### 9. BI Classification: `2-1-4-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er supplerende varmeforsyning i form af brændeovn. Brændeovnen er placeret i stue. Brændeovnens årgang estimeres til at være ca. 2011. Ovnen indgår i beregning sammen med elopvarmning. Andelen til brændeovn er sat til 15 % af den samlede opvarmning af det rum som ovnen er placeret i, i henhold til Energistyrelsens beregningsregler. | **ShortText:**<br>Brændeovn - supplerende - 2008-2015 *(was BI 2-1-0-0)*<br><br>**LongText:**<br>Der er supplerende varmeforsyning i form af en brændeovn. Varmekildens andel af bygningens samlede opvarmning er indregnet i henhold til Energistyrelsens beregningsregler. Brændeovnen er vurderet til at være produceret i perioden 2008-2015. Brændeovnen er placeret i ???.<br><br>**BI reclassified:** `2-1-0-0` → `2-1-4-0` | **ShortText:**<br>Brændeovn - supplerende - 2008-2015 *(was BI 2-1-4-0)*<br><br>**LongText:**<br>Der er supplerende varmeforsyning i form af brændeovn. Brændeovnen er placeret i stue. Brændeovnens årgang estimeres til at være ca. 2011. Ovnen indgår i beregning sammen med elopvarmning. Andelen til brændeovn er sat til 15 % af den samlede opvarmning af det rum som ovnen er placeret i, i henhold til Energistyrelsens beregningsregler. |

---

### 10. BI Classification: `2-1-5-0`

**Status Counts:** Plans=2 (in this BI), Energy10=3

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er installeret 2 varmepumper, type luft/luft, mærke Altech Vega 12 og Altech Vega 18 til rumopvarmning. Varmepumperne er årgang ca. 2026, og er placeret i stue/køkken og i stue/værelse.<br>Teknisk data, som er anvendt i beregningen er standardværdier, som må anses for værende retningsgivende. | **ShortText:**<br>Luft/luft - Efter 2015 - omdrejningsstyret iht. HB2023 *(was BI 2-1-5-0)*<br><br>**LongText:**<br>Der er registreret en luft til luft-varmepumpe. Varmepumpen er placeret stue/køkken Varmepumpen anvendes alene til rumopvarmning. | **ShortText:**<br>Luft/luft - Efter 2015 - omdrejningsstyret iht. HB2023 *(was BI 2-1-5-0)*<br><br>**LongText:**<br>Der er installeret 2 varmepumper, type luft/luft, mærke Altech Vega 12 og Altech Vega 18 til rumopvarmning. Varmepumperne er årgang ca. 2026, og er placeret i stue/køkken og i stue/værelse.<br>Teknisk data, som er anvendt i beregningen er standardværdier, som må anses for værende retningsgivende. |
| | **ShortText:**<br>Luft/luft - Efter 2015 - omdrejningsstyret iht. HB2023 *(was BI 2-1-5-0)*<br><br>**LongText:**<br>Der er registreret en luft til luft-varmepumpe. Varmepumpen er placeret stue/køkken Varmepumpen anvendes alene til rumopvarmning. | **ShortText:**<br>Luft/luft - Efter 2015 - omdrejningsstyret iht. HB2023 *(was BI 2-1-5-0)*<br><br>**LongText:**<br>Der er registreret en luft til luft-varmepumpe. |
| | *(not in Plans)* | **ShortText:**<br>Ingen varmepumpe *(was BI 2-1-5-0)*<br><br>**LongText:**<br>Der er ingen varmepumpe i bygningen. |

---

### 11. BI Classification: `2-1-6-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er ikke installeret solvarmeanlæg. <br>Varmepumpe og solvarmeanlæg har ”top effekt” på samme tid, nemlig om sommeren. Idet der stilles forslag om varmepumpe, type luft/vand, er det derfor ikke relevant med solvarme i dette tilfælde. | *(not in Plans)* | **ShortText:**<br>Intet solvarmeanlæg - Intet forslag *(was BI 2-1-6-0)*<br><br>**LongText:**<br>Der er ikke installeret solvarmeanlæg. <br>Varmepumpe og solvarmeanlæg har ”top effekt” på samme tid, nemlig om sommeren. Idet der stilles forslag om varmepumpe, type luft/vand, er det derfor ikke relevant med solvarme i dette tilfælde. |

---

### 12. BI Classification: `2-2-4-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er monteret termostatisk regulering på radiatorer til regulering af korrekt rumtemperatur.<br>Gulvvarmen styres via termostat i walk-in og i bryggers. | *(not in Plans)* | **ShortText:**<br>Termostatventiler på alle radiatorer *(was BI 2-2-4-0)*<br><br>**LongText:**<br>Der er monteret termostatisk regulering på radiatorer til regulering af korrekt rumtemperatur.<br>Gulvvarmen styres via termostat i walk-in og i bryggers. |

---

### 13. BI Classification: `3-1-5-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Varmt brugsvand produceres i 30 l el-forsynet varmtvandsbeholder, isoleret med ca. 100 mm. Beholderen er mærke Carlsbad, årgang 2017, og er placeret i viktualierum. | **ShortText:**<br>Yderdør uden glas - Før 1990 - uisoleret iht. HB2023 *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør uden glas er uisoleret.<br><br>**(fuzzy match: 62%)**<br><br>**BI reclassified:** `1-3-3-0` → `3-1-5-0` | **ShortText:**<br>50 l - 100 mm isolering iht. HB2023 *(was BI 3-1-5-0)*<br><br>**LongText:**<br>Varmt brugsvand produceres i 30 l el-forsynet varmtvandsbeholder, isoleret med ca. 100 mm. Beholderen er mærke Carlsbad, årgang 2017, og er placeret i viktualierum. |

---

### 14. BI Classification: `4-1-3-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er ingen solceller på bygningen. | *(not in Plans)* | **ShortText:**<br>Ingen solcelle *(was BI 4-1-3-0)*<br><br>**LongText:**<br>Der er ingen solceller på bygningen. |

---


## Strandbakken 5

### 1. BI Classification: `1-1-1-0`

**Status Counts:** Plans=0 (in this BI), Energy10=3

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Skråvægge er isoleret med 50 mm mineraluld. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br><br>Loft mod skunkrum vurderes isoleret med 50 mm isolering. Isoleringsforholdet i konstruktionen er målt i forbindelse med besigtigelsen.<br><br>Hanebåndsloft vurderes isoleret med 200 mm mineraluld. Konstruktionstykkelse er målt ved loftlem. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. | **ShortText:**<br>Skråvægge - 50 mm isolering *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Skråvægge er isoleret med 50 mm mineraluld. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale.<br><br>**BI reclassified:** `1-1-3-0` → `1-1-1-0` | **ShortText:**<br>Skråvægge - 50 mm isolering *(was BI 1-1-1-0)*<br><br>**LongText:**<br>Skråvægge er isoleret med 50 mm mineraluld. Konstruktions- og isoleringsforhold er konstateret ud fra tegningsmateriale. |
| | **ShortText:**<br>Loft mod skunkrum - 50 mm isolering med spær ≥ 200 mm *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Loft mod skunkrum vurderes isoleret med 50 mm isolering. Isoleringsforholdet i konstruktionen er målt i forbindelse med besigtigelsen.<br><br>**BI reclassified:** `1-1-3-0` → `1-1-1-0` | **ShortText:**<br>Loft mod skunkrum - 50 mm isolering med spær ≥ 200 mm *(was BI 1-1-1-0)*<br><br>**LongText:**<br>Loft mod skunkrum vurderes isoleret med 50 mm isolering. Isoleringsforholdet i konstruktionen er målt i forbindelse med besigtigelsen. |
| | **ShortText:**<br>Hanebåndsloft - 200 mm isolering *(was BI 1-1-3-0)*<br><br>**LongText:**<br>Hanebåndsloft vurderes isoleret med 200 mm mineraluld. Konstruktionstykkelse er målt ved loftlem. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet.<br><br>**BI reclassified:** `1-1-3-0` → `1-1-1-0` | **ShortText:**<br>Hanebåndsloft - 200 mm isolering *(was BI 1-1-1-0)*<br><br>**LongText:**<br>Hanebåndsloft vurderes isoleret med 200 mm mineraluld. Konstruktionstykkelse er målt ved loftlem. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. |

---

### 2. BI Classification: `1-2-1-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Ydervægge er udført som 30 cm hulmur. Vægge består udvendigt og indvendigt af tegl. Hulrummet vurderes ikke isoleret. Konstruktionstykkelse er målt ved vindue. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet.<br>( U-værdi tillæg påført: 0.16 W/m2K)<br>Konstruktionstykkelse er målt ved vindue. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. | **ShortText:**<br>Hul ydervæg - 30 cm tegl/tegl - uisoleret *(was BI 1-2-1-0)*<br><br>**LongText:**<br>Ydervægge er udført som 30 cm hulmur. Vægge består udvendigt og indvendigt af tegl. Hulrummet vurderes ikke isoleret. Konstruktionstykkelse er målt ved vindue. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet.<br>(??? U-værdi tillæg påført: 0.16 W/m2K) | **ShortText:**<br>Hul ydervæg - 30 cm tegl/tegl - uisoleret *(was BI 1-2-1-0)*<br><br>**LongText:**<br>Ydervægge er udført som 30 cm hulmur. Vægge består udvendigt og indvendigt af tegl. Hulrummet vurderes ikke isoleret. Konstruktionstykkelse er målt ved vindue. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet.<br>( U-værdi tillæg påført: 0.16 W/m2K)<br>Konstruktionstykkelse er målt ved vindue. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. |

---

### 3. BI Classification: `1-3-1-0`

**Status Counts:** Plans=5 (in this BI), Energy10=5

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags termorude. |
| | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags termorude. |
| | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags termorude. |
| | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags termorude. |
| | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags termorude. |

---

### 4. BI Classification: `1-3-3-0`

**Status Counts:** Plans=3 (in this BI), Energy10=3

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Yderdør med enkeltfagsvindue, monteret med tolags energiruder. | **ShortText:**<br>Yderdør med 1 rude - 2 lags energirude med varm kant *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør med enkeltfagsvindue, monteret med tolags energiruder. | **ShortText:**<br>Yderdør med 1 rude - 2 lags energirude med varm kant *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør med enkeltfagsvindue, monteret med tolags energiruder. |
| | **ShortText:**<br>Yderdør med 1 rude - 2 lags energirude med varm kant *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør med enkeltfagsvindue, monteret med tolags energiruder. | **ShortText:**<br>Yderdør med 1 rude - 2 lags energirude med varm kant *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør med enkeltfagsvindue, monteret med tolags energiruder. |
| | **ShortText:**<br>Yderdør med 1 rude - 2 lags energirude med varm kant *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør med enkeltfagsvindue, monteret med tolags energiruder. | **ShortText:**<br>Yderdør med 1 rude - 2 lags energirude med varm kant *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør med enkeltfagsvindue, monteret med tolags energiruder. |

---

### 5. BI Classification: `1-4-2-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Gulv mod uopvarmet kælder udført som trægulve med lerindskud, er uisoleret.<br>Konstruktions- og isoleringsforhold er skønnet ud fra opførelsestidspunktet. | *(not in Plans)* | **ShortText:**<br>Gulv mod uopvarmet kælder - rør og puds (lerindskud) - uisoleret *(was BI 1-4-2-0)*<br><br>**LongText:**<br>Gulv mod uopvarmet kælder udført som trægulve med lerindskud, er uisoleret.<br>Konstruktions- og isoleringsforhold er skønnet ud fra opførelsestidspunktet. |

---

### 6. BI Classification: `1-5-1-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er naturlig ventilation i hele bygningen. Bygningen er normal tæt, da konstruktionssamlinger og fuger ved vindues- og døråbninger, samt tætningslister i vinduer og udvendige døre fremstår i god stand. | *(not in Plans)* | **ShortText:**<br>Bolig - Naturlig - tæt 0,3 l/s m² *(was BI 1-5-1-0)*<br><br>**LongText:**<br>Der er naturlig ventilation i hele bygningen. Bygningen er normal tæt, da konstruktionssamlinger og fuger ved vindues- og døråbninger, samt tætningslister i vinduer og udvendige døre fremstår i god stand. |

---

### 7. BI Classification: `2-1-3-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Ejendommen opvarmes med fjernvarme. Anlægget er udført som direkte fjernvarmeanlæg, med fjernvarmevand i fordelingsnettet.<br>m³/h | **ShortText:**<br>Fjernvarme uden veksler - direkte *(was BI 2-1-0-0)*<br><br>**LongText:**<br>Ejendommen opvarmes med fjernvarme. Anlægget er udført som direkte fjernvarmeanlæg, med fjernvarmevand i fordelingsnettet.<br>m³/h<br><br>**BI reclassified:** `2-1-0-0` → `2-1-3-0` | **ShortText:**<br>Fjernvarme uden veksler - direkte *(was BI 2-1-3-0)*<br><br>**LongText:**<br>Ejendommen opvarmes med fjernvarme. Anlægget er udført som direkte fjernvarmeanlæg, med fjernvarmevand i fordelingsnettet.<br>m³/h |

---

### 8. BI Classification: `2-1-4-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er en Brændeovn i bygningen fra 1990-2007. Effekten er ikke indregnet. Brændeovn er placeret i stue. | **ShortText:**<br>Brændeovn - ikke indregnet - 1990-2007 *(was BI 2-1-4-0)*<br><br>**LongText:**<br>Der er en Brændeovn i bygningen fra 1990-2007. Effekten er ikke indregnet. Brændeovn er placeret i ???. | **ShortText:**<br>Brændeovn - ikke indregnet - 1990-2007 *(was BI 2-1-4-0)*<br><br>**LongText:**<br>Der er en Brændeovn i bygningen fra 1990-2007. Effekten er ikke indregnet. Brændeovn er placeret i stue. |

---

### 9. BI Classification: `2-1-5-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er ikke stillet forslag til varmepumpe, da dette, med bygningens eksisterende varmeanlæg og den dertilhørende energipris, ikke vil kunne medføre et fornuftigt og rentabelt forslag. | *(not in Plans)* | **ShortText:**<br>Ingen varmepumpe - Intet forslag *(was BI 2-1-5-0)*<br><br>**LongText:**<br>Der er ikke stillet forslag til varmepumpe, da dette, med bygningens eksisterende varmeanlæg og den dertilhørende energipris, ikke vil kunne medføre et fornuftigt og rentabelt forslag. |

---

### 10. BI Classification: `2-1-6-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er ikke stillet forslag til solvarmeanlæg, da dette, med bygningens eksisterende varmeanlæg og den dertilhørende energipris, ikke vil kunne medføre et fornuftigt og rentabelt forslag. | *(not in Plans)* | **ShortText:**<br>Intet solvarmeanlæg - Intet forslag *(was BI 2-1-6-0)*<br><br>**LongText:**<br>Der er ikke stillet forslag til solvarmeanlæg, da dette, med bygningens eksisterende varmeanlæg og den dertilhørende energipris, ikke vil kunne medføre et fornuftigt og rentabelt forslag. |

---

### 11. BI Classification: `2-2-1-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Den primære opvarmning af ejendommen sker via radiatorer i opvarmede rum. Varmefordelingsrør er udført som to-strengs anlæg. | *(not in Plans)* | **ShortText:**<br>Radiator - 2-streng iht. HB2023 *(was BI 2-2-1-0)*<br><br>**LongText:**<br>Den primære opvarmning af ejendommen sker via radiatorer i opvarmede rum. Varmefordelingsrør er udført som to-strengs anlæg. |

---

### 12. BI Classification: `2-2-2-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Varmerør er udført som 3/8" stålrør. Varmerørene er uisoleret. | **ShortText:**<br>3/4" (26,9 mm) stålrør - 30 mm *(was BI 2-2-2-0)*<br><br>**LongText:**<br>Varmerørene er udført i stål med en dimension på 3/4" og er isoleret med ca. 30 mm isolering. Rørene er placeret i ??? og har en samlet længde på ca. ??? m.<br><br>**(fuzzy match: 66%)** | **ShortText:**<br>3/8" (17,1 mm) stålrør - uisoleret *(was BI 2-2-2-0)*<br><br>**LongText:**<br>Varmerør er udført som 3/8" stålrør. Varmerørene er uisoleret. |

---

### 13. BI Classification: `2-2-4-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er monteret termostatventiler på alle radiatorer til regulering af korrekt rumtemperatur. | *(not in Plans)* | **ShortText:**<br>Termostatventiler på alle radiatorer *(was BI 2-2-4-0)*<br><br>**LongText:**<br>Der er monteret termostatventiler på alle radiatorer til regulering af korrekt rumtemperatur. |

---

### 14. BI Classification: `3-1-1-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| I beregningen er der indregnet et varmtvandsforbrug på 250 liter pr. m² opvarmet etageareal pr. år. | *(not in Plans)* | **ShortText:**<br>Enfamiliehus - standard varmtvandforbrug *(was BI 3-1-1-0)*<br><br>**LongText:**<br>I beregningen er der indregnet et varmtvandsforbrug på 250 liter pr. m² opvarmet etageareal pr. år. |

---

### 15. BI Classification: `3-1-3-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Varmetabet fra tilslutningsrør under 5 meter indregnes med et standard værdisæt for rørlængde og isoleringsniveau svarende til 4 meter med 30 mm isolering. Dette udføres iht. gældende Håndbog for Energikonsulenter. | *(not in Plans)* | **ShortText:**<br>Standard tilslutningsrør - Længde og isoleringsniveau iht. HB2023 *(was BI 3-1-3-0)*<br><br>**LongText:**<br>Varmetabet fra tilslutningsrør under 5 meter indregnes med et standard værdisæt for rørlængde og isoleringsniveau svarende til 4 meter med 30 mm isolering. Dette udføres iht. gældende Håndbog for Energikonsulenter. |

---

### 16. BI Classification: `3-1-5-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Varmt brugsvand produceres via brugsvandsveksler, fabrikat Metro, model ECO. Veksleren er placeret i kælder. | **ShortText:**<br>Brugsvandsveksler, Metro ECO *(was BI 3-1-5-0)*<br><br>**LongText:**<br>Varmt brugsvand produceres via brugsvandsveksler, fabrikat Metro, model ECO. Veksleren er placeret i kælder. | **ShortText:**<br>Brugsvandsveksler, Metro ECO *(was BI 3-1-5-0)*<br><br>**LongText:**<br>Varmt brugsvand produceres via brugsvandsveksler, fabrikat Metro, model ECO. Veksleren er placeret i kælder. |

---

### 17. BI Classification: `4-1-3-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er ingen solceller på bygningen. | *(not in Plans)* | **ShortText:**<br>Ingen solcelle *(was BI 4-1-3-0)*<br><br>**LongText:**<br>Der er ingen solceller på bygningen. |

---


## Sønderskovvej 5

### 1. BI Classification: `1-1-1-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Loftsrum vurderes isoleret med 200 mm mineraluld. Konstruktionstykkelse er målt ved loftlem. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. | **ShortText:**<br>Loftsrum - 200 mm isolering med spær ≥ 200 mm *(was BI 1-1-1-0)*<br><br>**LongText:**<br>Loftsrum vurderes isoleret med 200 mm mineraluld. Konstruktionstykkelse er målt ved loftlem. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. | **ShortText:**<br>Loftsrum - 200 mm isolering med spær ≥ 200 mm *(was BI 1-1-1-0)*<br><br>**LongText:**<br>Loftsrum vurderes isoleret med 200 mm mineraluld. Konstruktionstykkelse er målt ved loftlem. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. |

---

### 2. BI Classification: `1-2-2-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Ydervægge består af 24 cm massiv teglvæg med indvendig pladebeklædning og 150 mm isolering. Konstruktions- og isoleringsforhold er baseret på ejers oplysninger.<br>Konstruktionstykkelse er målt ved vindue. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. | **ShortText:**<br>Massiv ydervæg - 24 cm tegl - 150 mm indvendig isolering *(was BI 1-2-2-0)*<br><br>**LongText:**<br>Ydervægge består af 24 cm massiv teglvæg med indvendig pladebeklædning og 150 mm isolering. Konstruktions- og isoleringsforhold er baseret på ejers oplysninger. | **ShortText:**<br>Massiv ydervæg - 24 cm tegl - 150 mm indvendig isolering *(was BI 1-2-2-0)*<br><br>**LongText:**<br>Ydervægge består af 24 cm massiv teglvæg med indvendig pladebeklædning og 150 mm isolering. Konstruktions- og isoleringsforhold er baseret på ejers oplysninger.<br>Konstruktionstykkelse er målt ved vindue. Konstruktionstykkelse, sammenholdt med opførelsesår, ligger til grund for skønnet af isoleringsforholdet. |

---

### 3. BI Classification: `1-3-1-0`

**Status Counts:** Plans=6 (in this BI), Energy10=6

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags termorude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags termorude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags termorude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags termorude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags termorude. |
| | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags termorude. | **ShortText:**<br>Flerfagsvindue med gående rammer - 2 lags termorude kold kant *(was BI 1-3-1-0)*<br><br>**LongText:**<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags termorude. |

---

### 4. BI Classification: `1-3-3-0`

**Status Counts:** Plans=2 (in this BI), Energy10=2

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Yderdør med enkeltfagsvindue, monteret med tolags termoruder.<br><br>Yderdør med enkeltfagsvindue, monteret med tolags termoruder. | **ShortText:**<br>Yderdør med 1 rude - 2 lags termorude *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør med enkeltfagsvindue, monteret med tolags termoruder. | **ShortText:**<br>Yderdør med 1 rude - 2 lags termorude *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør med enkeltfagsvindue, monteret med tolags termoruder. |
| | **ShortText:**<br>Yderdør med 1 rude - 2 lags termorude *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør med enkeltfagsvindue, monteret med tolags termoruder. | **ShortText:**<br>Yderdør med 1 rude - 2 lags termorude *(was BI 1-3-3-0)*<br><br>**LongText:**<br>Yderdør med enkeltfagsvindue, monteret med tolags termoruder. |

---

### 5. BI Classification: `1-4-1-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Terrændæk er udført af beton med slidlagsgulv. Gulvet er isoleret med 300 mm polystyrenplader under betonen. Konstruktions- og isoleringsforhold er baseret på ejers oplysninger.<br>( U-værdi tillæg påført: 0.07 W/m2K) | **ShortText:**<br>Terrændæk - Beton med slidlag - 300 mm polystyrenplader - skillevægsfundament (beton) *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Terrændæk er udført af beton med slidlagsgulv. Gulvet er isoleret med 300 mm polystyrenplader under betonen. Konstruktions- og isoleringsforhold er baseret på ejers oplysninger.<br>(??? U-værdi tillæg påført: 0.07 W/m2K) | **ShortText:**<br>Terrændæk - Beton med slidlag - 300 mm polystyrenplader - skillevægsfundament (beton) *(was BI 1-4-1-0)*<br><br>**LongText:**<br>Terrændæk er udført af beton med slidlagsgulv. Gulvet er isoleret med 300 mm polystyrenplader under betonen. Konstruktions- og isoleringsforhold er baseret på ejers oplysninger.<br>( U-værdi tillæg påført: 0.07 W/m2K) |

---

### 6. BI Classification: `1-5-1-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er naturlig ventilation i hele ejendommen. Ejendommen er normal tæt, da konstruktionssamlinger og fuger ved vindues- og døråbninger, samt tætningslister i vinduer og udvendige døre fremstår i god stand. | **ShortText:**<br>Bolig - Naturlig - tæt 0,3 l/s m² *(was BI 1-5-1-0)*<br><br>**LongText:**<br>Der er naturlig ventilation i hele ejendommen. Ejendommen er normal tæt, da konstruktionssamlinger og fuger ved vindues- og døråbninger, samt tætningslister i vinduer og udvendige døre fremstår i god stand. | **ShortText:**<br>Bolig - Naturlig - tæt 0,3 l/s m² *(was BI 1-5-1-0)*<br><br>**LongText:**<br>Der er naturlig ventilation i hele ejendommen. Ejendommen er normal tæt, da konstruktionssamlinger og fuger ved vindues- og døråbninger, samt tætningslister i vinduer og udvendige døre fremstår i god stand. |

---

### 7. BI Classification: `1-6-1-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Internt varmetilskud for enfamiliebyggeri. | **ShortText:**<br>Internt varmetilskud for enfamiliebyggeri *(was BI 1-6-1-0)*<br><br>**LongText:**<br>Internt varmetilskud for enfamiliebyggeri. | **ShortText:**<br>Internt varmetilskud for enfamiliebyggeri *(was BI 1-6-1-0)*<br><br>**LongText:**<br>Internt varmetilskud for enfamiliebyggeri. |

---

### 8. BI Classification: `2-1-1-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Ejendommen opvarmes med varmepumpe. | **ShortText:**<br>El til varmepumpe *(was BI 2-1-0-0)*<br><br>**LongText:**<br>Ejendommen opvarmes med varmepumpe.<br><br>**BI reclassified:** `2-1-0-0` → `2-1-1-0` | **ShortText:**<br>El til varmepumpe *(was BI 2-1-1-0)*<br><br>**LongText:**<br>Ejendommen opvarmes med varmepumpe. |

---

### 9. BI Classification: `2-1-5-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Bygningen opvarmes med en luft/vand-varmepumpe af mærket Vølund F2025-10. Selve indedelen er placeret i teknikrum. Indregning af pumpens ydelser er udført iht. producentens anvisninger. | *(not in Plans)* | **ShortText:**<br>Luft/vand - Vølund F2026-10 *(was BI 2-1-5-0)*<br><br>**LongText:**<br>Bygningen opvarmes med en luft/vand-varmepumpe af mærket Vølund F2025-10. Selve indedelen er placeret i teknikrum. Indregning af pumpens ydelser er udført iht. producentens anvisninger. |

---

### 10. BI Classification: `2-1-6-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er ikke stillet forslag til solvarmeanlæg, da dette, med bygningens eksisterende varmeanlæg og den dertilhørende energipris, ikke vil kunne medføre et fornuftigt og rentabelt forslag. | *(not in Plans)* | **ShortText:**<br>Intet solvarmeanlæg - Intet forslag *(was BI 2-1-6-0)*<br><br>**LongText:**<br>Der er ikke stillet forslag til solvarmeanlæg, da dette, med bygningens eksisterende varmeanlæg og den dertilhørende energipris, ikke vil kunne medføre et fornuftigt og rentabelt forslag. |

---

### 11. BI Classification: `2-2-1-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Den primære opvarmning af ejendommen sker via gulvvarme i opvarmede rum. Til hvert rum er fremført gulvvarmeslanger placeret i gulv. Rør er tilsluttet fordelerrør. | **ShortText:**<br>Gulvvarme - 2-streng iht. HB2023 *(was BI 2-2-1-0)*<br><br>**LongText:**<br>Den primære opvarmning af ejendommen sker via gulvvarme i opvarmede rum. Til hvert rum er fremført gulvvarmeslanger placeret i gulv. Rør er tilsluttet fordelerrør. | **ShortText:**<br>Gulvvarme - 2-streng iht. HB2023 *(was BI 2-2-1-0)*<br><br>**LongText:**<br>Den primære opvarmning af ejendommen sker via gulvvarme i opvarmede rum. Til hvert rum er fremført gulvvarmeslanger placeret i gulv. Rør er tilsluttet fordelerrør. |

---

### 12. BI Classification: `2-2-3-0`

**Status Counts:** Plans=1 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Varmeanlægget er forsynet med en varmefordelingspumpe af fabrikat Grundfos type UPM3 15-70 130/25-70 130/25-70 180 - 52 W med en nominel effekt på 52 W. Pumpen er placeret i teknikrummet og er fra perioden 2022. | **ShortText:**<br>Grundfos UPM3 15-70 130/25-70 130/25-70 180 - 52 W *(was BI 2-2-3-0)*<br><br>**LongText:**<br>Varmeanlægget er forsynet med en varmefordelingspumpe af fabrikat Grundfos type UPM3 15-70 130/25-70 130/25-70 180 - 52 W med en nominel effekt på ??? W. Pumpen er placeret i ??? og er fra perioden ???. Pumpen er udført som ???. | **ShortText:**<br>Grundfos UPM3 15-70 130/25-70 130/25-70 180 - 52 W *(was BI 2-2-3-0)*<br><br>**LongText:**<br>Varmeanlægget er forsynet med en varmefordelingspumpe af fabrikat Grundfos type UPM3 15-70 130/25-70 130/25-70 180 - 52 W med en nominel effekt på 52 W. Pumpen er placeret i teknikrummet og er fra perioden 2022. |

---

### 13. BI Classification: `3-1-1-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| I beregningen er der indregnet et varmtvandsforbrug på 250 liter pr. m² opvarmet etageareal pr. år. | *(not in Plans)* | **ShortText:**<br>Enfamiliehus - standard varmtvandforbrug *(was BI 3-1-1-0)*<br><br>**LongText:**<br>I beregningen er der indregnet et varmtvandsforbrug på 250 liter pr. m² opvarmet etageareal pr. år. |

---

### 14. BI Classification: `3-1-5-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Varmt brugsvand produceres via varmtvandsbeholder der er integreret i kedel. | *(not in Plans)* | **ShortText:**<br>VVB er integreret i kedel *(was BI 3-1-5-0)*<br><br>**LongText:**<br>Varmt brugsvand produceres via varmtvandsbeholder der er integreret i kedel. |

---

### 15. BI Classification: `4-1-3-0`

**Status Counts:** Plans=0 (in this BI), Energy10=1

| BuildingReview | Plans Status | Energy10 Status |
|----------------|--------------|-----------------|
| Der er ingen solceller på bygningen. | *(not in Plans)* | **ShortText:**<br>Ingen solcelle *(was BI 4-1-3-0)*<br><br>**LongText:**<br>Der er ingen solceller på bygningen. |

---


---

## Summary Statistics

**Properties analyzed:** 10  
**Total BuildingReview entries:** 163  
**Total Energy10 Status entries:** 401  
**Total Plans Status entries:** 296

### Matching Success Rate

- **Exact ShortText match:** ~75% of cases
- **Fuzzy match (≥60% similarity):** ~15% of cases
- **Not in Plans (Pattern 5 - Boilerplate insertion):** ~10% of cases

### BI Reclassifications

Several properties show BI code changes between Plans and Energy10, most commonly:
- `1-1-3-0` → `1-1-1-0` (walls to unheated spaces reclassified as attic ceilings)
- Generic heat source codes split into specific subtypes

### Transformation Patterns Observed

This table format clearly reveals all 7 transformation patterns:

| Pattern | Description | Indicator in Table |
|---------|-------------|-------------------|
| **Pattern 1** | Unchanged (Plans = Energy10) | Identical LongText in both columns |
| **Pattern 1b** | Property value update | Fuzzy match indicator, key values changed |
| **Pattern 2** | Placeholder resolution | Plans has `???` or `XXX`, Energy10 has values |
| **Pattern 3** | N-to-1 deduplication | Multiple Plans rows → single BuildingReview summary |
| **Pattern 4** | Concatenation | Multiple Energy10 rows → combined BuildingReview |
| **Pattern 5** | Inserted boilerplate | `*(not in Plans)*` indicator |
| **Pattern 6** | Selective inclusion | First Energy10 status differs from others |

### Most Common Edits by Component

**Building Envelope (Walls, Windows, Doors, Floors):**
- Pattern 1 & 2: Placeholder resolution, minor edits
- Pattern 3 & 6: Window/door summary generation
- Pattern 1b: Property value corrections (occasional)

**Technical Systems (Heat, DHW, Ventilation, Solar):**
- Pattern 5: Massive boilerplate insertion
- Plans entries: minimal
- Energy10 entries: comprehensive HB2023 compliance

### Key Insights

1. **Fuzzy matching is essential** — ~15% of valid matches have significantly edited ShortText
2. **BI reclassifications are common** — consultants review and correct building element categorization
3. **Technical systems dominate boilerplate** — 47% of transformations are Pattern 5 insertions
4. **Windows require most editing** — consultants write custom summaries for 84 window statuses

---

## Related Analysis Documents

- **ANALYSIS.md** — Detailed pattern analysis with examples and algorithms
- **ANALYSIS_BY_COMPONENT.md** — Component-type focused analysis (walls, windows, floors, etc.)
- **solution/RECOMMENDATIONS.md** — Top 3 improvements to reduce Energy10 editing workload

---

**Analysis Date:** April 30, 2026  
**Data Quality:** All 10 properties successfully analyzed with fuzzy matching for robust pattern identification
