---
layout: default
title: "Metodologia"
vega: true
header_type: hero
header_img: assets/images/header.svg
header_title: "Metodologia di Analisi"
subtitle: "Dalla selezione dei casi studio all'approccio basato sul Sentiment Analysis"
---

## 1. Criteri di Selezione dei Casi Studio
La misurazione dell'impatto del CineTourism presenta sfide metodologiche non trascurabili. Per isolare il segnale cinematico dal rumore di fondo del turismo tradizionale, abbiamo definito criteri di selezione rigorosi per identificare le destinazioni oggetto della nostra analisi:

*   **Dimensione Demografica:** Abbiamo escluso sia le metropoli (es. Roma), dove l'impatto di una singola produzione è irrilevante rispetto al volume turistico totale, sia i borghi troppo piccoli, dove la carenza di dati sistematici rende impossibile l'analisi statistica.
*   **Finestra Temporale:** Le produzioni selezionate devono collocarsi in un periodo ottimale: non troppo datate (per garantire la disponibilità di tracce digitali) e non troppo recenti (per evitare distorsioni causate da campagne promozionali attive).
*   **Neutralizzazione dell'Effetto COVID-19:** Sono stati esclusi o normalizzati i periodi di interruzione forzata dei flussi turistici (2020-2022), che avrebbero invalidato qualsiasi confronto temporale sulla crescita della domanda.

## 2. Esplorazione dei Dati Strutturati (Tentativi Iniziali)
In una fase preliminare, abbiamo testato l'utilizzo di fonti istituzionali per misurare l'impatto reale:

*   **Dati ISTAT sugli arrivi:** Sebbene necessari, gli arrivi turistici ufficiali si sono rivelati poco sensibili alle fluttuazioni causate da singole produzioni cinematografiche, probabilmente a causa di un'alta latenza nel reporting comunale.
*   **Dati sulla produzione di rifiuti:** Abbiamo esplorato la correlazione tra presenze turistiche e tonnellate di rifiuti solidi urbani. Tuttavia, la variabilità stagionale e la mancanza di dati disaggregati per quartiere o area di interesse hanno reso questa metrica insufficiente per definire un nesso causale diretto con il CineTourism.

## 3. L'Approccio Metodologico Proposto: Data-Driven Sentiment Analysis
Data l'inconsistenza dei dati strutturati, abbiamo adottato un approccio alternativo basato sull'analisi del discorso pubblico digitale. La metodologia si articola nelle seguenti fasi:

1.  **Scraping Strategico:** Raccolta di notizie, articoli e post geolocalizzati pubblicati prima, durante e dopo le date chiave (rilascio del film, premi vinti, milestone promozionali).
2.  **Analisi del Sentiment:** Monitoraggio dei cambiamenti qualitativi nel linguaggio utilizzato per descrivere la destinazione. Misuriamo la variazione semantica nel tempo: il focus si sposta dalla "storia locale" al "set cinematografico"? Il sentiment economico è positivo o si corrompe a causa dello stress infrastrutturale?
3.  **Monitoraggio dei Milestone:** Analisi della correlazione tra l'attività mediatica e il volume di menzioni economiche, utilizzando gli strumenti di visualizzazione presenti nelle nostre **charts.markdown**.

## 4. Validazione dei Risultati
Attraverso questo framework, il nostro obiettivo è mappare il ciclo di vita del "Global Phenomenon" descritto in **cluster01.markdown**. Incrociando i dati estratti con le linee guida per la gestione turistica in **guide.markdown**, intendiamo offrire non solo una misurazione dell'impatto, ma uno strumento predittivo per supportare i decisori pubblici nel bilanciare la visibilità cinematografica con la vivibilità locale.

<div class="row pt-4">
    <div class="col-md-12 text-center">
        <blockquote class="blockquote">
            "La nostra metodologia trasforma il rumore digitale in evidenza empirica, permettendoci di osservare il CineTourism non come un evento isolato, ma come un processo evolutivo."
        </blockquote>
    </div>
</div>