---
layout: default
title: "Risultati dell'Analisi"
vega: true
header_type: hero
header_img: assets/images/header.svg
header_title: "Risultati dell'Analisi"
subtitle: "Lettura territoriale integrata: ISTAT e OpenStreetMap"
---

<div style="width: 100%; max-width: 850px; margin: 30px auto 50px auto; text-align: center;">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 420" width="100%" height="auto">
    <defs>
      <!-- Ombreggiatura per i blocchi -->
      <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">
        <feDropShadow dx="0" dy="5" stdDeviation="5" flood-color="#000000" flood-opacity="0.12"/>
      </filter>
      
      <!-- Punta delle frecce -->
      <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 0 L 10 5 L 0 10 z" fill="#94A3B8" />
      </marker>
      
      <!-- Gradienti moderni per i 3 pilastri e il risultato -->
      <linearGradient id="grad-istat" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#3B82F6"/> <!-- Blue -->
        <stop offset="100%" stop-color="#1E3A8A"/>
      </linearGradient>
      
      <linearGradient id="grad-osm" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#10B981"/> <!-- Emerald Green -->
        <stop offset="100%" stop-color="#064E3B"/>
      </linearGradient>
      
      <linearGradient id="grad-digital" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#F59E0B"/> <!-- Amber/Orange -->
        <stop offset="100%" stop-color="#78350F"/>
      </linearGradient>
      
      <linearGradient id="grad-iit" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#1E293B"/> <!-- Slate Dark -->
        <stop offset="100%" stop-color="#020617"/>
      </linearGradient>
    </defs>

    <!-- Titolo Infografica -->
    <text x="400" y="30" fill="#475569" font-family="system-ui, -apple-system, sans-serif" font-size="16" font-weight="800" text-anchor="middle" letter-spacing="2">PIPELINE METODOLOGICA INTEGRATA</text>

    <!-- ================= PILASTRI ================= -->
    
    <!-- 1. ISTAT -->
    <rect x="40" y="60" width="220" height="110" rx="14" fill="url(#grad-istat)" filter="url(#shadow)"/>
    <text x="150" y="105" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="22" font-weight="bold" text-anchor="middle">ISTAT</text>
    <text x="150" y="135" fill="#DBEAFE" font-family="system-ui, -apple-system, sans-serif" font-size="15" font-weight="500" text-anchor="middle">Macro-data</text>

    <!-- 2. OpenStreetMap -->
    <rect x="290" y="60" width="220" height="110" rx="14" fill="url(#grad-osm)" filter="url(#shadow)"/>
    <text x="400" y="105" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="22" font-weight="bold" text-anchor="middle">OpenStreetMap</text>
    <text x="400" y="135" fill="#D1FAE5" font-family="system-ui, -apple-system, sans-serif" font-size="15" font-weight="500" text-anchor="middle">Urban Ecosystem</text>

    <!-- 3. Digital Platforms -->
    <rect x="540" y="60" width="220" height="110" rx="14" fill="url(#grad-digital)" filter="url(#shadow)"/>
    <text x="650" y="105" fill="#FFFFFF" font-family="system-ui, -apple-system, sans-serif" font-size="22" font-weight="bold" text-anchor="middle">Digital Platforms</text>
    <text x="650" y="135" fill="#FEF3C7" font-family="system-ui, -apple-system, sans-serif" font-size="15" font-weight="500" text-anchor="middle">Trends &amp; Sentiment</text>

    <!-- ================= FRECCE DI COLLEGAMENTO ================= -->
    <!-- Linea Sinistra -->
    <path d="M 150 170 C 150 240, 330 220, 360 280" fill="none" stroke="#94A3B8" stroke-width="4" stroke-dasharray="6,4" marker-end="url(#arrow)"/>
    <!-- Linea Centrale -->
    <path d="M 400 170 L 400 280" fill="none" stroke="#94A3B8" stroke-width="4" stroke-dasharray="6,4" marker-end="url(#arrow)"/>
    <!-- Linea Destra -->
    <path d="M 650 170 C 650 240, 470 220, 440 280" fill="none" stroke="#94A3B8" stroke-width="4" stroke-dasharray="6,4" marker-end="url(#arrow)"/>

    <!-- ================= RISULTATO FINALE (IIT) ================= -->
    <rect x="225" y="290" width="350" height="100" rx="16" fill="url(#grad-iit)" filter="url(#shadow)"/>
    <text x="400" y="335" fill="#F8FAFC" font-family="system-ui, -apple-system, sans-serif" font-size="22" font-weight="bold" text-anchor="middle">L'Indice di Impatto</text>
    <text x="400" y="365" fill="#38BDF8" font-family="system-ui, -apple-system, sans-serif" font-size="24" font-weight="900" text-anchor="middle">Territoriale (IIT)</text>
  </svg>
