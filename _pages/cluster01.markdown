---
layout: default
title: "Cluster 1: Produzioni Internazionali in Italia"
vega: true
header_type: hero
header_img: assets/images/header.svg
header_title: "Analisi di Cluster: Produzioni Internazionali"
subtitle: "L'impatto di blockbuster globali e cult hollywoodiani sui territori italiani"
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

Il cluster raccoglie tre produzioni cinematografiche di risonanza mondiale, ciascuna legata a territori italiani specifici: Crema per **Call Me By Your Name**; Volterra e Montepulciano per **The Twilight Saga: New Moon**; il Forte di Bard e la Valle d'Aosta per **Avengers: Age of Ultron**, a cui si aggiunge il caso anomalo della serie **Curon** (Curon Venosta).

La scelta del nome per questo raggruppamento deriva dalla natura cross-culturale delle opere selezionate: si tratta di produzioni che hanno saputo fondere l'immaginario audiovisivo globale con le radici identitarie, enogastronomiche e storiche dei luoghi, trasformando una visibilità temporanea (il set) in un asset strategico e duraturo per il territorio. L'obiettivo è comprendere come la risonanza internazionale di un film possa ridefinire a lungo termine l'ecosistema turistico ed economico di realtà locali italiane.

<div class="row">
  <div class="col-md-12 text-center">
    <img src="{{site.baseurl}}/assets/images/cluster01/cluster_image.jpg"
         class="img-fluid mx-auto d-block"
         style="margin: 20px 0;"
         alt="Sovraffollamento al Lago di Braies">
  </div>
</div>

---

## Sezione 1 — Il fenomeno

_Il fenomeno esiste, è misurabile? Vediamo i primi numeri._

Le evidenze ISTAT validate (CIS > 0,7, RGR ≥ 0,15) mostrano segnali misurabili in tre delle quattro produzioni del cluster, con intensità molto diverse tra loro. 
L'impatto si adatta perfettamente alla vocazione del territorio: se a Crema l'effetto innesca un'esplosione di arrivi turistici e di visitatori museali, in Valle d'Aosta l'onda d'urto del blockbuster satura e fa esplodere la micro-ricettività (letti extra-alberghieri). Ancor più singolare è il caso di Curon Venosta, dove il fenomeno mediatico ha coinciso con un impatto misurabile persino sull'incidenza della popolazione straniera residente.

### Forte di Bard e Pont-Saint-Martin — _Avengers: Age of Ultron_
Esplosione della micro-ricettività: i **Letti extra-alberghieri** registrano variazioni enormi, con un **+233,33% a Bard** e addirittura un **+333,33% a Pont-Saint-Martin**. Gli scarti storici sono molto marcati (+8,19σ e +27,39σ) e le validazioni RGR confermano che lo shock è puramente locale (+228,47% e +457,64%). Anche i letti alberghieri tradizionali a Bard crescono del +30,14%.

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster01/rank_01_ev_032_pont-saint-martin_I67_RICALCOLATO_v3_18.json"></vegachart>
</div>

### Crema — _Call Me By Your Name_
Segnale eccezionale su più fronti turistici: gli **Arrivi Non Residenti** crescono del **+20,01%** (RGR +30,36%), ma il dato più impressionante riguarda i **Visitatori dei musei**, che segnano un **+114,41%** post-evento (RGR +47,93%). Anche l'Indice di turisticità globale cresce del +32,76% e le Presenze dei non residenti salgono del +30,84%. Il **CIS** si attesta tra l'89,74 e il 100/100 su tutti questi indicatori.


### Curon Venosta — _Curon_
Segnale pieno e coerente su un indicatore demografico e sociale: l'**Incidenza della popolazione straniera residente** cresce del **+27,71%**, con uno **Zeta Shift di +5,68σ** e **persistenza piena (1/1)**. Il **CIS** è **100/100**, e l’RGR raggiunge **+20,79%**.

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster01/rank_23_ev_018_curon-venosta_I06_RICALCOLATO_v3_18.json"></vegachart>
</div>

### Volterra e Montepulciano — _The Twilight Saga: New Moon_
**Nessuna evidenza** ISTAT validata tra gli indicatori selezionati per questa specifica ricerca. Il caso resta centrale nel cluster, ma l’impatto non emerge dai KPI ISTAT utilizzati.

### Uno sguardo d'insieme
Il quadro che emerge dimostra come i blockbuster globali agiscano da shock asimmetrici: non alzano tutti gli indicatori in modo uniforme, ma colpiscono selettivamente l'infrastruttura più esposta (es. B&B in Valle d'Aosta, musei a Crema) alterando in modo mirato l'equilibrio dei luoghi.

