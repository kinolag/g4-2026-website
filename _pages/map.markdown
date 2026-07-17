---
layout: default
title: "Mappa"
vega: true
header_type: hero
header_img: assets/images/header.svg
header_title: "Mappa del CineTourism in Italia"
subtitle: "Le produzioni e i loro territori"
---

<style>
  .map-container {
    width: 100%;
    max-width: 1100px;
    margin: 30px auto 40px;
    padding: 0 16px;
    box-sizing: border-box;
  }
  .map-container vegachart,
  .map-container .vega-embed { width: 100% !important; display: block !important; }
  .map-container canvas,
  .map-container svg { width: 100% !important; height: auto !important; object-fit: contain !important; }

  .note-box {
    border-left: 4px solid #2b6cb0;
    background: #f4f8fc;
    padding: 1rem 1.2rem;
    border-radius: 4px;
    margin: 1.6rem auto;
    max-width: 1100px;
  }
  .note-box .note-title { font-weight: 700; display: block; margin-bottom: .3rem; color: #24487e; }
  .note-box .note-title i { margin-right: .4rem; }

  .section-rule { border: 0; border-top: 1px solid #e6e8eb; margin: 3rem 0 2rem; }
</style>

## Esplora le produzioni sul territorio

Ogni produzione analizzata è legata a uno o più **luoghi di ripresa** in Italia.
La mappa raccoglie tutte le location del progetto, colorate per **cluster**:
cliccando su un punto, la scheda a fianco si aggiorna con i dettagli della
produzione corrispondente.

<div class="note-box">
  <span class="note-title"><i class="fas fa-hand-pointer" aria-hidden="true"></i>Come usarla</span>
  Clicca una località sulla mappa per selezionarla: la scheda a destra mostra
  produzione, tipo e cluster. Clicca in un punto vuoto per deselezionare.
</div>

<div class="map-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/mappa_italia.vl.json"></vegachart>
</div>

<!--
  Lo spec (mappa + scheda) è un unico file Vega-Lite. 
  L'interazione click->scheda funziona perché
  selezione e filtro stanno nella stessa specifica.
-->

<hr class="section-rule">

<a href="{{ site.baseurl }}/introduzione.html">Introduzione →</a>

<a href="{{ site.baseurl }}/methodology.html">Metodologia →</a>

<a href="{{ site.baseurl }}/results.html">Risultati →</a>
