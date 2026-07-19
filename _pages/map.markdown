---
layout: default
title: "CineTourism Map"
vega: true
header_type: hero
header_img: assets/images/header.svg
header_title: "CineTourism in Italia"
subtitle: "Le produzioni e le località"
---

<style>
  /* Mappa a dimensione naturale, centrata.
     IMPORTANTE: non forzare la larghezza dell'SVG/canvas: scalare il grafico via
     CSS sfasa il rilevamento di click e tooltip di Vega. Su schermi stretti si
     scorre orizzontalmente invece di deformare la mappa. */
  .map-container {
    margin: 30px auto 40px;
    text-align: center;
    overflow-x: auto;
  }

  .note-box {
    border-left: 4px solid #2b6cb0;
    background: #f4f8fc;
    padding: 1rem 1.2rem;
    border-radius: 4px;
    margin: 1.6rem auto;
    max-width: 900px;
  }
  .note-box .note-title { font-weight: 700; display: block; margin-bottom: .3rem; color: #24487e; }
  .note-box .note-title i { margin-right: .4rem; }

  .section-rule { border: 0; border-top: 1px solid #e6e8eb; margin: 3rem 0 2rem; }
  .page-links a { margin-right: 1.4rem; font-weight: 600; }
</style>

## Esplora le produzioni sul territorio

Ogni produzione analizzata è legata a uno o più **luoghi di ripresa** in Italia.
La mappa raccoglie tutte le location del progetto, colorate per **gruppi**:
cliccando su un punto si evidenziano tutte le località di quella produzione e la
scheda a fianco ne mostra i dettagli.

<div class="note-box">
  <span class="note-title"><i class="fas fa-hand-pointer" aria-hidden="true"></i>Come usare la mappa</span>
  Clicca una località per selezionare la sua produzione: la scheda a destra mostra
  titolo, gruppo di appartenenza, elenco delle località e altri dettagli. Doppio click per deselezionare.
  <br/>
  Mouse over sul gruppo per evidenziare le sue località.
</div>

<div class="map-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/mappa_italia.vl.json"></vegachart>
</div>

<!--
  Spec unico (mappa + scheda) generato da build_map.py a partire da
  dataset json. L'interazione click->scheda e il link nella scheda
  funzionano perché selezione, filtro e href stanno nella stessa specifica.
-->

<hr class="section-rule">

<div class="page-links">
  <a href="{{ site.baseurl }}/introduction.html">Introduzione →</a>
  <a href="{{ site.baseurl }}/methodology.html">Metodologia →</a>
  <a href="{{ site.baseurl }}/results.html">Risultati →</a>
</div>
