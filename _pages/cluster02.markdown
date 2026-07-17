---
layout: default
title: "Cluster: Serie TV italiane"
vega: true
header_type: hero
header_img: assets/images/header.svg
header_title: "Analisi di Cluster: Serie TV italiane"
subtitle: "Le serie televisive a lunga esposizione e i loro territori"
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

  .chart-outer-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

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

Il cluster raccoglie **quattro produzioni seriali italiane**, ciascuna legata a
uno o più territori specifici: il lago di **Braies**, **San Candido** e **San
Vito di Cadore** per _Un passo dal cielo_; **Spoleto** e **Gubbio** per _Don
Matteo_; la Sicilia di **Scicli**, **Ragusa** e **Santa Croce Camerina** per _Il
giovane Montalbano_; **Agliè** per _Elisa di Rivombrosa_.

Il filo conduttore è duplice. Da un lato l'ambientazione italiana e domestica,
lontana dai blockbuster internazionali (i casi Marvel e Twilight del Cluster 1) e
radicata in un immaginario televisivo generalista molto popolare in Italia.
Dall'altro la **longevità narrativa**: _Don Matteo_ trasmesso ininterrottamente
dal 2000, _Un passo dal cielo_ dal 2011 con più stagioni e persino più
ambientazioni nel tempo, _Il giovane Montalbano_ che eredita e prolunga di oltre
vent'anni la storia complessiva del commissario più famoso della fiction
italiana. Fa in parte eccezione _Elisa di Rivombrosa_, andata in onda per sole
due stagioni (2003-2005): la sua "durata" non è nel palinsesto ma nella **memoria
collettiva** — resta uno dei più grandi fenomeni di ascolto della fiction
generalista italiana, capace di ancorare stabilmente Agliè e il Castello ducale
al proprio immaginario.

Questa esposizione prolungata nel tempo — che derivi da anni di messa in onda o
da un'eredità culturale duratura — è la chiave di lettura scelta per analizzare
l'impatto cineturistico di questi territori: l'obiettivo è isolare non un picco
temporaneo, ma un **radicamento strutturale** costruito nel tempo.

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

### Scicli — _Il giovane Montalbano_

Segnale doppio e coerente: i letti extra-alberghieri salgono da 4 a **717 unità**
(2002-2024), con **persistenza piena (1/1)**: l'effetto non si esaurisce in un
picco isolato ma si mantiene stabile nel tempo. Anche gli autobus immatricolati
nel comune confermano la tendenza, con un incremento più contenuto in valore
assoluto (**+11,11%**) ma uno **Zeta Shift più alto (+2,91σ)**.

### Ragusa — _Il giovane Montalbano_

Segnale più moderato ma solido: letti extra-alberghieri arrivati a quasi **4.000
unità**, persistenza piena e **CIS 89,45/100** — secondo miglior punteggio del
gruppo. L'RGR più basso tra le quattro evidenze (**+10,19%**) suggerisce un
effetto reale ma meno pronunciato rispetto al contesto regionale.

### Agliè — _Elisa di Rivombrosa_

Il caso più eclatante in termini di grandezza: Delta **+76,12%**, **CIS più alto
del gruppo (93,33/100)** e un RGR fuori scala (**+229,33%**). È però anche
l'unico a mostrare crepe nella solidità: persistenza a **0,67/1**, contro il
pieno 1/1 degli altri tre.

### Uno sguardo d'insieme

Il quadro che emerge dal confronto è quasi **a due velocità**. Da un lato Scicli
e Ragusa, trainate da _Il giovane Montalbano_, disegnano il profilo più "sano"
del cluster — segnali magari meno appariscenti in termini assoluti, ma coerenti e
persistenti nel tempo su tutti gli indicatori. Dall'altro Agliè si impone come il
numero più grande in assoluto, ma con una solidità statistica più fragile: il
boom del Palazzo Ducale è reale, ma sembra pesare di più su un singolo balzo
iniziale che su una tenuta costante negli anni.

### Un passo dal cielo e Don Matteo

**Nessuna evidenza** tra le 18 selezionate: il segnale ISTAT per queste location
non ha superato le soglie.

<!-- GRAFICI ISTAT -->

<div class="chart-outer-container">
  <div class="chart-container">
    <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster02/s1/rank_19_ev_039_scicli_I67_RICALCOLATO_v3_18.json"></vegachart>
  </div>
  <div class="chart-container">
    <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster02/s1/rank_22_ev_040_scicli_I70_RICALCOLATO_v3_18.json"></vegachart>
  </div>
  <div class="chart-container">
    <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster02/s1/rank_29_ev_041_ragusa_I67_RICALCOLATO_v3_18.json"></vegachart>
  </div>
