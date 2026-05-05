# Generated vs PDFReportData Comparison

Side-by-side comparison of LLM-generated window/door summaries (from the Plans input XML) and the consultant's PDFReportData summaries (from the final XML).

**Legend:**
- ✅ Identical: byte-equal (after whitespace/case normalisation)
- ✅ Equivalent: ≥85% of the consultant's domain keywords are present in the generated text
- ⚠️ Partial overlap: 50-84% of the consultant's keywords are present
- ❌ Differs: less than 50% keyword overlap
- — No PDF text: consultant did not provide a PDFReportData entry for this classification

---

## Match Scoreboard

Total comparisons (with consultant text): **21**

| Match level | Count |
|---|---|
| ✅ Identical | 1 |
| ✅ Equivalent | 8 |
| ⚠️ Partial overlap | 7 |
| ❌ Differs | 5 |
| — No PDF text | 3 |

---

# Projects with JSON Enrichment

## Ivarsvej_27_5200_Odense_V (JSON enriched)

- Input XML: `Ivarsvej_27_5200_Odense_V.xml`
- Final XML: `Ivarsvej_27_5200_Odense_V final.xml`

### Combined view (all 10 entries across 3 classifications) · ⚠️ Partial overlap

<table>
<thead><tr><th style="width:30%">PDFReportData (all consultant text)</th><th style="width:30%">Generated (all classifications joined)</th><th style="width:40%">Individual Entries (all)</th></tr></thead>
<tbody><tr>
<td valign="top">[1-3-1-0]<br>Vinduerne er monteret med tolags energirude.<br><br>[1-3-2-0]<br>Ovenlysvindue er monteret med trelags energirude<br><br>[1-3-3-0]<br>Terrassedør og hoveddør med sideparti er monteret med tolags energiruder.</td>
<td valign="top">Vinduerne er monteret med tolags energirude.<br><br>Ovenlysvinduerne er monteret med trelags energirude.<br><br>Terrassedøren i køkkenet er monteret med tolags energirude, mens yderdøren i entreen har trelags energirude.</td>
<td valign="top"><strong style="color:#888">— Standard windows (Vinduer) (6) —</strong><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>2.26 m² · U=1.4 · mod øst<br><em>stueetage / Køkken / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>4.58 m² · U=1.4 · mod syd<br><em>stueetage / Dagligstue / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>2.41 m² · U=1.4 · mod syd<br><em>stueetage / Dagligstue / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>1.17 m² · U=1.4 · mod nord<br><em>1. sal / Badeværelse / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>1.54 m² · U=1.4 · mod nord<br><em>1. sal / Soveværelse / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>2.15 m² · U=1.4 · mod syd<br><em>1. sal / Soveværelse 2 / Væg 2</em><br><br><strong style="color:#888">— Skylights (Ovenlysvinduer) (2) —</strong><br><br><strong>Ovenlysvindue - 3 lags energirude - efter BR15</strong><br>1.12 m² · U=1.6 · mod vest<br><em>1. sal / Trapperum / Loft 5</em><br><br><strong>Ovenlysvindue - 3 lags energirude - efter BR15</strong><br>1.12 m² · U=1.6 · mod øst<br><em>1. sal / værelse / Loft 2</em><br><br><strong style="color:#888">— Doors with glass (Døre/Terrassedøre) (2) —</strong><br><br><strong>Terrassedør med sideparti - 2 lags energirude med varm kant</strong><br>2.05 m² · U=1.3 · mod nord<br><em>stueetage / Køkken / Væg 3</em><br><br><strong>Yderdør med sideparti - 3 lags energirude - energiklasse B</strong><br>1.96 m² · U=1.15 · mod vest<br><em>stueetage / Entre / Væg 1</em></td>
</tr></tbody>
</table>

<details><summary>Per-classification breakdown</summary>

#### 1-3-1-0 — Standard windows (Vinduer) (6 entries) · ✅ Identical

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">Vinduerne er monteret med tolags energirude.</td>
<td valign="top">Vinduerne er monteret med tolags energirude.</td>
<td valign="top"><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>2.26 m² · U=1.4 · mod øst<br><em>stueetage / Køkken / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>4.58 m² · U=1.4 · mod syd<br><em>stueetage / Dagligstue / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>2.41 m² · U=1.4 · mod syd<br><em>stueetage / Dagligstue / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>1.17 m² · U=1.4 · mod nord<br><em>1. sal / Badeværelse / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>1.54 m² · U=1.4 · mod nord<br><em>1. sal / Soveværelse / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>2.15 m² · U=1.4 · mod syd<br><em>1. sal / Soveværelse 2 / Væg 2</em></td>
</tr></tbody>
</table>

#### 1-3-2-0 — Skylights (Ovenlysvinduer) (2 entries) · ✅ Equivalent

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">Ovenlysvindue er monteret med trelags energirude</td>
<td valign="top">Ovenlysvinduerne er monteret med trelags energirude.</td>
<td valign="top"><strong>Ovenlysvindue - 3 lags energirude - efter BR15</strong><br>1.12 m² · U=1.6 · mod vest<br><em>1. sal / Trapperum / Loft 5</em><br><br><strong>Ovenlysvindue - 3 lags energirude - efter BR15</strong><br>1.12 m² · U=1.6 · mod øst<br><em>1. sal / værelse / Loft 2</em></td>
</tr></tbody>
</table>

#### 1-3-3-0 — Doors with glass (Døre/Terrassedøre) (2 entries) · ❌ Differs

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">Terrassedør og hoveddør med sideparti er monteret med tolags energiruder.</td>
<td valign="top">Terrassedøren i køkkenet er monteret med tolags energirude, mens yderdøren i entreen har trelags energirude.</td>
<td valign="top"><strong>Terrassedør med sideparti - 2 lags energirude med varm kant</strong><br>2.05 m² · U=1.3 · mod nord<br><em>stueetage / Køkken / Væg 3</em><br><br><strong>Yderdør med sideparti - 3 lags energirude - energiklasse B</strong><br>1.96 m² · U=1.15 · mod vest<br><em>stueetage / Entre / Væg 1</em></td>
</tr></tbody>
</table>

</details>

---

## Kirkegyden_15_5270_Odense_N (JSON enriched)

- Input XML: `Kirkegyden_15_5270_Odense_N.xml`
- Final XML: `Kirkegyden_15_5270_Odense_N final.xml`

### Combined view (all 22 entries across 2 classifications) · ⚠️ Partial overlap

