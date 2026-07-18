---
layout: default
title: "CineTourism Map"
vega: true
header_type: hero
header_img: assets/images/header.svg
header_title: "CineTourism: L'Impatto dei Media sul Territorio"
subtitle: "Un'analisi tra visibilità globale e sostenibilità locale"
---

<style>
  /* ---- Attacco / lead ---- */
  .lead-hook {
    font-size: 1.35rem;
    line-height: 1.45;
    font-weight: 700;
    color: #1a202c;
    margin: .5rem 0 1.2rem;
  }
  .lead-hook .hook-accent { color: #2b6cb0; }

  /* ---- Citazioni ---- */
  .quote-card {
    border-left: 4px solid #2b6cb0;
    background: #f7f9fb;
    border-radius: 4px;
    padding: 1.1rem 1.3rem;
    margin: 1.6rem 0;
  }
  .quote-card .q-text { font-size: 1.02rem; font-style: italic; color: #2d3748; line-height: 1.6; margin: 0 0 .6rem; }
  .quote-card .q-author { font-size: .85rem; color: #666; font-weight: 700; display: block; }
  .quote-card .q-role { font-weight: 400; color: #888; }

  /* ---- Numeri del progetto ---- */
  .facts-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: .9rem;
    margin: 1.6rem 0 2rem;
  }
  @media (max-width: 767.98px) { .facts-grid { grid-template-columns: 1fr; } }
  .fact-card {
    border: 1px solid #1a1a1a;
    border-radius: 4px;
    background: #fff;
    padding: 1rem 1.1rem;
    text-align: center;
  }
  .fact-num {
    display: block;
    font-size: 1.9rem;
    font-weight: 700;
    line-height: 1;
    color: #1a1a1a;
    margin-bottom: .35rem;
  }
  .fact-label { display: block; font-size: .85rem; color: #666; line-height: 1.35; }

  /* ---- Casi in evidenza: righe a piena larghezza ---- */
  .cases-list { margin: 1.8rem 0; }
  .case-row {
    display: flex;
    align-items: flex-start;
    gap: 1.4rem;
    border: 1px solid #e6e8eb;
    border-left: 5px solid var(--case-accent, #2b6cb0);
    border-radius: 6px;
    background: #fff;
    padding: 1.1rem 1.4rem;
    margin-bottom: .9rem;
    transition: box-shadow .2s ease;
  }
  .case-row:hover { box-shadow: 0 4px 14px rgba(0,0,0,.07); }
  .case-head { flex: 0 0 230px; }
  .case-body { flex: 1 1 auto; }
  .case-row .case-place {
    display: block;
    font-size: 1.08rem;
    font-weight: 700;
    color: #1a202c;
    line-height: 1.25;
  }
  .case-row .case-prod {
    display: block;
    font-size: .82rem;
    font-style: italic;
    color: var(--case-accent, #2b6cb0);
    margin-top: .2rem;
  }
  .case-row p { font-size: .94rem; color: #444; margin: 0; line-height: 1.55; }
  @media (max-width: 767.98px) {
    .case-row { flex-direction: column; gap: .6rem; }
    .case-head { flex: none; }
  }
  .case-1 { --case-accent: #c05621; }
  .case-2 { --case-accent: #2b6cb0; }
  .case-3 { --case-accent: #2f855a; }

  /* ---- Cluster ---- */
  .cluster-grid { margin: 1.8rem 0; }
  .cluster-card {
    height: 100%;
    display: flex;
    flex-direction: column;
    border: 1px solid #e6e8eb;
    border-top: 5px solid var(--cl-accent, #2b6cb0);
    border-radius: 8px;
    padding: 1.2rem;
    background: #fff;
    transition: box-shadow .2s ease, transform .2s ease;
  }
  .cluster-card:hover { box-shadow: 0 10px 24px rgba(0,0,0,.10); transform: translateY(-3px); }
  .cluster-card .cl-kicker {
    font-size: .72rem; font-weight: 700; letter-spacing: .08em;
    text-transform: uppercase; color: var(--cl-accent, #2b6cb0);
  }
  .cluster-card h4 { font-size: 1.08rem; margin: .35rem 0 .5rem; }
  .cluster-card p { font-size: .9rem; color: #444; flex-grow: 1; }
  .cluster-card .btn { margin-top: .8rem; align-self: flex-start; }
  .cl-1 { --cl-accent: #c05621; }
  .cl-2 { --cl-accent: #2b6cb0; }
  .cl-3 { --cl-accent: #2f855a; }

  /* ---- Mappa a dimensione naturale, centrata.
     IMPORTANTE: non forzare la larghezza dell'SVG/canvas: scalare il grafico via
     CSS sfasa il rilevamento di click e tooltip di Vega. Su schermi stretti si
     scorre orizzontalmente invece di deformare la mappa. ---- */
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
  .page-links { display: flex; flex-direction: column; gap: .6rem; }
  .page-links a { font-weight: 600; }
</style>

<p class="lead-hook">
  Spoiler: la tua prossima vacanza l'hai già vista al cinema.
  <span class="hook-accent">Prossima fermata? Il set!</span>
</p>

Ogni anno migliaia di persone si spostano non per una spiaggia o un museo, ma per un luogo che hanno già "visitato" attraverso un film o una serie TV. È il **cineturismo**: un fenomeno che trasforma borghi, laghi e città in spazi narrativi, capaci di attrarre visitatori da tutto il mondo o semplicemente di far riscoprire un pezzo d'Italia a chi già ci vive.

Cos'è che fa scattare davvero questa scintilla? Secondo lo youtuber ed esperto di cinema Rob McQuack, **tutto nasce da una scena che colpisce emotivamente**: il fan vuole tornare in quel luogo per respirare gli stessi profumi e gli stessi sapori che ha solo immaginato guardando lo schermo, un piccolo atto di fuga dalla realtà.

<hr class="section-rule">

## Misurare la scintilla

Questo progetto nasce per misurare quella scintilla, incrociando **dati ISTAT**, **ecosistema commerciale**, **stampa**, **Google Trends**, **Wikipedia**, **YouTube**, **Reddit**, **recensioni dei tour online** e le voci dirette di chi il fenomeno lo vive ogni giorno.

<div class="facts-grid">
  <div class="fact-card">
    <span class="fact-num">12</span>
    <span class="fact-label">casi di studio</span>
  </div>
  <div class="fact-card">
    <span class="fact-num">7</span>
    <span class="fact-label">filoni di analisi</span>
  </div>
  <div class="fact-card">
    <span class="fact-num">1</span>
    <span class="fact-label">domanda: cosa succede a un territorio quando finisce sullo schermo?</span>
  </div>
</div>

<hr class="section-rule">

## Le risposte non sono mai scontate

<div class="cases-list">

  <div class="case-row case-1">
    <div class="case-head">
      <span class="case-place">Crema</span>
      <span class="case-prod">Call Me by Your Name</span>
    </div>
    <div class="case-body">
      <p>Dopo il film, i visitatori dei musei sono <strong>più che raddoppiati</strong>.</p>
    </div>
  </div>

  <div class="case-row case-1">
    <div class="case-head">
      <span class="case-place">Bard e Pont-Saint-Martin</span>
      <span class="case-prod">Avengers: Age of Ultron</span>
    </div>
    <div class="case-body">
      <p>L'arrivo degli Avengers ha fatto esplodere la ricettività extra-alberghiera di <strong>oltre il 200%</strong>.</p>
    </div>
  </div>

  <div class="case-row case-1">
    <div class="case-head">
      <span class="case-place">Volterra</span>
      <span class="case-prod">The Twilight Saga: New Moon</span>
    </div>
    <div class="case-body">
      <p>Il successo ha imposto una scelta difficile. Come ci ha raccontato il responsabile del Consorzio Turistico, la priorità è sempre stata governare un fenomeno passeggero <strong>senza legare la città per sempre alla "città dei vampiri"</strong>, proteggendo un'immagine costruita in trent'anni di promozione culturale.</p>
    </div>
  </div>

  <div class="case-row case-2">
    <div class="case-head">
      <span class="case-place">Lago di Braies</span>
      <span class="case-prod">Un passo dal cielo</span>
    </div>
    <div class="case-body">
      <p>Un successo così grande da mettere in crisi il territorio: appena <strong>650 residenti</strong>, contro punte di <strong>15.000 visitatori</strong> in un solo giorno. Dal 2025 l'accesso al lago è regolato da prenotazione obbligatoria e numero chiuso — un modello che le istituzioni altoatesine indicano oggi come esempio da replicare altrove.</p>
    </div>
  </div>

  <div class="case-row case-3">
    <div class="case-head">
      <span class="case-place">Castellabate</span>
      <span class="case-prod">Benvenuti al Sud</span>
    </div>
    <div class="case-body">
      <p>Quattordici anni dopo l'uscita, il paese continua a incuriosire più della pellicola stessa: le ricerche online per la località superano ancora oggi quelle per i protagonisti del film, con <strong>picchi ricorrenti ogni estate</strong> (luglio su tutti).</p>
    </div>
  </div>

</div>

<hr class="section-rule">

## Esplora le produzioni sul territorio

Ogni produzione analizzata è legata a uno o più **luoghi di ripresa** in Italia.
La mappa raccoglie tutte le location del progetto, colorate per **cluster**:
cliccando su un punto si evidenziano tutte le località di quella produzione e la
scheda a fianco ne mostra i dettagli.

<div class="note-box">
  <span class="note-title"><i class="fas fa-hand-pointer" aria-hidden="true"></i>Come usare la mappa</span>
  Clicca una località per selezionare la sua produzione: la scheda a destra mostra
  titolo, cluster di appartenenza, elenco delle località e altri dettagli. Doppio click per deselezionare.
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

## Tre cluster, tre modi di raccontare lo stesso fenomeno

<div class="row cluster-grid">
  <div class="col-md-4 mb-4">
    <div class="cluster-card cl-1">
      <span class="cl-kicker">Cluster 01</span>
      <h4>Blockbuster globali</h4>
      <p>Grandi produzioni internazionali girate in Italia: impatto improvviso e alta volatilità.</p>
      <a href="{{ site.baseurl }}/cluster01.html" class="btn btn-primary">Vai al Cluster 01</a>
    </div>
  </div>
  <div class="col-md-4 mb-4">
    <div class="cluster-card cl-2">
      <span class="cl-kicker">Cluster 02</span>
      <h4>Lunghe serialità italiane</h4>
      <p>Fiction radicate nel territorio nel corso di anni, se non decenni, di messa in onda.</p>
      <a href="{{ site.baseurl }}/cluster02.html" class="btn btn-primary">Vai al Cluster 02</a>
    </div>
  </div>
  <div class="col-md-4 mb-4">
    <div class="cluster-card cl-3">
      <span class="cl-kicker">Cluster 03</span>
      <h4>Produzioni di nicchia</h4>
      <p>Casi non riconducibili ai cluster precedenti: impatto focalizzato e target specifico.</p>
      <a href="{{ site.baseurl }}/cluster03.html" class="btn btn-primary">Vai al Cluster 03</a>
    </div>
  </div>
</div>

<hr class="section-rule">

<div class="page-links">
  <a href="{{ site.baseurl }}/introduzione.html">Introduzione →</a>
  <a href="{{ site.baseurl }}/methodology.html">Metodologia →</a>
  <a href="{{ site.baseurl }}/results.html">Risultati →</a>
</div>
