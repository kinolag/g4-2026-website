---
layout: default
title: "Cluster: Produzioni Internazionali in Italia"
vega: true
header_type: hero
header_img: assets/images/header.svg
header_title: "Analisi di Cluster: Produzioni Internazionali"
---

<style>
  /* 1. Forza il contenitore ad allargarsi per tutto lo schermo (Viewport Width) */
  .full-width-chart {
    width: 100vw;
    position: relative;
    left: 50%;
    right: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
    margin-top: 40px;
    margin-bottom: 50px;
    padding: 0 5vw; /* Lascia un piccolo margine ai lati dello schermo */
    box-sizing: border-box;
  }

  /* 2. Impedisce ai temi Jekyll di "stirare" verticalmente il grafico */
  .full-width-chart vegachart,
  .full-width-chart .vega-embed {
    width: 100% !important;
    display: block !important;
  }
  
  .full-width-chart canvas, 
  .full-width-chart svg {
    width: 100% !important;
    height: auto !important; /* RISOLVE L'EFFETTO STIRATO VERTICALE */
    max-height: 700px; /* Evita che su schermi giganti diventi troppo alto */
    object-fit: contain !important;
  }
</style>

## Introduzione e Metodologia
Il presente report analizza un cluster specifico all'interno del più ampio progetto **CineTourism**. Tale cluster si concentra su produzioni di natura internazionale che hanno scelto il territorio italiano come set cinematografico: *Call Me By Your Name* (Crema), *Avengers: Age of Ultron* (Valle d'Aosta) e *The Twilight Saga: New Moon* (Volterra e Montepulciano).

La scelta del nome per questo raggruppamento deriva dalla natura cross-culturale delle opere selezionate: si tratta di produzioni che hanno saputo fondere l'immaginario audiovisivo globale con le radici identitarie, enogastronomiche e storiche dei luoghi, trasformando una visibilità temporanea (il set) in un asset strategico e duraturo per il territorio. L'obiettivo è comprendere come la risonanza internazionale di un film possa ridefinire a lungo termine l'ecosistema turistico ed economico di realtà locali italiane.

---

## 1. Il Cambiamento Fisico: Ecosistema, Ricettività ed Esperienza sul Campo

L'impatto di una produzione internazionale si manifesta in primo luogo sul tessuto strutturale e commerciale del territorio ospitante.

### A. Iper-Accelerazione Asimmetrica dell'Ecosistema Turistico (OpenStreetMap)
Il tratto più evidente che accomuna le tre produzioni è la profonda alterazione del tessuto commerciale locale. Il CineTourism agisce come un catalizzatore urbano asimmetrico, polarizzando lo sviluppo verso i servizi di accoglienza a discapito delle attività tradizionali.

* **Crema (*Call Me By Your Name*):** L'ecosistema turistico ha registrato un'impennata a ridosso dell'uscita del film (da 13 attività a inizio 2017 a 20 nell'aprile 2018), superando nettamente la crescita dei negozi locali standard.
* **Forte di Bard (*Avengers: Age of Ultron*):** Le location turistiche attive sono esplose, passando da circa 40 unità a fine 2014 a oltre 100 a fine 2015, innescando un trend rialzista ininterrotto che ha superato le 240 unità nel 2026.
* **Montepulciano (*The Twilight Saga: New Moon*):** L'effetto a lungo termine è drastico, con le attività turistiche che passano da zero nel 2007 a oltre 380 all'inizio del 2026, lasciando i negozi di prossimità fermi a quota 99.

<div class="full-width-chart">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/chart_chiamami_col_tuo_nome_geo_Crema_Area_ecosystem.json"></vegachart>
</div>

<div class="full-width-chart">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/chart_avengers_age_of_ultron_geo_Forte_di_Bard_Area_ecosystem.json"></vegachart>
</div>

<div class="full-width-chart">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/chart_the_twilight_saga_new_moon_geo_Montepulciano_Area_ecosystem.json"></vegachart>
</div>

### B. Adattamento della Capacità Ricettiva (Dati ISTAT)
Per misurare concretamente la risposta territoriale, i dati ISTAT sulla capacità ricettiva del Forte di Bard rivelano come l'offerta si modifichi per assorbire l'urto dei nuovi flussi. La disponibilità di posti letto — differenziata tra strutture alberghiere classiche e soluzioni extra-alberghiere (come i B&B e le locazioni brevi) — mostra un adattamento immediato a partire dall'inizio delle riprese, evidenziando una progressiva trasformazione dell'economia immobiliare locale a favore dell'ospitalità. 
In particolare, i letti alberghieri hanno registrato una variazione post-evento del +30,14%, mentre i letti extra-alberghieri hanno subìto un'impennata eccezionale del +233,33%.

<div class="full-width-chart">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/rank_17_ev_035_bard_I66_RICALCOLATO_v3_18.json"></vegachart>
</div>

<div class="full-width-chart">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/rank_03_ev_036_bard_I67_RICALCOLATO_v3_18.json"></vegachart>
</div>

