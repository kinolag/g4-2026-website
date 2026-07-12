---
layout: default
title: "Cluster 3: Cineturismo Nazionale – Analisi dei Casi di Studio Italiani"
vega: true
header_type: hero
header_img: assets/images/header.svg
header_title: "Cluster 3: Cineturismo Nazionale – Analisi dei Casi di Studio Italiani"
subtitle: " Come lo schermo trasforma i territori: produzioni italiane ad alto impatto territoriale "
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

## Introduzione e Metodologia
In questa sezione procediamo con l’analisi di un cluster specifico del progetto **CineTourism**, dedicato alle produzioni italiane che hanno generato trasformazioni misurabili nei territori in cui sono state ambientate: _Benvenuti al Sud_ (Castellabate), _Curon_ (Lago di Resia / Curon Venosta), _Rocco Schiavone_ (Aosta) e _Un mondo a parte_ (Opi e Pescasseroli).
Si tratta di opere molto diverse per genere, distribuzione, pubblico e natura produttiva, ma accomunate da un tratto fondamentale: la capacità di riscrivere la percezione dei luoghi, modificare le narrazioni mediatiche e influenzare in modo strutturale l’ecosistema turistico ed economico.
L’obiettivo è comprendere come il cinema e le serie TV, anche quando non hanno risonanza internazionale, possano generare effetti persistenti e misurabili, trasformando borghi, città e paesaggi naturali in asset territoriali.


---


## 1. Dinamiche Condivise (Tratti Distintivi del Cluster)

### A. La Rottura di Trend: il “prima” e il “dopo” l’opera
In tutti e quattro i casi si osserva una dinamica comune: l’uscita dell’opera segna una **discontinuità** **netta** nelle curve di sentiment, nei volumi di discussione e nella crescita dell’ecosistema turistico. Prima del film o della serie, i territori mostrano narrazioni frammentate, volumi bassi e un turismo stabile. Dopo, si apre una fase nuova: picchi di attenzione, polarizzazioni emotive, nuove categorie tematiche e una crescita tangibile delle attività turistiche.

Su **Castellabate** la curva del **sentiment longitudinale** mostra come turismo ed economia abbiano mantenuto nel tempo valori positivi, con oscillazioni stagionali ma una tendenza stabile verso l’ottimismo:

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/castellabate1.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>

**Curon** vede un aumento di oltre trenta attività turistiche entro cinque chilometri dal lago:

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/curon1.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>

**Aosta** cresce del +26% nella densità ricettiva:

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/aosta1.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>

**Opi** e **Pescasseroli** mostrano un’espansione coerente dell’offerta turistica dopo l’uscita del film. 
 
<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/opi2.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>

Il cineturismo, in tutti i casi, si manifesta come **acceleratore strutturale**.

### B. La Dicotomia del Sentiment: Opportunità vs. Criticità
La narrazione mediatica segue un pattern ricorrente: entusiasmo immediato, seguito da una fase di complessità. I temi “Economic Boom”, “Cine Tourism” e “Deseasonalization” mostrano polarità positive elevate, mentre “Infrastructure Strain” e “Overtourism” emergono come cluster critici.

Questo vale per **Castellabate**, dove la narrazione evolve da entusiasmo a riflessione:

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/castellabate2.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>
 
per **Curon**, dove la pressione turistica diventa tema centrale dal 2023:

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/curon2.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>
 
per **Aosta**, dove la città viene reinterpretata come spazio narrativo:

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/aosta2.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div> 
 
<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/aosta2_2.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>

e per **Opi**, dove il film introduce nuove categorie di fruizione del territorio:

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/opi4.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>
 
### C. Persistenza dell’Effetto: la Long Tail del Cineturismo
Google Trends e Wikipedia confermano che l’interesse non è effimero. **Castellabate** supera gli attori del film in visibilità: 

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/castellabate3.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>

**Curon** mostra ciclicità stagionale:

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/curon3.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/curon3_3.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>

**Opi e Pescasseroli** vedono crescere la curiosità digitale dopo l’uscita in sala e in streaming:

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/opi3.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>

<div class="chart-container">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/opi3_3.json" style="width: 100%; height: 100%; display: block;"></vegachart>
</div>
 
Il cinema diventa così una **porta d’ingresso** alla curiosità geografica, che si rinnova nel tempo.


---


## 2. Varianza Intra Cluster (Differenze Chiave)
### A. Quattro Modelli di Cineturismo
Ogni caso rappresenta un modello distinto:
* **Castellabate – Cineturismo identitario mediterraneo**. Il film ridefinisce l’immaginario del borgo, trasformandolo in simbolo di autenticità. L’effetto è narrativo, economico e digitale.
* **Curon – Cineturismo digitale globale**. La serie Netflix genera un’esplosione internazionale. Il luogo reale supera la fiction e diventa icona culturale. La crescita infrastrutturale è lenta ma profonda.
* **Aosta – Cineturismo urbano identitario**. La città non viene scoperta, ma reinterpretata. Aosta diventa personaggio. L’effetto è culturale, narrativo e ricettivo.
* **Opi/Pescasseroli – Cineturismo naturalistico diffuso**. Il film amplifica un discorso preesistente. L’impatto è equilibrato: nuove attività turistiche, nuove categorie narrative, sentiment complesso.

### B. Intensità e Velocità dell’Impatto
La velocità dell’impatto varia: Castellabate e Curon mostrano accelerazioni immediate; Aosta cresce in modo progressivo grazie alla serialità; Opi e Pescasseroli vivono una maturazione graduale.

### C. Natura della Narrazione Pubblica
La narrazione di Castellabate è fortemente positiva; quella di Curon è polarizzata; quella di Aosta è identitaria; quella di Opi è equilibrata e legata alla scoperta del territorio.

---


## 3.Dalla Curiosità Digitale alla Trasformazione Fisica
L’interesse digitale si traduce in trasformazioni reali: nuove attività turistiche, crescita ricettiva, investimenti locali. Il cinema non solo racconta i luoghi, ma li modifica. In tutti i casi, la risposta del territorio è decisiva: quando il luogo intercetta la visibilità con infrastrutture, servizi e narrazioni coerenti, l’effetto diventa strutturale.


---


## Conclusioni
L’analisi dei quattro casi mostra che il cineturismo italiano è un fenomeno complesso, stratificato e profondamente territoriale. Ogni opera genera un impatto diverso, ma tutte seguono la stessa traiettoria: un’opera audiovisiva accende l’attenzione, modifica la percezione, genera conversazioni, trasforma l’immaginario e, quando il territorio risponde, produce cambiamenti concreti nell’economia e nell’ecosistema turistico.
Il cinema diventa così uno strumento di riscrittura territoriale: non solo rappresenta i luoghi, ma li cambia. Castellabate, Curon, Aosta e Opi raccontano quattro modi diversi di vivere questa trasformazione, ma tutti mostrano la stessa verità: quando un luogo entra nell’immaginario collettivo, non è più solo un luogo. Diventa un racconto che continua nel tempo.

[Link di ritorno a Risultati](results.html)