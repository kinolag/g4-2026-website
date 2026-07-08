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

## 1. Dinamiche Condivise (Tratti Distintivi del Cluster)

### A. Iper-Accelerazione Asimmetrica dell'Ecosistema Turistico
Il tratto più evidente che accomuna le tre produzioni è la profonda alterazione del tessuto commerciale locale. Il CineTourism agisce come un catalizzatore urbano asimmetrico, polarizzando lo sviluppo verso i servizi di accoglienza a discapito delle attività tradizionali.

* **Crema (*Call Me By Your Name*):** L'ecosistema turistico ha registrato un'impennata a ridosso dell'uscita del film (da 13 attività a inizio 2017 a 20 nell'aprile 2018), superando nettamente la crescita dei negozi locali standard.
* **Forte di Bard (*Avengers: Age of Ultron*):** Le location turistiche attive sono esplose, passando da circa 40 unità a fine 2014 a oltre 100 a fine 2015, innescando un trend rialzista ininterrotto che ha superato le 240 unità nel 2026.
* **Montepulciano (*The Twilight Saga: New Moon*):** L'effetto a lungo termine è drastico, con le attività turistiche che passano da zero nel 2007 a oltre 380 all'inizio del 2026, lasciando i negozi di prossimità fermi a quota 99.

<div style="width: 100%; height: 500px; margin-top: 20px; margin-bottom: 50px; position: relative; clear: both;">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/chart_chiamami_col_tuo_nome_geo_Crema_Area_ecosystem.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>

<div style="width: 100%; height: 500px; margin-top: 20px; margin-bottom: 50px; position: relative; clear: both;">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/chart_avengers_age_of_ultron_geo_Forte_di_Bard_Area_ecosystem.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>

<div style="width: 100%; height: 500px; margin-top: 20px; margin-bottom: 50px; position: relative; clear: both;">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/chart_the_twilight_saga_new_moon_geo_Montepulciano_Area_ecosystem.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>

### B. La Dicotomia del Sentiment: Boom Economico vs. Pressione Infrastrutturale
L'analisi tematica trasversale dimostra che l'iniezione di capitali turistici genera invariabilmente una tensione sociale ed economica all'interno delle comunità ospitanti. 

* Il sentiment associato al "Economic Boom" registra picchi di estrema positività (spesso tra 0.8 e 1.0) guidato dai volumi generati dall'indotto cinematografico.
* Specularmente, i temi "Infrastructure Strain" e "Overtourism" registrano forti polarità negative (fino a -1.0), legate a carenze logistiche e pressioni sui centri storici.

<vegachart schema-url="{{site.baseurl}}/assets/charts/chart_the_twilight_saga_new_moon_sentiment_2_evolution.json"></vegachart>

---

## 2. Varianza Intra-Cluster (Differenze Chiave)

### A. La Metamorfosi del Brand: Attribuzione Esplicita vs. Implicita
Il modo in cui il territorio assorbe la narrativa del film varia radicalmente a seconda della natura dell'opera.

* **Il Modello "Blockbuster" (Avengers):** Il nome del film continua a essere citato esplicitamente come asset per la promozione turistica negli anni, mantenendo un legame diretto tra l'opera e l'indotto (es. picchi espliciti di menzioni turistiche nei mesi estivi).
* **Il Modello "Autoriale/Letterario" (CMBYN e Twilight):** L'attribuzione diretta si diluisce; il territorio interiorizza il successo, convertendo l'interesse cinematografico originario in un riposizionamento stabile su altre leve turistiche (enogastronomia, turismo lento, cultura).

<div style="width: 100%; height: 500px; margin-top: 20px; margin-bottom: 50px; position: relative; clear: both;">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/chart_chiamami_col_tuo_nome_news_impact.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>

<div style="width: 100%; height: 500px; margin-top: 20px; margin-bottom: 50px; position: relative; clear: both;">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/chart_avengers_age_of_ultron_news_impact.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>

