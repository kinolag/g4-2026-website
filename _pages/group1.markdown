---
layout: default
title: "Gruppo 1: Produzioni Internazionali in Italia"
vega: true
header_type: hero
header_img: assets/images/header.svg
header_title: "Analisi di Gruppo: Produzioni Internazionali"
subtitle: "L'impatto di blockbuster globali e cult hollywoodiani sui territori italiani"
---

<style>
  /* =======================================================
     1. CONTENITORI (Gestiscono lo spazio, non il grafico)
     ======================================================= */

  /* Contenitore Full-Width: esce dai margini e occupa tutto lo schermo */
  .full-width-chart {
    width: 100vw;
    position: relative;
    left: 50%;
    right: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
    margin-top: 40px;
    margin-bottom: 50px;
    padding: 0 5vw; /* Margine di respiro laterale */
    box-sizing: border-box;
  }

  /* Contenitore Standard: centrato con una larghezza massima */
  .chart-container {
    width: 100%;
    max-width: 1000px;
    margin: 40px auto;
    padding: 0 20px;
    box-sizing: border-box;
  }

  /* Outer Container opzionale (se ti serve per incolonnare elementi) */
  .chart-outer-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  /* =======================================================
     2. FIX VEGA (Risolve lo shift dell'hover per entrambi)
     ======================================================= */
  
  /* Diciamo al div contenitore generato da Vega di centrarsi e occupare il 100% */
  .full-width-chart vegachart,
  .full-width-chart .vega-embed,
  .chart-container vegachart,
  .chart-container .vega-embed {
    display: flex;
    justify-content: center;
    width: 100%;
  }

  /* NOTA: Tutte le forzature su 'canvas' e 'svg' sono state volutamente 
     eliminate per non rompere le coordinate dell'hover di Vega. */
</style>

## Panoramica

Il gruppo raccoglie quattro produzioni cinematografiche e seriali di risonanza mondiale, ciascuna legata a territori italiani specifici: Crema per *Call Me By Your Name*; Volterra e Montepulciano per *The Twilight Saga: New Moon*; il Forte di Bard e la Valle d'Aosta per *Avengers: Age of Ultron*; Pienza, Firenze e la Val d'Orcia per la serie internazionale *I Medici*.

La scelta del nome per questo raggruppamento deriva dalla natura cross-culturale delle opere selezionate: si tratta di produzioni che hanno saputo fondere l'immaginario audiovisivo globale con le radici identitarie, enogastronomiche e storiche dei luoghi, trasformando una visibilità temporanea (il set) in un asset strategico e duraturo per il territorio. L'obiettivo è comprendere come la risonanza internazionale di un'opera possa ridefinire a lungo termine l'ecosistema turistico ed economico di realtà locali italiane.

<div class="row">
  <div class="col-md-12 text-center">
    <img src="{{site.baseurl}}/assets/images/group1/cluster_image.png"
         class="img-fluid mx-auto d-block"
         style="margin: 20px 0 5px 0; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"
         alt="Locandine delle produzioni analizzate: Avengers, Call Me By Your Name, I Medici, New Moon">
    <p style="font-size: 0.85em; color: #6c757d; margin-bottom: 40px;">
      <em>
        Locandine promozionali ufficiali. I diritti d'autore appartengono alle rispettive case di produzione: 
        &copy; Marvel Studios / Walt Disney Studios, &copy; Frenesy Film / Sony Pictures, 
        &copy; Lux Vide / Rai Fiction, &copy; Summit Entertainment. <br>
        Immagini utilizzate esclusivamente a scopo analitico, di ricerca e illustrativo ai sensi dell'art. 70 della Legge 633/1941 (Diritto di citazione).
      </em>
    </p>
  </div>
</div>

---

## Sezione 1 — Il fenomeno

_Il fenomeno esiste, è misurabile? Vediamo i primi numeri._

Le evidenze ISTAT validate (CIS > 0,7, RGR ≥ 0,15) mostrano segnali misurabili in tre delle quattro produzioni del gruppo, con intensità molto diverse tra loro. 
L'impatto si adatta perfettamente alla vocazione del territorio: se a Crema l'effetto innesca un'esplosione di arrivi turistici e di visitatori museali, in Valle d'Aosta l'onda d'urto del blockbuster satura e fa esplodere la micro-ricettività (letti extra-alberghieri). Per *I Medici* a Pienza, invece, al boom degli arrivi turistici corrisponde un impatto diretto e inusuale sulla gestione dei servizi urbani, come evidenziato dal balzo della raccolta differenziata.

### Forte di Bard e Pont-Saint-Martin — _Avengers: Age of Ultron_
Esplosione della micro-ricettività: i **Letti extra-alberghieri** registrano variazioni enormi, con un **+233,33% a Bard** e addirittura un **+333,33% a Pont-Saint-Martin**. Gli scarti storici sono molto marcati (+8,19σ e +27,39σ) e le validazioni RGR confermano che lo shock è puramente locale (+228,47% e +457,64%). Anche i letti alberghieri tradizionali a Bard crescono del +30,14%.

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/group1/rank_01_ev_032_pont-saint-martin_I67_RICALCOLATO_v3_18.json"></vegachart>
</div>

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/group1/rank_03_ev_036_bard_I67_RICALCOLATO_v3_18.json"></vegachart>
</div>

