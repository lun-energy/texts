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

Total comparisons (with consultant text): **7**

| Match level | Count |
|---|---|
| ✅ Identical | 0 |
| ✅ Equivalent | 4 |
| ⚠️ Partial overlap | 2 |
| ❌ Differs | 1 |
| — No PDF text | 4 |

---

# Projects with JSON Enrichment

## Gyvelvænget_10_8543_Hornslet (JSON enriched)

- Input XML: `Gyvelvænget_10_8543_Hornslet.xml`
- Final XML: `Gyvelvænget_10_8543_Hornslet final.xml`

### Combined view (all 9 entries across 2 classifications) · ⚠️ Partial overlap

<table>
<thead><tr><th style="width:30%">PDFReportData (all consultant text)</th><th style="width:30%">Generated (all classifications joined)</th><th style="width:40%">Individual Entries (all)</th></tr></thead>
<tbody><tr>
<td valign="top">[1-3-1-0]<br>Der er generelt ældre vinduer med skiftede ruder, til energiruder med kolde kante. Dog er vindue mod øst i stuen med tolags termoruder.<br><br>[1-3-3-0]<br>Yderdøre i entre og bryggers med sideparti, samt terrassedør i stuen er med tolags termoruder.</td>
<td valign="top">Vinduerne er hovedsageligt monteret med tolags energirude. Et vindue i dagligstuen mod øst er monteret med tolags termorude.<br><br>Yderdørene med sideparti og terrassedøren er alle monteret med tolags termorude.</td>
<td valign="top"><strong style="color:#888">— Standard windows (Vinduer) (6) —</strong><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>2.79 m² · U=1.42 · mod nord<br><em>stueetage / Køkken / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>1.55 m² · U=1.42 · mod nord<br><em>stueetage / Badeværelse / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>1.69 m² · U=1.42 · mod vest<br><em>stueetage / Værelse nordvest / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>3.02 m² · U=1.42 · mod vest<br><em>stueetage / Værelse sydvest / Væg 2</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>1.69 m² · U=1.42 · mod syd<br><em>stueetage / Dagligstue / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags termorude kold kant</strong><br>4.1 m² · U=2.7 · mod øst<br><em>stueetage / Dagligstue / Væg 3</em><br><br><strong style="color:#888">— Doors with glass (Døre/Terrassedøre) (3) —</strong><br><br><strong>Yderdør med sideparti - 2 lags termorude</strong><br>2.66 m² · U=2.7 · mod øst<br><em>stueetage / Bryggers / Væg 1</em><br><br><strong>Yderdør med sideparti - 2 lags termorude</strong><br>2.95 m² · U=2.7 · mod nord<br><em>stueetage / Entre / Væg 1</em><br><br><strong>Terrassedør med 1 rude - 2 lags termorude</strong><br>1.67 m² · U=2.7 · mod syd<br><em>stueetage / Dagligstue / Væg 1</em></td>
</tr></tbody>
</table>

<details><summary>Per-classification breakdown</summary>

#### 1-3-1-0 — Standard windows (Vinduer) (6 entries) · ✅ Equivalent

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">Der er generelt ældre vinduer med skiftede ruder, til energiruder med kolde kante. Dog er vindue mod øst i stuen med tolags termoruder.</td>
<td valign="top">Vinduerne er hovedsageligt monteret med tolags energirude. Et vindue i dagligstuen mod øst er monteret med tolags termorude.</td>
<td valign="top"><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>2.79 m² · U=1.42 · mod nord<br><em>stueetage / Køkken / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>1.55 m² · U=1.42 · mod nord<br><em>stueetage / Badeværelse / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>1.69 m² · U=1.42 · mod vest<br><em>stueetage / Værelse nordvest / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>3.02 m² · U=1.42 · mod vest<br><em>stueetage / Værelse sydvest / Væg 2</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>1.69 m² · U=1.42 · mod syd<br><em>stueetage / Dagligstue / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 2 lags termorude kold kant</strong><br>4.1 m² · U=2.7 · mod øst<br><em>stueetage / Dagligstue / Væg 3</em></td>
</tr></tbody>
</table>