<table>
<thead><tr><th style="width:30%">PDFReportData (all consultant text)</th><th style="width:30%">Generated (all classifications joined)</th><th style="width:40%">Individual Entries (all)</th></tr></thead>
<tbody><tr>
<td valign="top">[1-3-1-0]<br>De fleste vinduer er monteret med tolags termorude. Vinduer i bryggers er monteret med etlags glasruder. Vinduer i værelse mod nordvest er monteret med etlags glasrude og forsatsrude.<br>Enkelte vinduer er monteret med tolags energiruder.<br><br>[1-3-3-0]<br>Yderdøre er med uisoleret fyldning og enkeltfagsvindue monteret med tolags termoruder.<br><br>Yderdør ved gang i nordøstfløj, monteret med tolags energiruder.</td>
<td valign="top">Vinduerne er hovedsageligt monteret med tolags termorude. Vinduer i køkkenet mod nordvest er monteret med etlags glas, vinduer i gangen og i et værelse mod nordøst er monteret med tolags energirude, og vinduer i et værelse mod nordvest er monteret med etlags glasrude og forsatsrude.<br><br>Yderdørene er hovedsageligt monteret med tolags termorude, mens yderdøren i gangen har tolags energirude.</td>
<td valign="top"><strong style="color:#888">— Standard windows (Vinduer) (16) —</strong><br><br><strong>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant</strong><br>0.82 m² · U=2.7 · mod sydøst<br><em>stueetage / værelse / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer og sprosser - 1 lag glas</strong><br>0.9 m² · U=4.1 · mod nordvest<br><em>stueetage / Køkken / Væg 2</em><br><br><strong>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant</strong><br>0.89 m² · U=2.7 · mod nordvest<br><em>stueetage / Bryggers / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant</strong><br>0.73 m² · U=2.7 · mod nordvest<br><em>stueetage / Køkken / Væg 2</em><br><br><strong>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant</strong><br>0.88 m² · U=2.7 · mod sydøst<br><em>stueetage / Køkken 2 viktualierum / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant</strong><br>4.23 m² · U=2.7 · mod sydvest<br><em>stueetage / Dagligstue / Væg 2</em><br><br><strong>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant</strong><br>0.96 m² · U=2.7 · mod nordøst<br><em>stueetage / Soveværelse / Væg 2</em><br><br><strong>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant</strong><br>1.26 m² · U=2.7 · mod nordøst<br><em>stueetage / Dagligstue 2 / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant</strong><br>0.77 m² · U=2.7 · mod nordøst<br><em>stueetage / Dagligstue 3 / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant</strong><br>0.91 m² · U=2.7 · mod nordøst<br><em>stueetage / Dagligstue 3 / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer og sprosser - 2 lags energirude med varm kant</strong><br>0.97 m² · U=1.4 · mod sydvest<br><em>stueetage / Gang / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant</strong><br>1.46 m² · U=2.7 · mod nordøst<br><em>stueetage / Kontor / Væg 3</em><br><br><strong>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant</strong><br>0.89 m² · U=2.7 · mod sydvest<br><em>stueetage / Badeværelse 2 / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer og sprosser - 2 lags energirude med kold kant</strong><br>0.8 m² · U=1.5 · mod nordøst<br><em>stueetage / værelse / Væg 3</em><br><br><strong>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant</strong><br>0.32 m² · U=2.7 · mod sydøst<br><em>stueetage / Badeværelse 4 / Væg 2</em><br><br><strong>Flerfagsvindue med gående rammer - 1+1 lag glas</strong><br>0.69 m² · U=2.2 · mod nordvest<br><em>stueetage / værelse / Væg 1</em><br><br><strong style="color:#888">— Doors with glass (Døre/Terrassedøre) (6) —</strong><br><br><strong>Yderdør med uisoleret fyldning og 1 rude - 2 lags termorude</strong><br>1.65 m² · U=2.8 · mod sydvest<br><em>stueetage / Bryggers / Væg 3</em><br><br><strong>Yderdør med uisoleret fyldning og 1 rude - 2 lags termorude</strong><br>1.62 m² · U=2.8 · mod nordvest<br><em>stueetage / Entre / Væg 1</em><br><br><strong>Yderdør med uisoleret fyldning og 1 rude - 2 lags termorude</strong><br>3.49 m² · U=2.8 · mod sydøst<br><em>stueetage / Dagligstue 2 / Væg 2</em><br><br><strong>Yderdør med 1 rude - 2 lags energirude med varm kant</strong><br>2.77 m² · U=1.3 · mod sydvest<br><em>stueetage / Gang / Væg 1</em><br><br><strong>Yderdør med uisoleret fyldning og 1 rude - 2 lags termorude</strong><br>1.71 m² · U=2.8 · mod nordøst<br><em>stueetage / Gang 3 / Væg 3</em><br><br><strong>Yderdør med uisoleret fyldning og 1 rude - 2 lags termorude</strong><br>2.12 m² · U=2.8 · mod sydvest<br><em>stueetage / Gang 3 / Væg 4</em></td>
</tr></tbody>
</table>

<details><summary>Per-classification breakdown</summary>

#### 1-3-1-0 — Standard windows (Vinduer) (16 entries) · ✅ Equivalent

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">De fleste vinduer er monteret med tolags termorude. Vinduer i bryggers er monteret med etlags glasruder. Vinduer i værelse mod nordvest er monteret med etlags glasrude og forsatsrude.<br>Enkelte vinduer er monteret med tolags energiruder.</td>
<td valign="top">Vinduerne er hovedsageligt monteret med tolags termorude. Vinduer i køkkenet mod nordvest er monteret med etlags glas, vinduer i gangen og i et værelse mod nordøst er monteret med tolags energirude, og vinduer i et værelse mod nordvest er monteret med etlags glasrude og forsatsrude.</td>
<td valign="top"><strong>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant</strong><br>0.82 m² · U=2.7 · mod sydøst<br><em>stueetage / værelse / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer og sprosser - 1 lag glas</strong><br>0.9 m² · U=4.1 · mod nordvest<br><em>stueetage / Køkken / Væg 2</em><br><br><strong>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant</strong><br>0.89 m² · U=2.7 · mod nordvest<br><em>stueetage / Bryggers / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant</strong><br>0.73 m² · U=2.7 · mod nordvest<br><em>stueetage / Køkken / Væg 2</em><br><br><strong>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant</strong><br>0.88 m² · U=2.7 · mod sydøst<br><em>stueetage / Køkken 2 viktualierum / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant</strong><br>4.23 m² · U=2.7 · mod sydvest<br><em>stueetage / Dagligstue / Væg 2</em><br><br><strong>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant</strong><br>0.96 m² · U=2.7 · mod nordøst<br><em>stueetage / Soveværelse / Væg 2</em><br><br><strong>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant</strong><br>1.26 m² · U=2.7 · mod nordøst<br><em>stueetage / Dagligstue 2 / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant</strong><br>0.77 m² · U=2.7 · mod nordøst<br><em>stueetage / Dagligstue 3 / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant</strong><br>0.91 m² · U=2.7 · mod nordøst<br><em>stueetage / Dagligstue 3 / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer og sprosser - 2 lags energirude med varm kant</strong><br>0.97 m² · U=1.4 · mod sydvest<br><em>stueetage / Gang / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant</strong><br>1.46 m² · U=2.7 · mod nordøst<br><em>stueetage / Kontor / Væg 3</em><br><br><strong>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant</strong><br>0.89 m² · U=2.7 · mod sydvest<br><em>stueetage / Badeværelse 2 / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer og sprosser - 2 lags energirude med kold kant</strong><br>0.8 m² · U=1.5 · mod nordøst<br><em>stueetage / værelse / Væg 3</em><br><br><strong>Flerfagsvindue med gående rammer og sprosser - 2 lags termorude kold kant</strong><br>0.32 m² · U=2.7 · mod sydøst<br><em>stueetage / Badeværelse 4 / Væg 2</em><br><br><strong>Flerfagsvindue med gående rammer - 1+1 lag glas</strong><br>0.69 m² · U=2.2 · mod nordvest<br><em>stueetage / værelse / Væg 1</em></td>
</tr></tbody>
</table>

#### 1-3-3-0 — Doors with glass (Døre/Terrassedøre) (6 entries) · ❌ Differs

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">Yderdøre er med uisoleret fyldning og enkeltfagsvindue monteret med tolags termoruder.<br><br>Yderdør ved gang i nordøstfløj, monteret med tolags energiruder.</td>
<td valign="top">Yderdørene er hovedsageligt monteret med tolags termorude, mens yderdøren i gangen har tolags energirude.</td>
<td valign="top"><strong>Yderdør med uisoleret fyldning og 1 rude - 2 lags termorude</strong><br>1.65 m² · U=2.8 · mod sydvest<br><em>stueetage / Bryggers / Væg 3</em><br><br><strong>Yderdør med uisoleret fyldning og 1 rude - 2 lags termorude</strong><br>1.62 m² · U=2.8 · mod nordvest<br><em>stueetage / Entre / Væg 1</em><br><br><strong>Yderdør med uisoleret fyldning og 1 rude - 2 lags termorude</strong><br>3.49 m² · U=2.8 · mod sydøst<br><em>stueetage / Dagligstue 2 / Væg 2</em><br><br><strong>Yderdør med 1 rude - 2 lags energirude med varm kant</strong><br>2.77 m² · U=1.3 · mod sydvest<br><em>stueetage / Gang / Væg 1</em><br><br><strong>Yderdør med uisoleret fyldning og 1 rude - 2 lags termorude</strong><br>1.71 m² · U=2.8 · mod nordøst<br><em>stueetage / Gang 3 / Væg 3</em><br><br><strong>Yderdør med uisoleret fyldning og 1 rude - 2 lags termorude</strong><br>2.12 m² · U=2.8 · mod sydvest<br><em>stueetage / Gang 3 / Væg 4</em></td>
</tr></tbody>
</table>

</details>

---

## Lunden_3_8464_Galten (JSON enriched)

- Input XML: `Lunden_3_8464_Galten.xml`
- Final XML: `Lunden_3_8464_Galten final.xml`

### Combined view (all 9 entries across 2 classifications) · ⚠️ Partial overlap

