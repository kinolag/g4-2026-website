---
layout: default
title: "Metodologia"
vega: true
header_type: hero
header_img: assets/images/header.svg
header_title: "Metodologia di Analisi"
subtitle: "Dalla selezione dei casi di studio ai sette filoni di analisi"
---

## 1. Criteri di Selezione dei Casi di Studio

La storia del cinema e della televisione italiana vanta un numero altissimo di produzioni girate sul territorio nazionale: analizzarle tutte non è l'obiettivo di questo progetto. Per costruire un campione gestibile e significativo abbiamo quindi definito **cinque criteri di selezione**, pensati non solo per isolare il segnale cineturistico dal rumore di fondo del turismo tradizionale, ma anche per garantire che ogni caso di studio fosse effettivamente analizzabile con gli strumenti scelti.

In particolare, poiché la metodologia si basa in gran parte sull'analisi del discorso digitale (media, social, sentiment), sono state escluse a monte le produzioni troppo datate: un caso come *Il Padrino*, girato in Sicilia decenni prima dell'esistenza di internet, sarebbe stato impossibile da studiare con questo approccio, indipendentemente dalla sua rilevanza culturale.

La selezione delle produzioni è stata quindi guidata dai seguenti criteri:

*   **Copertura geografica:** solo comuni del territorio italiano, per garantire uniformità normativa nei dati ISTAT e confrontabilità diretta con le statistiche nazionali.
*   **Dimensione demografica:** popolazione generalmente inferiore a 50.000 abitanti, per garantire che l'impatto di una singola produzione sia visibile nei dati e non si disperda nel rumore statistico tipico delle grandi città. Fa eccezione **Ragusa** (73.878 ab.), inclusa per la rilevanza del legame territoriale con la saga di Montalbano.
*   **Varietà geografica:** copertura equilibrata tra le tre macro-aree del paese (Nord, Centro, Sud), per costruire un portafoglio di casi studio il più eterogeneo possibile.
*   **Finestra temporale:** produzioni generalmente collocate tra il **2010 e il 2024**, intervallo che copre la transizione da un modello basato principalmente sulla TV generalista a uno che include lo streaming multicanale, garantendo sia una presenza digitale sufficiente sia una copertura di dati ISTAT adeguata in fase pre e post-uscita. Vanno contestualizzati i casi di lunga serialità come *Don Matteo*, che si colloca in questa finestra nonostante sia iniziato nel 2000; *The Twilight Saga: New Moon* (2009), fuori dalla finestra di un solo anno; e la vera eccezione, *Elisa di Rivombrosa* (2003), inclusa per la sua particolare rilevanza culturale.
*   **Varietà di formato e produzione:** il campione include sia film che serie/fiction, sia produzioni internazionali che domestiche, per evitare che l'analisi restituisse un quadro parziale legato a un solo tipo di prodotto audiovisivo.

A questi si aggiunge un **accorgimento trasversale** applicato a più filoni dell'analisi: la neutralizzazione dell'effetto **COVID-19**, con l'esclusione o normalizzazione dei periodi di interruzione forzata dei flussi turistici, che avrebbero altrimenti invalidato qualsiasi confronto temporale sulla crescita della domanda.

### 1.1 Selezione delle location all'interno di ogni produzione

Un'ulteriore precisazione riguarda non le produzioni in sé, ma le **location** scelte per ognuna di esse. La maggior parte delle produzioni analizzate non è stata girata in un unico luogo, ma ha coinvolto più comuni o addirittura più regioni nel corso delle proprie stagioni e dei periodi di riprese.

Per ogni produzione abbiamo selezionato solo le **location principali** — quelle che ospitano l'ambientazione narrativa portante o una quota sostanziale delle riprese — escludendo deliberatamente comparse marginali o location visibili solo per pochi fotogrammi, prive di un legame narrativo stabile con l'opera.

## 2. Esplorazione dei Dati Strutturati (Tentativi Iniziali)

In una fase preliminare, abbiamo testato l'utilizzo di fonti istituzionali per misurare l'impatto reale:

*   **Dati ISTAT sugli arrivi:** pur trattandosi della fonte più diretta e istituzionale, il singolo indicatore si è rivelato da solo insufficiente a certificare l'esistenza di un "effetto cineturismo". In diverse location, infatti, non si osservava un incremento dei flussi abbastanza netto da poter essere isolato con sicurezza dal turismo ordinario. Questa evidenza ha reso necessario estendere l'analisi a un ventaglio più ampio di indicatori e a un focus più marcato sulla componente digitale.
*   **Dati sulla produzione di rifiuti:** si è esplorata la correlazione tra presenze turistiche e tonnellate di rifiuti urbani. Tuttavia, la variabilità stagionale e la mancanza di dati disaggregati per quartiere o area di interesse hanno reso questa metrica insufficiente per definire un nesso causale diretto con il fenomeno del cineturismo.

Nella sezione che segue si spiegherà come si è ovviato a questi limiti.

## 3. Le Fonti Adottate e l'Approccio Metodologico Proposto

Il progetto si articola in **sette filoni di analisi**, ciascuno costruito per intercettare una diversa manifestazione del fenomeno cineturistico.