#### 1-3-3-0 — Doors with glass (Døre/Terrassedøre) (3 entries) · ⚠️ Partial overlap

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">Yderdøre i entre og bryggers med sideparti, samt terrassedør i stuen er med tolags termoruder.</td>
<td valign="top">Yderdørene med sideparti og terrassedøren er alle monteret med tolags termorude.</td>
<td valign="top"><strong>Yderdør med sideparti - 2 lags termorude</strong><br>2.66 m² · U=2.7 · mod øst<br><em>stueetage / Bryggers / Væg 1</em><br><br><strong>Yderdør med sideparti - 2 lags termorude</strong><br>2.95 m² · U=2.7 · mod nord<br><em>stueetage / Entre / Væg 1</em><br><br><strong>Terrassedør med 1 rude - 2 lags termorude</strong><br>1.67 m² · U=2.7 · mod syd<br><em>stueetage / Dagligstue / Væg 1</em></td>
</tr></tbody>
</table>

</details>

---

## Januarvænget_62_6000_Kolding (JSON enriched)

- Input XML: `Januarvænget_62_6000_Kolding.xml`
- Final XML: `Januarvænget_62_6000_Kolding final.xml`

### Combined view (all 7 entries across 2 classifications) · ✅ Equivalent

<table>
<thead><tr><th style="width:30%">PDFReportData (all consultant text)</th><th style="width:30%">Generated (all classifications joined)</th><th style="width:40%">Individual Entries (all)</th></tr></thead>
<tbody><tr>
<td valign="top">[1-3-1-0]<br>Vinduet i køkkenet er med tolags energirude. Øvrige vinduer og døre er med tolags termoruder.<br>Beskrivelse og glasforhold vedrørende vinduer og døre er baseret på visuel kontrol ved konsulent.</td>
<td valign="top">Vinduerne er hovedsageligt monteret med tolags termorude. Vinduet i køkkenet mod vest er monteret med tolags energirude.<br><br>Yderdørene i bryggerset og gangen er monteret med tolags termorude, ligesom terrassedøren i dagligstuen.</td>
<td valign="top"><strong style="color:#888">— Standard windows (Vinduer) (4) —</strong><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>1.78 m² · U=1.42 · mod vest<br><em>stueetage / Køkken / Væg 2</em><br><br><strong>Enkeltfagsvindue i fast ramme - 2 lags termorude kold kant</strong><br>4.03 m² · U=2.8 · mod øst<br><em>stueetage / Dagligstue / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>1.56 m² · U=2.8 · mod øst<br><em>stueetage / Soveværelse / Væg 2</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>1.68 m² · U=2.8 · mod vest<br><em>stueetage / værelse / Væg 3</em><br><br><strong style="color:#888">— Doors with glass (Døre/Terrassedøre) (3) —</strong><br><br><strong>Yderdør med flere ruder - 2 lags termorude</strong><br>2.03 m² · U=2.7 · mod vest<br><em>stueetage / Bryggers / Væg 4</em><br><br><strong>Terrassedør med 1 rude - 2 lags termorude</strong><br>1.63 m² · U=2.7 · mod øst<br><em>stueetage / Dagligstue / Væg 1</em><br><br><strong>Yderdør med flere ruder - 2 lags termorude</strong><br>2.97 m² · U=2.7 · mod vest<br><em>stueetage / Gang / Væg 2</em></td>
</tr></tbody>
</table>

<details><summary>Per-classification breakdown</summary>

#### 1-3-1-0 — Standard windows (Vinduer) (4 entries) · ✅ Equivalent

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">Vinduet i køkkenet er med tolags energirude. Øvrige vinduer og døre er med tolags termoruder.<br>Beskrivelse og glasforhold vedrørende vinduer og døre er baseret på visuel kontrol ved konsulent.</td>
<td valign="top">Vinduerne er hovedsageligt monteret med tolags termorude. Vinduet i køkkenet mod vest er monteret med tolags energirude.</td>
<td valign="top"><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>1.78 m² · U=1.42 · mod vest<br><em>stueetage / Køkken / Væg 2</em><br><br><strong>Enkeltfagsvindue i fast ramme - 2 lags termorude kold kant</strong><br>4.03 m² · U=2.8 · mod øst<br><em>stueetage / Dagligstue / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>1.56 m² · U=2.8 · mod øst<br><em>stueetage / Soveværelse / Væg 2</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>1.68 m² · U=2.8 · mod vest<br><em>stueetage / værelse / Væg 3</em></td>
</tr></tbody>
</table>