</div>


## Lettura territoriale integrata: ISTAT e OpenStreetMap

Seguendo e adattando l’impostazione multidimensionale utilizzata da ISTAT per la lettura dei fenomeni territoriali, gli 82 (81+1) indicatori mappati possono essere ricondotti a sei aree tematiche:

*   **Domanda turistica e flussi:** arrivi, presenze, intensità turistica e componente non residente.
*   **Offerta ricettiva e capacità di accoglienza:** esercizi, densità ricettiva, letti alberghieri ed extra-alberghieri.
*   **Cultura, patrimonio e attrattori territoriali:** musei, monumenti, luoghi della cultura e relativi visitatori.
*   **Imprese, occupazione e lavoro:** unità locali, addetti, servizi al consumatore e composizione della forza lavoro.
*   **Mobilità e infrastrutture locali:** trasporto collettivo e dotazioni funzionali alla fruizione del territorio.
*   **Demografia, ambiente e contesto territoriale:** popolazione, composizione demografica, rifiuti e altre variabili ambientali e territoriali.

Per **evidenza** si intende qui un segnale statistico basato sull’analisi delle 1.621 serie storiche mappate lungo 82 indicatori che ha superato le nostre soglie di robustezza (CIS, RGR). 

### L'Indice di Impatto Territoriale (IIT)

Definiamo ora per ciascuna opera audiovisiva investigata un **Indice di Impatto Territoriale (IIT)** quale indice descrittivo e comparativo che combina, con uguale peso:
1.  **Numero di evidenze** associate all’opera;
2.  **Forza media delle evidenze**, misurata dal CIS medio;
3.  **Ampiezza tematica**, misurata dal numero di aree tematiche interessate.

Dove:
*   $E$ = n. evidenze forti associate all’opera
*   $E_{max}$ = massimo n. evidenze osservato
*   $\overline{CIS}$ = CIS medio dell’opera
*   $A$ = n. aree tematiche interessate
*   $A_{max}$ = massima ampiezza tematica osservata

L’IIT sintetizza per ciascuna opera investigata il suo impatto su metriche territoriali ISTAT, basandosi sull’importanza relativa del portafoglio di evidenze che hanno passato il nostro screening, approssimata combinando numero, intensità e ampiezza tematica di queste.

---

## Matrice per il calcolo dell’Indice di Impatto Territoriale

| Opera | Location considerate | N. evidenze | Distribuzione per area tematica | N. aree tematiche | CIS medio | IIT |
| :--- | :--- | :---: | :--- | :---: | :---: | :---: |
| **I Medici – Masters of Florence** | Pienza | 5 | Domanda turistica e flussi: 2<br>Imprese, occupazione e lavoro: 2<br>Demografia, ambiente e contesto: 1 | 3 | 100,0 | **100,0** |
| **Call Me by Your Name** | Crema | 4 | Domanda turistica e flussi: 3<br>Cultura, patrimonio e attrattori: 1 | 2 | 97,4 | **81,4** |
| **Il giovane Montalbano** | Scicli e Ragusa | 3 | Offerta ricettiva e accoglienza: 2<br>Mobilità e infrastrutture locali: 1 | 2 | 88,8 | **71,8** |
| **Avengers: Age of Ultron** | Bard e Pont-Saint-Martin | 3 | Offerta ricettiva e accoglienza: 3 | 1 | 100,0 | **64,4** |
| **Rocco Schiavone** | Aosta | 1 | Offerta ricettiva e accoglienza: 1 | 1 | 100,0 | **51,1** |
| **Curon** | Curon Venosta | 1 | Demografia, ambiente e contesto: 1 | 1 | 100,0 | **51,1** |
| **Benvenuti al Sud** | Castellabate | 1 | Offerta ricettiva e accoglienza: 1 | 1 | 93,3 | **48,9** |
| **Elisa di Rivombrosa** | Agliè | 1 | Cultura, patrimonio e attrattori: 1 | 1 | 93,3 | **48,9** |