<table>
<thead><tr><th style="width:30%">PDFReportData (all consultant text)</th><th style="width:30%">Generated (all classifications joined)</th><th style="width:40%">Individual Entries (all)</th></tr></thead>
<tbody><tr>
<td valign="top">[1-3-1-0]<br>Vinduer i ejendommen er alle med tolags energiruder med kolde kante.<br><br>[1-3-3-0]<br>Entredør uden glas vurderes isoleret med ca. 15 mm isolering, mens terrasse skydedør i stue i tilbygningen er med trelags energiruder med varme kante.</td>
<td valign="top">Vinduerne er monteret med tolags energirude.<br><br>Skydedørspartiet er monteret med trelags energirude, mens yderdøren i entreen er uden glas og isoleret.</td>
<td valign="top"><strong style="color:#888">— Standard windows (Vinduer) (7) —</strong><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant</strong><br>1.69 m² · U=1.5 · mod nord<br><em>stueetage / Bryggers / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant</strong><br>1.67 m² · U=1.5 · mod vest<br><em>stueetage / Køkken / Væg 3</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant</strong><br>3.25 m² · U=1.5 · mod syd<br><em>stueetage / Stue / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant</strong><br>6.62 m² · U=1.5 · mod syd<br><em>stueetage / Stue / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant</strong><br>1.69 m² · U=1.5 · mod syd<br><em>stueetage / Soveværelse / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant</strong><br>1.71 m² · U=1.5 · mod øst<br><em>stueetage / Værelse / Væg 2</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant</strong><br>0.46 m² · U=1.5 · mod nord<br><em>stueetage / Badeværelse / Væg 3</em><br><br><strong style="color:#888">— Doors with glass (Døre/Terrassedøre) (2) —</strong><br><br><strong>Yderdør uden glas - 2000-2009 - isoleret med 15 mm iht. HB2023</strong><br>2.2 m² · U=1.4 · mod nord<br><em>stueetage / Entre / Væg 3</em><br><br><strong>Skydedørsparti - 1 fast og 1 gående - 3 lags energirude - energiklasse B</strong><br>5.96 m² · U=1.15 · mod vest<br><em>stueetage / Stue / Væg 3</em></td>
</tr></tbody>
</table>

<details><summary>Per-classification breakdown</summary>

#### 1-3-1-0 — Standard windows (Vinduer) (7 entries) · ✅ Equivalent

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">Vinduer i ejendommen er alle med tolags energiruder med kolde kante.</td>
<td valign="top">Vinduerne er monteret med tolags energirude.</td>
<td valign="top"><strong>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant</strong><br>1.69 m² · U=1.5 · mod nord<br><em>stueetage / Bryggers / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant</strong><br>1.67 m² · U=1.5 · mod vest<br><em>stueetage / Køkken / Væg 3</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant</strong><br>3.25 m² · U=1.5 · mod syd<br><em>stueetage / Stue / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant</strong><br>6.62 m² · U=1.5 · mod syd<br><em>stueetage / Stue / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant</strong><br>1.69 m² · U=1.5 · mod syd<br><em>stueetage / Soveværelse / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant</strong><br>1.71 m² · U=1.5 · mod øst<br><em>stueetage / Værelse / Væg 2</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant</strong><br>0.46 m² · U=1.5 · mod nord<br><em>stueetage / Badeværelse / Væg 3</em></td>
</tr></tbody>
</table>

#### 1-3-3-0 — Doors with glass (Døre/Terrassedøre) (2 entries) · ⚠️ Partial overlap

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">Entredør uden glas vurderes isoleret med ca. 15 mm isolering, mens terrasse skydedør i stue i tilbygningen er med trelags energiruder med varme kante.</td>
<td valign="top">Skydedørspartiet er monteret med trelags energirude, mens yderdøren i entreen er uden glas og isoleret.</td>
<td valign="top"><strong>Yderdør uden glas - 2000-2009 - isoleret med 15 mm iht. HB2023</strong><br>2.2 m² · U=1.4 · mod nord<br><em>stueetage / Entre / Væg 3</em><br><br><strong>Skydedørsparti - 1 fast og 1 gående - 3 lags energirude - energiklasse B</strong><br>5.96 m² · U=1.15 · mod vest<br><em>stueetage / Stue / Væg 3</em></td>
</tr></tbody>
</table>

</details>

---

## Lungstedløkken_15_5250_Odense_SV (JSON enriched)

- Input XML: `Lungstedløkken_15_5250_Odense_SV.xml`
- Final XML: `Lungstedløkken_15_5250_Odense_SV final.xml`

### Combined view (all 10 entries across 3 classifications) · ⚠️ Partial overlap

<table>
<thead><tr><th style="width:30%">PDFReportData (all consultant text)</th><th style="width:30%">Generated (all classifications joined)</th><th style="width:40%">Individual Entries (all)</th></tr></thead>
<tbody><tr>
<td valign="top">[1-3-1-0]<br>Vinduerne i bygningen er fortrinsvis med 2 og 3 lags energiruder. Undtaget er vinduespartier ved tagterrasse i overetagen.<br><br>[1-3-2-0]<br>Ovenlysvinduer er monteret med tolags termoruder.<br><br>[1-3-3-0]<br>Terrassedør i stueetage er monteret med tolags energiruder.<br><br>Hoveddør er monteret med tolags energiruder.<br><br>Terrassedør i overetagen er monteret med tolags termoruder.</td>
<td valign="top">Vinduerne er hovedsageligt monteret med tolags energirude. Vinduet i værelset på 1. sal mod nordvest er monteret med tolags termorude, mens vinduerne i værelset på 1. sal mod sydøst har trelags energirude.<br><br>Ovenlysvinduerne er monteret med tolags termorude.<br><br>Terrassedøren i dagligstuen og yderdøren i entreen er monteret med tolags energirude, mens terrassedøren på 1. sal har tolags termorude.</td>
<td valign="top"><strong style="color:#888">— Standard windows (Vinduer) (5) —</strong><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>1.35 m² · U=1.42 · mod nord<br><em>stueetage / Køkken / Væg 2</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>1.79 m² · U=1.42 · mod sydøst<br><em>stueetage / værelse / Væg 2</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>1.48 m² · U=1.42 · mod nordøst<br><em>stueetage / Bryggers / Væg 6</em><br><br><strong>Enkeltfagsvindue i fast ramme - 2 lags termorude kold kant</strong><br>5.75 m² · U=2.8 · mod nordvest<br><em>1. sal / værelse / Væg 4</em><br><br><strong>Flerfagsvindue med gående rammer - 3 lags energirude - energiklasse B</strong><br>0.91 m² · U=1.2 · mod sydøst<br><em>1. sal / værelse / Væg 2</em><br><br><strong style="color:#888">— Skylights (Ovenlysvinduer) (2) —</strong><br><br><strong>Ovenlysvindue - 2 lags termorude kold kant</strong><br>0.67 m² · U=2.8 · mod sydvest<br><em>1. sal / værelse / Ceiling 1</em><br><br><strong>Ovenlysvindue - 2 lags termorude kold kant</strong><br>0.67 m² · U=2.8 · mod nordøst<br><em>1. sal / værelse / Ceiling 2</em><br><br><strong style="color:#888">— Doors with glass (Døre/Terrassedøre) (3) —</strong><br><br><strong>Terrassedør med sideparti - 2 lags energirude med kold kant</strong><br>9.64 m² · U=1.42 · mod sydvest<br><em>stueetage / Dagligstue / Væg 1</em><br><br><strong>Yderdør med sideparti - 2 lags energirude med kold kant</strong><br>3.99 m² · U=1.42 · mod nordøst<br><em>stueetage / Entre / Væg 1</em><br><br><strong>Terrassedør med sideparti - 2 lags termorude</strong><br>5.28 m² · U=2.7 · mod nordøst<br><em>1. sal / værelse / Væg 5</em></td>
</tr></tbody>
</table>

<details><summary>Per-classification breakdown</summary>

