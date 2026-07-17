---
layout: default
title: "Cluster 3: Cineturismo Nazionale – Analisi dei Casi di Studio Italiani"
vega: true
header_type: hero
header_img: assets/images/header.svg
header_title: "Analisi di Cluster: altre Produzioni italiane"
subtitle: " Come lo schermo trasforma i territori: produzioni di nicchia o non riconducibili ai cluster precedenti"
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

Il cluster raccoglie **quattro produzioni italiane**, ciascuna legata a uno o più territori specifici: **Castellabate** per *Benvenuti al Sud*; 
**Curon Venosta / Lago di Resia** per *Curon*; **Aosta** per *Rocco Schiavone*; **Opi e Pescasseroli** per *Un mondo a parte*.

Le produzioni raccolte nel cluster appartengono a un immaginario **interamente italiano**, lontano dai blockbuster internazionali analizzati 
nei cluster precedenti e radicato in un pubblico domestico che riconosce nei luoghi rappresentati una geografia familiare. Sono opere che non 
hanno avuto particolare risonanza all’estero, ma che in Italia hanno saputo incidere profondamente sulla percezione dei territori, trasformando 
borghi, laghi e città in spazi narrativi riconoscibili.
Accanto a questa dimensione nazionale, emerge la loro capacità di **lasciare un segno duraturo**: _Benvenuti al Sud_ ha ridefinito l’immaginario 
di Castellabate, _Curon_ ha trasformato il Lago di Resia in un simbolo culturale, _Rocco Schiavone_ ha reinterpretato Aosta come personaggio 
urbano, _Un mondo a parte_ ha amplificato la visibilità di Opi e Pescasseroli. Non si tratta di opere sostenute da franchise globali o da 
serialità ultralongeve, ma di casi di studio che, pur partendo da una scala produttiva più contenuta, hanno generato 
**effetti misurabili e persistenti** sui territori.

Questa combinazione — una produzione non globale, ma capace di produrre una **rottura di trend** evidente — è 
la chiave di lettura scelta per analizzare il cluster: l’obiettivo non è misurare l’eco di un successo planetario, bensì 
osservare come opere nate per il pubblico italiano possano comunque costruire nel tempo un **radicamento strutturale**, modificando 
narrazioni, percezioni e dinamiche turistiche. Non un picco isolato, ma una trasformazione che si consolida e si rinnova.

Si tratta di opere molto diverse per genere, distribuzione, pubblico e natura produttiva, ma accomunate da un tratto fondamentale: 
la capacità di riscrivere la percezione dei luoghi, modificare le narrazioni mediatiche e influenzare in modo strutturale l’ecosistema 
turistico ed economico.
L’obiettivo è comprendere come il cinema e le serie TV, anche quando non hanno risonanza internazionale, possano generare effetti 
persistenti e misurabili, trasformando borghi, città e paesaggi naturali in asset territoriali.

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

### Castellabate — _Benvenuti al Sud_

**Nessuna evidenza** tra gli indicatori selezionati: il segnale ISTAT non ha superato le soglie di validazione.
Il caso resta comunque rilevante nel cluster, ma l’impatto misurabile non emerge dagli indicatori ISTAT utilizzati.

### Curon Venosta — _Curon_

Segnale pieno e coerente: la **popolazione straniera** cresce del **+27,71%**, con uno **Zeta Shift di +5,68σ** e **persistenza piena (1/1)**. 
Il **CIS** è **100/100**, e l’RGR raggiunge **+20,79%**.
È un caso che non presenta anomalie: la crescita è moderata ma stabile, e si manifesta come una trasformazione graduale del territorio, 
più che come un picco isolato. La serie Netflix ha introdotto una discontinuità evidente, ma senza sbilanciare gli equilibri locali.

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster03/curon_istat.json"></vegachart>
</div>


### Aosta — _Rocco Schiavone_

Segnale solido e lineare: la **densità degli esercizi ricettivi** aumenta del **+26,19%**, con uno **Zeta Shift molto alto (+21,45σ)** e 
**persistenza piena (1/1)**. Il **CIS** è **100/100**, e l’**RGR** si attesta a **+18,48%**.
Non ci sono balzi improvvisi, ma una crescita coerente con la serialità e con la capacità della produzione di mantenere nel tempo 
un’attenzione costante sulla città. È un caso “pulito”, privo di estremi, che riflette bene la natura progressiva dell’impatto.

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster03/aosta_istat.json"></vegachart>
</div>