---

## Integrazione con OpenStreetMap: Raggruppamento Ex-Post

Integrando l’analisi effettuata sulla base delle evidenze ISTAT emerse con i dati raccolti da OpenStreetMap (OSM), è possibile affinare la lettura dell’IIT e giungere a una valutazione complessiva e differenziata dell’impatto territoriale delle varie opere. I dati OSM non costituiscono una settima area tematica, ma descrivono la materializzazione fisica dell’ecosistema turistico intorno ai set: alloggi, ristorazione, attrazioni, servizi e attività rivolte ai visitatori.

L’analisi integrata suggerisce **quattro tipi di impatti**:

### 1. Impatto multidimensionale e trasformativo (Demand-led)
*Riferito a: I Medici e Call Me By Your Name.*

In questi casi il cineturismo appare soprattutto come attivazione di interesse, visite e consumo culturale. Per **Pienza**, in particolare, la domanda turistica si accompagna a segnali relativi al lavoro e al contesto locale, configurando il profilo più ampio e multidimensionale. La dinamica sottostante è trainata dall’aumento di desiderabilità del luogo: il pubblico riconosce la location, la associa alla storia o ai personaggi e vuole visitarla direttamente. Un effetto demand-led è più probabile quando la location è riconoscibile e centrale nella narrazione, il pubblico è ampio o internazionale, la destinazione è accessibile ed il luogo è già inserito in un circuito turistico fruibile.

Le evidenze OSM corroborano questa appartenenza:
*   A **Pienza** le attività turistiche mappate crescono da 96 nel 2014 a 290 all’inizio del 2026, molto più rapidamente dei negozi di vicinato (passati da 14 a 57). Il segnale ISTAT si associa quindi a una progressiva specializzazione dell’economia locale verso turismo e accoglienza.
*   A **Crema**, la crescita da 13 attività turistiche all’inizio del 2017 a 20 nell’aprile 2018 è più circoscritta, ma temporalmente vicina all’uscita del film e coerente con il profilo ISTAT fondato su arrivi, presenze, turisticità e fruizione culturale. 

*Sintesi:* Pienza presenta una trasformazione territoriale più ampia; Crema una dinamica più chiaramente trainata dalla domanda e dalla riconoscibilità culturale.

### 2. Impatto prevalentemente ricettivo (Supply-led)
*Riferito a: Avengers, Benvenuti al Sud, Rocco Schiavone e, in parte, Il giovane Montalbano.*

In questi casi il cineturismo appare soprattutto come adattamento economico e ricettivo del territorio: aumenta la capacità di accoglienza in risposta a una domanda osservata, attesa o percepita. Tale dinamica può derivare dall’apertura o conversione di alloggi, dalle aspettative degli operatori, dalla permanenza di troupe e visitatori o dalla necessità di rafforzare servizi già insufficienti rispetto alla nuova visibilità.

OpenStreetMap rafforza soprattutto il caso di **Bard**. Le evidenze ISTAT di *Avengers* sono molto intense ma concentrate sui letti alberghieri ed extra-alberghieri; parallelamente, le attività turistiche mappate intorno al Forte passano da circa 40 alla fine del 2014 a oltre 100 nel 2015, proseguendo fino a superare le 240 nel 2026. Il profilo non appare limitato a un aumento dei posti letto, ma si estende a una più generale densificazione dei servizi turistici. **Castellabate** rimane invece un caso di forte shock ricettivo verticale: l’incremento ISTAT dei letti extra-alberghieri è eccezionale, ma non è accompagnato da una diffusione comparabile in altre aree tematiche.

### 3. Impatto “mordi e fuggi”
*Riferito a: Twilight, Un Mondo a Parte e le location di Un passo dal cielo.*

Questo gruppo comprende esclusivamente opere e località per le quali non sono emerse evidenze ISTAT finali e va interpretato con cautela. La presenza di segnali molto forti in OSM potrebbe indicare che il cineturismo si sia manifestato attraverso canali non pienamente intercettati dalle statistiche ufficiali: ad esempio un’offerta locale insufficiente, escursioni giornaliere, turismo “mordi e fuggi” o visite orientate alla produzione di contenuti social senza pernottamento.