#### 1-3-1-0 — Standard windows (Vinduer) (5 entries) · ⚠️ Partial overlap

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">Vinduerne i bygningen er fortrinsvis med 2 og 3 lags energiruder. Undtaget er vinduespartier ved tagterrasse i overetagen.</td>
<td valign="top">Vinduerne er hovedsageligt monteret med tolags energirude. Vinduet i værelset på 1. sal mod nordvest er monteret med tolags termorude, mens vinduerne i værelset på 1. sal mod sydøst har trelags energirude.</td>
<td valign="top"><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>1.35 m² · U=1.42 · mod nord<br><em>stueetage / Køkken / Væg 2</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>1.79 m² · U=1.42 · mod sydøst<br><em>stueetage / værelse / Væg 2</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>1.48 m² · U=1.42 · mod nordøst<br><em>stueetage / Bryggers / Væg 6</em><br><br><strong>Enkeltfagsvindue i fast ramme - 2 lags termorude kold kant</strong><br>5.75 m² · U=2.8 · mod nordvest<br><em>1. sal / værelse / Væg 4</em><br><br><strong>Flerfagsvindue med gående rammer - 3 lags energirude - energiklasse B</strong><br>0.91 m² · U=1.2 · mod sydøst<br><em>1. sal / værelse / Væg 2</em></td>
</tr></tbody>
</table>

#### 1-3-2-0 — Skylights (Ovenlysvinduer) (2 entries) · ✅ Equivalent

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">Ovenlysvinduer er monteret med tolags termoruder.</td>
<td valign="top">Ovenlysvinduerne er monteret med tolags termorude.</td>
<td valign="top"><strong>Ovenlysvindue - 2 lags termorude kold kant</strong><br>0.67 m² · U=2.8 · mod sydvest<br><em>1. sal / værelse / Ceiling 1</em><br><br><strong>Ovenlysvindue - 2 lags termorude kold kant</strong><br>0.67 m² · U=2.8 · mod nordøst<br><em>1. sal / værelse / Ceiling 2</em></td>
</tr></tbody>
</table>

#### 1-3-3-0 — Doors with glass (Døre/Terrassedøre) (3 entries) · ⚠️ Partial overlap

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">Terrassedør i stueetage er monteret med tolags energiruder.<br><br>Hoveddør er monteret med tolags energiruder.<br><br>Terrassedør i overetagen er monteret med tolags termoruder.</td>
<td valign="top">Terrassedøren i dagligstuen og yderdøren i entreen er monteret med tolags energirude, mens terrassedøren på 1. sal har tolags termorude.</td>
<td valign="top"><strong>Terrassedør med sideparti - 2 lags energirude med kold kant</strong><br>9.64 m² · U=1.42 · mod sydvest<br><em>stueetage / Dagligstue / Væg 1</em><br><br><strong>Yderdør med sideparti - 2 lags energirude med kold kant</strong><br>3.99 m² · U=1.42 · mod nordøst<br><em>stueetage / Entre / Væg 1</em><br><br><strong>Terrassedør med sideparti - 2 lags termorude</strong><br>5.28 m² · U=2.7 · mod nordøst<br><em>1. sal / værelse / Væg 5</em></td>
</tr></tbody>
</table>

</details>

---

## Møllehøj_15_6400_Sønderborg (JSON enriched)

- Input XML: `Møllehøj_15_6400_Sønderborg plans.xml`
- Final XML: `Møllehøj_15_6400_Sønderborg final.xml`

### Combined view (all 9 entries across 3 classifications) · ❌ Differs

<table>
<thead><tr><th style="width:30%">PDFReportData (all consultant text)</th><th style="width:30%">Generated (all classifications joined)</th><th style="width:40%">Individual Entries (all)</th></tr></thead>
<tbody><tr>
<td valign="top">[1-3-1-0]<br>Beskrivelse og glasforhold vedrørende vinduer, ovenlys/tagvinduer og døre er baseret på visuel kontrol ved konsulent.<br>Vinduer, ovenlys/tagvinduer og døre er med to-lags energiruder med kold kant.<br>Den massive yderdør er isoleret.<br><br>Der er ikke givet forslag til udskiftning af vinduer, ovenlys/tagvinduer og døre, da den årlige besparelse vil være minimal i forhold til investeringen.</td>
<td valign="top">Vinduerne er monteret med tolags energirude.<br><br>Ovenlysvinduerne er monteret med tolags energirude.<br><br>Terrassedørene er monteret med tolags energirude, mens yderdøren i bryggerset er uden glas og isoleret.</td>
<td valign="top"><strong style="color:#888">— Standard windows (Vinduer) (5) —</strong><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant</strong><br>0.66 m² · U=1.5 · mod øst<br><em>stueetage / Badeværelse / Væg 6</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant</strong><br>1.42 m² · U=1.5 · mod øst<br><em>stueetage / Soveværelse / Væg 3</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant</strong><br>1.46 m² · U=1.5 · mod vest<br><em>stueetage / Værelse syd / Væg 2</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant</strong><br>1.6 m² · U=1.5 · mod øst<br><em>stueetage / Køkken / Væg 2</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant</strong><br>0.7 m² · U=1.5 · mod nord<br><em>stueetage / Badeværelse nord / Væg 3</em><br><br><strong style="color:#888">— Skylights (Ovenlysvinduer) (1) —</strong><br><br><strong>Ovenlysvindue - 2 lags energirude med kold kant</strong><br>1.05 m² · U=1.8 · mod vest<br><em>stueetage / Køkken / Loft 2</em><br><br><strong style="color:#888">— Doors with glass (Døre/Terrassedøre) (3) —</strong><br><br><strong>Terrassedør med flere ruder - 2 lags energirude med kold kant</strong><br>4.17 m² · U=1.42 · mod vest<br><em>stueetage / Dagligstue / Væg 1</em><br><br><strong>Terrassedør med flere ruder - 2 lags energirude med kold kant</strong><br>4.09 m² · U=1.42 · mod vest<br><em>stueetage / Køkken / Væg 1</em><br><br><strong>Yderdør uden glas - 2000-2009 - isoleret med 15 mm iht. HB2023</strong><br>2.7 m² · U=1.4 · mod øst<br><em>stueetage / Bryggers / Væg 8</em></td>
</tr></tbody>
</table>

<details><summary>Per-classification breakdown</summary>

#### 1-3-1-0 — Standard windows (Vinduer) (5 entries) · ❌ Differs

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">Beskrivelse og glasforhold vedrørende vinduer, ovenlys/tagvinduer og døre er baseret på visuel kontrol ved konsulent.<br>Vinduer, ovenlys/tagvinduer og døre er med to-lags energiruder med kold kant.<br>Den massive yderdør er isoleret.<br><br>Der er ikke givet forslag til udskiftning af vinduer, ovenlys/tagvinduer og døre, da den årlige besparelse vil være minimal i forhold til investeringen.</td>
<td valign="top">Vinduerne er monteret med tolags energirude.</td>
<td valign="top"><strong>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant</strong><br>0.66 m² · U=1.5 · mod øst<br><em>stueetage / Badeværelse / Væg 6</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant</strong><br>1.42 m² · U=1.5 · mod øst<br><em>stueetage / Soveværelse / Væg 3</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant</strong><br>1.46 m² · U=1.5 · mod vest<br><em>stueetage / Værelse syd / Væg 2</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant</strong><br>1.6 m² · U=1.5 · mod øst<br><em>stueetage / Køkken / Væg 2</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med kold kant</strong><br>0.7 m² · U=1.5 · mod nord<br><em>stueetage / Badeværelse nord / Væg 3</em></td>
</tr></tbody>
</table>

#### 1-3-2-0 — Skylights (Ovenlysvinduer) (1 entries) · — No PDF text

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">_(no PDFReportData entry)_</td>
<td valign="top">Ovenlysvinduerne er monteret med tolags energirude.</td>
<td valign="top"><strong>Ovenlysvindue - 2 lags energirude med kold kant</strong><br>1.05 m² · U=1.8 · mod vest<br><em>stueetage / Køkken / Loft 2</em></td>
</tr></tbody>
</table>

#### 1-3-3-0 — Doors with glass (Døre/Terrassedøre) (3 entries) · — No PDF text

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">_(no PDFReportData entry)_</td>
<td valign="top">Terrassedørene er monteret med tolags energirude, mens yderdøren i bryggerset er uden glas og isoleret.</td>
<td valign="top"><strong>Terrassedør med flere ruder - 2 lags energirude med kold kant</strong><br>4.17 m² · U=1.42 · mod vest<br><em>stueetage / Dagligstue / Væg 1</em><br><br><strong>Terrassedør med flere ruder - 2 lags energirude med kold kant</strong><br>4.09 m² · U=1.42 · mod vest<br><em>stueetage / Køkken / Væg 1</em><br><br><strong>Yderdør uden glas - 2000-2009 - isoleret med 15 mm iht. HB2023</strong><br>2.7 m² · U=1.4 · mod øst<br><em>stueetage / Bryggers / Væg 8</em></td>
</tr></tbody>
</table>