### Crema — _Call Me By Your Name_
Segnale eccezionale su più fronti turistici: gli **Arrivi Non Residenti** crescono del **+20,01%** (RGR +30,36%), ma il dato più impressionante riguarda i **Visitatori dei musei**, che segnano un **+114,41%** post-evento (RGR +47,93%). Anche l'Indice di turisticità globale cresce del +32,76% e le Presenze dei non residenti salgono del +30,84%. Il **CIS** si attesta tra l'89,74 e il 100/100 su tutti questi indicatori.


### Pienza — _I Medici_
Segnale di crescita turistica eccezionale: gli **Arrivi Non Residenti** aumentano del **+48,57%** (RGR +31,55%), spingendo l'**Indice di turisticità (arrivi)** a un **+37,60%** (RGR +51,39%). Un dato particolarmente interessante è l'impatto misurabile sui servizi e sulle infrastrutture urbane: la **Raccolta differenziata dei rifiuti urbani** registra infatti un balzo del **+31,11%** (RGR +27,80%), indicando una pressione logistica direttamente proporzionale al nuovo afflusso turistico. Tutti e tre gli indicatori raggiungono un CIS pieno di **100/100**.


### Volterra e Montepulciano — _The Twilight Saga: New Moon_
**Nessuna evidenza** ISTAT validata tra gli indicatori selezionati per questa specifica ricerca. Il caso resta centrale nel gruppo, ma l’impatto non emerge dai KPI ISTAT utilizzati.

### Uno sguardo d'insieme
Il quadro che emerge dimostra come i blockbuster globali agiscano da shock asimmetrici: non alzano tutti gli indicatori in modo uniforme, ma colpiscono selettivamente l'infrastruttura più esposta (es. B&B in Valle d'Aosta, musei a Crema, gestione dei rifiuti a Pienza) alterando in modo mirato l'equilibrio dei luoghi.

### L'ecosistema turistico attorno ai set (OpenStreetMap)
Il tratto più evidente che accomuna queste produzioni è la profonda alterazione del tessuto commerciale locale. Il Cineturismo agisce come un catalizzatore urbano asimmetrico, polarizzando lo sviluppo verso i servizi di accoglienza a discapito delle attività tradizionali.

* **Crema (*Call Me By Your Name*):** L'ecosistema turistico ha registrato un'impennata a ridosso dell'uscita del film (da 13 attività a inizio 2017 a 20 nell'aprile 2018), superando nettamente la crescita dei negozi locali standard.
* **Forte di Bard (*Avengers: Age of Ultron*):** Le location turistiche attive sono esplose, passando da circa 40 unità a fine 2014 a oltre 100 a fine 2015, innescando un trend rialzista ininterrotto che ha superato le 240 unità nel 2026.
* **Montepulciano (*The Twilight Saga: New Moon*):** L'effetto a lungo termine è drastico, con le attività turistiche che passano da zero nel 2007 a oltre 380 all'inizio del 2026, lasciando i negozi di prossimità fermi a quota 99.
* **Pienza (*I Medici*):** La serie contribuisce all'innesco di un'espansione senza sosta dell'infrastruttura di accoglienza. A Pienza l'ecosistema turistico triplica quasi i propri volumi in poco più di dieci anni, passando da 96 location nel 2014 a 290 a inizio 2026, distanziando in modo netto l'evoluzione dei negozi di vicinato (cresciuti più timidamente da 14 a 57).

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/group1/chart_the_twilight_saga_new_moon_geo_Montepulciano_Area_ecosystem.json"></vegachart>
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
      <img src="{{site.baseurl}}/assets/images/group1/Volterra New Moon Map-images-0.jpg"
           class="img-fluid mx-auto d-block"
           style="border: 1px solid #e5e7eb; border-radius: 12px; padding: 5px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);"
           alt="Mappa Turistica New Moon Volterra">
    </div>
  </div>
</div>

---

## Sezione 2 — Racconto dall'alto

_L'eco dei media: come raccontano i media le località del Gruppo 1?_

Oltre all'infrastruttura fisica, il cineturismo altera profondamente il modo in cui il territorio viene raccontato dai media e vissuto dalla comunità locale. Qui vediamo come la stampa e le fonti locali inquadrano il fenomeno attraverso l'evoluzione del sentiment nel tempo e l'impatto tematico (le news).

### Crema — _Call Me By Your Name_
**Il Modello "Autoriale/Letterario":** L'attribuzione diretta si diluisce nel tempo; il territorio interiorizza il successo, convertendo l'interesse cinematografico originario in un riposizionamento stabile su altre leve turistiche (enogastronomia, turismo lento, cultura).

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/group1/chart_chiamami_col_tuo_nome_news_impact.json"></vegachart>
</div>