*   A **Montepulciano**, le attività turistiche censite passano da zero nel 2007 a oltre 380 nel 2026, mentre i negozi ordinari si fermano a 99. Emerge una forte specializzazione turistica di lungo periodo, difficilmente attribuibile alla sola *Twilight*, considerata l'attrattività preesistente della destinazione. 
*   Le location di **Un passo dal cielo** mostrano una crescita marcata e cumulativa: **San Candido** passa da 22 attività turistiche nel 2011 a 197 nel 2026, **Braies** da 21 a 105 e **San Vito di Cadore** da 57 a 93 (con un'accelerazione coincidente con il trasferimento del set nel 2021).
*   A **Opi e Pescasseroli** (*Un mondo a parte*), OSM intercetta una dinamica emergente e intermittente: un primo incremento dopo l’uscita cinematografica, una stabilizzazione, e una nuova crescita con la distribuzione in streaming.

### 4. Impatto focalizzato o indiretto
*Riferito a: Elisa di Rivombrosa, Curon e, in parte, Il giovane Montalbano.*

Casi in cui il segnale si concentra in un ambito specifico (attrattore) oppure compare in dimensioni non strettamente turistiche. 
*   Ad **Agliè**, l’evidenza riguarda direttamente i visitatori del Palazzo Ducale, creando un legame riconoscibile tra opera e bene culturale.
*   A **Scicli**, la crescita dei letti extra-alberghieri è accompagnata da un segnale relativo alla mobilità (ricaduta indiretta).
*   A **Curon** emerge una variazione demografica meno direttamente interpretabile come effetto turistico, da leggere con particolare cautela.

---

## Sintesi

Nel complesso, questo raggruppamento ex-post integra e raffina il raggruppamento iniziale ex-ante. Considerato che per Volterra e Montepulciano non sono emerse evidenze ISTAT forti, la scala internazionale dell’opera, da sola, non sembra determinare né una maggiore intensità misurabile né uno specifico tipo di impatto. Gli esiti dipendono quindi dall’interazione tra visibilità dell’opera, riconoscibilità della location, accessibilità, vocazione turistica preesistente e capacità del territorio di trasformare l’attenzione in domanda, servizi e infrastrutture.

> **Nota:** Le serie OSM descrivono l’evoluzione delle attività mappate e non un censimento amministrativo delle effettive aperture. Nei casi privi di conferma ISTAT costituiscono quindi evidenze territoriali esplorative, utili a integrare e problematizzare il quadro, ma non prove causali autonome.

---

## Lettura digitale integrata: Google News e digital platforms
**(Google Trends, Reddit, YouTube)**

Si evidenzia una profonda differenza strutturale tra un interesse forte e stabile (come nel caso di **Crema**) rispetto a un interesse periodico e caratterizzato da forti oscillazioni (come nel caso di **Castellabate**), configurando una chiara dicotomia tra **stabilità vs volatilità** dell'attenzione digitale.


<div class="row">
    <div class="col-md-4">
        <div class="card mb-4 shadow-sm">
            <div class="card-body">
                <h5 class="card-title">Gruppo 1</h5>
                <p class="card-text">Il Fenomeno Globale: Impatto improvviso e alta volatilità.</p>
                <a href="{{site.baseurl}}/group1.html" class="btn btn-primary">Vai al Gruppo 1</a>
            </div>
        </div>
    </div>
    <div class="col-md-4">
        <div class="card mb-4 shadow-sm">
            <div class="card-body">
                <h5 class="card-title">Gruppo 2</h5>
                <p class="card-text">Destinazioni Radicate: Crescita sostenibile e integrazione locale.</p>
                <a href="{{site.baseurl}}/group2.html" class="btn btn-primary">Vai al Gruppo 2</a>
            </div>
        </div>
    </div>
    <div class="col-md-4">
        <div class="card mb-4 shadow-sm">
            <div class="card-body">
                <h5 class="card-title">Gruppo 3</h5>
                <p class="card-text">Set di Nicchia: Impatto focalizzato e target specifico.</p>
                <a href="{{site.baseurl}}/group3.html" class="btn btn-primary">Vai al Gruppo 3</a>
            </div>
        </div>
    </div>
</div>