### B. Curiosità Digitale (Web Curiosity): Google Trends vs Wikipedia
L'interesse digitale si manifesta in modo diverso se analizziamo le ricerche per parole chiave geografiche (Google Trends) rispetto all'approfondimento enciclopedico (Wikipedia).

1. **Volume Diretto sulle Location (Google Trends):** L'analisi delle ricerche geografiche su Google mostra che le mete, spinte dai film, generano picchi netti in concomitanza con le uscite o gli anniversari, con un interesse stabilizzato su livelli più alti rispetto al periodo pre-produzione.

<div style="width: 100%; height: 500px; margin-top: 20px; margin-bottom: 50px; position: relative; clear: both;">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/chart_avengers_age_of_ultron_trends_1_google.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>

<div style="width: 100%; height: 500px; margin-top: 20px; margin-bottom: 50px; position: relative; clear: both;">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/chart_the_twilight_saga_new_moon_trends_1_google.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>

2. **Ricerca Documentale e Cineturismo Puro (Wikipedia):** L'approfondimento documentale tramite le pagine Wikipedia offre ulteriori chiavi di lettura, mostrando ad esempio una forte ciclicità stagionale estiva per il Forte di Bard e una *long-tail* intergenerazionale per le saghe come Twilight, capace di rigenerare altissimi volumi di ricerca anche a decenni dall'uscita.

<div style="width: 100%; height: 500px; margin-top: 20px; margin-bottom: 50px; position: relative; clear: both;">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/chart_avengers_age_of_ultron_trends_2_wikipedia.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>

<div style="width: 100%; height: 500px; margin-top: 20px; margin-bottom: 50px; position: relative; clear: both;">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/chart_the_twilight_saga_new_moon_trends_2_wikipedia.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>

---

## 3. Dalla Curiosità Digitale alla Presenza Fisica: L'Esperienza sul Campo

L'analisi si completa incrociando l'interesse digitale con l'effettiva presenza fisica sul territorio, valutata attraverso l'offerta di tour strutturati (dati GetYourGuide) e le metriche sui flussi ufficiali (ISTAT).

### Provenienza e Vocazione Internazionale
I dati dimostrano il respiro marcatamente globale di questo cluster cinematografico.
* L'analisi delle recensioni e delle provenienze conferma l'assoluta prevalenza del turismo internazionale, attratto specificamente dal richiamo delle grandi pellicole: il 90.6% degli utenti che prenota queste esperienze proviene dall'estero, contro appena il 9.4% di turisti italiani.
* Le rilevazioni ISTAT confermano che l'offerta culturale, amplificata dalle riprese, risulta la prima motivazione di visita degli stranieri in Italia, mantenendo elevati i volumi complessivi di presenze turistiche anche nei periodi di generale flessione.

<div style="width: 100%; height: 500px; margin-top: 20px; margin-bottom: 50px; position: relative; clear: both;">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/provenienza_turisti_gyg.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>

### Offerta Strutturata e Qualità dell'Esperienza
Le produzioni internazionali hanno dato vita a decine di prodotti turistici strutturati, trasformando la fiction in pacchetti esperienziali reali (es. "Tour sull'Inferno di Dan Brown" a Firenze, "Tour del Padrino" in Sicilia).

* La valutazione del *Sentiment Combinato* (voto + analisi testuale) evidenzia una polarizzazione legata alle aspettative del viaggiatore: i tour ottengono punteggi di assoluta eccellenza (0.8 - 1.0) quando le guide riescono a connettere abilmente la storia reale del luogo con la narrativa del film.
* Di contro, emergono sentiment neutrali o negativi in due casi specifici: disorganizzazione logistica e ritardi (problemi strutturali dei centri minori) e la delusione di una "visita normale" venduta come tour cinematografico ma carente di riferimenti ai luoghi specifici del set.

<div style="width: 100%; height: 600px; margin-top: 20px; margin-bottom: 50px; position: relative; clear: both;">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/sentiment_combinato_recensioni_gyg.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>

<div style="width: 100%; height: 600px; margin-top: 20px; margin-bottom: 50px; position: relative; clear: both;">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/sentiment_medio_per_tour.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>