### L'ecosistema turistico attorno ai set (OpenStreetMap)
Il tratto più evidente che accomuna le tre produzioni è la profonda alterazione del tessuto commerciale locale. Il CineTourism agisce come un catalizzatore urbano asimmetrico, polarizzando lo sviluppo verso i servizi di accoglienza a discapito delle attività tradizionali.

* **Crema (*Call Me By Your Name*):** L'ecosistema turistico ha registrato un'impennata a ridosso dell'uscita del film (da 13 attività a inizio 2017 a 20 nell'aprile 2018), superando nettamente la crescita dei negozi locali standard.
* **Forte di Bard (*Avengers: Age of Ultron*):** Le location turistiche attive sono esplose, passando da circa 40 unità a fine 2014 a oltre 100 a fine 2015, innescando un trend rialzista ininterrotto che ha superato le 240 unità nel 2026.
* **Montepulciano (*The Twilight Saga: New Moon*):** L'effetto a lungo termine è drastico, con le attività turistiche che passano da zero nel 2007 a oltre 380 all'inizio del 2026, lasciando i negozi di prossimità fermi a quota 99.

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster01/chart_the_twilight_saga_new_moon_geo_Montepulciano_Area_ecosystem.json"></vegachart>
</div>

<div class="card border-primary mb-4">
  <div class="card-body">
    <h5 class="card-title">📌 Box 1 — L'istituzionalizzazione dell'offerta: La mappa di Volterra</h5>
    <p class="card-text">
      L'adattamento dell'ecosistema urbano non avviene solo tramite l'apertura spontanea di nuove attività, ma passa anche attraverso iniziative dirette di destination marketing.
    </p>
    <p class="card-text">
      La mappa tematica ufficiale di <em>New Moon</em> distribuita a Volterra rappresenta un esempio perfetto di come un territorio si adatti proattivamente all'urto mediatico. Sebbene per questa specifica produzione non si registrino picchi anomali nei macro-dati ISTAT, a livello qualitativo l'amministrazione ha sovrapposto in modo ingegnoso la narrazione finzionale alla topografia reale. Strade ed edifici storici (come il <em>vicolo Mazzoni</em> o il <em>Palazzo dei Priori</em>) vengono ri-mappati seguendo le esatte traiettorie dei personaggi (es. <em>"run in the yellow Porsche"</em> o <em>"Bella finds Edward"</em>), trasformando la città da semplice location a uno spazio di "pellegrinaggio" esperienziale che intercetta e capitalizza la devozione dei fan in modo istituzionale.
    </p>
    <div class="text-center mt-4 mb-2">
      <img src="{{site.baseurl}}/assets/images/cluster01/Volterra New Moon Map-images-0.jpg"
           class="img-fluid mx-auto d-block"
           style="border: 1px solid #e5e7eb; border-radius: 12px; padding: 5px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"
           alt="Mappa Turistica New Moon Volterra">
    </div>
  </div>
</div>

---

## Sezione 2 — Racconto dall'alto

_L'eco dei media: come raccontano i media le località del Cluster 1?_

Oltre all'infrastruttura fisica, il cineturismo altera profondamente il modo in cui il territorio viene raccontato dai media e vissuto dalla comunità locale. Qui vediamo come la stampa e le fonti locali inquadrano il fenomeno attraverso l'evoluzione del sentiment nel tempo e l'impatto tematico (le news).

### Crema — _Call Me By Your Name_
**Il Modello "Autoriale/Letterario":** L'attribuzione diretta si diluisce nel tempo; il territorio interiorizza il successo, convertendo l'interesse cinematografico originario in un riposizionamento stabile su altre leve turistiche (enogastronomia, turismo lento, cultura).

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster01/chart_chiamami_col_tuo_nome_news_impact.json"></vegachart>
</div>

### Forte di Bard e Valle d'Aosta — _Avengers: Age of Ultron_
**Il Modello "Blockbuster":** Il nome del film continua a essere citato esplicitamente come asset per la promozione turistica negli anni, mantenendo un legame diretto tra l'opera e l'indotto (evidente nei picchi di menzioni turistiche in concomitanza con la stagione estiva).

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster01/chart_avengers_age_of_ultron_sentiment_3_heatmap.json"></vegachart>
</div>

### Volterra e Montepulciano — _The Twilight Saga: New Moon_
**La dicotomia del sentiment:** L'analisi tematica trasversale della rassegna stampa dimostra che l'iniezione di capitali turistici genera invariabilmente una tensione tra opportunità e pressione comunitaria, visibile nel tracciamento del sentiment nel lungo periodo.

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster01/chart_the_twilight_saga_new_moon_sentiment_2_evolution.json"></vegachart>
</div>