</div>

### L'ecosistema turistico attorno ai set

Sulle tre location legate a _Un passo dal cielo_, il numero di **attività a
vocazione turistica** (ristoranti, alloggi, negozi di souvenir, ecc.) entro un
raggio di 5 km è cresciuto in modo pressoché continuo lungo tutto l'arco delle
otto stagioni:

- **San Candido** (ambientazione ufficiale, stagioni 1-5): da **22** attività
  turistiche nel 2011 a **197** nel 2026 — quasi 9 volte tanto. Anche i negozi
  "standard" locali sono aumentati, segno di una crescita economica generale del
  territorio, non solo turistica.
- **Braies** (dove sono state girate la maggior parte delle scene): da **21** a
  **105** attività turistiche (5x), con un'accelerazione particolarmente marcata
  negli ultimi anni (da 69 nel 2024 a 105 nel 2026).
- **San Vito di Cadore** (nuova ambientazione dalla 6ª stagione, 2021): da **57** a
  **93** attività turistiche. La crescita più marcata coincide proprio con
  l'arrivo della serie come "nuovo set" a partire dal 2021.

<!-- GRAFICI ECOSYSTEM -->

<div class="chart-outer-container">
  <div class="chart-container">
    <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster02/s1/chart_un_passo_dal_cielo_geo_Braies_Area_ecosystem.json"></vegachart>
  </div>
  <div class="chart-container">
    <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster02/s1/chart_un_passo_dal_cielo_geo_San_Candido_Area_ecosystem.json"></vegachart>
  </div>
  <div class="chart-container">
    <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster02/s1/chart_un_passo_dal_cielo_geo_San_Vito_di_Cadore_Area_ecosystem.json"></vegachart>
  </div>
</div>

<div class="card border-primary mb-4">
  <div class="card-body">
    <h5 class="card-title">📌 Box 1 — La voce di chi il cinema lo vive</h5>
    <p class="card-text">
      <em>Davide Marra, podcaster e appassionato di cinema, racconta un episodio
      diretto legato a una fiction italiana:</em>
    </p>
    <blockquote class="blockquote">
      "Ho avuto modo di intervistare Marco D'Amore e lui mi ha detto proprio questo,
      che in seguito a Gomorra c'è stata una grande mobilitazione in quelle zone di
      Napoli. La serie ha portato tanti turisti e anche un fiorire di attività
      artistiche. Sono stato più volte a Napoli, ho fatto anche degli eventi al
      cinema con Criticoni ed effettivamente questo è un fenomeno interessante da
      analizzare."
    </blockquote>
    <p class="card-text">
      Un riscontro indiretto ma significativo: anche una produzione seriale italiana
      radicata in un territorio specifico può generare un effetto duraturo su turismo
      e tessuto culturale locale, confermando dall'interno del settore quello che i
      dati ISTAT del cluster misurano dall'esterno.
    </p>
  </div>
</div>

---

## Sezione 2 — Racconto dall'alto

<!-- Risponde alla domanda 2: i media offrono riscontri e alimentano il fenomeno? -->

_L'eco dei media: come raccontano i media le località del Cluster 2?_