Le fonti si dividono in due grandi famiglie: da un lato i **dati fisici/territoriali** — indicatori ISTAT e trasformazione del tessuto commerciale locale (OpenStreetMap) — che misurano l'impatto direttamente sul territorio; dall'altro i **dati digitali** — Reddit, stampa, Google Trends/Wikipedia, YouTube, GetYourGuide — che ne osservano il riflesso nel comportamento e nel discorso online.

La distinzione non è sempre netta: le recensioni GetYourGuide, ad esempio, sono dati digitali a tutti gli effetti, ma raccontano un'esperienza **fisica realmente vissuta** sul luogo, non un'opinione formata a distanza come può essere un commento Reddit o YouTube.

Di seguito il dettaglio tecnico di ciascun filone.

### 3.1 — Indicatori ISTAT comunali (CIS/RGR)

Analisi quantitativa su **82 indicatori socioeconomici comunali** (ISTAT/MiC-MiBACT), estesa oltre i semplici arrivi/presenze per superare i limiti descritti in Sezione 2.

Per ogni coppia comune-indicatore viene calcolato un **Cineturismo Impact Score (CIS)**, indice composito endogeno che combina tre componenti calcolate sulla singola serie storica:

*   **Delta:** variazione percentuale tra baseline pre-evento e finestra post-evento.
*   **Zeta Shift:** scostamento standardizzato in σ rispetto alla media storica.
*   **Persistenza:** continuità del segnale nella finestra post-evento (scala 0-1).

Le evidenze con **CIS > 0,7** vengono validate esternamente tramite **Relative Growth Rate (RGR)**, che confronta la crescita del comune con il benchmark della relativa regione, con soglia di accettazione **RGR ≥ 0,15**. Il processo ha prodotto **18 evidenze**.

### 3.2 — Ecosistema commerciale (OpenStreetMap)

Analisi geospaziale della trasformazione del tessuto commerciale locale: per ogni location è stata tracciata un'**area circolare di 5 km di raggio**, e i punti di interesse (POI) al suo interno sono stati classificati tramite tag OSM in **ecosistema turistico** (ad esempio, le attività di ristorazione e le strutture ricettive/promozionali) *versus* **tessuto commerciale standard** (ad esempio, supermercati, panetterie, ferramenta).

Il confronto tra le due categorie permette di osservare l'eventuale **adattamento strutturale** della zona all'aumento dei flussi turistici.

### 3.3 — Analisi dell'esposizione mediatica (sentiment e topic modeling)

Questa fase mira a quantificare la copertura mediatica e a valutare la percezione pubblica dei territori coinvolti, confrontando i periodi antecedenti e successivi all'uscita della produzione.

L'acquisizione dei dati è avvenuta tramite estrazione massiva (*scraping*) di articoli giornalistici con l'**API di Google News**, su una finestra temporale che va dai due anni precedenti l'uscita dell'opera fino a maggio 2026, con interrogazioni mirate a notizie riguardanti il turismo e l'economia locale delle aree di interesse. Su questo corpus sono stati valutati sia il **volume** di articoli pubblicati nel tempo sia il **tono** generale di ciascun articolo, classificato con un modello di Sentiment Analysis su una scala continua da **-1** (fortemente negativo) a **+1** (fortemente positivo).

Parallelamente, un **topic modeling** tematico ha identificato all'interno dei testi le tematiche più rilevanti, per comprendere quali aspetti dell'impatto territoriale sono stati maggiormente discussi. I topic monitorati sono:

*   **Cine Tourism** — turismo cinematografico
*   **Urban Change** — cambiamenti del tessuto urbano
*   **Infrastructure Strain** — sforzo/sovraccarico infrastrutturale
*   **Economic Boom** — crescita economica
*   **Overtourism** — sovraffollamento turistico
*   **Deseasonalization** — destagionalizzazione dei flussi

Per ogni topic menzionato all'interno di un articolo è stato inoltre calcolato uno specifico punteggio di sentiment (**ABSA**, *Aspect-Based Sentiment Analysis*), sempre su scala da -1 a +1 — un livello di dettaglio che permette di tracciare l'evoluzione temporale della percezione di ogni singolo fenomeno, indipendentemente dal tono generale dell'articolo in cui compare.

### 3.4 — Google Trends e Wikipedia (interesse informativo e comportamento di ricerca)

È stata valutata la risonanza del prodotto audiovisivo sul **comportamento di ricerca online** e sull'interesse informativo generale degli utenti, tramite l'utilizzo combinato dei dati di **Google Trends** e delle visualizzazioni delle pagine **Wikipedia**.

Per ogni produzione sono state identificate le pagine Wikipedia relative alle location di riferimento, da cui è stato estratto lo storico delle visite nel tempo. Le serie storiche così costruite sono state **allineate alle date di rilascio** dell'opera, per quantificare sia i picchi di traffico immediati sia l'andamento dell'interesse digitale generato nel tempo.

### 3.5 — YouTube (rilevamento della presenza della produzione nei commenti)