#### 1-3-3-0 — Doors with glass (Døre/Terrassedøre) (3 entries) · — No PDF text

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">_(no PDFReportData entry)_</td>
<td valign="top">Yderdørene i bryggerset og gangen er monteret med tolags termorude, ligesom terrassedøren i dagligstuen.</td>
<td valign="top"><strong>Yderdør med flere ruder - 2 lags termorude</strong><br>2.03 m² · U=2.7 · mod vest<br><em>stueetage / Bryggers / Væg 4</em><br><br><strong>Terrassedør med 1 rude - 2 lags termorude</strong><br>1.63 m² · U=2.7 · mod øst<br><em>stueetage / Dagligstue / Væg 1</em><br><br><strong>Yderdør med flere ruder - 2 lags termorude</strong><br>2.97 m² · U=2.7 · mod vest<br><em>stueetage / Gang / Væg 2</em></td>
</tr></tbody>
</table>

</details>

---

## Lamdrup_Møllevej_2_5854_Gislev (JSON enriched)

- Input XML: `Lamdrup_Møllevej_2_5854_Gislev.xml`
- Final XML: `Lamdrup_Møllevej_2_5854_Gislev final.xml`

### Combined view (all 14 entries across 2 classifications) · ⚠️ Partial overlap

<table>
<thead><tr><th style="width:30%">PDFReportData (all consultant text)</th><th style="width:30%">Generated (all classifications joined)</th><th style="width:40%">Individual Entries (all)</th></tr></thead>
<tbody><tr>
<td valign="top">[1-3-1-0]<br>Vinduerne er monteret med etlags glasrude og forsatsrude.<br><br>Enkelte vinduer er monteret med etlags glasrude og forsatsrude med termorude<br><br>Vindue i badeværelse er monteret med tolags termorude.<br><br>[1-3-3-0]<br>Yderdør mod nordvest er monteret med etlags glasruder og forsatsruder med termorude<br><br>Yderdør mod sydøst er monteret med tolags termorude</td>
<td valign="top">Vinduerne er primært monteret med etlags glasrude og forsatsrude, dog er vinduer i soveværelset mod nordvest og sydvest monteret med etlags glasrude og forsatsrude med energiglas, mens vinduet i badeværelset er monteret med tolags termorude.<br><br>Yderdørene i gangen og bryggerset er monteret med henholdsvis etlags glas med forsatsrude og tolags energirude, mens yderdøren i køkkenet er uden glas og isoleret.</td>
<td valign="top"><strong style="color:#888">— Standard windows (Vinduer) (11) —</strong><br><br><strong>Flerfagsvindue med gående rammer - 1+1 lag glas</strong><br>1.34 m² · U=2.2 · mod nordøst<br><em>stueetage / Gang / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 1+1 energiglas</strong><br>2.12 m² · U=1.7 · mod nordvest<br><em>stueetage / Soveværelse / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 1+1 energiglas</strong><br>1.28 m² · U=1.7 · mod sydvest<br><em>stueetage / Soveværelse / Væg 3</em><br><br><strong>Flerfagsvindue med gående rammer - 1+1 energiglas</strong><br>1.06 m² · U=1.7 · mod sydvest<br><em>stueetage / Soveværelse 2 / Væg 3</em><br><br><strong>Flerfagsvindue med gående rammer - 1+1 lag glas</strong><br>1.84 m² · U=2.2 · mod nordøst<br><em>stueetage / Dagligstue / Væg 2</em><br><br><strong>Flerfagsvindue med gående rammer - 1+1 lag glas</strong><br>1.17 m² · U=2.2 · mod sydvest<br><em>stueetage / Bryggers / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 1+1 lag glas</strong><br>1.02 m² · U=2.2 · mod sydvest<br><em>stueetage / Soveværelse 3 / Væg 5</em><br><br><strong>Flerfagsvindue med gående rammer - 1+1 lag glas</strong><br>1.39 m² · U=2.2 · mod sydvest<br><em>stueetage / Soveværelse 3 / Væg 5</em><br><br><strong>Flerfagsvindue med gående rammer - 1+1 lag glas</strong><br>1.06 m² · U=2.2 · mod nordøst<br><em>stueetage / Køkken / Væg 1</em><br><br><strong>Enkeltfagsvindue i fast ramme - 2 lags termorude kold kant</strong><br>0.48 m² · U=2.8 · mod nordøst<br><em>stueetage / Badeværelse / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 1+1 lag glas</strong><br>1.9 m² · U=2.2 · mod sydøst<br><em>stueetage / Bryggers / Væg 2</em><br><br><strong style="color:#888">— Doors with glass (Døre/Terrassedøre) (3) —</strong><br><br><strong>Yderdør med 1 rude - 1+1 energiglas</strong><br>1.99 m² · U=1.7 · mod nordvest<br><em>stueetage / Gang / Væg 2</em><br><br><strong>Yderdør uden glas</strong><br>1.9 m² · U=1.5 · mod nordøst<br><em>stueetage / Køkken / Væg 1</em><br><br><strong>Yderdør med 1 rude - 2 lags energirude med kold kant</strong><br>2.15 m² · U=1.42 · mod sydøst<br><em>stueetage / Bryggers / Væg 2</em></td>
</tr></tbody>
</table>