### C. L'Offerta Turistica e la Vocazione Internazionale (GetYourGuide)
L'evoluzione dell'ecosistema urbano trova riscontro nell'offerta di tour strutturati. I dati dimostrano il respiro marcatamente globale di questo cluster: il 90.6% degli utenti che prenota esperienze legate ai set cinematografici in Italia proviene dall'estero. Le rilevazioni confermano che l'offerta culturale, amplificata dalle riprese, risulta la prima motivazione di visita degli stranieri in Italia, mantenendo elevati i volumi complessivi di presenze turistiche.

<div class="full-width-chart">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/provenienza_turisti_gyg.json"></vegachart>
</div>

---

## 2. L'Analisi delle News: Metamorfosi del Brand e Impatto Sociale

Oltre all'infrastruttura fisica, il cineturismo altera profondamente il modo in cui il territorio viene raccontato dai media e vissuto dalla comunità locale.

### A. La Dicotomia del Sentiment: Boom Economico vs. Pressione Infrastrutturale
L'analisi tematica della rassegna stampa e dei social locali dimostra che l'iniezione di capitali turistici genera invariabilmente una tensione. Il sentiment associato all'"Economic Boom" registra un andamento fortemente positivo, mentre emerge una persistente polarità negativa legata ai temi dell'"Infrastructure Strain" e dell'"Overtourism", sintomo di comunità che faticano a gestire logisticamente il successo mediatico prolungato nel tempo.

<div class="full-width-chart">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/chart_the_twilight_saga_new_moon_sentiment_2_evolution.json"></vegachart>
</div>

### B. L'Attribuzione del Successo: Esplicita vs. Implicita
Il modo in cui le testate giornalistiche associano il boom turistico all'opera originaria varia radicalmente:
* **Il Modello "Blockbuster" (Avengers):** Il nome del film continua a essere citato esplicitamente come asset per la promozione turistica negli anni, mantenendo un legame diretto tra l'opera e l'indotto.
* **Il Modello "Autoriale/Letterario" (CMBYN):** L'attribuzione diretta si diluisce; il territorio interiorizza il successo, emancipandosi dal film per riposizionarsi stabilmente su altre eccellenze (cultura, turismo lento).

<div class="full-width-chart">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/chart_chiamami_col_tuo_nome_news_impact.json"></vegachart>
</div>

<div class="full-width-chart">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/chart_avengers_age_of_ultron_news_impact.json"></vegachart>
</div>

---

## 3. L'Impatto Digitale: Motori di Ricerca e Community

L'analisi si chiude esaminando l'impronta digitale lasciata da queste produzioni, che si manifesta in cicli di attenzione ben distinti.

### A. Curiosità Geografica e Ricerca (Google Trends vs Wikipedia)
L'interesse digitale si sviluppa su due binari: la ricerca diretta della destinazione e l'approfondimento enciclopedico.
1. **Google Trends:** Le ricerche geografiche mostrano picchi netti in concomitanza con le uscite cinematografiche, con un interesse che permane stabilizzato su livelli più elevati rispetto alla baseline pre-produzione.
2. **Wikipedia:** La ricerca documentale rivela dinamiche di *long-tail* intergenerazionale, con picchi che ritornano ciclicamente a distanza di anni, trainati dalle riprogrammazioni televisive o dallo streaming.

<div class="full-width-chart">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/chart_avengers_age_of_ultron_trends_1_google.json"></vegachart>
</div>

<div class="full-width-chart">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/chart_the_twilight_saga_new_moon_trends_1_google.json"></vegachart>
</div>

<div class="full-width-chart">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/chart_avengers_age_of_ultron_trends_2_wikipedia.json"></vegachart>
</div>

<div class="full-width-chart">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/chart_the_twilight_saga_new_moon_trends_2_wikipedia.json"></vegachart>
</div>

### B. Il Dibattito Organico sulle Community (Reddit)
L'analisi delle discussioni sulla piattaforma Reddit permette di osservare la reazione "non filtrata" e gli interessi reali degli utenti a seguito del rilascio di una pellicola.

Prendendo in esame la community e le interazioni relative alla città di Crema dopo l'uscita di *Call Me By Your Name*, i dati estratti (su un campione di 293 commenti) rivelano una transizione fondamentale nell'intento di viaggio del pubblico:
*   Il **Turismo Culturale** domina in modo netto le conversazioni organiche, rappresentando quasi il 27% (esattamente il 26,96%) dei commenti classificati.
*   Il **Cineturismo** allo stato puro si attesta come seconda motivazione di discussione, raccogliendo circa l'11,6% dei commenti.
*   Seguono, con volumi decisamente inferiori, il turismo sportivo e quello balneare/lacuale (attorno al 4%), l'enogastronomico (1,3%) e il turismo montano (1%).

Questi dati confermano empiricamente l'ipotesi della "Metamorfosi del Brand" descritta nell'analisi delle news: la pellicola internazionale ha funzionato da innesco iniziale per attrarre l'attenzione (Cineturismo), ma la community ha convertito rapidamente questo stimolo in un interesse più profondo e radicato per il patrimonio storico, artistico e architettonico del territorio (Turismo Culturale).

<div class="full-width-chart">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/grafico_crema_commenti_tipologia_turismo_dopo_uscita_film.json"></vegachart>
</div>