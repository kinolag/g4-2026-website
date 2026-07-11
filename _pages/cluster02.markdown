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
</style>

## Panoramica

Il cluster raccoglie **quattro produzioni seriali italiane**, ciascuna legata a
uno o più territori specifici: il lago di **Braies**, **San Candido** e **San
Vito di Cadore** per *Un passo dal cielo*; **Spoleto** e **Gubbio** per *Don
Matteo*; la Sicilia di **Scicli**, **Ragusa** e **Santa Croce Camerina** per *Il
giovane Montalbano*; **Agliè** per *Elisa di Rivombrosa*.

Il filo conduttore è duplice. Da un lato l'ambientazione italiana e domestica,
lontana dai blockbuster internazionali (i casi Marvel e Twilight del Cluster 1) e
radicata in un immaginario televisivo generalista molto popolare in Italia.
Dall'altro la **longevità narrativa**: *Don Matteo* trasmesso ininterrottamente
dal 2000, *Un passo dal cielo* dal 2011 con più stagioni e persino più
ambientazioni nel tempo, *Il giovane Montalbano* che eredita e prolunga oltre
vent'anni di storia complessiva del commissario più famoso della fiction
italiana. Fa in parte eccezione *Elisa di Rivombrosa*, andata in onda per sole
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

*Il fenomeno esiste, è misurabile? Vediamo i primi numeri.*

Le evidenze **ISTAT** validate (CIS > 0,7, RGR ≥ 0,15) mostrano segnali
misurabili per **due delle quattro produzioni** del cluster, con intensità molto
diverse tra loro.

### Scicli — *Il giovane Montalbano*

Segnale doppio e coerente: i letti extra-alberghieri salgono da 4 a **717 unità**
(2002-2024), Delta **+22,56%**, con **persistenza piena (1/1)** — l'effetto non
si esaurisce in un picco isolato ma si mantiene stabile nel tempo. Anche gli
autobus immatricolati confermano la tendenza, con un incremento più contenuto in
valore assoluto (+11,11%) ma uno **Zeta Shift più alto (+2,91σ)**: pur essendo un
numero piccolo, il cambiamento è statisticamente più marcato rispetto alla storia
di quell'indicatore.

### Ragusa — *Il giovane Montalbano*

Segnale più moderato ma solido: letti extra-alberghieri arrivati a quasi **4.000
unità**, persistenza piena e **CIS 89,45/100** — secondo miglior punteggio del
gruppo. L'RGR più basso tra le quattro evidenze (**+10,19%**) suggerisce un
effetto reale ma meno pronunciato rispetto al contesto regionale.

### Agliè — *Elisa di Rivombrosa*

Il caso più eclatante in termini di grandezza: Delta **+76,12%**, **CIS più alto
del gruppo (93,33/100)** e un RGR fuori scala (**+229,33%**). È però anche
l'unico a mostrare crepe nella solidità: persistenza a **0,67/1** (contro il
pieno 1/1 degli altri tre) e uno **Zeta Shift di +21,12σ**, un valore così
anomalo rispetto al resto (tutti sotto i 3σ) da richiedere una verifica prima di
essere trattato come dato definitivo.

### Un passo dal cielo e Don Matteo

**Nessuna evidenza** tra le 30 selezionate: il segnale ISTAT per queste location
non ha superato le soglie.

### Uno sguardo d'insieme

Il quadro che emerge dal confronto è quasi **a due velocità**. Da un lato Scicli
e Ragusa, trainate da *Il giovane Montalbano*, disegnano il profilo più "sano"
del cluster — segnali magari meno appariscenti in termini assoluti, ma coerenti e
persistenti nel tempo su tutti gli indicatori. Dall'altro Agliè si impone come il
numero più grande in assoluto, ma con una solidità statistica più fragile: il
boom del Palazzo Ducale è reale, ma sembra pesare di più su un singolo balzo
iniziale che su una tenuta costante negli anni.

<!-- GRAFICI ISTAT: <vegachart schema-url="{{ site.baseurl }}/assets/charts/istat_*.json"></vegachart> -->

### L'ecosistema turistico attorno ai set

Sulle tre location legate a *Un passo dal cielo*, il numero di **attività a
vocazione turistica** (ristoranti, alloggi, negozi di souvenir, ecc.) entro un
raggio di 5 km è cresciuto in modo pressoché continuo lungo tutto l'arco delle
otto stagioni:

- **San Candido** (ambientazione ufficiale, stagioni 1-5): da **22** attività
  turistiche nel 2011 a **197** nel 2026 — quasi 9 volte tanto. Anche i negozi
  "standard" locali sono più che triplicati (2 → 64), segno di una crescita
  economica generale del territorio, non solo turistica.
- **Braies** (dove sono state girate la maggior parte delle scene): da **21** a
  **105** attività turistiche (5x), con un'accelerazione particolarmente marcata
  negli ultimi anni (69 nel 2024 → 105 nel 2026).
- **San Vito di Cadore** (nuova ambientazione dalla 6ª stagione, 2021): da **6** a
  **93** attività turistiche — la crescita relativa più alta delle tre
  (**+1450%**), interessante perché coincide proprio con l'arrivo della serie come
  "nuovo set" a partire dal 2021.

<!-- GRAFICI ECOSYSTEM: <vegachart schema-url="{{ site.baseurl }}/assets/charts/ecosystem_*.json"></vegachart> -->

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

*L'eco dei media: come raccontano le località del Cluster 2?*