<details><summary>Per-classification breakdown</summary>

#### 1-3-1-0 — Standard windows (Vinduer) (11 entries) · ✅ Equivalent

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">Vinduerne er monteret med etlags glasrude og forsatsrude.<br><br>Enkelte vinduer er monteret med etlags glasrude og forsatsrude med termorude<br><br>Vindue i badeværelse er monteret med tolags termorude.</td>
<td valign="top">Vinduerne er primært monteret med etlags glasrude og forsatsrude, dog er vinduer i soveværelset mod nordvest og sydvest monteret med etlags glasrude og forsatsrude med energiglas, mens vinduet i badeværelset er monteret med tolags termorude.</td>
<td valign="top"><strong>Flerfagsvindue med gående rammer - 1+1 lag glas</strong><br>1.34 m² · U=2.2 · mod nordøst<br><em>stueetage / Gang / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 1+1 energiglas</strong><br>2.12 m² · U=1.7 · mod nordvest<br><em>stueetage / Soveværelse / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 1+1 energiglas</strong><br>1.28 m² · U=1.7 · mod sydvest<br><em>stueetage / Soveværelse / Væg 3</em><br><br><strong>Flerfagsvindue med gående rammer - 1+1 energiglas</strong><br>1.06 m² · U=1.7 · mod sydvest<br><em>stueetage / Soveværelse 2 / Væg 3</em><br><br><strong>Flerfagsvindue med gående rammer - 1+1 lag glas</strong><br>1.84 m² · U=2.2 · mod nordøst<br><em>stueetage / Dagligstue / Væg 2</em><br><br><strong>Flerfagsvindue med gående rammer - 1+1 lag glas</strong><br>1.17 m² · U=2.2 · mod sydvest<br><em>stueetage / Bryggers / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 1+1 lag glas</strong><br>1.02 m² · U=2.2 · mod sydvest<br><em>stueetage / Soveværelse 3 / Væg 5</em><br><br><strong>Flerfagsvindue med gående rammer - 1+1 lag glas</strong><br>1.39 m² · U=2.2 · mod sydvest<br><em>stueetage / Soveværelse 3 / Væg 5</em><br><br><strong>Flerfagsvindue med gående rammer - 1+1 lag glas</strong><br>1.06 m² · U=2.2 · mod nordøst<br><em>stueetage / Køkken / Væg 1</em><br><br><strong>Enkeltfagsvindue i fast ramme - 2 lags termorude kold kant</strong><br>0.48 m² · U=2.8 · mod nordøst<br><em>stueetage / Badeværelse / Væg 1</em><br><br><strong>Flerfagsvindue med gående rammer - 1+1 lag glas</strong><br>1.9 m² · U=2.2 · mod sydøst<br><em>stueetage / Bryggers / Væg 2</em></td>
</tr></tbody>
</table>