Se nella Sezione 1 abbiamo visto se il fenomeno lascia un segno nei numeri, qui
vediamo **come i media lo raccontano**. Sono state usate due chiavi di lettura
complementari: l'**evoluzione del sentiment** nel tempo (quanto se ne parla, con
che tono) e la **polarizzazione tematica** (di cosa si parla, e se prevale
l'entusiasmo o la critica).

### Don Matteo — Spoleto, Gubbio

Il racconto mediatico più contenuto e più "pulito" dei tre. Il tema dominante è
l'**Economic Boom** (70 menzioni), seguito da Urban Change (25) e —
sorprendentemente — **il Cine Tourism arriva tardi e resta marginale**: solo 13
menzioni, e non prima del 2020, nonostante la serie sia in onda dal 2000. Le
criticità (Infrastructure Strain, Overtourism) sono quasi assenti: appena 2
menzioni di Overtourism in tutto il periodo, ma fortemente negative (sentiment
-0,75) — un tema minoritario che, quando emerge, emerge male. Economic Boom conta
69 menzioni positive contro appena 1 negativa, e non ci sono critiche vere e
proprie sul fronte turismo/cine-turismo esplicito.

### Un passo dal cielo — Braies, San Candido e San Vito di Cadore

Il quadro opposto e più complesso: **Infrastructure Strain è il secondo tema più
discusso in assoluto (175 menzioni) con sentiment fortemente negativo**, seguito
da Overtourism (138 menzioni); questi due temi critici insieme superano il volume
di Cine Tourism (58 menzioni). Nella polarizzazione il contrasto è netto:
Infrastructure Strain 12 positivi contro **163 negativi**, Overtourism 17 contro
**121 negativi**. È l'unica delle tre produzioni in cui il "costo" del turismo —
sovraffollamento, pressione sulle infrastrutture — è un tema mediatico tanto
forte quanto il beneficio economico.

Questo aspetto è stato riportato anche su _La Repubblica_:

<blockquote class="blockquote">
  "Instagram e la celeberrima serie televisiva
  Rai "Un passo dal cielo" (interpretata da Terence Hill e Daniele Liotti, a cui contribuisce anche la
  Provincia di Bolzano), hanno fatto sì che il pittoresco laghetto di Braies, dove è ambientata, si
  trasformasse, nel giro di pochi anni, da oasi per amanti della tranquillità in caotico punto di ritrovo di
  turisti mordi e fuggi. A fronte di 650 abitanti, a Braies ci sono giornate in cui arrivano 15.000 turisti. E se
  in un anno sono 1,6 milioni le persone che trascorrono un paio d'ore in valle, i pernottamenti sono
  appena 140.000." 
  <footer class="blockquote-footer">
    <a href="https://www.repubblica.it/viaggi/2020/02/11/news/dolomiti_l_overtourism_stritola_il_lago_di_terence_hill_braies_si_dara_delle_regole-248335368/"
     target="_blank" rel="noopener">
      La Repubblica — <cite title="...">Dolomiti: l'overtourism stritola il lago di Terence Hill...</cite>
    </a>
  </footer>
</blockquote>

<div class="chart-outer-container">
  <div class="chart-container">
    <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster02/s2/chart_un_passo_dal_cielo_sentiment_5_polar.json"></vegachart>
  </div>
  <div class="chart-container">
    <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster02/s2/chart_un_passo_dal_cielo_sentiment_2_evolution.json"></vegachart>
  </div>
</div>

### Il giovane Montalbano — località in Sicilia

Qui il **Cine Tourism è protagonista assoluto**: 136 menzioni, di gran lunga il
volume più alto tra le tre produzioni sul tema specifico "turismo legato al film",
con 132 menzioni positive contro solo 4 negative nella polarizzazione. È la
produzione che i media collegano più esplicitamente e più positivamente al
fenomeno cineturistico. Le criticità ci sono (Infrastructure Strain 27 menzioni,
Overtourism 17) ma restano contenute rispetto al volume enorme di narrazione
positiva.
<div class="chart-outer-container">
  <div class="chart-container">
    <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster02/s2/chart_Il_giovane_Montalbano_Sicilia_sentiment_5_polar.json"></vegachart>
  </div>
  <div class="chart-container">
    <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster02/s2/chart_Il_giovane_Montalbano_Sicilia_sentiment_2_evolution.json"></vegachart>
  </div>
</div>

### Uno sguardo d'insieme

Il confronto disegna **tre profili narrativi ben distinti**. _Il giovane
Montalbano_ è la produzione che i media raccontano più esplicitamente come
fenomeno cineturistico: non solo il fenomeno esiste, ma gli articoli lo nominano
e lo celebrano. Nelle località di _Don Matteo_ il fenomeno turistico è presente e
positivo, ma è meno forte come "effetto della serie". _Un passo dal cielo_ è
l'unica in cui il racconto mediatico include sistematicamente il **lato
problematico** del successo turistico: sovraffollamento e pressione
infrastrutturale non sono note a margine, ma temi centrali.

<!-- GRAFICI: sentiment evolution e sentiment polarization per ogni location -->

<!-- <div class="full-width-chart">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster02/s2/name.vl.json"></vegachart>
</div> -->

<div class="card border-primary mb-4">
  <div class="card-body">
    <h5 class="card-title">📌 Box 2 — Quando il cinema sa cosa sta facendo</h5>
    <p class="card-text">
      <em>Alla domanda se chi lavora nel cinema sia consapevole dell'effetto
      turistico di una location, Davide Marra risponde:</em>
    </p>
    <blockquote class="blockquote">
      "In alcuni casi ci sono proprio delle operazioni dichiarate in cui si fanno
      anche delle collaborazioni con enti, regioni in determinate zone per
      valorizzare il territorio; quindi, in certi casi la risposta è assolutamente
      sì. Sono consapevoli e l'intento è proprio quello pubblicitario..."
    </blockquote>
    <p class="card-text">
      Il fenomeno Montalbano conferma questa lettura in modo quasi istituzionale: i
      luoghi nati dalla penna di Andrea Camilleri e dalle riprese Palomar sono
      entrati ufficialmente nel <strong>Registro delle Eredità Immateriali della
      Sicilia (REIS)</strong>, catalogati nel "Libro degli Spazi Simbolici" — la
      sezione che tutela i luoghi legati a eventi storici, tradizioni o entrati
      nella memoria collettiva attraverso opere letterarie e cinematografiche.
      Secondo la definizione UNESCO, le Eredità Immateriali sono l'insieme delle
      pratiche, rappresentazioni, espressioni, conoscenze e tecniche che le comunità
      riconoscono come parte del proprio patrimonio culturale. Non è più solo un
      effetto collaterale della narrazione: è un <strong>riconoscimento
      formale</strong>, deciso dall'Assessorato regionale dei Beni Culturali, che
      certifica quanto il legame tra fiction e territorio sia diventato parte del
      patrimonio riconosciuto della regione.
    </p>
  </div>
</div>

---

## Sezione 3 — Racconto dal basso

Cosa emerge dalle **rilevazioni online** e dalle comunità di utenti: l'attenzione
digitale rivolta al luogo e alla produzione.

_Gli utenti viaggiano per la serie, o la "visitano" da casa?_

La nostra ricerca fin dall'inizio si è chiesta se, accanto ai segnali fisici, si potessero trovare segnali di un "turismo virtuale" descrivibili in generale come **"attenzione digitale"**, immaginando quindi utenti alla ricerca di informazioni in rete prima di visitare una determinata località filmica, o magari senza una reale intenzione di visitarla direttamente.

Questo concetto risulta utile in quanto accomuna tanto indicatori più affermati come Google Trends e Wikipedia, quanto rilevazioni su media e comunità diversi come Reddit e YouTube.

In particolare abbiamo assemblato - mediante pipeline parallele e sequenze strutturate di query - dataset testuali contenenti post Reddit e commenti YouTube relativi alle località filmiche delle produzioni esaminate.

L'analisi testuale dei documenti così raccolti, pur non portando a risultati generalizzabili, ha comunque offerto elementi interessanti sulle serie TV che, grazie a un processo di diffusione mediatica prolungato nel tempo, sembrano generare un seguito attivo che lascia tracce visibili anche in rete.

Vediamo alcuni esempi di questo fenomeno.

**Fonti:** Google Trends, Wikipedia, Reddit, YouTube.

<!-- GRAFICO: Google Trends / pageview Wikipedia -->
<!-- <div class="full-width-chart">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster02/s3/name.vl.json"></vegachart>
</div> -->

<!-- GRAFICO: attenzione Reddit + YouTube -->

<!-- ### Reddit

Commenti per tipologia di turismo dopo l'uscita - Gubbio

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster02/s3/grafico_gubbio_commenti_tipologia_turismo_dopo_uscita_film.json"></vegachart>
</div>

Commenti per tipologia di turismo dopo l'uscita - Spoleto

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster02/s3/grafico_spoleto_commenti_tipologia_turismo_dopo_uscita_film.json"></vegachart>
</div> -->

### YouTube

<div class="chart-outer-container">
  <span>
    Tasso di commenti contenenti un riferimento:
    nei <em>video su produzione e location</em>.
  </span>
  <div class="chart-container">
    <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster02/s3/recap_reference_rate_run1_cluster02.vl.json"></vegachart>
  </div>

  <span>
    Tasso di commenti contenenti un riferimento:
    nei <em>video su sola location</em>.
  </span>
  <div class="chart-container">
    <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster02/s3/recap_reference_rate_run2_cluster02.vl.json"></vegachart>
  </div>
</div>

<div class="chart-outer-container">
  <span>
    Timeline dei commenti contenenti un riferimento:
    nei <em>video su produzione e location</em>.
  </span>
  <div class="chart-container">
    <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster02/s3/timeline_un_passo_dal_cielo_run1.vl.json"></vegachart>
  </div>

  <span>
    Timeline dei commenti contenenti un riferimento:
    nei <em>video su sola location</em>.
  </span>
  <div class="chart-container">
    <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster02/s3/timeline_un_passo_dal_cielo_run1.vl.json"></vegachart>
  </div>
</div>

<!-- <div class="chart-outer-container">
  <span>Timeline dei commenti contenenti un riferimento:
  nei <em>video su produzione e location</em>.</span>
  <div class="chart-container">
    <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster02/s3/timeline_il_giovane_montalbano_run1.vl.json"></vegachart>
  </div>
</div> -->


_Sezione in lavorazione._

---

## In sintesi

<!-- IN PROGRESS: cosa dicono insieme le tre voci per il Cluster 02 -->

_Sezione in lavorazione._

<a href="{{ site.baseurl }}/results.html">← Torna ai Risultati</a>