</details>

---

## Nypølsgade_14_6470_Sydals (JSON enriched)

- Input XML: `Nypølsgade_14_6470_Sydals.xml`
- Final XML: `Nypølsgade_14_6470_Sydals final.xml`

### Combined view (all 21 entries across 2 classifications) · ❌ Differs

<table>
<thead><tr><th style="width:30%">PDFReportData (all consultant text)</th><th style="width:30%">Generated (all classifications joined)</th><th style="width:40%">Individual Entries (all)</th></tr></thead>
<tbody><tr>
<td valign="top">[1-3-1-0]<br>Beskrivelse og glasforhold vedrørende vinduer og døre er baseret på visuel kontrol ved konsulent.<br>Vinduer mod nord og vest i værksted er med 1 lag glas. Øvrige vinduer i boligen, samt yderdøre er med to-lags energiruder med varm kant. Den massive yderdør ved værksted er uden isolering.<br><br>Der er ikke givet forslag til udskiftning af vinduer og døre med energiruder, da den årlige besparelse vil være minimal i forhold til investeringen.</td>
<td valign="top">Vinduerne er hovedsageligt monteret med tolags energirude. Vinduer i værkstedet er dog monteret med etlags glas.<br><br>Terrassedørene er monteret med tolags energirude, mens yderdøren i værkstedet er uden glas og isoleret.</td>
<td valign="top"><strong style="color:#888">— Standard windows (Vinduer) (16) —</strong><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>0.88 m² · U=1.4 · mod øst<br><em>stueetage / Bryggers / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>0.95 m² · U=1.4 · mod vest<br><em>stueetage / Stue/køkken / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>0.78 m² · U=1.4 · mod øst<br><em>stueetage / Stue/køkken / Væg 2</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>0.88 m² · U=1.4 · mod syd<br><em>stueetage / Stue/køkken / Væg 5</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>1.08 m² · U=1.4 · mod vest<br><em>stueetage / Soveværelse / Væg 3</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>1.24 m² · U=1.4 · mod vest<br><em>stueetage / Soveværelse 2 / Væg 3</em><br><br><strong>Flerfagsvindue med gående rammer - 1 lag glas</strong><br>0.19 m² · U=4.1 · mod nord<br><em>stueetage / Værksted / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>0.25 m² · U=1.4 · mod øst<br><em>stueetage / Værksted / Væg 2</em><br><br><strong>Flerfagsvindue med gående rammer - 1 lag glas</strong><br>0.21 m² · U=4.1 · mod vest<br><em>stueetage / Værksted / Væg 3</em><br><br><strong>Flerfagsvindue med gående rammer - 1 lag glas</strong><br>0.21 m² · U=4.1 · mod nord<br><em>stueetage / Værksted / Væg 4</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>1.19 m² · U=1.4 · mod syd<br><em>1. sal / Stue/værelse / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>0.87 m² · U=1.4 · mod vest<br><em>1. sal / Stue/værelse / Væg 3</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>0.74 m² · U=1.4 · mod vest<br><em>1. sal / Stue/værelse / Væg 8</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>0.89 m² · U=1.4 · mod øst<br><em>1. sal / Stue/værelse / Væg 17</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>0.89 m² · U=1.4 · mod øst<br><em>1. sal / Stue/værelse / Væg 18</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>0.25 m² · U=1.4 · mod øst<br><em>1. sal / Badeværelse / Væg 10</em><br><br><strong style="color:#888">— Doors with glass (Døre/Terrassedøre) (5) —</strong><br><br><strong>Terrassedør med flere ruder - 2 lags energirude med varm kant</strong><br>1.51 m² · U=1.3 · mod øst<br><em>stueetage / Bryggers / Væg 1</em><br><br><strong>Terrassedør med flere ruder - 2 lags energirude med varm kant</strong><br>1.65 m² · U=1.3 · mod syd<br><em>stueetage / Stue/køkken / Væg 4</em><br><br><strong>Terrassedør med flere ruder - 2 lags energirude med varm kant</strong><br>1.64 m² · U=1.3 · mod vest<br><em>stueetage / værelse / Væg 3</em><br><br><strong>Yderdør uden glas - Før 1990 - uisoleret iht. HB2023</strong><br>1.6 m² · U=2 · mod vest<br><em>stueetage / Værksted / Væg 3</em><br><br><strong>Terrassedør med flere ruder - 2 lags energirude med varm kant</strong><br>1.6 m² · U=1.3 · mod øst<br><em>stueetage / Viktualierum / Væg 3</em></td>
</tr></tbody>
</table>

<details><summary>Per-classification breakdown</summary>

#### 1-3-1-0 — Standard windows (Vinduer) (16 entries) · ❌ Differs

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">Beskrivelse og glasforhold vedrørende vinduer og døre er baseret på visuel kontrol ved konsulent.<br>Vinduer mod nord og vest i værksted er med 1 lag glas. Øvrige vinduer i boligen, samt yderdøre er med to-lags energiruder med varm kant. Den massive yderdør ved værksted er uden isolering.<br><br>Der er ikke givet forslag til udskiftning af vinduer og døre med energiruder, da den årlige besparelse vil være minimal i forhold til investeringen.</td>
<td valign="top">Vinduerne er hovedsageligt monteret med tolags energirude. Vinduer i værkstedet er dog monteret med etlags glas.</td>
<td valign="top"><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>0.88 m² · U=1.4 · mod øst<br><em>stueetage / Bryggers / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>0.95 m² · U=1.4 · mod vest<br><em>stueetage / Stue/køkken / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>0.78 m² · U=1.4 · mod øst<br><em>stueetage / Stue/køkken / Væg 2</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>0.88 m² · U=1.4 · mod syd<br><em>stueetage / Stue/køkken / Væg 5</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>1.08 m² · U=1.4 · mod vest<br><em>stueetage / Soveværelse / Væg 3</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>1.24 m² · U=1.4 · mod vest<br><em>stueetage / Soveværelse 2 / Væg 3</em><br><br><strong>Flerfagsvindue med gående rammer - 1 lag glas</strong><br>0.19 m² · U=4.1 · mod nord<br><em>stueetage / Værksted / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>0.25 m² · U=1.4 · mod øst<br><em>stueetage / Værksted / Væg 2</em><br><br><strong>Flerfagsvindue med gående rammer - 1 lag glas</strong><br>0.21 m² · U=4.1 · mod vest<br><em>stueetage / Værksted / Væg 3</em><br><br><strong>Flerfagsvindue med gående rammer - 1 lag glas</strong><br>0.21 m² · U=4.1 · mod nord<br><em>stueetage / Værksted / Væg 4</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>1.19 m² · U=1.4 · mod syd<br><em>1. sal / Stue/værelse / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>0.87 m² · U=1.4 · mod vest<br><em>1. sal / Stue/værelse / Væg 3</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>0.74 m² · U=1.4 · mod vest<br><em>1. sal / Stue/værelse / Væg 8</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>0.89 m² · U=1.4 · mod øst<br><em>1. sal / Stue/værelse / Væg 17</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>0.89 m² · U=1.4 · mod øst<br><em>1. sal / Stue/værelse / Væg 18</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags energirude med varm kant</strong><br>0.25 m² · U=1.4 · mod øst<br><em>1. sal / Badeværelse / Væg 10</em></td>
</tr></tbody>
</table>