#### 1-3-3-0 — Doors with glass (Døre/Terrassedøre) (3 entries) · ❌ Differs

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">Yderdør mod nordvest er monteret med etlags glasruder og forsatsruder med termorude<br><br>Yderdør mod sydøst er monteret med tolags termorude</td>
<td valign="top">Yderdørene i gangen og bryggerset er monteret med henholdsvis etlags glas med forsatsrude og tolags energirude, mens yderdøren i køkkenet er uden glas og isoleret.</td>
<td valign="top"><strong>Yderdør med 1 rude - 1+1 energiglas</strong><br>1.99 m² · U=1.7 · mod nordvest<br><em>stueetage / Gang / Væg 2</em><br><br><strong>Yderdør uden glas</strong><br>1.9 m² · U=1.5 · mod nordøst<br><em>stueetage / Køkken / Væg 1</em><br><br><strong>Yderdør med 1 rude - 2 lags energirude med kold kant</strong><br>2.15 m² · U=1.42 · mod sydøst<br><em>stueetage / Bryggers / Væg 2</em></td>
</tr></tbody>
</table>

</details>

---

## Lokesvej_40_8660_Skanderborg (JSON enriched)

- Input XML: `Lokesvej_40_8660_Skanderborg.xml`
- Final XML: `Lokesvej_40_8660_Skanderborg final.xml`

### Combined view (all 10 entries across 2 classifications) · ✅ Equivalent

<table>
<thead><tr><th style="width:30%">PDFReportData (all consultant text)</th><th style="width:30%">Generated (all classifications joined)</th><th style="width:40%">Individual Entries (all)</th></tr></thead>
<tbody><tr>
<td valign="top">[1-3-1-0]<br>Alle vinduer og døre i ejendommen er med trelags energiruder med varme kante.</td>
<td valign="top">Vinduerne er monteret med trelags energirude.<br><br>Yderdøren i bryggerset og terrassedøren i køkken-alrummet er monteret med trelags energirude.</td>
<td valign="top"><strong style="color:#888">— Standard windows (Vinduer) (8) —</strong><br><br><strong>Enkeltfagsvindue med gående ramme - 3 lags energirude - energiklasse B</strong><br>1.16 m² · U=1.15 · mod nordøst<br><em>stueetage / Køkken-alrum / Væg 2</em><br><br><strong>Enkeltfagsvindue med gående ramme - 3 lags energirude - energiklasse B</strong><br>2.17 m² · U=1.15 · mod nordvest<br><em>stueetage / Køkken-alrum / Væg 4</em><br><br><strong>Enkeltfagsvindue med gående ramme - 3 lags energirude - energiklasse B</strong><br>1.93 m² · U=1.15 · mod nordøst<br><em>stueetage / Køkken-alrum / Væg 7</em><br><br><strong>Enkeltfagsvindue i fast ramme - 3 lags energirude - energiklasse B</strong><br>2.14 m² · U=1.15 · mod sydvest<br><em>stueetage / Køkken-alrum / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 3 lags energirude - energiklasse B</strong><br>1.19 m² · U=1.15 · mod sydvest<br><em>stueetage / Soveværelse / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 3 lags energirude - energiklasse B</strong><br>0.42 m² · U=1.15 · mod sydvest<br><em>stueetage / Badeværelse vest / Væg 3</em><br><br><strong>Enkeltfagsvindue med gående ramme - 3 lags energirude - energiklasse B</strong><br>1.22 m² · U=1.15 · mod sydøst<br><em>stueetage / Værelse syd / Væg 2</em><br><br><strong>Enkeltfagsvindue med gående ramme - 3 lags energirude - energiklasse B</strong><br>0.48 m² · U=1.15 · mod nordøst<br><em>stueetage / Badeværelse 2 / Væg 1</em><br><br><strong style="color:#888">— Doors with glass (Døre/Terrassedøre) (2) —</strong><br><br><strong>Yderdør med 1 rude - 3 lags energirude - energiklasse B</strong><br>1.87 m² · U=1.15 · mod nordøst<br><em>stueetage / Bryggers / Væg 1</em><br><br><strong>Terrassedør med 1 rude - 3 lags energirude - energiklasse B</strong><br>2.01 m² · U=1.15 · mod sydvest<br><em>stueetage / Køkken-alrum / Væg 1</em></td>
</tr></tbody>
</table>

