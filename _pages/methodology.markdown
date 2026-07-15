---
layout: default
title: "Metodologia"
vega: true
header_type: hero
header_img: assets/images/header.svg
header_title: "Metodologia di Analisi"
subtitle: "Dalla selezione dei casi di studio ai sette filoni di analisi"
---

<style>
  /* ---- Criteri di selezione: card con icona ---- */
  .criteria-grid { margin: 2rem 0 1rem; }
  .criteria-card {
    height: 100%;
    border: 1px solid #e6e8eb;
    border-left: 4px solid #2b6cb0;
    border-radius: 6px;
    padding: 1.1rem 1.2rem;
    background: #fff;
    transition: box-shadow .2s ease, transform .2s ease;
  }
  .criteria-card:hover {
    box-shadow: 0 6px 18px rgba(0,0,0,.08);
    transform: translateY(-2px);
  }
  .criteria-card .crit-num {
    display: inline-block;
    font-size: .72rem;
    font-weight: 700;
    letter-spacing: .08em;
    color: #2b6cb0;
    text-transform: uppercase;
    margin-bottom: .35rem;
  }
  .criteria-card h4 {
    font-size: 1.05rem;
    margin: 0 0 .5rem;
    line-height: 1.3;
  }
  .criteria-card h4 i { color: #2b6cb0; margin-right: .45rem; width: 1.1em; text-align: center; }
  .family-card h4 i   { color: #2b6cb0; margin-right: .45rem; }
  .note-box .note-title i { margin-right: .4rem; }
  .criteria-card p { font-size: .92rem; margin: 0; color: #444; }

  /* box riepilogo (cella libera della griglia 3-2) */
  .criteria-recap {
    background: #f4f8fc;
    border-left-color: #24487e;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  .criteria-recap .recap-list {
    margin: .4rem 0 0;
    padding-left: 1.5rem;
    counter-reset: none;
  }
  .criteria-recap .recap-list li {
    font-size: .95rem;
    font-weight: 600;
    color: #24487e;
    margin-bottom: .75rem;
    line-height: 1.5;
  }
  .criteria-recap .recap-list li:last-child { margin-bottom: 0; }

  /* ---- Nota trasversale (COVID) ---- */
  .note-box {
    border-left: 4px solid #d69e2e;
    background: #fffaf0;
    padding: 1rem 1.2rem;
    border-radius: 4px;
    margin: 1.5rem 0 2rem;
  }
  .note-box .note-title { font-weight: 700; display: block; margin-bottom: .3rem; }

  /* variante informativa (piu' neutra del warning) */
  .note-box.note-info {
    border-left-color: #2b6cb0;
    background: #f4f8fc;
  }
  .note-box.note-info .note-title { color: #24487e; }

  /* ---- Badge famiglia dati (fisico / digitale) ---- */
  .fam-badge {
    display: inline-block;
    font-size: .7rem;
    font-weight: 700;
    letter-spacing: .04em;
    text-transform: uppercase;
    padding: .18rem .5rem;
    border-radius: 3px;
    vertical-align: middle;
    margin-left: .5rem;
  }
  .fam-fisico   { background: #e6f4ea; color: #1e6c3a; }
  .fam-digitale { background: #e8effa; color: #24487e; }
  .fam-misto    { background: #f3ecfa; color: #5a3a86; }

  /* ---- Due famiglie di fonti ---- */
  .family-card {
    height: 100%;
    border-radius: 6px;
    padding: 1.2rem 1.3rem;
    background: #fafbfc;
    border: 1px solid #e6e8eb;
  }
  .family-card h4 { font-size: 1.05rem; margin-top: 0; }
  .family-card ul { margin: .6rem 0 0; padding-left: 1.1rem; font-size: .92rem; }

  /* ---- Cluster: blocchi cliccabili ---- */
  .cluster-grid { margin: 2rem 0; }
  .cluster-card {
    height: 100%;
    display: flex;
    flex-direction: column;
    border: 1px solid #e6e8eb;
    border-top: 5px solid var(--cl-accent, #2b6cb0);
    border-radius: 8px;
    padding: 1.3rem;
    background: #fff;
    transition: box-shadow .2s ease, transform .2s ease;
  }
  .cluster-card:hover {
    box-shadow: 0 10px 24px rgba(0,0,0,.10);
    transform: translateY(-3px);
  }
  .cluster-card .cl-kicker {
    font-size: .72rem; font-weight: 700; letter-spacing: .08em;
    text-transform: uppercase; color: var(--cl-accent, #2b6cb0);
  }
  .cluster-card h4 { font-size: 1.12rem; margin: .35rem 0 .6rem; }
  .cluster-card p  { font-size: .9rem; color: #444; flex-grow: 1; }
  .cluster-card .cl-places { font-size: .85rem; color: #666; font-style: italic; }
  .cluster-card .btn { margin-top: .9rem; align-self: flex-start; }

  .cl-1 { --cl-accent: #c05621; }
  .cl-2 { --cl-accent: #2b6cb0; }
  .cl-3 { --cl-accent: #2f855a; }

  /* ---- Topic monitorati: chip compatti ---- */
  .topic-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);   /* desktop: 3 colonne */
    gap: .6rem;
    margin: 1.4rem 0 1.8rem;
  }
  @media (max-width: 991.98px) {             /* tablet: 2 colonne */
    .topic-grid { grid-template-columns: repeat(2, 1fr); }
  }
  @media (max-width: 767.98px) {             /* mobile: 1 colonna */
    .topic-grid { grid-template-columns: 1fr; }
  }
  .topic-chip {
    border: 1px solid #1a1a1a;
    border-radius: 4px;
    background: #fff;
    padding: .6rem .8rem;
    transition: background .15s ease, color .15s ease;
  }
  .topic-chip:hover { background: #1a1a1a; }
  .topic-chip:hover .topic-name,
  .topic-chip:hover .topic-desc { color: #fff; }
  .topic-name {
    display: block;
    font-weight: 700;
    font-size: .88rem;
    letter-spacing: .02em;
    color: #1a1a1a;
    line-height: 1.25;
  }
  .topic-desc {
    display: block;
    font-size: .78rem;
    color: #666;
    margin-top: .15rem;
    line-height: 1.3;
  }

  /* ---- Componenti del CIS: tre box ---- */
  .cis-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: .9rem;
    margin: 1.4rem 0 1.8rem;
  }
  .cis-card {
    border: 1px solid #1a1a1a;
    border-radius: 4px;
    background: #fff;
    padding: 1rem 1.1rem;
    text-align: center;
  }
  .cis-symbol {
    display: block;
    font-size: 1.7rem;
    font-weight: 700;
    line-height: 1;
    color: #1a1a1a;
    margin-bottom: .45rem;
    font-family: Georgia, "Times New Roman", serif;
  }
  .cis-name {
    display: block;
    font-weight: 700;
    font-size: .92rem;
    color: #1a1a1a;
    margin-bottom: .3rem;
  }
  .cis-desc { display: block; font-size: .82rem; color: #666; line-height: 1.4; }

  .section-rule { border: 0; border-top: 1px solid #e6e8eb; margin: 3rem 0 2rem; }
</style>

## 1. Criteri di Selezione dei Casi Studio

La storia del cinema e della televisione italiana vanta un numero altissimo di produzioni girate sul territorio nazionale: analizzarle tutte non è l'obiettivo di questo progetto. Per costruire un campione gestibile e significativo abbiamo quindi definito **cinque criteri di selezione**, pensati non solo per isolare il segnale cineturistico dal rumore di fondo del turismo tradizionale, ma anche per garantire che ogni caso di studio fosse effettivamente analizzabile con gli strumenti scelti.

In particolare, poiché la metodologia si basa in gran parte sull'analisi del discorso digitale (media, social, sentiment), sono state escluse a monte le produzioni troppo datate: un caso come *Il Padrino*, girato in Sicilia decenni prima dell'esistenza di internet, sarebbe stato impossibile da studiare con questo approccio, indipendentemente dalla sua rilevanza culturale.

<div class="row criteria-grid">
  <div class="col-md-6 col-lg-4 mb-4">
    <div class="criteria-card criteria-recap">
      <span class="crit-num">I cinque criteri</span>
      <ol class="recap-list">
        <li>Copertura geografica</li>
        <li>Dimensione demografica</li>
        <li>Varietà geografica</li>
        <li>Finestra temporale</li>
        <li>Varietà di formato e produzione</li>
      </ol>
    </div>
  </div>
  <div class="col-md-6 col-lg-4 mb-4">
    <div class="criteria-card">
      <span class="crit-num">Criterio 1</span>
      <h4><i class="fas fa-map-marked-alt" aria-hidden="true"></i>Copertura geografica</h4>
      <p>Solo comuni del territorio italiano, per garantire uniformità normativa nei dati ISTAT e confrontabilità diretta con le statistiche nazionali.</p>
    </div>
  </div>
  <div class="col-md-6 col-lg-4 mb-4">
    <div class="criteria-card">
      <span class="crit-num">Criterio 2</span>
      <h4><i class="fas fa-users" aria-hidden="true"></i>Dimensione demografica</h4>
      <p>Popolazione generalmente inferiore a <strong>50.000 abitanti</strong>, perché l'impatto di una singola produzione sia visibile nei dati e non si disperda nel rumore statistico delle grandi città. Fa eccezione <strong>Ragusa</strong> (73.878 ab.), inclusa per la rilevanza del legame con la saga di Montalbano.</p>
    </div>
  </div>
  <div class="col-md-6 col-lg-4 mb-4">
    <div class="criteria-card">
      <span class="crit-num">Criterio 3</span>
      <h4><i class="fas fa-compass" aria-hidden="true"></i>Varietà geografica</h4>
      <p>Copertura equilibrata tra le tre macro-aree del paese (Nord, Centro, Sud), per costruire un portafoglio di casi studio il più eterogeneo possibile.</p>
    </div>
  </div>
  <div class="col-md-6 col-lg-4 mb-4">
    <div class="criteria-card">
      <span class="crit-num">Criterio 4</span>
      <h4><i class="fas fa-calendar-alt" aria-hidden="true"></i>Finestra temporale</h4>
      <p>Produzioni collocate tra il <strong>2010 e il 2024</strong>, intervallo che copre la transizione dalla TV generalista allo streaming multicanale, garantendo sia presenza digitale sufficiente sia copertura ISTAT pre e post-uscita. Vanno contestualizzati i casi di lunga serialità come <em>Don Matteo</em> (dal 2000), <em>The Twilight Saga: New Moon</em> (2009), fuori finestra di un solo anno, e la vera eccezione <em>Elisa di Rivombrosa</em> (2003), inclusa per la sua particolare rilevanza culturale.</p>
    </div>
  </div>
  <div class="col-md-6 col-lg-4 mb-4">
    <div class="criteria-card">
      <span class="crit-num">Criterio 5</span>
      <h4><i class="fas fa-film" aria-hidden="true"></i>Varietà di formato e produzione</h4>
      <p>Il campione include sia film che serie/fiction, sia produzioni internazionali che domestiche, per evitare un quadro parziale legato a un solo tipo di prodotto audiovisivo.</p>
    </div>
  </div>
</div>

<div class="note-box">
  <span class="note-title"><i class="fas fa-exclamation-triangle" aria-hidden="true"></i>Accorgimento trasversale — Effetto COVID-19</span>
  A questi criteri si aggiunge la neutralizzazione dell'effetto COVID-19, con l'esclusione o normalizzazione dei periodi di interruzione forzata dei flussi turistici, che avrebbero altrimenti invalidato qualsiasi confronto temporale sulla crescita della domanda.
</div>

### 1.1 Selezione delle location all'interno di ogni produzione

Un'ulteriore precisazione riguarda non le produzioni in sé, ma le **location** scelte per ognuna di esse. La maggior parte delle produzioni analizzate non è stata girata in un unico luogo, ma ha coinvolto più comuni o addirittura più regioni nel corso delle proprie stagioni e dei periodi di riprese.

Per ogni produzione abbiamo selezionato solo le **location principali** — quelle che ospitano l'ambientazione narrativa portante o una quota sostanziale delle riprese — escludendo deliberatamente comparse marginali o location visibili solo per pochi fotogrammi, prive di un legame narrativo stabile con l'opera.

<hr class="section-rule">

## 2. Esplorazione dei Dati Strutturati (Tentativi Iniziali)

In una fase preliminare, abbiamo testato l'utilizzo di fonti istituzionali per misurare l'impatto reale:

*   **Dati ISTAT sugli arrivi:** pur trattandosi della fonte più diretta e istituzionale, il singolo indicatore si è rivelato da solo insufficiente a certificare l'esistenza di un "effetto cineturismo". In diverse location, infatti, non si osservava un incremento dei flussi abbastanza netto da poter essere isolato con sicurezza dal turismo ordinario. Questa evidenza ha reso necessario estendere l'analisi a un ventaglio più ampio di indicatori e a un focus più marcato sulla componente digitale.
*   **Dati sulla produzione di rifiuti:** si è esplorata la correlazione tra presenze turistiche e tonnellate di rifiuti urbani. Tuttavia, la variabilità stagionale e la mancanza di dati disaggregati per quartiere o area di interesse hanno reso questa metrica insufficiente per definire un nesso causale diretto con il fenomeno del cineturismo.

Nella sezione che segue si spiegherà come si è ovviato a questi limiti.

<hr class="section-rule">

## 3. Le Fonti Adottate e l'Approccio Metodologico Proposto

Il progetto si articola in **sette filoni di analisi**, ciascuno costruito per intercettare una diversa manifestazione del fenomeno cineturistico. Le fonti si dividono in due grandi famiglie:

<div class="row" style="margin: 1.5rem 0;">
  <div class="col-md-6 mb-3">
    <div class="family-card">
      <h4><i class="fas fa-mountain" aria-hidden="true"></i>Dati fisici / territoriali</h4>
      <p style="font-size:.92rem; margin:0; color:#444;">Misurano l'impatto direttamente sul territorio.</p>
      <ul>
        <li>Indicatori ISTAT comunali (CIS/RGR)</li>
        <li>Ecosistema commerciale (OpenStreetMap)</li>
      </ul>
    </div>
  </div>
  <div class="col-md-6 mb-3">
    <div class="family-card">
      <h4><i class="fas fa-comments" aria-hidden="true"></i>Dati digitali</h4>
      <p style="font-size:.92rem; margin:0; color:#444;">Osservano il riflesso nel comportamento e nel discorso online.</p>
      <ul>
        <li>Stampa (sentiment e topic modeling)</li>
        <li>Google Trends e Wikipedia</li>
        <li>YouTube</li>
        <li>Reddit</li>
        <li>GetYourGuide</li>
      </ul>
    </div>
  </div>
</div>

La distinzione non è sempre netta: le recensioni GetYourGuide, ad esempio, sono dati digitali a tutti gli effetti, ma raccontano un'esperienza **fisica realmente vissuta** sul luogo, non un'opinione formata a distanza come può essere un commento Reddit o YouTube.

Di seguito il dettaglio tecnico di ciascun filone.

### 3.1 — Indicatori ISTAT comunali (CIS/RGR) <span class="fam-badge fam-fisico">Fisico</span>

Analisi quantitativa su **82 indicatori socioeconomici comunali** (ISTAT/MiC-MiBACT), estesa oltre i semplici arrivi/presenze per superare i limiti descritti in Sezione 2.

Per ogni coppia comune-indicatore viene calcolato un **Cineturismo Impact Score (CIS)**, indice composito endogeno che combina tre componenti calcolate sulla singola serie storica:

<div class="cis-grid">
  <div class="cis-card">
    <span class="cis-symbol">&Delta;</span>
    <span class="cis-name">Delta</span>
    <span class="cis-desc">Variazione percentuale tra baseline pre-evento e finestra post-evento.</span>
  </div>
  <div class="cis-card">
    <span class="cis-symbol">&sigma;</span>
    <span class="cis-name">Zeta Shift</span>
    <span class="cis-desc">Scostamento standardizzato in &sigma; rispetto alla media storica.</span>
  </div>
  <div class="cis-card">
    <span class="cis-symbol">0&ndash;1</span>
    <span class="cis-name">Persistenza</span>
    <span class="cis-desc">Continuità del segnale nella finestra post-evento (scala 0-1).</span>
  </div>
</div>

Le evidenze con **CIS > 0,7** vengono validate esternamente tramite **Relative Growth Rate (RGR)**, che confronta la crescita del comune con il benchmark della relativa regione, con soglia di accettazione **RGR ≥ 0,15**. Il processo ha prodotto **18 evidenze**.

### 3.2 — Ecosistema commerciale (OpenStreetMap) <span class="fam-badge fam-fisico">Fisico</span>

Analisi geospaziale della trasformazione del tessuto commerciale locale: per ogni location è stata tracciata un'**area circolare di 5 km di raggio**, e i punti di interesse (POI) al suo interno sono stati classificati tramite tag OSM in **ecosistema turistico** (ad esempio, le attività di ristorazione e le strutture ricettive/promozionali) *versus* **tessuto commerciale standard** (ad esempio, supermercati, panetterie, ferramenta).

Il confronto tra le due categorie permette di osservare l'eventuale **adattamento strutturale** della zona all'aumento dei flussi turistici.

### 3.3 — Analisi dell'esposizione mediatica (sentiment e topic modeling) <span class="fam-badge fam-digitale">Digitale</span>

Questa fase mira a quantificare la copertura mediatica e a valutare la percezione pubblica dei territori coinvolti, confrontando i periodi antecedenti e successivi all'uscita della produzione.

L'acquisizione dei dati è avvenuta tramite estrazione massiva (*scraping*) di articoli giornalistici con l'**API di Google News**, su una finestra temporale che va dai due anni precedenti l'uscita dell'opera fino a maggio 2026, con interrogazioni mirate a notizie riguardanti il turismo e l'economia locale delle aree di interesse. Su questo corpus sono stati valutati sia il **volume** di articoli pubblicati nel tempo sia il **tono** generale di ciascun articolo, classificato con un modello di Sentiment Analysis su una scala continua da **-1** (fortemente negativo) a **+1** (fortemente positivo).

Parallelamente, un **topic modeling** tematico ha identificato all'interno dei testi le tematiche più rilevanti, per comprendere quali aspetti dell'impatto territoriale sono stati maggiormente discussi. I topic monitorati sono:

<div class="topic-grid">
  <div class="topic-chip">
    <span class="topic-name">Cine Tourism</span>
    <span class="topic-desc">Turismo cinematografico</span>
  </div>
  <div class="topic-chip">
    <span class="topic-name">Urban Change</span>
    <span class="topic-desc">Cambiamenti del tessuto urbano</span>
  </div>
  <div class="topic-chip">
    <span class="topic-name">Infrastructure Strain</span>
    <span class="topic-desc">Sovraccarico infrastrutturale</span>
  </div>
  <div class="topic-chip">
    <span class="topic-name">Economic Boom</span>
    <span class="topic-desc">Crescita economica</span>
  </div>
  <div class="topic-chip">
    <span class="topic-name">Overtourism</span>
    <span class="topic-desc">Sovraffollamento turistico</span>
  </div>
  <div class="topic-chip">
    <span class="topic-name">Deseasonalization</span>
    <span class="topic-desc">Destagionalizzazione dei flussi</span>
  </div>
</div>

Per ogni topic menzionato all'interno di un articolo è stato inoltre calcolato uno specifico punteggio di sentiment (**ABSA**, *Aspect-Based Sentiment Analysis*), sempre su scala da -1 a +1 — un livello di dettaglio che permette di tracciare l'evoluzione temporale della percezione di ogni singolo fenomeno, indipendentemente dal tono generale dell'articolo in cui compare.

### 3.4 — Google Trends e Wikipedia (interesse informativo e comportamento di ricerca) <span class="fam-badge fam-digitale">Digitale</span>

È stata valutata la risonanza del prodotto audiovisivo sul **comportamento di ricerca online** e sull'interesse informativo generale degli utenti, tramite l'utilizzo combinato dei dati di **Google Trends** e delle visualizzazioni delle pagine **Wikipedia**.

Per ogni produzione sono state identificate le pagine Wikipedia relative alle location di riferimento, da cui è stato estratto lo storico delle visite nel tempo. Le serie storiche così costruite sono state **allineate alle date di rilascio** dell'opera, per quantificare sia i picchi di traffico immediati sia l'andamento dell'interesse digitale generato nel tempo.

### 3.5 — YouTube (rilevamento della presenza della produzione nei commenti) <span class="fam-badge fam-digitale">Digitale</span>

L'obiettivo di questo filone è verificare se, e quanto, la presenza di una produzione su YouTube si rifletta effettivamente nei **commenti ai video girati nelle sue location**.

La pipeline è partita dalla ricerca dei video tramite **YouTube Data API v3**, seguita dalla raccolta dei commenti e delle relative risposte. Sono stati messi a confronto i risultati emersi da **due query diverse**: "produzione + location" e "location".

I testi sono stati poi ripuliti — rimozione di URL, emoji e contenuti vuoti, deduplicazione — prima di passare a una fase di **lexical matching, embedding e scoring** che ha permesso di rilevare le menzioni della produzione all'interno dei commenti. I risultati sono stati infine aggregati sia per produzione che per location, per rendere confrontabili i due approcci di ricerca.

È importante specificare che il metodo **confronta due strategie di ricerca tra loro**, ma non dimostra di per sé un nesso causale tra la produzione e l'attenzione generata sul luogo.

### 3.6 — Reddit (analisi del discorso della community) <span class="fam-badge fam-digitale">Digitale</span>

La raccolta dati è stata condotta tramite l'**API PullPush**, con query mirate per produzione e location sui 12 casi studio, concentrandosi su subreddit popolari generici e sui principali subreddit dedicati al turismo e ai consigli di viaggio.

Il volume grezzo estratto era molto rumoroso, e ha richiesto una **pipeline di pulizia a tre stadi** — filtri regex, poi un *bi-encoder*, infine un *cross-encoder* — per isolare i contenuti effettivamente pertinenti.

Dopo la pulizia dei dati è iniziata una prima analisi esplorativa dedicata alla validazione di una **finestra temporale di 3 anni pre/post uscita**: solo **5 produzioni su 12** disponevano di dati sufficienti per un confronto in questo arco temporale. Per queste produzioni sono state condotte analisi descrittive (volumi e lingua della discussione).

Successivamente si è proseguito con la **classificazione** dei post e dei commenti dell'intero corpus raccolto. Usando il modello `moritz-laurer/mDeBERTa` (*zero-shot classification*) sono state distinte 6 etichette corrispondenti a sei tipologie di turismo. Di queste, l'etichetta "Cineturismo" è stata la meno accurata, per cui i risultati sono stati affinati con **Gemini Flash 2.5**. Inoltre è stato analizzato anche il **tipo di cineturista**, secondo le categorie individuate dagli autori Bolan, Boy e Bell (*scenico*, *emotivo* e *puro*).

### 3.7 — GetYourGuide (analisi di tour ed esperienze) <span class="fam-badge fam-misto">Digitale · esperienza fisica</span>

L'analisi è partita da un dataset relativo ai **tour e alle relative recensioni** disponibili sulla piattaforma. Una prima fase descrittiva ha esaminato le distribuzioni di durata, prezzo e voto medio dei tour, con inclusa una matrice di correlazione tra le variabili.

Sul fronte testuale, descrizioni e recensioni sono state tokenizzate, ripulite dalle *stopword* e lemmatizzate con **simplemma**, per estrarne le frequenze lessicali. Su questo corpus è stato applicato un **topic modeling LDA** (Gensim) a 3 topic — *giudizio globale*, *dettagli pratici*, *contenuti culturali/cinematografici* — scelti sulla base del miglior *silhouette score* ottenuto.

Il sentiment è stato calcolato in due passaggi: un primo punteggio tramite **Pattern.it** sul testo della recensione, poi combinato in modo ponderato con il **voto numerico normalizzato** — una scelta introdotta per correggere la tendenza del modello linguistico a sottostimare recensioni molto positive ma scritte in tono neutro.

<hr class="section-rule">

## 4. Dai Dati ai Cluster Narrativi del Sito

I sette filoni descritti confluiscono nel sito attraverso **tre cluster tematici**, ciascuno dedicato a un diverso profilo di produzione.

<div class="row cluster-grid">
  <div class="col-md-4 mb-4">
    <div class="cluster-card cl-1">
      <span class="cl-kicker">Cluster 01</span>
      <h4>Grandi produzioni internazionali</h4>
      <p>Film di successo globale, girati in Italia: impatto improvviso e alta volatilità.</p>
      <p class="cl-places">Crema (Chiamami col tuo nome) · Volterra e Montepulciano (Twilight) · Bard, Vèrres, Pont-Saint-Martin (Avengers) · Pienza (I Medici)</p>
      <a href="{{ site.baseurl }}/cluster01.html" class="btn btn-primary">Vai al Cluster 01</a>
    </div>
  </div>
  <div class="col-md-4 mb-4">
    <div class="cluster-card cl-2">
      <span class="cl-kicker">Cluster 02</span>
      <h4>Serie italiane di lunga durata</h4>
      <p>Fiction radicate nel territorio nel corso di anni, se non decenni, di messa in onda.</p>
      <p class="cl-places">Braies, San Vito di Cadore, San Candido (Un passo dal cielo) · Spoleto e Gubbio (Don Matteo) · Agliè (Elisa di Rivombrosa) · Ragusa, Scicli, Santa Croce Camerina (Il giovane Montalbano)</p>
      <a href="{{ site.baseurl }}/cluster02.html" class="btn btn-primary">Vai al Cluster 02</a>
    </div>
  </div>
  <div class="col-md-4 mb-4">
    <div class="cluster-card cl-3">
      <span class="cl-kicker">Cluster 03</span>
      <h4>Produzioni di nicchia</h4>
      <p>Casi non riconducibili ai cluster precedenti: impatto focalizzato e target specifico.</p>
      <p class="cl-places">Castellabate (Benvenuti al Sud) · Curon Venosta (Curon) · Opi e Pescasseroli (Un mondo a parte) · Aosta (Rocco Schiavone)</p>
      <a href="{{ site.baseurl }}/cluster03.html" class="btn btn-primary">Vai al Cluster 03</a>
    </div>
  </div>
</div>

<div class="note-box note-info">
  <span class="note-title"><i class="fas fa-info-circle" aria-hidden="true"></i>Come leggere i cluster</span>
  Ogni cluster attinge in proporzioni diverse ai dati fisici e digitali qui descritti, a seconda della <strong>disponibilità</strong> e della <strong>rilevanza</strong> di ciascuna fonte per il caso specifico.
</div>

<div class="row pt-4">
    <div class="col-md-12 text-center">
        <blockquote class="blockquote">
            "La nostra metodologia trasforma il rumore digitale in evidenza empirica, permettendoci di osservare il CineTourism non come un evento isolato, ma come un processo evolutivo."
        </blockquote>
    </div>
</div>
