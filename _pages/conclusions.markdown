---
layout: default
title: "Conclusioni"
vega: true
header_type: hero
header_img: assets/images/header.svg
header_title: "Conclusioni"
subtitle: "Risultati dell'analisi"
---

<style>
  /* ---- Schemi ricorrenti: righe a piena larghezza ---- */
  .pattern-list { margin: 1.8rem 0 2.2rem; }
  .pattern-row {
    display: flex;
    align-items: flex-start;
    gap: 1.4rem;
    border: 1px solid #e6e8eb;
    border-left: 5px solid var(--pat-accent, #2b6cb0);
    border-radius: 6px;
    background: #fff;
    padding: 1.1rem 1.4rem;
    margin-bottom: .9rem;
    transition: box-shadow .2s ease;
  }
  .pattern-row:hover { box-shadow: 0 4px 14px rgba(0,0,0,.07); }
  .pattern-head { flex: 0 0 230px; }
  .pattern-body { flex: 1 1 auto; }
  .pattern-row .pat-title {
    display: block;
    font-size: 1.05rem;
    font-weight: 700;
    color: #1a202c;
    line-height: 1.25;
  }
  .pattern-row .pat-places {
    display: block;
    font-size: .8rem;
    font-style: italic;
    color: var(--pat-accent, #2b6cb0);
    margin-top: .25rem;
    line-height: 1.4;
  }
  .pattern-row p { font-size: .94rem; color: #444; margin: 0; line-height: 1.55; }
  @media (max-width: 767.98px) {
    .pattern-row { flex-direction: column; gap: .6rem; }
    .pattern-head { flex: none; }
  }
  .pat-ok    { --pat-accent: #2f855a; }
  .pat-fisico{ --pat-accent: #c05621; }
  .pat-eco   { --pat-accent: #2b6cb0; }
  .pat-none  { --pat-accent: #718096; }

  /* ---- Osservazioni trasversali ---- */
  .obs-grid { margin: 1.8rem 0 2rem; }
  .obs-card {
    height: 100%;
    border: 1px solid #e6e8eb;
    border-left: 4px solid #2b6cb0;
    border-radius: 6px;
    background: #fff;
    padding: 1.1rem 1.2rem;
  }
  .obs-card .obs-num {
    display: inline-block;
    font-size: .72rem;
    font-weight: 700;
    letter-spacing: .08em;
    color: #2b6cb0;
    text-transform: uppercase;
    margin-bottom: .35rem;
  }
  .obs-card h4 { font-size: 1rem; margin: 0 0 .5rem; line-height: 1.3; }
  .obs-card p { font-size: .9rem; margin: 0; color: #444; line-height: 1.55; }

  /* ---- Modelli di gestione: card ---- */
  .models-grid { margin: 1.8rem 0 2.4rem; }
  .model-card {
    height: 100%;
    display: flex;
    flex-direction: column;
    border: 1px solid #e6e8eb;
    border-top: 5px solid var(--mod-accent, #2b6cb0);
    border-radius: 8px;
    padding: 1.2rem;
    background: #fff;
    transition: box-shadow .2s ease, transform .2s ease;
  }
  .model-card:hover { box-shadow: 0 10px 24px rgba(0,0,0,.10); transform: translateY(-3px); }
  .model-card .mod-kicker {
    font-size: .72rem; font-weight: 700; letter-spacing: .08em;
    text-transform: uppercase; color: var(--mod-accent, #2b6cb0);
  }
  .model-card h4 { font-size: 1.02rem; margin: .35rem 0 .5rem; line-height: 1.3; }
  .model-card p { font-size: .88rem; color: #444; margin: 0; flex-grow: 1; line-height: 1.5; }
  .model-card .mod-place {
    display: block;
    font-size: .78rem;
    font-style: italic;
    color: #8a94a0;
    margin-top: .7rem;
  }
  .mod-1 { --mod-accent: #c05621; }
  .mod-2 { --mod-accent: #2b6cb0; }
  .mod-3 { --mod-accent: #2f855a; }

  /* ---- Numeri in evidenza ---- */
  .facts-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: .8rem;
    margin: 1.6rem 0 2rem;
  }
  @media (max-width: 767.98px) { .facts-grid { grid-template-columns: repeat(2, 1fr); } }
  .fact-card {
    border: 1px solid #1a1a1a;
    border-radius: 4px;
    background: #fff;
    padding: .9rem 1rem;
    text-align: center;
  }
  .fact-num {
    display: block;
    font-size: 1.6rem;
    font-weight: 700;
    line-height: 1;
    color: #1a1a1a;
    margin-bottom: .3rem;
  }
  .fact-label { display: block; font-size: .78rem; color: #666; line-height: 1.35; }

  /* ---- Box informativi ---- */
  .note-box {
    border-left: 4px solid #2b6cb0;
    background: #f4f8fc;
    padding: 1rem 1.2rem;
    border-radius: 4px;
    margin: 1.6rem 0;
  }
  .note-box .note-title { font-weight: 700; display: block; margin-bottom: .3rem; color: #24487e; }
  .note-box .note-title i { margin-right: .4rem; }
  .note-box.note-warning { border-left-color: #d69e2e; background: #fffaf0; }
  .note-box.note-warning .note-title { color: #92400e; }

  /* ---- Grafici ----
     Il contenitore gestisce lo spazio; il grafico NON viene scalato via CSS
     (scalare svg/canvas sposta le coordinate e rompe hover e tooltip). */
  .chart-container {
    width: 100%;
    max-width: 1200px;
    margin: 40px auto;
    padding: 0 20px;
    box-sizing: border-box;
    overflow-x: auto;   /* se il grafico è più largo, si scorre */
  }
  .chart-container vegachart,
  .chart-container .vega-embed {
    display: flex;
    justify-content: center;
    justify-content: safe center;  /* se sborda, allinea a sinistra invece di tagliare */
    width: 100%;
  }
  .chart-caption {
    display: block;
    width: 100%;
    max-width: 1200px;
    margin: 26px auto -20px;
    padding: 0 20px;
    box-sizing: border-box;
    font-size: 1rem;
    font-weight: 600;
    line-height: 1.4;
    color: #1a202c;
  }

  .section-rule { border: 0; border-top: 1px solid #e6e8eb; margin: 3rem 0 2rem; }
  .page-links { display: flex; flex-direction: column; gap: .6rem; }
  .page-links a { font-weight: 600; }
</style>

## I risultati in sintesi

Il confronto tra le **dodici produzioni** analizzate restituisce un quadro tutt'altro che uniforme, ma attraversato da alcuni schemi ricorrenti.

Nella maggior parte dei casi in cui il territorio mostra un'evidenza **ISTAT** solida — Crema, Pienza, Castellabate, Curon Venosta e le location siciliane di _Montalbano_ e valdostane di _Avengers_ — il segnale digitale si muove nella stessa direzione, con toni prevalentemente positivi e una rassegna stampa che parla di crescita economica e destagionalizzazione. In particolare, nei casi con dati Google Trends e Wikipedia disponibili (Crema, Castellabate) si registrano **rotture di interesse permanenti**, non picchi effimeri, anche se con andamenti diversi nel tempo: a Crema l'interesse si è stabilizzato su un nuovo livello costante, mentre a Castellabate resta forte ma marcatamente stagionalizzato. Negli altri casi, tuttavia, l'entusiasmo convive con tensioni latenti: a Pienza come a Curon Venosta emergono col tempo temi di pressione infrastrutturale che accompagnano il successo senza ancora comprometterlo.

<div class="pattern-list">

  <div class="pattern-row pat-ok">
    <div class="pattern-head">
      <span class="pat-title">Segnali convergenti</span>
      <span class="pat-places">Crema · Pienza · Castellabate · Curon Venosta · location siciliane di Montalbano · location valdostane di Avengers</span>
    </div>
    <div class="pattern-body">
      <p>Evidenza ISTAT solida <strong>e</strong> conversazione digitale che si muove nella stessa direzione, con toni prevalentemente positivi. Dove disponibili, Google Trends e Wikipedia mostrano rotture di interesse permanenti anziché picchi effimeri.</p>
    </div>
  </div>

  <div class="pattern-row pat-fisico">
    <div class="pattern-head">
      <span class="pat-title">Impatto senza rumore</span>
      <span class="pat-places">Agliè · Aosta</span>
    </div>
    <div class="pattern-body">
      <p>Due casi rovesciano l'aspettativa: il territorio mostra un impatto fisico reale e misurabile, ma la conversazione digitale non lo intercetta affatto. Un impatto che <strong>esiste senza fare rumore online</strong>.</p>
    </div>
  </div>

  <div class="pattern-row pat-eco">
    <div class="pattern-head">
      <span class="pat-title">Eco senza riscontro istituzionale</span>
      <span class="pat-places">Volterra e Montepulciano · Opi e Pescasseroli · Braies e San Candido</span>
    </div>
    <div class="pattern-body">
      <p>Segnale digitale evidente senza un riscontro ISTAT altrettanto netto, seppur con un'<strong>evidenza territoriale esplorativa</strong> rilevata su OpenStreetMap.</p>
    </div>
  </div>

  <div class="pattern-row pat-none">
    <div class="pattern-head">
      <span class="pat-title">Nessuna evidenza territoriale</span>
      <span class="pat-places">Spoleto e Gubbio</span>
    </div>
    <div class="pattern-body">
      <p>I casi più estremi: nessun riscontro sul territorio, <strong>nemmeno su OpenStreetMap</strong>.</p>
    </div>
  </div>

</div>

<div class="note-box note-warning">
  <span class="note-title"><i class="fas fa-exclamation-triangle" aria-hidden="true"></i>Il caso più critico</span>
  Resta quello delle <strong>location dolomitiche</strong> di <em>Un passo dal cielo</em>, dove la narrazione mediatica sull'overtourism supera in volume quella sul cineturismo stesso.
</div>

<hr class="section-rule">

## Mappatura delle evidenze di cineturismo

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/conclusions/evoluzione_temporale_cineturismo.json"></vegachart>
</div>

Il primo grafico mostra l'**evoluzione temporale dell'impatto cineturistico complessivo** — evidenza territoriale e digitale combinate in un unico punteggio — rispetto all'anno di uscita di ciascuna opera, distinguendo produzioni internazionali, serie TV italiane e altre produzioni italiane.

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/conclusions/conclusioni_mappatura_cineturismo.json"></vegachart>
</div>

Il secondo grafico mappa invece le dodici produzioni lungo **due assi graduati**: sull'asse orizzontale l'ampiezza delle **evidenze territoriali**, dall'assenza di segnale fino alla conferma su più macro-aree ISTAT/MiBACT; sull'asse verticale la maturità delle **evidenze digitali**, dall'assenza fino alla combinazione più completa di rassegna stampa, ricerche online e conversazione spontanea su piattaforme come YouTube o Reddit.

<div class="note-box">
  <span class="note-title"><i class="fas fa-map-signs" aria-hidden="true"></i>Come leggere la mappa</span>
  La <strong>forma</strong> del punto indica il tipo di produzione — cerchio per le produzioni internazionali, quadrato per le serie TV italiane, triangolo per le altre produzioni italiane. Il <strong>colore</strong> rappresenta il tono prevalente del racconto digitale. L'<strong>alone</strong> segnala i casi in cui il dato ISTAT/MiBACT trova conferma incrociata anche su OpenStreetMap.
</div>

### Tre osservazioni trasversali

<div class="row obs-grid">
  <div class="col-md-4 mb-4">
    <div class="obs-card">
      <span class="obs-num">Osservazione 01</span>
      <h4>L'anno di uscita conta</h4>
      <p>Le produzioni troppo recenti o troppo datate mostrano un punteggio di impatto complessivo più basso, mentre il massimo si concentra sugli anni intermedi. È un limite <strong>più metodologico che sostanziale</strong>, legato alla finestra temporale in cui esistono dati sia ISTAT/MiBACT sia digitali comparabili.</p>
    </div>
  </div>
  <div class="col-md-4 mb-4">
    <div class="obs-card">
      <span class="obs-num">Osservazione 02</span>
      <h4>Senza territorio, niente toni positivi</h4>
      <p>Le produzioni prive di evidenze territoriali istituzionali (ISTAT/MiBACT) ottengono <strong>sempre un tono neutro o negativo</strong>, mai positivo.</p>
    </div>
  </div>
  <div class="col-md-4 mb-4">
    <div class="obs-card">
      <span class="obs-num">Osservazione 03</span>
      <h4>Il tipo di produzione non basta</h4>
      <p>La tipologia non spiega il profilo di impatto: produzioni internazionali come <em>Call Me by Your Name</em> e <em>The Twilight Saga: New Moon</em> occupano posizioni distanti fra loro, così come, tra le serie italiane, <em>Il giovane Montalbano</em> e <em>Don Matteo</em>.</p>
    </div>
  </div>
</div>

<div class="note-box">
  <span class="note-title"><i class="fas fa-lightbulb" aria-hidden="true"></i>La conseguenza</span>
  Non è il <em>tipo</em> di produzione a determinare se un'opera avrà un impatto cineturistico sul luogo, ma piuttosto <strong>come quel fenomeno viene gestito</strong> una volta innescato. È a questa gestione, e ai modelli che i casi analizzati suggeriscono, che dedichiamo la prossima sezione.
</div>

<hr class="section-rule">

## Raccomandazioni e modelli di gestione del fenomeno

Dai casi analizzati emergono **tre modelli** di risposta al fenomeno cineturistico, distinti per grado di intervento e per soggetto che lo promuove.

<div class="row models-grid">
  <div class="col-md-4 mb-4">
    <div class="model-card mod-1">
      <span class="mod-kicker">Modello 01</span>
      <h4>Contenimento dell'overtourism</h4>
      <p>Gestire i flussi senza vietarli, redistribuendo la pressione verso orari e modalità più sostenibili.</p>
      <span class="mod-place">Braies</span>
    </div>
  </div>
  <div class="col-md-4 mb-4">
    <div class="model-card mod-2">
      <span class="mod-kicker">Modello 02</span>
      <h4>Valorizzazione identitaria attiva e istituzionalizzazione</h4>
      <p>Governare la narrazione mentre il fenomeno è in corso, poi consolidarla a livello formale perché sopravviva al ciclo di popolarità dell'opera.</p>
      <span class="mod-place">Volterra · location de Il giovane Montalbano</span>
    </div>
  </div>
  <div class="col-md-4 mb-4">
    <div class="model-card mod-3">
      <span class="mod-kicker">Modello 03</span>
      <h4>Valorizzazione dal basso e comunitaria</h4>
      <p>Riconoscere e sostenere le iniziative organiche già nate sul territorio, senza gestirle dall'alto.</p>
      <span class="mod-place">Crema</span>
    </div>
  </div>
</div>

### Contenimento dell'overtourism — modello Braies

Nella mappatura, le location di _Un passo dal cielo_ sono l'unico caso a combinare un'evidenza territoriale **solo esplorativa** (rilevata su OpenStreetMap e non confermata da ISTAT/MiBACT) con un segnale digitale forte ma **di segno negativo**: la combinazione più critica dell'intera mappa.

Il **Tourismusverein Pragser Tal** (Associazione Turistica della Valle di Braies) aggiunge un tassello importante su chi è oggi il visitatore tipo: il turista **Instagram e TikTok-driven**, che ha sostituito il cineturista "puro" — il fan della serie — ormai in netto calo. Questa dinamica ha trasformato radicalmente il lago di Braies, convertendolo da riserva di tranquillità in una meta d'attrazione rapida, esposta a flussi turistici sempre più "mordi e fuggi".

L'articolo de _La Repubblica_ quantifica questo costo in modo netto:

<div class="facts-grid">
  <div class="fact-card">
    <span class="fact-num">650</span>
    <span class="fact-label">abitanti</span>
  </div>
  <div class="fact-card">
    <span class="fact-num">15.000</span>
    <span class="fact-label">turisti al giorno nelle punte</span>
  </div>
  <div class="fact-card">
    <span class="fact-num">1,6 mln</span>
    <span class="fact-label">visitatori annui</span>
  </div>
  <div class="fact-card">
    <span class="fact-num">140.000</span>
    <span class="fact-label">pernottamenti</span>
  </div>
</div>

È il caso da manuale di **turismo di passaggio**: pesa sulle infrastrutture senza generare ricadute economiche proporzionali.

<div class="note-box">
  <span class="note-title"><i class="fas fa-ticket-alt" aria-hidden="true"></i>La risposta del territorio</span>
  Nell'estate 2025 l'amministrazione comunale ha introdotto un sistema di <strong>accesso a prenotazione obbligatoria</strong> per auto, moto, camper e bus, tra le 9:30 e le 16:00, con ticket a pagamento. Fuori da questa fascia l'accesso resta libero, ma con parcheggio a pagamento.
</div>

È un esempio di come sia possibile gestire i flussi senza vietarli. Resta però aperta la sfida di fondo, che il solo contenimento degli accessi non può risolvere: **convertire il turismo "usa e getta" in soggiorno prolungato**, valorizzando l'intera Alta Pusteria anziché il singolo scatto al lago.

### Valorizzazione identitaria attiva e istituzionalizzazione — modello Volterra e location de Il giovane Montalbano

Nella mappatura, **Volterra e Montepulciano** occupano una posizione intermedia su entrambi gli assi — evidenza territoriale esplorativa (solo su dati OSM) e segnale digitale limitato alla sola stampa online — mentre le **location de _Il giovane Montalbano_** si collocano quasi al vertice opposto, con evidenze territoriali confermate su più macro-aree e un segnale digitale più forte.

A raccontare la gestione del fenomeno è prima di tutto Volterra: la testimonianza diretta del **Consorzio Turistico di Volterra Valdicecina** rappresenta il cuore di questa raccomandazione. Di fronte all'urto di un blockbuster globale, la prima preoccupazione del territorio non è stata cavalcare il fenomeno, ma **governarlo**: da qui il rifiuto esplicito dell'etichetta "città dei vampiri" e l'aggancio dei Volturi al mito etrusco preesistente — un popolo già percepito come "misterioso", e quindi naturalmente compatibile con l'immaginario della saga.

Questo approccio narrativo ha avuto una traduzione fisica e istituzionale concreta: l'amministrazione ha realizzato e distribuito una **mappa tematica ufficiale** di _New Moon_, che sovrappone la topografia reale della città alle traiettorie esatte dei personaggi e alle scene chiave del film.

Il modello operativo che ne emerge è duplice: usare il film come **"imbuto" verso il patrimonio culturale e storico preesistente** — evitando che la finzione sostituisca l'identità del luogo — e tradurre questa scelta in strumenti concreti, come la mappa ufficiale, che la rendano immediatamente fruibile e capitalizzabile.

Le location de _Il giovane Montalbano_ portano questa logica di istituzionalizzazione ancora più avanti: non solo una mappa o un tour promozionale, ma un vero e proprio **riconoscimento patrimoniale formale**. I luoghi legati al fenomeno Montalbano sono entrati nel **Registro delle Eredità Immateriali della Sicilia**, all'interno del "Libro degli Spazi Simbolici", certificati dall'Assessorato regionale dei Beni Culturali come parte integrante dell'identità della regione.

<div class="note-box">
  <span class="note-title"><i class="fas fa-arrow-right" aria-hidden="true"></i>Due tempi dello stesso modello</span>
  Se <strong>Volterra</strong> dimostra come governare la narrazione <em>mentre</em> il fenomeno è in corso, il <strong>caso siciliano</strong> mostra il passo successivo: consolidare il cineturismo a livello istituzionale affinché sopravviva al naturale ciclo di popolarità dell'opera audiovisiva.
</div>

### Valorizzazione dal basso e comunitaria — modello Crema

Non è un caso che _Call Me by Your Name_ occupi il **punto più alto della mappatura su entrambi gli assi**. È l'unica produzione a raggiungere il livello massimo di maturità digitale — rassegna stampa, ricerche online e conversazione spontanea insieme — affiancato da un'evidenza territoriale pienamente confermata.

Dietro questo risultato possiamo individuare un terzo modello, diverso dai precedenti, che sono tutti *top-down* e istituzionali: l'**Elio & Oliver Love Tour** è un'iniziativa nata spontaneamente dal passaparola dei fan (Gary Potter, da turista a co-fondatore della guida), oggi capace di accogliere centinaia di persone.

La raccomandazione qui è diversa in natura: le istituzioni non devono per forza "gestire dall'alto". A volte il compito più utile è **riconoscere, sostenere e non ostacolare** iniziative organiche già nate sul territorio.

<hr class="section-rule">

## Riflessioni e prospettive

Il cineturismo è un fenomeno ampiamente raccontato a livello descrittivo, ma qui si è rivelato **difficile da misurare con rigore** proprio perché trasversale: attraversa dati turistici ufficiali, ecosistemi di servizi, narrazione mediatica e conversazione online, senza che nessuna fonte da sola lo catturi per intero — e con una profondità di dettaglio qualitativo che, come visto, non è omogenea tra tutti i casi.

<div class="note-box note-warning">
  <span class="note-title"><i class="fas fa-exclamation-triangle" aria-hidden="true"></i>Il limite principale</span>
  Il campione è ridotto e non generalizzabile statisticamente: le conclusioni vanno lette come indicazioni sui singoli casi studio, non come misure estendibili al fenomeno nel suo complesso.
</div>

La **pipeline metodologica** costruita — l'integrazione di ISTAT, OpenStreetMap, rassegna stampa e piattaforme digitali — è però replicabile, e apre la strada a un'estensione futura ad altri casi studio.

<hr class="section-rule">

<div class="page-links">
  <a href="{{ site.baseurl }}/methodology.html">Metodologia →</a>
  <a href="{{ site.baseurl }}/results.html">Risultati →</a>
</div>