<details><summary>Per-classification breakdown</summary>

#### 1-3-1-0 — Standard windows (Vinduer) (8 entries) · ✅ Equivalent

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">Alle vinduer og døre i ejendommen er med trelags energiruder med varme kante.</td>
<td valign="top">Vinduerne er monteret med trelags energirude.</td>
<td valign="top"><strong>Enkeltfagsvindue med gående ramme - 3 lags energirude - energiklasse B</strong><br>1.16 m² · U=1.15 · mod nordøst<br><em>stueetage / Køkken-alrum / Væg 2</em><br><br><strong>Enkeltfagsvindue med gående ramme - 3 lags energirude - energiklasse B</strong><br>2.17 m² · U=1.15 · mod nordvest<br><em>stueetage / Køkken-alrum / Væg 4</em><br><br><strong>Enkeltfagsvindue med gående ramme - 3 lags energirude - energiklasse B</strong><br>1.93 m² · U=1.15 · mod nordøst<br><em>stueetage / Køkken-alrum / Væg 7</em><br><br><strong>Enkeltfagsvindue i fast ramme - 3 lags energirude - energiklasse B</strong><br>2.14 m² · U=1.15 · mod sydvest<br><em>stueetage / Køkken-alrum / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 3 lags energirude - energiklasse B</strong><br>1.19 m² · U=1.15 · mod sydvest<br><em>stueetage / Soveværelse / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 3 lags energirude - energiklasse B</strong><br>0.42 m² · U=1.15 · mod sydvest<br><em>stueetage / Badeværelse vest / Væg 3</em><br><br><strong>Enkeltfagsvindue med gående ramme - 3 lags energirude - energiklasse B</strong><br>1.22 m² · U=1.15 · mod sydøst<br><em>stueetage / Værelse syd / Væg 2</em><br><br><strong>Enkeltfagsvindue med gående ramme - 3 lags energirude - energiklasse B</strong><br>0.48 m² · U=1.15 · mod nordøst<br><em>stueetage / Badeværelse 2 / Væg 1</em></td>
</tr></tbody>
</table>

#### 1-3-3-0 — Doors with glass (Døre/Terrassedøre) (2 entries) · — No PDF text

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">_(no PDFReportData entry)_</td>
<td valign="top">Yderdøren i bryggerset og terrassedøren i køkken-alrummet er monteret med trelags energirude.</td>
<td valign="top"><strong>Yderdør med 1 rude - 3 lags energirude - energiklasse B</strong><br>1.87 m² · U=1.15 · mod nordøst<br><em>stueetage / Bryggers / Væg 1</em><br><br><strong>Terrassedør med 1 rude - 3 lags energirude - energiklasse B</strong><br>2.01 m² · U=1.15 · mod sydvest<br><em>stueetage / Køkken-alrum / Væg 1</em></td>
</tr></tbody>
</table>

</details>

---

## Vandmøllevej_65_8723_Løsning (JSON enriched)

- Input XML: `Vandmøllevej_65_8723_Løsning.xml`
- Final XML: `Vandmøllevej_65_8723_Løsning final.xml`

### Combined view (all 18 entries across 3 classifications) · ⚠️ Partial overlap