#### 1-3-3-0 — Doors with glass (Døre/Terrassedøre) (5 entries) · — No PDF text

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">_(no PDFReportData entry)_</td>
<td valign="top">Terrassedørene er monteret med tolags energirude, mens yderdøren i værkstedet er uden glas og isoleret.</td>
<td valign="top"><strong>Terrassedør med flere ruder - 2 lags energirude med varm kant</strong><br>1.51 m² · U=1.3 · mod øst<br><em>stueetage / Bryggers / Væg 1</em><br><br><strong>Terrassedør med flere ruder - 2 lags energirude med varm kant</strong><br>1.65 m² · U=1.3 · mod syd<br><em>stueetage / Stue/køkken / Væg 4</em><br><br><strong>Terrassedør med flere ruder - 2 lags energirude med varm kant</strong><br>1.64 m² · U=1.3 · mod vest<br><em>stueetage / værelse / Væg 3</em><br><br><strong>Yderdør uden glas - Før 1990 - uisoleret iht. HB2023</strong><br>1.6 m² · U=2 · mod vest<br><em>stueetage / Værksted / Væg 3</em><br><br><strong>Terrassedør med flere ruder - 2 lags energirude med varm kant</strong><br>1.6 m² · U=1.3 · mod øst<br><em>stueetage / Viktualierum / Væg 3</em></td>
</tr></tbody>
</table>

</details>

---

## Spangsvej_15_5210_Odense_NV (JSON enriched)

- Input XML: `Spangsvej_15_5210_Odense_NV.xml`
- Final XML: `Spangsvej_15_5210_Odense_NV final.xml`

### Combined view (all 12 entries across 2 classifications) · ⚠️ Partial overlap

<table>
<thead><tr><th style="width:30%">PDFReportData (all consultant text)</th><th style="width:30%">Generated (all classifications joined)</th><th style="width:40%">Individual Entries (all)</th></tr></thead>
<tbody><tr>
<td valign="top">[1-3-1-0]<br>Vinduerne er monteret med to- og trelags energiruder.<br><br>[1-3-3-0]<br>Skydedørsparti er monteret med tolags termoruder.<br><br>Hoveddør og bryggersdør er monteret med tolags energiruder.</td>
<td valign="top">Vinduerne er hovedsageligt monteret med tolags energirude. Vinduer i bryggerset, badeværelset og walk in closet er monteret med trelags energirude.<br><br>Skydedørspartierne er monteret med tolags termorude, mens yderdøren med sideparti i entreen har tolags energirude.</td>
<td valign="top"><strong style="color:#888">— Standard windows (Vinduer) (9) —</strong><br><br><strong>Enkeltfagsvindue i fast ramme - 2 lags energirude med varm kant</strong><br>0.67 m² · U=1.3 · mod syd<br><em>kælder / værelse / Væg 4</em><br><br><strong>Enkeltfagsvindue i fast ramme - 3 lags energirude - energiklasse B</strong><br>1.11 m² · U=1.15 · mod øst<br><em>stueetage / Bryggers / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>1.47 m² · U=1.42 · mod syd<br><em>stueetage / Entre / Væg 5</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>1.26 m² · U=1.42 · mod syd<br><em>stueetage / Dagligstue 2 / Væg 4</em><br><br><strong>Enkeltfagsvindue i fast ramme - 2 lags energirude med varm kant</strong><br>1.03 m² · U=1.3 · mod vest<br><em>stueetage / Dagligstue / Væg 3</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>1.85 m² · U=1.42 · mod nord<br><em>stueetage / Dagligstue 2 / Væg 3</em><br><br><strong>Enkeltfagsvindue i fast ramme - 3 lags energirude - energiklasse B</strong><br>1.28 m² · U=1.15 · mod syd<br><em>stueetage / Badeværelse / Væg 1</em><br><br><strong>Enkeltfagsvindue i fast ramme - 2 lags energirude med varm kant</strong><br>3.49 m² · U=1.3 · mod vest<br><em>stueetage / Soveværelse / Væg 2</em><br><br><strong>Enkeltfagsvindue i fast ramme - 3 lags energirude - energiklasse B</strong><br>1.39 m² · U=1.15 · mod nord<br><em>stueetage / Walk in / Væg 1</em><br><br><strong style="color:#888">— Doors with glass (Døre/Terrassedøre) (3) —</strong><br><br><strong>Skydedørsparti - 1 fast og 1 gående - 2 lags termorude</strong><br>1.94 m² · U=2.7 · mod nord<br><em>stueetage / Bryggers / Væg 7</em><br><br><strong>Yderdør med sideparti - 2 lags energirude med kold kant</strong><br>1.8 m² · U=1.42 · mod øst<br><em>stueetage / Entre / Væg 2</em><br><br><strong>Skydedørsparti - 1 fast og 1 gående - 2 lags termorude</strong><br>2.76 m² · U=2.7 · mod nord<br><em>stueetage / Dagligstue 2 / Væg 3</em></td>
</tr></tbody>
</table>

<details><summary>Per-classification breakdown</summary>

#### 1-3-1-0 — Standard windows (Vinduer) (9 entries) · ✅ Equivalent

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">Vinduerne er monteret med to- og trelags energiruder.</td>
<td valign="top">Vinduerne er hovedsageligt monteret med tolags energirude. Vinduer i bryggerset, badeværelset og walk in closet er monteret med trelags energirude.</td>
<td valign="top"><strong>Enkeltfagsvindue i fast ramme - 2 lags energirude med varm kant</strong><br>0.67 m² · U=1.3 · mod syd<br><em>kælder / værelse / Væg 4</em><br><br><strong>Enkeltfagsvindue i fast ramme - 3 lags energirude - energiklasse B</strong><br>1.11 m² · U=1.15 · mod øst<br><em>stueetage / Bryggers / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>1.47 m² · U=1.42 · mod syd<br><em>stueetage / Entre / Væg 5</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>1.26 m² · U=1.42 · mod syd<br><em>stueetage / Dagligstue 2 / Væg 4</em><br><br><strong>Enkeltfagsvindue i fast ramme - 2 lags energirude med varm kant</strong><br>1.03 m² · U=1.3 · mod vest<br><em>stueetage / Dagligstue / Væg 3</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>1.85 m² · U=1.42 · mod nord<br><em>stueetage / Dagligstue 2 / Væg 3</em><br><br><strong>Enkeltfagsvindue i fast ramme - 3 lags energirude - energiklasse B</strong><br>1.28 m² · U=1.15 · mod syd<br><em>stueetage / Badeværelse / Væg 1</em><br><br><strong>Enkeltfagsvindue i fast ramme - 2 lags energirude med varm kant</strong><br>3.49 m² · U=1.3 · mod vest<br><em>stueetage / Soveværelse / Væg 2</em><br><br><strong>Enkeltfagsvindue i fast ramme - 3 lags energirude - energiklasse B</strong><br>1.39 m² · U=1.15 · mod nord<br><em>stueetage / Walk in / Væg 1</em></td>
</tr></tbody>
</table>

#### 1-3-3-0 — Doors with glass (Døre/Terrassedøre) (3 entries) · ⚠️ Partial overlap

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">Skydedørsparti er monteret med tolags termoruder.<br><br>Hoveddør og bryggersdør er monteret med tolags energiruder.</td>
<td valign="top">Skydedørspartierne er monteret med tolags termorude, mens yderdøren med sideparti i entreen har tolags energirude.</td>
<td valign="top"><strong>Skydedørsparti - 1 fast og 1 gående - 2 lags termorude</strong><br>1.94 m² · U=2.7 · mod nord<br><em>stueetage / Bryggers / Væg 7</em><br><br><strong>Yderdør med sideparti - 2 lags energirude med kold kant</strong><br>1.8 m² · U=1.42 · mod øst<br><em>stueetage / Entre / Væg 2</em><br><br><strong>Skydedørsparti - 1 fast og 1 gående - 2 lags termorude</strong><br>2.76 m² · U=2.7 · mod nord<br><em>stueetage / Dagligstue 2 / Væg 3</em></td>
</tr></tbody>
</table>

</details>

---

## Spurvevej_13_7100_Vejle (JSON enriched)

- Input XML: `Spurvevej_13_7100_Vejle.xml`
- Final XML: `Spurvevej_13_7100_Vejle final.xml`

### Combined view (all 17 entries across 3 classifications) · ❌ Differs