<div class="card border-primary mb-4" style="margin-top: 30px;">
  <div class="card-body">
    <h5 class="card-title">📌 Box 2 — La voce del territorio: Il "Paradosso Volterra" e la difesa del Brand</h5>
    <p class="card-text">
      L'intervista al Consorzio Turistico di Volterra offre una testimonianza diretta di come un territorio debba gestire attivamente l'urto di un blockbuster globale per preservare la propria identità. Emerge quello che possiamo definire il <strong>"Paradosso Volterra/Montepulciano"</strong>: sebbene le riprese di <em>New Moon</em> siano state effettuate fisicamente a Montepulciano, i flussi turistici si sono riversati massicciamente su Volterra. Questo è avvenuto perché i fan erano legati alla matrice letteraria dell'opera e perché il nome "Volterra" proiettato sullo schermo ha funzionato da calamita, specialmente per i turisti stranieri.
    </p>
    <blockquote class="blockquote">
      "La nostra paura che una città come Volterra, che ha una forte identità legata all’arte e alla cultura, si trasformasse nella 'Città dei vampiri'. [...] Questo non è successo perché [...] abbiamo favorito questo aspetto attraverso un’attenta attività di promozione che non ha mai usato la parola 'vampiri' ma piuttosto quella 'Volturi' legando al passato etrusco della città."
    </blockquote>
    <p class="card-text">
      Il Consorzio ha messo in atto una vera e propria <strong>strategia di assimilazione del brand</strong>: ha rifiutato la banalizzazione commerciale (niente "pizze di Edward e Bella") favorendo invece l'artigianato locale, come la produzione di mele e cuori in alabastro. L'integrazione tra fiction e patrimonio reale (i Volturi associati al mistero degli Etruschi, i tour conclusi nelle cisterne romane) ha garantito un turismo di fascia più alta e un effetto <em>long-tail</em> sorprendente: a oltre dieci anni di distanza, i teenager di allora tornano oggi a Volterra con le proprie famiglie.
    </p>
  </div>
</div>

### Uno sguardo d'insieme
Il sentiment associato all'"Economic Boom" registra un andamento fortemente positivo, mentre emerge parallelamente una persistente polarità negativa legata ai temi dell'"Infrastructure Strain" e dell'"Overtourism", sintomo di comunità che faticano a gestire logisticamente il successo mediatico prolungato nel tempo.

---

## Sezione 3 — Racconto dal basso

Cosa emerge dalle **rilevazioni online** e dalle comunità di utenti: l'attenzione digitale rivolta al luogo e alla produzione.

_Gli utenti viaggiano per il film, o la "visitano" da casa?_

L'analisi si chiude esaminando l'impronta digitale lasciata da queste produzioni per misurare il "turismo virtuale" e la curiosità pre-visita.

### Google Trends e Wikipedia
L'interesse digitale si sviluppa su due binari: la ricerca diretta della destinazione e l'approfondimento enciclopedico. Le ricerche geografiche mostrano picchi netti in concomitanza con le uscite cinematografiche, con un interesse che permane stabilizzato su livelli più elevati rispetto alla baseline pre-produzione. Dal lato enciclopedico, la ricerca documentale rivela dinamiche di *long-tail* intergenerazionale, con picchi che ritornano ciclicamente a distanza di anni, trainati dalle riprogrammazioni televisive o dallo streaming.

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster01/crema_trends_chart.json"></vegachart>
</div>

### Reddit
L'analisi delle discussioni sulla piattaforma Reddit permette di osservare la reazione "non filtrata" e gli interessi reali degli utenti a seguito del rilascio di una pellicola.

Prendendo in esame la community e le interazioni relative alla città di Crema dopo l'uscita di *Call Me By Your Name*, i dati estratti (su un campione di 293 commenti) rivelano una transizione fondamentale nell'intento di viaggio del pubblico:
*   Il **Turismo Culturale** domina in modo netto le conversazioni organiche, rappresentando quasi il 27% (esattamente il 26,96%) dei commenti classificati.
*   Il **Cineturismo** allo stato puro si attesta come seconda motivazione di discussione, raccogliendo circa l'11,60% dei commenti.
*   Seguono, con volumi decisamente inferiori, il turismo sportivo e quello balneare/lacuale (attorno al 4,09%), l'enogastronomico (1,36%) e il turismo montano (1,02%).

Questi dati confermano empiricamente l'ipotesi della "Metamorfosi del Brand" descritta nell'analisi delle news: la pellicola internazionale ha funzionato da innesco iniziale per attrarre l'attenzione (Cineturismo), ma la community ha convertito rapidamente questo stimolo in un interesse più profondo e radicato per il patrimonio storico, artistico e architettonico del territorio (Turismo Culturale).

**Post per tipologia di turismo dopo l'uscita di *Call Me By Your Name* - Crema:**
<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster01/grafico_crema_commenti_tipologia_turismo_dopo_uscita_film.json"></vegachart>
</div>

[Link di ritorno a Risultati](results.html)