<table>
<thead><tr><th style="width:30%">PDFReportData (all consultant text)</th><th style="width:30%">Generated (all classifications joined)</th><th style="width:40%">Individual Entries (all)</th></tr></thead>
<tbody><tr>
<td valign="top">[1-3-1-0]<br>Vinduer i køkken og bad samt ét vindue i spisestuen og to i stuen og de to gavlvinduer og de to store ovenlysvinduer på 1. sal er med tolags energirude. Vinduet i soveværelset er med trelags termorude. Øvrige vinduer og døre er med tolags termorude.<br>Beskrivelse og glasforhold vedrørende vinduer og døre er baseret på visuel kontrol ved konsulent.</td>
<td valign="top">Vinduerne er hovedsageligt monteret med tolags energirude. Enkelte vinduer i dagligstuen mod nord, i dagligstue 2 mod vest og i værelset er dog monteret med tolags termorude, mens vinduet i soveværelset på stueetagen har trelags termorude.<br><br>Ovenlysvinduerne er hovedsageligt monteret med tolags energirude, dog er ovenlysvinduet mod syd monteret med tolags termorude.<br><br>Yderdørene i gangen og i værelset mod øst er monteret med tolags termorude, mens yderdøren i værelset mod syd er uden glas og uisoleret.</td>
<td valign="top"><strong style="color:#888">— Standard windows (Vinduer) (12) —</strong><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>0.69 m² · U=1.42 · mod øst<br><em>1. sal / Soveværelse / Wall 7</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>0.76 m² · U=1.42 · mod vest<br><em>1. sal / Gang / Væg 3</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>1.01 m² · U=2.8 · mod nord<br><em>stueetage / Dagligstue / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>1.06 m² · U=1.42 · mod øst<br><em>stueetage / Dagligstue / Væg 3</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med varm kant</strong><br>1.09 m² · U=1.3 · mod nord<br><em>stueetage / Dagligstue 2 / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med varm kant</strong><br>0.97 m² · U=1.3 · mod nord<br><em>stueetage / Dagligstue 2 / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>0.81 m² · U=2.8 · mod vest<br><em>stueetage / Dagligstue 2 / Væg 3</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>1.35 m² · U=1.42 · mod syd<br><em>stueetage / Køkken / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>0.93 m² · U=1.42 · mod syd<br><em>stueetage / Badeværelse / Væg 3</em><br><br><strong>Enkeltfagsvindue med gående ramme - 3 lags termorude kold kant</strong><br>1.3 m² · U=2.2 · mod syd<br><em>stueetage / Soveværelse / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>1.02 m² · U=2.8 · mod vest<br><em>stueetage / værelse / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>0.95 m² · U=2.8 · mod øst<br><em>stueetage / værelse / Væg 3</em><br><br><strong style="color:#888">— Skylights (Ovenlysvinduer) (3) —</strong><br><br><strong>Ovenlysvindue - 2 lags energirude med kold kant</strong><br>1.01 m² · U=1.8 · mod nord<br><em>1. sal / Soveværelse / Ceiling 4</em><br><br><strong>Ovenlysvindue - 2 lags termorude kold kant</strong><br>0.72 m² · U=2.8 · mod syd<br><em>1. sal / Gang / Loft 2</em><br><br><strong>Ovenlysvindue - 2 lags energirude med kold kant</strong><br>1.01 m² · U=1.8 · mod nord<br><em>1. sal / Gang / Loft 3</em><br><br><strong style="color:#888">— Doors with glass (Døre/Terrassedøre) (3) —</strong><br><br><strong>Yderdør med uisoleret fyldning og 1 rude - 2 lags termorude</strong><br>1.79 m² · U=2.8 · mod syd<br><em>stueetage / Gang / Væg 2</em><br><br><strong>Yderdør med uisoleret fyldning og 1 rude - 2 lags termorude</strong><br>1.78 m² · U=2.8 · mod øst<br><em>stueetage / værelse / Væg 1</em><br><br><strong>Yderdør uden glas - Før 1990 - uisoleret iht. HB2023</strong><br>1.88 m² · U=2 · mod syd<br><em>stueetage / værelse / Væg 2</em></td>
</tr></tbody>
</table>

<details><summary>Per-classification breakdown</summary>

