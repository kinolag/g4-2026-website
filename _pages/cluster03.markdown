---
layout: default
title: "Cluster 3: Cineturismo Nazionale – Analisi dei Casi di Studio Italiani"
vega: true
header_type: hero
header_img: assets/images/header.svg
header_title: "Analisi di Cluster: altre Produzioni italiane"
subtitle: " Come lo schermo trasforma i territori: produzioni di nicchia o non riconducibili ai cluster precedenti"
---

<style>
  /* Contenitore standard, centrato e responsivo */
  .chart-container {
    width: 100%;
    max-width: 1000px; /* limite per evitare grafici troppo grandi */
    margin: 40px auto; /* centra il grafico */
    padding: 0 20px; /* margine laterale su mobile */
    box-sizing: border-box;
  }

  /* Vega charts: impedisce stiramenti */
  .chart-container vegachart,
  .chart-container .vega-embed {
    width: 100% !important;
    height: auto !important;
    display: block !important;
  }

  .chart-container canvas,
  .chart-container svg {
    width: 100% !important;
    height: auto !important;
    object-fit: contain !important;
  }
</style>

## Panoramica

Il cluster raccoglie **quattro produzioni italiane**, ciascuna legata a uno o più territori specifici: **Castellabate** per *Benvenuti al Sud*; 
**Curon Venosta / Lago di Resia** per *Curon*; **Aosta** per *Rocco Schiavone*; **Opi e Pescasseroli** per *Un mondo a parte*.

Le produzioni raccolte nel cluster appartengono a un immaginario **interamente italiano**, lontano dai blockbuster internazionali analizzati 
nei cluster precedenti e radicato in un pubblico domestico che riconosce nei luoghi rappresentati una geografia familiare. Sono opere che non 
hanno avuto particolare risonanza all’estero, ma che in Italia hanno saputo incidere profondamente sulla percezione dei territori, trasformando 
borghi, laghi e città in spazi narrativi riconoscibili.
Accanto a questa dimensione nazionale, emerge la loro capacità di **lasciare un segno duraturo**: _Benvenuti al Sud_ ha ridefinito l’immaginario 
di Castellabate, _Curon_ ha trasformato il Lago di Resia in un simbolo culturale, _Rocco Schiavone_ ha reinterpretato Aosta come personaggio 
urbano, _Un mondo a parte_ ha amplificato la visibilità di Opi e Pescasseroli. Non si tratta di opere sostenute da franchise globali o da 
serialità ultralongeve, ma di casi di studio che, pur partendo da una scala produttiva più contenuta, hanno generato 
**effetti misurabili e persistenti** sui territori.

Questa combinazione — una produzione non globale, ma capace di produrre una **rottura di trend** evidente — è 
la chiave di lettura scelta per analizzare il cluster: l’obiettivo non è misurare l’eco di un successo planetario, bensì 
osservare come opere nate per il pubblico italiano possano comunque costruire nel tempo un **radicamento strutturale**, modificando 
narrazioni, percezioni e dinamiche turistiche. Non un picco isolato, ma una trasformazione che si consolida e si rinnova.

Si tratta di opere molto diverse per genere, distribuzione, pubblico e natura produttiva, ma accomunate da un tratto fondamentale: 
la capacità di riscrivere la percezione dei luoghi, modificare le narrazioni mediatiche e influenzare in modo strutturale l’ecosistema 
turistico ed economico.
L’obiettivo è comprendere come il cinema e le serie TV, anche quando non hanno risonanza internazionale, possano generare effetti 
persistenti e misurabili, trasformando borghi, città e paesaggi naturali in asset territoriali.

<!-- IMMAGINE: foto di apertura del cluster -->

<!--
  Domande-guida della pagina (temporaneamente non visibili):
  1. Il fenomeno esiste ed è misurabile? (i primi numeri)
  2. Il panorama dei media offre riscontri e alimenta il fenomeno?
  3. Le persone viaggiano per la serie, o la "visitano" da casa?
-->

---

## Sezione 1 — Il fenomeno

<!-- Risponde alla domanda 1: il fenomeno esiste ed è misurabile? -->

_Il fenomeno esiste, è misurabile? Vediamo i primi numeri._

Le evidenze **ISTAT** validate (CIS > 0,7, RGR ≥ 0,15) mostrano segnali
misurabili in **due delle quattro produzioni** del cluster, con intensità molto
diverse tra loro.

### Castellabate — _Benvenuti al Sud_

**Nessuna evidenza** tra gli indicatori selezionati: il segnale ISTAT non ha superato le soglie di validazione.
Il caso resta comunque rilevante nel cluster, ma l’impatto misurabile non emerge dagli indicatori ISTAT utilizzati.

### Curon Venosta — _Curon_

Segnale pieno e coerente: la **popolazione straniera** cresce del **+27,71%**, con uno **Zeta Shift di +5,68σ** e **persistenza piena (1/1)**. 
Il **CIS** è **100/100**, e l’RGR raggiunge **+20,79%**.
È un caso che non presenta anomalie: la crescita è moderata ma stabile, e si manifesta come una trasformazione graduale del territorio, 
più che come un picco isolato. La serie Netflix ha introdotto una discontinuità evidente, ma senza sbilanciare gli equilibri locali.

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/clsuter03/curon_istat.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>

### Aosta — _Rocco Schiavone_

Segnale solido e lineare: la **densità degli esercizi ricettivi** aumenta del **+26,19%**, con uno **Zeta Shift molto alto (+21,45σ)** e 
**persistenza piena (1/1)**. Il **CIS** è **100/100**, e l’**RGR** si attesta a **+18,48%**.
Non ci sono balzi improvvisi, ma una crescita coerente con la serialità e con la capacità della produzione di mantenere nel tempo 
un’attenzione costante sulla città. È un caso “pulito”, privo di estremi, che riflette bene la natura progressiva dell’impatto.

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/clsuter03/aosta_istat.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>

### Opi e Pescasseroli — _Un mondo a parte_

Nessuna evidenza tra gli indicatori selezionati: nessun indicatore validato, nessun RGR sopra soglia.
L’effetto del film è reale e riconoscibile sul territorio, ma non si manifesta nei KPI ISTAT considerati.

### Uno sguardo d'insieme

Il quadro che emerge dal confronto è quasi a due velocità.
Da un lato Curon e Aosta disegnano il profilo più “sano” del cluster — segnali coerenti, persistenti nel tempo, privi di anomalie 
statistiche.
Dall’altro Castellabate e Opi/Pescasseroli, pur centrali nella narrazione del cluster, non superano le soglie ISTAT: l’impatto esiste, 
ma non è misurabile attraverso gli indicatori selezionati.


<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/castellabate1.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>


[Link di ritorno a Risultati](results.html)