<table>
<thead><tr><th style="width:30%">PDFReportData (all consultant text)</th><th style="width:30%">Generated (all classifications joined)</th><th style="width:40%">Individual Entries (all)</th></tr></thead>
<tbody><tr>
<td valign="top">[1-3-1-0]<br>Alle vinduer er monteret med tolags termoruder.<br><br>Vindue ved trappe er med glasbyggesten.<br><br>[1-3-2-0]<br>Ovenlysvindue er monteret med trelags energirude.<br><br>[1-3-3-0]<br>Yderdør i kælder er monteret med tolags termoruder.<br><br>Terrassedør i stue er monteret med tolags termorude.<br><br>Yderdør med sideparti i entre er monteret med tolags termoruder.<br><br>Terrassedør på første sal er monteret med tolags energirude.<br><br>Portpanelet i garage er udført som et sandwichmodul som dobbelt lag stål og med isolering imellem.<br><br>Dør til uopvarmet kælderrum er uisoleret</td>
<td valign="top">Vinduerne er hovedsageligt monteret med tolags termorude. Dog er der et vindue i gangen på stueetagen udført som glasbyggesten.<br><br>Ovenlysvinduerne er monteret med trelags energirude.<br><br>Terrassedørene og yderdørene er primært monteret med tolags termorude. Terrassedøren i gangen i kælderen og terrassedøren i dagligstuen på 1. sal har tolags energirude. Garagen har en isoleret stålport uden vinduer.</td>
<td valign="top"><strong style="color:#888">— Standard windows (Vinduer) (9) —</strong><br><br><strong>Flerfagsvindue med gående rammer - 2 lags termorude kold kant</strong><br>1.48 m² · U=2.7 · mod øst<br><em>stueetage / Køkken / Væg 4</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>1.56 m² · U=2.8 · mod vest<br><em>kælder / Bryggers / Væg 3</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>1.5 m² · U=2.8 · mod syd<br><em>stueetage / Værelse mod syd / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>1.8 m² · U=2.8 · mod øst<br><em>stueetage / Værelse / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>2 m² · U=2.8 · mod syd<br><em>1. sal / Gang / Væg 4</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>0.53 m² · U=2.8 · mod nord<br><em>stueetage / Badeværelse / Væg 2</em><br><br><strong>Glasbyggesten</strong><br>0.55 m² · U=3 · mod nord<br><em>stueetage / Gang / Væg 2</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>1.64 m² · U=2.8 · mod nord<br><em>stueetage / Køkken / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags termorude kold kant</strong><br>3.87 m² · U=2.7 · mod vest<br><em>1. sal / Dagligstue / Væg 2</em><br><br><strong style="color:#888">— Skylights (Ovenlysvinduer) (2) —</strong><br><br><strong>Ovenlysvindue - 3 lags energirude - efter BR15</strong><br>0.99 m² · U=1.6 · mod syd<br><em>1. sal / Dagligstue / Loft 6</em><br><br><strong>Ovenlysvindue - 3 lags energirude - efter BR15</strong><br>0.99 m² · U=1.6 · mod nord<br><em>1. sal / Badeværelse / Loft 2</em><br><br><strong style="color:#888">— Doors with glass (Døre/Terrassedøre) (6) —</strong><br><br><strong>Terrassedør med 1 rude - 2 lags energirude med varm kant</strong><br>1.7 m² · U=1.3 · mod nord<br><em>kælder / Gang / Væg 3</em><br><br><strong>Yderdør med flere ruder - 2 lags termorude</strong><br>1.89 m² · U=2.7 · mod vest<br><em>kælder / Bryggers / Væg 3</em><br><br><strong>Hörmann indbygget stålport - isoleret 42 mm - uden vinduer</strong><br>5.56 m² · U=1.3 · mod vest<br><em>kælder / Garage / Væg 4</em><br><br><strong>Terrassedør med 1 rude - 2 lags termorude</strong><br>1.86 m² · U=2.7 · mod syd<br><em>stueetage / Dagligstue / Væg 1</em><br><br><strong>Yderdør med sideparti - 2 lags termorude</strong><br>1.97 m² · U=2.7 · mod nord<br><em>stueetage / Entre / Væg 3</em><br><br><strong>Terrassedør med 1 rude - 2 lags energirude med varm kant</strong><br>1.69 m² · U=1.3 · mod vest<br><em>1. sal / Dagligstue / Væg 2</em></td>
</tr></tbody>
</table>

<details><summary>Per-classification breakdown</summary>

#### 1-3-1-0 — Standard windows (Vinduer) (9 entries) · ⚠️ Partial overlap

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">Alle vinduer er monteret med tolags termoruder.<br><br>Vindue ved trappe er med glasbyggesten.</td>
<td valign="top">Vinduerne er hovedsageligt monteret med tolags termorude. Dog er der et vindue i gangen på stueetagen udført som glasbyggesten.</td>
<td valign="top"><strong>Flerfagsvindue med gående rammer - 2 lags termorude kold kant</strong><br>1.48 m² · U=2.7 · mod øst<br><em>stueetage / Køkken / Væg 4</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>1.56 m² · U=2.8 · mod vest<br><em>kælder / Bryggers / Væg 3</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>1.5 m² · U=2.8 · mod syd<br><em>stueetage / Værelse mod syd / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>1.8 m² · U=2.8 · mod øst<br><em>stueetage / Værelse / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>2 m² · U=2.8 · mod syd<br><em>1. sal / Gang / Væg 4</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>0.53 m² · U=2.8 · mod nord<br><em>stueetage / Badeværelse / Væg 2</em><br><br><strong>Glasbyggesten</strong><br>0.55 m² · U=3 · mod nord<br><em>stueetage / Gang / Væg 2</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>1.64 m² · U=2.8 · mod nord<br><em>stueetage / Køkken / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags termorude kold kant</strong><br>3.87 m² · U=2.7 · mod vest<br><em>1. sal / Dagligstue / Væg 2</em></td>
</tr></tbody>
</table>

#### 1-3-2-0 — Skylights (Ovenlysvinduer) (2 entries) · ✅ Equivalent

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">Ovenlysvindue er monteret med trelags energirude.</td>
<td valign="top">Ovenlysvinduerne er monteret med trelags energirude.</td>
<td valign="top"><strong>Ovenlysvindue - 3 lags energirude - efter BR15</strong><br>0.99 m² · U=1.6 · mod syd<br><em>1. sal / Dagligstue / Loft 6</em><br><br><strong>Ovenlysvindue - 3 lags energirude - efter BR15</strong><br>0.99 m² · U=1.6 · mod nord<br><em>1. sal / Badeværelse / Loft 2</em></td>
</tr></tbody>
</table>

#### 1-3-3-0 — Doors with glass (Døre/Terrassedøre) (6 entries) · ❌ Differs

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">Yderdør i kælder er monteret med tolags termoruder.<br><br>Terrassedør i stue er monteret med tolags termorude.<br><br>Yderdør med sideparti i entre er monteret med tolags termoruder.<br><br>Terrassedør på første sal er monteret med tolags energirude.<br><br>Portpanelet i garage er udført som et sandwichmodul som dobbelt lag stål og med isolering imellem.<br><br>Dør til uopvarmet kælderrum er uisoleret</td>
<td valign="top">Terrassedørene og yderdørene er primært monteret med tolags termorude. Terrassedøren i gangen i kælderen og terrassedøren i dagligstuen på 1. sal har tolags energirude. Garagen har en isoleret stålport uden vinduer.</td>
<td valign="top"><strong>Terrassedør med 1 rude - 2 lags energirude med varm kant</strong><br>1.7 m² · U=1.3 · mod nord<br><em>kælder / Gang / Væg 3</em><br><br><strong>Yderdør med flere ruder - 2 lags termorude</strong><br>1.89 m² · U=2.7 · mod vest<br><em>kælder / Bryggers / Væg 3</em><br><br><strong>Hörmann indbygget stålport - isoleret 42 mm - uden vinduer</strong><br>5.56 m² · U=1.3 · mod vest<br><em>kælder / Garage / Væg 4</em><br><br><strong>Terrassedør med 1 rude - 2 lags termorude</strong><br>1.86 m² · U=2.7 · mod syd<br><em>stueetage / Dagligstue / Væg 1</em><br><br><strong>Yderdør med sideparti - 2 lags termorude</strong><br>1.97 m² · U=2.7 · mod nord<br><em>stueetage / Entre / Væg 3</em><br><br><strong>Terrassedør med 1 rude - 2 lags energirude med varm kant</strong><br>1.69 m² · U=1.3 · mod vest<br><em>1. sal / Dagligstue / Væg 2</em></td>
</tr></tbody>
</table>

</details>

---

## Strandbakken_5_5900_Rudkøbing (JSON enriched)

- Input XML: `Strandbakken_5_5900_Rudkøbing.xml`
- Final XML: `Strandbakken_5_5900_Rudkøbing final.xml`