### Forte di Bard e Valle d'Aosta — _Avengers: Age of Ultron_
**Il Modello "Blockbuster":** Il nome del film continua a essere citato esplicitamente come asset per la promozione turistica negli anni, mantenendo un legame diretto tra l'opera e l'indotto (evidente nei picchi di menzioni turistiche in concomitanza con la stagione estiva).

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/group1/chart_avengers_age_of_ultron_sentiment_3_heatmap.json"></vegachart>
</div>

### Pienza, Firenze e Val d'Orcia — _I Medici_
**Il Modello "Storico-Rinascimentale":** L'analisi tematica della rassegna stampa rivela che il racconto mediatico si appropria del successo internazionale della serie per rafforzare l'identità preesistente delle location. Il tema dell'"Economic Boom" domina con polarità altamente positive, tuttavia la pressione generata dai turisti scatena forti tensioni latenti legate all'"Infrastructure Strain" e all'"Overtourism", sintomi di comunità e paesaggi (come la Val d'Orcia) che faticano a tutelare il proprio ecosistema di fronte alla serialità dell'esposizione.

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/group1/chart_i_medici_toscana_sentiment_3_heatmap.json"></vegachart>
</div>

### Volterra e Montepulciano — _The Twilight Saga: New Moon_
**La dicotomia del sentiment:** L'analisi tematica trasversale della rassegna stampa dimostra che l'iniezione di capitali turistici genera invariabilmente una tensione tra opportunità e pressione comunitaria, visibile nel tracciamento del sentiment nel lungo periodo.

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/group1/chart_the_twilight_saga_new_moon_sentiment_2_evolution.json"></vegachart>
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

L’interesse digitale si sviluppa su due binari: la ricerca diretta della destinazione e l’approfondimento enciclopedico. Le ricerche geografiche mostrano picchi netti in concomitanza con le uscite cinematografiche, con un interesse che permane stabilizzato su livelli più elevati rispetto alla baseline pre-produzione. Dal lato enciclopedico, la ricerca documentale rivela dinamiche di long-tail intergenerazionale, con picchi che ritornano ciclicamente a distanza di anni, trainati dalle riprogrammazioni televisive o dallo streaming.

Per la serie I Medici, i volumi delle ricerche su Wikipedia e Google Trends rivelano una sincronizzazione millimetrica con le tre stagioni (ottobre 2016, ottobre 2018, dicembre 2019). Questo dimostra in modo lampante come la serialità televisiva riesca a rinvigorire ciclicamente e a più riprese l’attenzione globale sia sull’opera stessa che sulle location storiche.

Per quanto riguarda il film *Call Me By Your Name*, i volumi delle ricerche su Google Trends per la città di Crema mostrano una frattura strutturale evidente: partendo da una baseline pre-produzione stagnante intorno a valori di 15-20
, l'interesse subisce una prima impennata in concomitanza con le riprese (2016) e si consolida in modo definitivo con le uscite internazionali e italiane tra la fine del 2017 e l'inizio del 2018. Come visibile nel grafico sottostante, il successo cinematografico non si è limitato a un picco effimero, ma ha innalzato permanentemente l'interesse organico verso la location, stabilizzatosi negli anni successivi in un range nettamente superiore (tra 70 e 100) senza mai tornare ai livelli originari.

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/group1/crema_trends_chart.json"></vegachart>
</div>

### Reddit
L'analisi delle discussioni sulla piattaforma Reddit permette di osservare la reazione "non filtrata" e gli interessi reali degli utenti a seguito del rilascio di una pellicola.

Prendendo in esame la community e le interazioni relative alla città di Crema dopo l'uscita di *Call Me By Your Name*, i dati estratti relativi ai **post** (su un campione di 77 contenuti creati dagli utenti, di cui 12 con un focus turistico esplicito) rivelano chiaramente quale sia l'innesco primario che genera la curiosità del pubblico:
*   Il **Cineturismo** domina in modo netto l'apertura delle conversazioni, rappresentando il motore principale per la ricerca di informazioni sulla destinazione (8 post tematici, pari a circa il 10,4% del campione totale).
*   Il **Turismo Culturale** si attesta come seconda motivazione di discussione, emergendo in circa il 2,6% dei post totali (2 post).
*   Seguono, con volumi residuali, il turismo sportivo e quello balneare/lacuale (attorno all'1,3% ciascuno), mentre risultano assenti riferimenti diretti all'enogastronomia o alla montagna nella fase di creazione dei topic.

Questi dati evidenziano l'enorme forza del "gancio" cinematografico: la pellicola internazionale funziona come la calamita principale (Cineturismo) per catturare l'attenzione del pubblico globale e spingerlo ad avviare proattivamente discussioni sulla città, facendo da apripista indispensabile per la successiva scoperta del patrimonio storico e architettonico locale (Turismo Culturale).

**Post per tipologia di turismo dopo l'uscita di *Call Me By Your Name* - Crema:**
<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/group1/grafico_stacked_crema_post.json"></vegachart>
</div>

<!-- <a href="{{ site.baseurl }}/results.html">← Torna ai Risultati</a> -->