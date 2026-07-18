---
layout: default
title: "Introduzione al CineTourism"
vega: true
header_type: hero
header_img: assets/images/header.svg
header_title: "Introduzione al CineTourism"
subtitle: "Un fenomeno in rapida evoluzione"
---

<style>
  /* Contenitore standard, centrato e responsivo */
  .chart-container {
    width: 100%;
    max-width: 1000px;
    margin: 40px auto;
    padding: 0 20px;
    box-sizing: border-box;
  }
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

  /* ---- Pro / Contro: due colonne a confronto ---- */
  .pro-contro { margin: 2rem 0; }
  .pc-card {
    height: 100%;
    border: 1px solid #e6e8eb;
    border-top: 4px solid var(--pc-accent, #2b6cb0);
    border-radius: 6px;
    padding: 1.2rem 1.3rem;
    background: #fff;
  }
  .pc-card h4 { font-size: 1.05rem; margin: 0 0 .8rem; color: var(--pc-accent, #2b6cb0); }
  .pc-card h4 i { margin-right: .45rem; }
  .pc-card ul { margin: 0; padding-left: 1.1rem; }
  .pc-card li { font-size: .93rem; margin-bottom: .6rem; line-height: 1.5; }
  .pc-card li:last-child { margin-bottom: 0; }
  .pc-pro    { --pc-accent: #2f855a; }
  .pc-contro { --pc-accent: #c05621; }

  /* ---- Citazioni dalle interviste ---- */
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

  /* ---- Immagini con didascalia ---- */
  figure.photo { margin: 2rem auto; max-width: 900px; }
  figure.photo img { width: 100%; height: auto; border-radius: 6px; display: block; }
  figure.photo figcaption { font-size: .85rem; color: #666; text-align: center; margin-top: .6rem; line-height: 1.5; }

  /* ---- Box informativo (coerente con la pagina Metodologia) ---- */
  .note-box {
    border-left: 4px solid #2b6cb0;
    background: #f4f8fc;
    padding: 1rem 1.2rem;
    border-radius: 4px;
    margin: 1.8rem 0;
  }
  .note-box .note-title { font-weight: 700; display: block; margin-bottom: .3rem; color: #24487e; }
  .note-box .note-title i { margin-right: .4rem; }
  .stat-inline { font-weight: 700; color: #2b6cb0; }

  .section-rule { border: 0; border-top: 1px solid #e6e8eb; margin: 3rem 0 2rem; }
</style>

## Definizione e Complessità del Fenomeno

Il **CineTourism** identifica lo spostamento di flussi turistici verso destinazioni rese celebri da film o serie TV, un processo che fonde la realtà geografica con l'immaginario narrativo. La letteratura internazionale lo descrive come una forma di turismo esperienziale e identitario, in cui il visitatore cerca di "vivere" la storia che ha visto sullo schermo. Non si tratta solo di visitare un set, ma di entrare in un universo simbolico: un luogo reale che diventa spazio emotivo e culturale.

<div class="quote-card">
  <p class="q-text">«Il cinema dà valore a ciò che abbiamo a disposizione.»</p>
  <span class="q-author">Davide Marra <span class="q-role">— podcaster</span></span>
</div>

Guardare un film può trasformare un luogo familiare in qualcosa di nuovo, risvegliando curiosità e senso di appartenenza. Allo stesso modo, il doppiatore **Rob McQuack** sottolinea che oggi il fenomeno è amplificato dallo streaming e dai social: scene iconiche diventano trend globali, e i fan si spostano per ricrearle.

<div class="quote-card">
  <p class="q-text">«[I fan cercano di] portare un po' di quella magia nella realtà.»</p>
  <span class="q-author">Rob McQuack <span class="q-role">— doppiatore</span></span>
</div>

<hr class="section-rule">

## Il Paradosso della Visibilità: Perché è Importante?

Il successo mediatico di un'opera può trasformarsi in un **paradosso territoriale**: da un lato genera visibilità, investimenti e crescita economica; dall'altro espone il territorio a **stress infrastrutturali**, perdita di autenticità e sovraffollamento.

<div class="row pro-contro">
  <div class="col-md-6 mb-4">
    <div class="pc-card pc-pro">
      <h4><i class="fas fa-arrow-trend-up" aria-hidden="true"></i>Pro</h4>
      <ul>
        <li><strong>Boom economico e occupazionale:</strong> l'aumento dei flussi turistici porta nuove attività ricettive, ristorative e culturali.</li>
        <li><strong>Valorizzazione del patrimonio locale:</strong> i luoghi diventano simboli identitari e attrattori di interesse internazionale.</li>
        <li><strong>Rinascita culturale:</strong> come nel caso di <em>Gomorra</em>, citato da Davide Marra, la produzione audiovisiva può stimolare nuove iniziative artistiche e sociali.</li>
      </ul>
    </div>
  </div>
  <div class="col-md-6 mb-4">
    <div class="pc-card pc-contro">
      <h4><i class="fas fa-triangle-exclamation" aria-hidden="true"></i>Contro</h4>
      <ul>
        <li><strong>Sovraffollamento e degrado ambientale:</strong> l'afflusso non pianificato di visitatori può compromettere ecosistemi fragili.</li>
        <li><strong>Perdita della "vera storia" del luogo:</strong> il territorio rischia di essere percepito solo attraverso la lente del film o della serie, riducendone la complessità culturale.</li>
        <li><strong>Stereotipizzazione:</strong> come osserva McQuack, l'Italia viene spesso rappresentata con cliché turistici che non riflettono la realtà contemporanea.</li>
      </ul>
    </div>
  </div>
</div>

<figure class="photo">
  <img src="{{site.baseurl}}/assets/images/cinetourism_locations/braies_crowd_1.jpg"
       alt="Sovraffollamento al Lago di Braies">
  <figcaption>
    <strong>Lago di Braies.</strong> Il successo mediatico attira capitali ma espone il territorio a stress
    infrastrutturali non pianificati: l'afflusso di migliaia di turisti ha reso necessarie misure di gestione
    obbligate, come la chiusura della strada nei mesi di picco per preservare l'ecosistema.
  </figcaption>
</figure>

<hr class="section-rule">

## Dal Film al Territorio: Attività e Impatti

Il cineturismo è oggi un **fenomeno emergente** e in rapida evoluzione. Accanto agli studi sociologici e culturali, questo progetto propone di affiancare una **dimensione quantitativa**, basata su analisi di dati e metriche territoriali. L'obiettivo è costruire una **pipeline metodologica riciclabile**, capace di analizzare casi di studio in Italia e all'estero, integrando dati di sentiment, flussi turistici, trend digitali e trasformazioni economiche.

Studiare il cineturismo significa comprendere come l'immaginario audiovisivo influenzi comportamenti reali, economie locali e identità collettive. È un campo di ricerca che unisce **media studies**, **data analytics** e **geografia culturale**, con l'ambizione di trasformare la visibilità mediatica in uno strumento di sviluppo sostenibile.

### Le esperienze nate attorno ai film

La crescita del cineturismo ha generato un ecosistema di **attività commerciali e culturali** che rispondono alle nuove esigenze dei visitatori. Tra queste, iniziative indipendenti come l'**Elio & Oliver Love Tour** di Crema, dedicato a *Call Me By Your Name*: nato dal passaparola dei fan, oggi accoglie centinaia di persone ogni giorno, creando legami umani e culturali attorno al film.

<div class="quote-card">
  <p class="q-text">«Cerchiamo solo di continuare a condividere l'amore il più a lungo possibile.»</p>
  <span class="q-author">Gary Potter <span class="q-role">— organizzatore dell'Elio &amp; Oliver Love Tour, Crema</span></span>
</div>

### Cosa raccontano i tour e le recensioni

Accanto alle iniziative indipendenti ci sono i **tour cinematografici** organizzati da piattaforme come **GetYourGuide**, di cui abbiamo analizzato descrizioni e recensioni.

Le **descrizioni** dei tour, analizzate con tecniche NLP, mostrano che gli operatori costruiscono un immaginario centrato sulla scoperta, sulla storia, sulla cultura cinematografica e sulla narrazione dei luoghi iconici.

Sulle **recensioni** abbiamo studiato la distribuzione dei voti, la lunghezza dei testi, la provenienza dei turisti e la stagionalità. È emerso che il cineturismo attira in modo particolare turisti stranieri, soprattutto giovani, mentre gli italiani risultano meno rappresentati. Le recensioni estive sono più numerose e più entusiaste, segno che l'esperienza cinematografica si intreccia con la dimensione emozionale del viaggio.

Infine, la parte più delicata è stata la **sentiment analysis**: abbiamo usato Pattern.it e poi costruito un sentiment combinato che integra il tono del testo con il voto numerico della recensione, ottenendo una misura molto più stabile e realistica.

<div class="note-box">
  <span class="note-title"><i class="fas fa-info-circle" aria-hidden="true"></i>Il risultato</span>
  Il sentiment medio dei tour è fortemente positivo, con valori compresi tra <span class="stat-inline">0,4</span> e <span class="stat-inline">0,6</span>. Le <strong>guide competenti</strong> sono il fattore più determinante; i pochi valori più bassi riguardano problemi organizzativi o aspettative non soddisfatte.
</div>

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/sentiment_combinato_recensioni_gyg.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>

Questi esempi mostrano come il cineturismo non sia solo un fenomeno economico, ma anche **sociale e affettivo**: un modo per costruire comunità, condividere esperienze e riscoprire il valore dei luoghi attraverso la lente del cinema.

Di seguito la wordcloud delle recensioni di GetYourGuide:

<div class="row">
  <div class="col-md-12 text-center">
    <img src="{{site.baseurl}}/assets/images/introduzione/wordcloud_recensioni.png"
         class="img-fluid mx-auto d-block"
         style="margin: 20px 0 5px 0; border-radius: 8px;"
         alt="Locandine delle produzioni analizzate: Benvenuti al Sud, Curon, Rocco Schiavone, Un mondo a parte">
  </div>
</div>
<hr class="section-rule">

## Conclusioni e Prospettive

Il cineturismo è un laboratorio di trasformazione territoriale e culturale. Studiare questo fenomeno significa interrogarsi su come i media plasmino la realtà, e su come i territori possano rispondere in modo sostenibile.

L'integrazione tra **analisi qualitativa** (narrazioni, percezioni, esperienze) e **analisi quantitativa** (dati, trend, metriche) è la chiave per comprendere e gestire il futuro di un turismo che nasce dallo schermo ma vive nel mondo reale.

<a href="{{ site.baseurl }}/methodology.html">Metodologia →</a>