### Opi e Pescasseroli — _Un mondo a parte_

Nessuna evidenza tra gli indicatori selezionati: nessun indicatore validato, nessun RGR sopra soglia.
L’effetto del film è reale e riconoscibile sul territorio, ma non si manifesta nei KPI ISTAT considerati.

### Uno sguardo d'insieme

Il quadro che emerge dal confronto è quasi a due velocità.
Da un lato Curon e Aosta disegnano il profilo più “sano” del cluster — segnali coerenti, persistenti nel tempo, privi di anomalie 
statistiche.
Dall’altro Castellabate e Opi/Pescasseroli, pur centrali nella narrazione del cluster, non superano le soglie ISTAT: l’impatto esiste, 
ma non è misurabile attraverso gli indicatori selezionati.

### L'ecosistema turistico attorno ai set

Sulle location legate a _Un mondo a parte_ (Opi e Pescasseroli), il numero di **attività a
vocazione turistica** (ristoranti, alloggi, negozi di souvenir, ecc.) entro un 
raggio di 5 km mostra una dinamica chiara: dopo l’uscita del film nelle sale nel 2024 si registra 
un primo incremento netto, seguito da una fase di **stabilizzazione** che dura circa due anni.  
La curva riprende a salire in modo evidente con la **release del lungometraggio sulle piattaforme di streaming**, che 
introduce una seconda ondata di attenzione e porta a un ulteriore ampliamento dell’ecosistema turistico locale.

In altre parole, l’effetto non si esaurisce nel momento della distribuzione cinematografica: si **riattiva** quando il film entra 
nel circuito domestico e raggiunge un pubblico più ampio, suggerendo un impatto che non è solo immediato, ma capace di rinnovarsi nel tempo.

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster03/opi_ecosistema.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>

---

## Sezione 2 — Racconto dall'alto

<!-- Risponde alla domanda 2: i media offrono riscontri e alimentano il fenomeno? -->

_L'eco dei media: come raccontano i media le località del Cluster 3?_