### Combined view (all 8 entries across 2 classifications) · ⚠️ Partial overlap

<table>
<thead><tr><th style="width:30%">PDFReportData (all consultant text)</th><th style="width:30%">Generated (all classifications joined)</th><th style="width:40%">Individual Entries (all)</th></tr></thead>
<tbody><tr>
<td valign="top">[1-3-1-0]<br>Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags termorude.<br><br>[1-3-3-0]<br>Yderdør med enkeltfagsvindue, monteret med tolags energiruder.</td>
<td valign="top">Vinduerne er monteret med tolags termorude.<br><br>Yderdørene er monteret med tolags energirude.</td>
<td valign="top"><strong style="color:#888">— Standard windows (Vinduer) (5) —</strong><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>1.7 m² · U=2.8 · mod nordvest<br><em>stueetage / Entre / Væg 2</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>1.63 m² · U=2.8 · mod nordøst<br><em>stueetage / Køkken / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>2.74 m² · U=2.8 · mod sydvest<br><em>stueetage / Dagligstue / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>1.78 m² · U=2.8 · mod nordøst<br><em>1. sal / Værelse mod vejen / Væg 2</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>1.45 m² · U=2.8 · mod sydvest<br><em>1. sal / Soveværelse / Væg 2</em><br><br><strong style="color:#888">— Doors with glass (Døre/Terrassedøre) (3) —</strong><br><br><strong>Yderdør med 1 rude - 2 lags energirude med varm kant</strong><br>2.03 m² · U=1.3 · mod nordøst<br><em>stueetage / Entre / Væg 1</em><br><br><strong>Yderdør med 1 rude - 2 lags energirude med varm kant</strong><br>4.75 m² · U=1.3 · mod sydvest<br><em>stueetage / Dagligstue / Væg 1</em><br><br><strong>Yderdør med 1 rude - 2 lags energirude med varm kant</strong><br>1.91 m² · U=1.3 · mod sydvest<br><em>1. sal / Soveværelse / Væg 2</em></td>
</tr></tbody>
</table>

<details><summary>Per-classification breakdown</summary>

#### 1-3-1-0 — Standard windows (Vinduer) (5 entries) · ✅ Equivalent

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">Oplukkelige vinduer med et fag. Vinduerne er monteret med tolags termorude.</td>
<td valign="top">Vinduerne er monteret med tolags termorude.</td>
<td valign="top"><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>1.7 m² · U=2.8 · mod nordvest<br><em>stueetage / Entre / Væg 2</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>1.63 m² · U=2.8 · mod nordøst<br><em>stueetage / Køkken / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>2.74 m² · U=2.8 · mod sydvest<br><em>stueetage / Dagligstue / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>1.78 m² · U=2.8 · mod nordøst<br><em>1. sal / Værelse mod vejen / Væg 2</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>1.45 m² · U=2.8 · mod sydvest<br><em>1. sal / Soveværelse / Væg 2</em></td>
</tr></tbody>
</table>

#### 1-3-3-0 — Doors with glass (Døre/Terrassedøre) (3 entries) · ⚠️ Partial overlap

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">Yderdør med enkeltfagsvindue, monteret med tolags energiruder.</td>
<td valign="top">Yderdørene er monteret med tolags energirude.</td>
<td valign="top"><strong>Yderdør med 1 rude - 2 lags energirude med varm kant</strong><br>2.03 m² · U=1.3 · mod nordøst<br><em>stueetage / Entre / Væg 1</em><br><br><strong>Yderdør med 1 rude - 2 lags energirude med varm kant</strong><br>4.75 m² · U=1.3 · mod sydvest<br><em>stueetage / Dagligstue / Væg 1</em><br><br><strong>Yderdør med 1 rude - 2 lags energirude med varm kant</strong><br>1.91 m² · U=1.3 · mod sydvest<br><em>1. sal / Soveværelse / Væg 2</em></td>
</tr></tbody>
</table>

</details>

---

## Sønderskovvej_5_5932_Humble (JSON enriched)

- Input XML: `Sønderskovvej_5_5932_Humble.xml`
- Final XML: `Sønderskovvej_5_5932_Humble final.xml`

### Combined view (all 8 entries across 2 classifications) · ⚠️ Partial overlap

<table>
<thead><tr><th style="width:30%">PDFReportData (all consultant text)</th><th style="width:30%">Generated (all classifications joined)</th><th style="width:40%">Individual Entries (all)</th></tr></thead>
<tbody><tr>
<td valign="top">[1-3-1-0]<br>Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags termorude.<br><br>[1-3-3-0]<br>Yderdør med enkeltfagsvindue, monteret med tolags termoruder.<br><br>Yderdør med enkeltfagsvindue, monteret med tolags termoruder.</td>
<td valign="top">Vinduerne er monteret med tolags termorude.<br><br>Yderdørene er monteret med tolags termorude.</td>
<td valign="top"><strong style="color:#888">— Standard windows (Vinduer) (6) —</strong><br><br><strong>Flerfagsvindue med gående rammer - 2 lags termorude kold kant</strong><br>0.95 m² · U=2.7 · mod øst<br><em>stueetage / Køkken / Væg 2</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags termorude kold kant</strong><br>1.27 m² · U=2.7 · mod vest<br><em>stueetage / Dagligstue / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags termorude kold kant</strong><br>1.12 m² · U=2.7 · mod vest<br><em>stueetage / Dagligstue / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags termorude kold kant</strong><br>0.94 m² · U=2.7 · mod øst<br><em>stueetage / Dagligstue / Væg 2</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags termorude kold kant</strong><br>2.17 m² · U=2.7 · mod øst<br><em>stueetage / Soveværelse / Væg 3</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags termorude kold kant</strong><br>0.79 m² · U=2.7 · mod nord<br><em>stueetage / Badeværelse / Væg 2</em><br><br><strong style="color:#888">— Doors with glass (Døre/Terrassedøre) (2) —</strong><br><br><strong>Yderdør med 1 rude - 2 lags termorude</strong><br>1.7 m² · U=2.7 · mod vest<br><em>stueetage / Entre / Væg 1</em><br><br><strong>Yderdør med 1 rude - 2 lags termorude</strong><br>1.52 m² · U=2.7 · mod nord<br><em>stueetage / Bryggers / Væg 2</em></td>
</tr></tbody>
</table>

<details><summary>Per-classification breakdown</summary>

#### 1-3-1-0 — Standard windows (Vinduer) (6 entries) · ✅ Equivalent

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">Oplukkelige vinduer med flere fag. Vinduerne er monteret med tolags termorude.</td>
<td valign="top">Vinduerne er monteret med tolags termorude.</td>
<td valign="top"><strong>Flerfagsvindue med gående rammer - 2 lags termorude kold kant</strong><br>0.95 m² · U=2.7 · mod øst<br><em>stueetage / Køkken / Væg 2</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags termorude kold kant</strong><br>1.27 m² · U=2.7 · mod vest<br><em>stueetage / Dagligstue / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags termorude kold kant</strong><br>1.12 m² · U=2.7 · mod vest<br><em>stueetage / Dagligstue / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags termorude kold kant</strong><br>0.94 m² · U=2.7 · mod øst<br><em>stueetage / Dagligstue / Væg 2</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags termorude kold kant</strong><br>2.17 m² · U=2.7 · mod øst<br><em>stueetage / Soveværelse / Væg 3</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags termorude kold kant</strong><br>0.79 m² · U=2.7 · mod nord<br><em>stueetage / Badeværelse / Væg 2</em></td>
</tr></tbody>
</table>

#### 1-3-3-0 — Doors with glass (Døre/Terrassedøre) (2 entries) · ⚠️ Partial overlap

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">Yderdør med enkeltfagsvindue, monteret med tolags termoruder.<br><br>Yderdør med enkeltfagsvindue, monteret med tolags termoruder.</td>
<td valign="top">Yderdørene er monteret med tolags termorude.</td>
<td valign="top"><strong>Yderdør med 1 rude - 2 lags termorude</strong><br>1.7 m² · U=2.7 · mod vest<br><em>stueetage / Entre / Væg 1</em><br><br><strong>Yderdør med 1 rude - 2 lags termorude</strong><br>1.52 m² · U=2.7 · mod nord<br><em>stueetage / Bryggers / Væg 2</em></td>
</tr></tbody>
</table>

</details>

---
