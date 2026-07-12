---
layout: default
title: "Introduzione al CineTourism"
vega: true
header_type: hero
header_img: assets/images/header.svg
header_title: "CineTourism: L'Impatto dei Media sul Territorio"
subtitle: "Analisi multidisciplinare tra visibilità globale e sostenibilità locale"
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


## Definizione e Complessità del Fenomeno
Il **CineTourism** identifica lo spostamento di flussi turistici verso destinazioni rese celebri da film o serie TV, un processo che fonde la realtà geografica con l’immaginario narrativo. La letteratura internazionale lo descrive come una forma di turismo esperienziale e identitario, in cui il visitatore cerca di “vivere” la storia che ha visto sullo schermo. Non si tratta solo di visitare un set, ma di entrare in un universo simbolico: un luogo reale che diventa spazio emotivo e culturale.

Come ha raccontato il podcaster **Davide Marra**, «_il cinema dà valore a ciò che abbiamo a disposizione_». Guardare un film può trasformare un luogo familiare in qualcosa di nuovo, risvegliando curiosità e senso di appartenenza. Allo stesso modo, il doppiatore **Rob McQuack** sottolinea che oggi il fenomeno è amplificato dallo streaming e dai social: scene iconiche diventano trend globali, e i fan si spostano per ricrearle, cercando di “_portare un po’ di quella magia nella realtà_”.

---

## Il Paradosso della Visibilità: Perché è Importante?
Il successo mediatico di un’opera può trasformarsi in un **paradosso territoriale**: da un lato genera visibilità, investimenti e crescita economica; dall’altro espone il territorio a **stress infrastrutturali**, perdita di autenticità e sovraffollamento.

### **Pro**
- **Boom economico e occupazionale:** l’aumento dei flussi turistici porta nuove attività ricettive, ristorative e culturali.  
- **Valorizzazione del patrimonio locale:** i luoghi diventano simboli identitari e attrattori di interesse internazionale.  
- **Rinascita culturale:** come nel caso di *Gomorra*, citato da Davide Marra, la produzione audiovisiva può stimolare nuove iniziative artistiche e sociali.

### **Contro**
- **Sovraffollamento e degrado ambientale:** l’afflusso non pianificato di visitatori può compromettere ecosistemi fragili.  
- **Perdita della “vera storia” del luogo:** il territorio rischia di essere percepito solo attraverso la lente del film o della serie, riducendo la sua complessità culturale.  
- **Stereotipizzazione:** come osserva McQuack, l’Italia viene spesso rappresentata con cliché turistici che non riflettono la realtà contemporanea.

<div class="row">
  <div class="col-md-12 text-center">
    <img src="{{site.baseurl}}/assets/images/cinetourism_locations/braies_crowd_1.jpg"
         class="img-fluid mx-auto d-block"
         style="margin: 20px 0;"
         alt="Sovraffollamento al Lago di Braies">
  </div>
</div>


La visibilità globale può trasformarsi in un "paradosso": il successo mediatico attira capitali ma espone il territorio a stress infrastrutturali non pianificati. Il caso del <strong>Lago di Braies</strong> mostra come una serie TV possa attrarre migliaia di turisti, portando a soluzioni di gestione del traffico obbligate, come la chiusura della strada nei mesi di picco per preservare l'ecosistema.

---

## Dal Film al Territorio: Attività e Impatti
Il cineturismo è oggi un **fenomeno emergente** e in rapida evoluzione.  
Accanto agli studi sociologici e culturali, questo progetto propone di affiancare una **dimensione quantitativa**, basata su analisi di dati e metriche territoriali.  
L’obiettivo è costruire una **pipeline metodologica riciclabile**, capace di analizzare casi di studio in Italia e all’estero, integrando dati di sentiment, flussi turistici, trend digitali e trasformazioni economiche.
Studiare il cineturismo significa comprendere come l’immaginario audiovisivo influenzi comportamenti reali, economie locali e identità collettive.  
È un campo di ricerca che unisce **media studies**, **data analytics** e **geografia culturale**, con l’ambizione di trasformare la visibilità mediatica in uno strumento di sviluppo sostenibile.

La crescita del cineturismo ha generato un ecosistema di **attività commerciali e culturali** che rispondono alle nuove esigenze dei visitatori.  
Tra queste, iniziative indipendenti come l’**Elio & Oliver Love Tour** di Crema, dedicato a *Call Me By Your Name*. Come racconta l'organizzatore di questo tour,  **Gary Potter**, il tour è nato dal passaparola dei fan e oggi accoglie centinaia di persone ogni giorno, creando legami umani e culturali attorno al film: «Cerchiamo solo di continuare a condividere l’amore il più a lungo possibile.»

Oppure i **tour cinematografici** organizzati da piattaforme come **GetYourGuide**, di cui abbiamo analizzato descrizioni e recensioni. Le descrizioni dei tour sono state analizzate con tecniche NLP, mostrando che gli operatori costruiscono un immaginario centrato sulla scoperta, sulla storia, sulla cultura cinematografica e sulla narrazione dei luoghi iconici.
Sulle recensioni, invece, abbiamo studiato la distribuzione dei voti, la lunghezza dei testi, la provenienza dei turisti e la stagionalità. È emerso che il cineturismo attira in modo particolare turisti stranieri, soprattutto giovani, mentre gli italiani risultano meno rappresentati. Le recensioni estive sono più numerose e più entusiaste, segno che l’esperienza cinematografica si intreccia con la dimensione emozionale del viaggio.
Infine, la parte più delicata è stata la **sentiment analysis**: abbiamo usato Pattern.it e poi costruito un sentiment combinato che integra il tono del testo con il voto numerico della recensione. Questo approccio ha prodotto una misura molto più stabile e realistica. Il risultato è chiaro: il sentiment medio dei tour è fortemente positivo, con valori compresi tra **0.4** e **0.6**. Le guide competenti sono il fattore più determinante del sentiment; i pochi valori più bassi riguardano problemi organizzativi o aspettative non soddisfatte.

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/sentiment_combinato_recensioni_gyg.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>

Questi esempi mostrano come il cineturismo non sia solo un fenomeno economico, ma anche **sociale e affettivo**: un modo per costruire comunità, condividere esperienze e riscoprire il valore dei luoghi attraverso la lente del cinema.
Di seguito la wordcloud delle recensioni di Get Your Guide:

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/wordcloud_recensioni_gyg.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>

---

## 4. Conclusioni e Prospettive
Il cineturismo è un laboratorio di trasformazione territoriale e culturale.  
Studiare questo fenomeno significa interrogarsi su come i media plasmino la realtà, e su come i territori possano rispondere in modo sostenibile.  
L’integrazione tra **analisi qualitativa** (narrazioni, percezioni, esperienze) e **analisi quantitativa** (dati, trend, metriche) è la chiave per comprendere e gestire il futuro di un turismo che nasce dallo schermo ma vive nel mondo reale.