Se nella Sezione 1 abbiamo visto se il fenomeno lascia un segno nei numeri, qui
vediamo **come i media lo raccontano**. Sono state usate due chiavi di lettura
complementari: l'**evoluzione del sentiment** nel tempo (quanto se ne parla, con
che tono) e la **polarizzazione tematica** (di cosa si parla, e se prevale
l'entusiasmo o la critica).

### Castellabate — _Benvenuti al Sud_

Il racconto mediatico legato al film mostra una **progressione chiara e coerente nel tempo**. Dopo la fase iniziale — tra il 2009 e il 2011, 
segnata dall’avvio delle riprese e dall’uscita in sala — la narrazione si stabilizza su toni **prevalentemente positivi**, con una polarità media 
compresa tra **+0,6 e +1,0**.
Il tema dominante è l’**Economic Boom**, seguito da **Deseasonalization** e **Urban Cange**. **Overtourism** e **Infrastructure Strain** emergono negli anni più recenti, 
quando il volume di articoli cresce sensibilmente.
Tra il 2018 e il 2026 si osserva una **densificazione del racconto**: le menzioni si moltiplicano e si diversificano, ma il sentiment resta 
complessivamente ottimista. Le criticità — legate alla pressione turistica e alle infrastrutture — compaiono in modo episodico e con polarità 
negativa, ma non alterano il tono generale.
Il **Cine Tourism** è presente, ma non dominante: si inserisce come tema trasversale, spesso associato alla crescita economica e alla trasformazione 
urbana.

In sintesi, il grafico racconta un **fenomeno mediatico ampio, maturo e prevalentemente positivo**, dove l’entusiasmo per lo sviluppo territoriale 
convive con una consapevolezza crescente dei suoi effetti collaterali.

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster03/castellabate_evoluzione_sentiment.json"></vegachart>
</div>

### Curon Venosta — _Curon_

Il racconto mediatico legato a Curon mostra una **progressione netta e ben scandita nel tempo**. Dopo la fase iniziale — tra il 2018 e il 2020 — 
la narrazione si concentra su toni **positivi e curiosi**, con una polarità media compresa tra **+0,5 e +1,0**, in corrispondenza della **release su 
piattaforme di streaming (giugno 2020)**.
Il tema dominante è l’**Economic Boom**, seguito da **Cine Tourism** e **Urban Change**, che insieme delineano un quadro di entusiasmo verso la scoperta 
del territorio e la sua trasformazione in attrattore culturale.
Negli anni successivi, tra il 2023 e il 2026, il racconto **si amplia e si diversifica**: compaiono le prime menzioni di **Infrastructure Strain** 
e **Overtourism**, con polarità più negativa, segno di una crescente consapevolezza dei limiti del successo turistico. Tuttavia, il tono generale 
resta prevalentemente positivo, e le criticità non superano mai il volume dei temi economici e culturali.

In sintesi, il grafico racconta un fenomeno mediatico **vivace e in evoluzione**: l’entusiasmo iniziale per la serie e per il luogo si consolida 
nel tempo, mentre la narrazione si arricchisce di sfumature più mature, che riconoscono tanto le opportunità quanto le tensioni generate dal 
turismo cinematografico.

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster03/curon_evoluzione_sentiment.json"></vegachart>
</div>

### Opi e Pescasseroli — _Un mondo a parte_

Il racconto mediatico legato a Un mondo a parte — ambientato tra Opi e Pescasseroli — mostra una **narrazione compatta ma ben articolata**, 
che si sviluppa in due fasi distinte.
La prima, in corrispondenza della **release cinematografica (marzo 2024)**, è dominata da toni positivi e ottimistici, con polarità media tra 
**+0,5 e +1,0**: prevalgono i temi di **Economic Boom**, **Deseasonalization** e **Urban Change**, che raccontano il film come occasione di riscoperta 
territoriale e di valorizzazione economica.
La seconda fase, dopo la release in streaming (inizio 2026), introduce una narrazione più complessa: compaiono i temi di Infrastructure 
Strain e Overtourism, con polarità negativa e volumi più consistenti. È il momento in cui il successo turistico diventa anche oggetto di 
riflessione critica, segno di una maturazione del discorso pubblico.

Nel complesso, il grafico restituisce un racconto **vivace e coerente**, dove l’entusiasmo iniziale per la rinascita del territorio si accompagna, 
negli anni successivi, a una crescente consapevolezza dei suoi effetti collaterali. Un fenomeno mediatico che evolve da **celebrazione locale a 
analisi strutturale**, mantenendo sempre un tono prevalentemente positivo.

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster03/opi_evoluzione_sentiment.json"></vegachart>
</div>

### Uno sguardo d'insieme

Il confronto disegna **tre profili narrativi ben distinti**.  
*Benvenuti al Sud* è la produzione che i media raccontano più esplicitamente come **fenomeno di rinascita territoriale**: 
non solo il successo del film è riconosciuto, ma gli articoli lo celebrano come motore di sviluppo e simbolo identitario per Castellabate.  
*Curon* rappresenta invece il caso più **polarizzato**: l’entusiasmo iniziale per la serie e per la riscoperta del Lago di Resia 
convive con un crescente dibattito sulle criticità del turismo, tra sovraffollamento e pressione infrastrutturale.  
*Un mondo a parte* si colloca in una posizione intermedia: il racconto mediatico è positivo e diffuso, ma evolve nel tempo, 
passando dalla curiosità per la novità del film alla riflessione più matura sull’impatto turistico e ambientale nelle aree di Opi e Pescasseroli.  

In sintesi, il cluster mostra come il cinema italiano possa generare **narrazioni territoriali di natura diversa** — dalla celebrazione 
economica alla consapevolezza critica — ma tutte accomunate da un tratto comune: la capacità di trasformare luoghi reali in spazi simbolici 
dell’immaginario collettivo.

---

## Sezione 3 — Racconto dal basso

Cosa emerge dalle **rilevazioni online** e dalle comunità di utenti: l'attenzione
digitale rivolta al luogo e alla produzione.

_Gli utenti viaggiano per la serie, o la "visitano" da casa?_

La nostra ricerca fin dall'inizio si è chiesta se, accanto ai segnali fisici, si potessero trovare segnali di 
un "turismo virtuale" descrivibili in generale come **"attenzione digitale"**, immaginando quindi utenti alla ricerca 
di informazioni in rete prima di visitare una determinata località filmica, o magari senza una reale intenzione di visitarla direttamente.

Questo concetto risulta utile in quanto accomuna tanto indicatori più affermati come Google Trends e Wikipedia, 
quanto rilevazioni su media e comunità diversi come Reddit.

In particolare abbiamo assemblato - mediante pipeline parallele e sequenze strutturate di query - 
dataset testuali contenenti post Reddit e commenti YouTube relativi alle località filmiche delle produzioni esaminate.

L'analisi testuale dei documenti così raccolti, pur non portando a risultati generalizzabili, ha comunque offerto 
elementi interessanti sulle serie TV che, grazie a un processo di diffusione mediatica prolungato nel tempo, sembrano 
generare un seguito attivo che lascia tracce visibili anche in rete.

Vediamo alcuni esempi di questo fenomeno.

**Fonti:** Google Trends, Wikipedia, Reddit.

### Google Trends e Wikipedia

Google Trends e Wikipedia confermano che l’interesse non è effimero. **Castellabate** supera gli attori del film in **visibilità**:

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster03/castellabate_google_trends.json"></vegachart>
</div>

### Reddit

Post per tipologia di turismo **prima** dell'uscita di _Rocco Schiavone_ - Aosta:

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster03/aosta_post_reddit_prima.json"></vegachart>
</div>

Post per tipologia di turismo **dopo** l'uscita di _Rocco Schiavone_ - Aosta:

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/cluster03/aosta_post_reddit_dopo.json"></vegachart>
</div>

---

## In sintesi

Il cineturismo italiano mostra una struttura chiara: ogni opera audiovisiva crea una rottura di trend, 
un “prima” e un “dopo” che ridisegna la percezione del luogo, genera un sentiment ambivalente fatto di 
opportunità e criticità, e produce un effetto persistente che si trascina nel tempo come una long tail 
capace di influenzare narrazioni, economie e immaginari. All’interno di questa dinamica comune, però, i 
territori reagiscono in modi diversi, dando vita a modelli distinti che mostrano la ricchezza e la complessità del fenomeno.

Castellabate rappresenta il cineturismo identitario mediterraneo: il film non si limita a mostrare il borgo, 
ma lo reinventa, trasformandolo in simbolo di autenticità e qualità della vita. L’impatto è narrativo, economico 
e digitale, e rispecchia ciò che Marra definirebbe “la magia del cinema che dà valore a ciò che hai a disposizione”. 
Curon, invece, incarna il cineturismo digitale globale: la serie Netflix proietta il paese in un immaginario 
internazionale, dove il luogo reale supera la fiction e diventa icona culturale. La crescita infrastrutturale 
è lenta ma profonda, segno di un processo che non si esaurisce nell’hype iniziale. Aosta offre un modello urbano 
identitario: la città non viene scoperta, ma reinterpretata. Diventa personaggio, assume un ruolo narrativo e 
culturale che rafforza il senso di appartenenza. McQuack parla di “campanilismo inevitabile” quando Hollywood 
o la serialità scelgono un luogo italiano, e Aosta ne è un esempio evidente. Infine Opi e Pescasseroli mostrano 
un cineturismo naturalistico diffuso: il film amplifica un discorso già esistente, senza stravolgere il territorio. 
L’impatto è equilibrato, fatto di nuove attività turistiche, nuove categorie narrative e un sentiment complesso 
che alterna entusiasmo e cautela.

L’analisi dei quattro casi rivela che il cineturismo italiano è un fenomeno stratificato e profondamente territoriale. 
Ogni opera genera un impatto diverso, ma tutte seguono la stessa traiettoria: accendono l’attenzione, modificano 
la percezione, alimentano conversazioni, trasformano l’immaginario e, quando il territorio risponde, producono 
cambiamenti concreti nell’economia e nell’ecosistema turistico. Come ricorda Marra, il cinema può farci “innamorare 
di ciò che non avevamo davvero guardato”, mentre McQuack sottolinea come possa diventare “una via di fuga sensoriale” 
che spinge le persone a cercare nella realtà la magia vista sullo schermo. In questo senso il cinema diventa uno 
strumento di riscrittura territoriale: non si limita a rappresentare i luoghi, li cambia. Castellabate, Curon, Aosta 
e Opi raccontano quattro modi diversi di vivere questa trasformazione, ma tutti mostrano la stessa verità. Quando un 
luogo entra nell’immaginario collettivo, non è più soltanto un luogo: diventa un racconto che continua nel tempo.

[Link di ritorno a Risultati](results.html)