L'obiettivo di questo filone è verificare se, e quanto, la presenza di una produzione su YouTube si rifletta effettivamente nei **commenti ai video girati nelle sue location**.

La pipeline è partita dalla ricerca dei video tramite **YouTube Data API v3**, seguita dalla raccolta dei commenti e delle relative risposte. Sono stati messi a confronto i risultati emersi da **due query diverse**: "produzione + location" e "location".

I testi sono stati poi ripuliti — rimozione di URL, emoji e contenuti vuoti, deduplicazione — prima di passare a una fase di **lexical matching, embedding e scoring** che ha permesso di rilevare le menzioni della produzione all'interno dei commenti. I risultati sono stati infine aggregati sia per produzione che per location, per rendere confrontabili i due approcci di ricerca.

È importante specificare che il metodo **confronta due strategie di ricerca tra loro**, ma non dimostra di per sé un nesso causale tra la produzione e l'attenzione generata sul luogo.

### 3.6 — Reddit (analisi del discorso della community)

La raccolta dati è stata condotta tramite l'**API PullPush**, con query mirate per produzione e location sui 12 casi studio, concentrandosi su subreddit popolari generici e sui principali subreddit dedicati al turismo e ai consigli di viaggio.

Il volume grezzo estratto era molto rumoroso, e ha richiesto una **pipeline di pulizia a tre stadi** — filtri regex, poi un *bi-encoder*, infine un *cross-encoder* — per isolare i contenuti effettivamente pertinenti.

Dopo la pulizia dei dati è iniziata una prima analisi esplorativa dedicata alla validazione di una **finestra temporale di 3 anni pre/post uscita**: solo **5 produzioni su 12** disponevano di dati sufficienti per un confronto in questo arco temporale. Per queste produzioni sono state condotte analisi descrittive (volumi e lingua della discussione).

Successivamente si è proseguito con la **classificazione** dei post e dei commenti dell'intero corpus raccolto. Usando il modello `moritz-laurer/mDeBERTa` (*zero-shot classification*) sono state distinte 6 etichette corrispondenti a sei tipologie di turismo. Di queste, l'etichetta "Cineturismo" è stata la meno accurata, per cui i risultati sono stati affinati con **Gemini Flash 2.5**. Inoltre è stato analizzato anche il **tipo di cineturista**, secondo le categorie individuate dagli autori Bolan, Boy e Bell (*scenico*, *emotivo* e *puro*).

### 3.7 — GetYourGuide (analisi di tour ed esperienze)

L'analisi è partita da un dataset relativo ai **tour e alle relative recensioni** disponibili sulla piattaforma. Una prima fase descrittiva ha esaminato le distribuzioni di durata, prezzo e voto medio dei tour, con inclusa una matrice di correlazione tra le variabili.

Sul fronte testuale, descrizioni e recensioni sono state tokenizzate, ripulite dalle *stopword* e lemmatizzate con **simplemma**, per estrarne le frequenze lessicali. Su questo corpus è stato applicato un **topic modeling LDA** (Gensim) a 3 topic — *giudizio globale*, *dettagli pratici*, *contenuti culturali/cinematografici* — scelti sulla base del miglior *silhouette score* ottenuto.

Il sentiment è stato calcolato in due passaggi: un primo punteggio tramite **Pattern.it** sul testo della recensione, poi combinato in modo ponderato con il **voto numerico normalizzato** — una scelta introdotta per correggere la tendenza del modello linguistico a sottostimare recensioni molto positive ma scritte in tono neutro.

## 4. Dai Dati ai Cluster Narrativi del Sito

I sette filoni descritti confluiscono nel sito attraverso **tre cluster tematici**, ciascuno dedicato a un diverso profilo di produzione:

1.  **Grandi produzioni internazionali** di successo globale, girate in Italia: Crema (*Chiamami col tuo nome*), Volterra/Montepulciano (*Twilight*), Bard, Vèrres, Pont-Saint-Martin (*Avengers*) e Pienza (*I Medici*).
2.  **Serie italiane di lunga durata**, radicate nel territorio nel corso di anni se non decenni di messa in onda: Braies, San Vito di Cadore, San Candido (*Un passo dal cielo*), Spoleto/Gubbio (*Don Matteo*), Agliè (*Elisa di Rivombrosa*) e Ragusa, Scicli, Santa Croce Camerina (*Il giovane Montalbano*).
3.  **Produzioni di nicchia** o non riconducibili ai cluster precedenti: Castellabate (*Benvenuti al Sud*), Curon Venosta (*Curon*), Opi e Pescasseroli (*Un mondo a parte*) e Aosta (*Rocco Schiavone*).

Ogni cluster attinge in proporzioni diverse ai dati fisici e digitali qui descritti, a seconda della **disponibilità** e della **rilevanza** di ciascuna fonte per il caso specifico.

<div class="row pt-4">
    <div class="col-md-12 text-center">
        <blockquote class="blockquote">
            "La nostra metodologia trasforma il rumore digitale in evidenza empirica, permettendoci di osservare il CineTourism non come un evento isolato, ma come un processo evolutivo."
        </blockquote>
    </div>
</div>