Se nella Sezione 1 abbiamo visto se il fenomeno lascia un segno nei numeri, qui
vediamo **come i media lo raccontano**. Per ciascuna produzione, due chiavi di
lettura complementari: l'**evoluzione del sentiment** nel tempo (quanto se ne
parla, con che tono) e la **polarizzazione tematica** (di cosa si parla, e se
prevale l'entusiasmo o la critica).

### Don Matteo — Umbria

Il racconto mediatico più contenuto e più "pulito" dei tre. Il tema dominante è
l'**Economic Boom** (71 menzioni, sentiment 0,648), seguito da Urban Change (25)
e — sorprendentemente — **il Cine Tourism arriva tardi e resta marginale**: solo
13 menzioni, e non prima del 2020, nonostante la serie sia in onda dal 2000. Le
criticità (Infrastructure Strain, Overtourism) sono quasi assenti: appena 2
menzioni di Overtourism in tutto il periodo, ma fortemente negative (sentiment
-0,75) — un tema minoritario che, quando emerge, emerge male. Nella
polarizzazione quasi tutto è verde: Economic Boom 69 positivi contro 1 negativo,
zero critiche vere su turismo o cine-turismo esplicito.

### Un passo dal cielo — Trentino-Alto Adige e San Vito di Cadore

Il quadro opposto e più complesso: **Infrastructure Strain è il secondo tema più
discusso in assoluto (177 menzioni) con sentiment fortemente negativo (-0,532)**,
seguito da Overtourism (138 menzioni, -0,382) — questi due temi critici insieme
superano il volume di Cine Tourism (62 menzioni). Anche Urban Change, di solito
positivo altrove, qui è quasi neutro (0,109). Nella polarizzazione il contrasto è
netto: Infrastructure Strain 12 positivi contro **163 negativi**, Overtourism 17
contro **121 negativi**. È l'unica delle produzioni in cui il "costo" del turismo
— sovraffollamento, pressione sulle infrastrutture — è un tema mediatico tanto
forte quanto il beneficio economico.

### Il giovane Montalbano — Sicilia

Qui il **Cine Tourism è protagonista assoluto**: 144 menzioni, sentiment 0,635 —
di gran lunga il volume più alto tra le produzioni sul tema specifico "turismo
legato al film", con 132 menzioni positive contro solo 4 negative. È la
produzione che i media collegano più esplicitamente e più positivamente al
fenomeno cineturistico. Le criticità ci sono (Infrastructure Strain 35 menzioni,
sentiment -0,333; Overtourism 22, -0,356) ma restano contenute rispetto al volume
enorme di narrazione positiva.

### Uno sguardo d'insieme

Il confronto disegna **tre profili narrativi ben distinti**. *Il giovane
Montalbano* è la produzione che i media raccontano più esplicitamente come
fenomeno cineturistico: non solo il fenomeno esiste, ma i giornalisti lo nominano
e lo celebrano (132 menzioni positive di Cine Tourism, il numero più alto in
assoluto). *Don Matteo* è il caso opposto: il fenomeno economico e turistico è
presente e positivo, ma quasi mai raccontato come "effetto della serie" — il
legame resta implicito, il volume di copertura è il più basso e le critiche sono
talmente rare da risultare quasi assenti dal dibattito. *Un passo dal cielo*, la
produzione più longeva (15 anni, 8 stagioni), è l'unica in cui il racconto
mediatico include sistematicamente il **lato problematico** del successo
turistico: sovraffollamento e pressione infrastrutturale non sono note a margine,
ma temi centrali quanto il boom economico stesso.

<!-- GRAFICI: sentiment evolution e sentiment polarization per ogni location -->

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

*Gli utenti viaggiano per la serie, o la "visitano" da casa?*

La nostra ricerca fin dall'inizio si è chiesta se, accanto ai segnali fisici, si potessero trovare segnali di un "turismo virtuale" descrivibili in generale come **"attenzione digitale"**, immaginando quindi utenti alla ricerca di informazioni in rete prima di visitare una determinata località filmica, o magari senza una reale intenzione di visitarla direttamente.

Questo concetto risulta utile in quanto accomuna tanto indicatori più affermati come Google trends e Wikipedia, quanto rilevazioni su media e comunità diversi come Reddit e YouTube.

In particolare abbiamo assemblato - mediante pipeline parallele e sequenze strutturate di query - dataset testuali contenenti post Reddit e commenti YouTube relativi alle località filmiche delle produzioni esaminate.

L'analisi testuale dei documenti così raccolti, pur non portando a risultati generalizzabili, ha comunque offerto elementi interessanti sulle serie TV che, grazie a un processo di diffusione mediatica prolungato nel tempo, sembrano generare un seguito attivo che lascia tracce visibili anche in rete.

Vediamo alcuni esempi di questa fenomeno.

**Fonti:** Google Trends, Wikipedia, Reddit, YouTube.

<!-- GRAFICO: Google Trends / pageview Wikipedia -->
<!-- <div class="full-width-chart">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster02/name.vl.json"></vegachart>
</div> -->

<!-- GRAFICO: attenzione Reddit + YouTube -->

### YouTube

Tasso di commenti contenenti un riferimento:
nei _video su produzione e location_.

<div class="full-width-chart">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster02/recap_reference_rate_run1_cluster02.vl.json"></vegachart>
</div>

Tasso di commenti contenenti un riferimento:
nei _video su sola location_.

<div class="full-width-chart">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster02/recap_reference_rate_run2_cluster02.vl.json"></vegachart>
</div>

<!-- <div class="full-width-chart">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster02/gubbio.vl.json"></vegachart>
</div> -->
<!-- <div class="full-width-chart">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster02/spoleto.vl.json"></vegachart>
</div> -->

*Sezione in lavorazione.*

---

## In sintesi

<!-- IN PROGRESS: cosa dicono insieme le tre voci per il Cluster 02 -->

*Sezione in lavorazione.*

<a href="{{ site.baseurl }}/results.html">← Torna ai Risultati</a>