#### 1-3-1-0 — Standard windows (Vinduer) (12 entries) · ⚠️ Partial overlap

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">Vinduer i køkken og bad samt ét vindue i spisestuen og to i stuen og de to gavlvinduer og de to store ovenlysvinduer på 1. sal er med tolags energirude. Vinduet i soveværelset er med trelags termorude. Øvrige vinduer og døre er med tolags termorude.<br>Beskrivelse og glasforhold vedrørende vinduer og døre er baseret på visuel kontrol ved konsulent.</td>
<td valign="top">Vinduerne er hovedsageligt monteret med tolags energirude. Enkelte vinduer i dagligstuen mod nord, i dagligstue 2 mod vest og i værelset er dog monteret med tolags termorude, mens vinduet i soveværelset på stueetagen har trelags termorude.</td>
<td valign="top"><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>0.69 m² · U=1.42 · mod øst<br><em>1. sal / Soveværelse / Wall 7</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>0.76 m² · U=1.42 · mod vest<br><em>1. sal / Gang / Væg 3</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>1.01 m² · U=2.8 · mod nord<br><em>stueetage / Dagligstue / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>1.06 m² · U=1.42 · mod øst<br><em>stueetage / Dagligstue / Væg 3</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med varm kant</strong><br>1.09 m² · U=1.3 · mod nord<br><em>stueetage / Dagligstue 2 / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med varm kant</strong><br>0.97 m² · U=1.3 · mod nord<br><em>stueetage / Dagligstue 2 / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>0.81 m² · U=2.8 · mod vest<br><em>stueetage / Dagligstue 2 / Væg 3</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>1.35 m² · U=1.42 · mod syd<br><em>stueetage / Køkken / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags energirude med kold kant</strong><br>0.93 m² · U=1.42 · mod syd<br><em>stueetage / Badeværelse / Væg 3</em><br><br><strong>Enkeltfagsvindue med gående ramme - 3 lags termorude kold kant</strong><br>1.3 m² · U=2.2 · mod syd<br><em>stueetage / Soveværelse / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>1.02 m² · U=2.8 · mod vest<br><em>stueetage / værelse / Væg 1</em><br><br><strong>Enkeltfagsvindue med gående ramme - 2 lags termorude kold kant</strong><br>0.95 m² · U=2.8 · mod øst<br><em>stueetage / værelse / Væg 3</em></td>
</tr></tbody>
</table>

#### 1-3-2-0 — Skylights (Ovenlysvinduer) (3 entries) · — No PDF text

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">_(no PDFReportData entry)_</td>
<td valign="top">Ovenlysvinduerne er hovedsageligt monteret med tolags energirude, dog er ovenlysvinduet mod syd monteret med tolags termorude.</td>
<td valign="top"><strong>Ovenlysvindue - 2 lags energirude med kold kant</strong><br>1.01 m² · U=1.8 · mod nord<br><em>1. sal / Soveværelse / Ceiling 4</em><br><br><strong>Ovenlysvindue - 2 lags termorude kold kant</strong><br>0.72 m² · U=2.8 · mod syd<br><em>1. sal / Gang / Loft 2</em><br><br><strong>Ovenlysvindue - 2 lags energirude med kold kant</strong><br>1.01 m² · U=1.8 · mod nord<br><em>1. sal / Gang / Loft 3</em></td>
</tr></tbody>
</table>

#### 1-3-3-0 — Doors with glass (Døre/Terrassedøre) (3 entries) · — No PDF text

<table>
<thead><tr><th style="width:30%">PDFReportData (consultant, from Final)</th><th style="width:30%">Generated (LLM, from Plans + JSON)</th><th style="width:40%">Individual Entries (input)</th></tr></thead>
<tbody><tr>
<td valign="top">_(no PDFReportData entry)_</td>
<td valign="top">Yderdørene i gangen og i værelset mod øst er monteret med tolags termorude, mens yderdøren i værelset mod syd er uden glas og uisoleret.</td>
<td valign="top"><strong>Yderdør med uisoleret fyldning og 1 rude - 2 lags termorude</strong><br>1.79 m² · U=2.8 · mod syd<br><em>stueetage / Gang / Væg 2</em><br><br><strong>Yderdør med uisoleret fyldning og 1 rude - 2 lags termorude</strong><br>1.78 m² · U=2.8 · mod øst<br><em>stueetage / værelse / Væg 1</em><br><br><strong>Yderdør uden glas - Før 1990 - uisoleret iht. HB2023</strong><br>1.88 m² · U=2 · mod syd<br><em>stueetage / værelse / Væg 2</em></td>
</tr></tbody>
</table>

</details>

---
