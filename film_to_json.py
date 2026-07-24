
# git status
# git add .
# git commit -m "Update cluster pages"
# git pull


import json
import os

# === LISTA COMPLETA DELLE PRODUZIONI ===
produzioni = [
    {"nome": "avengers age of ultron", "locations": ["bard", "vèrres", "pont-saint-martin"], "tipo": "film_int",
     "actors": ["robert downey jr", "chris evans", "chris hemsworth"],
     "characters": ["iron man", "tony stark", "captain america", "thor", "ultron"],
     "aliases": ["avengers", "age of ultron", "marvel"],
     "dates": {"global_start": "2013-04-22", "global_end": "2026-06-01"},
     "milestones": [
         {"date": "2015-04-22", "name": "Theatrical Release (Apr 2015)", "color": "#8B0000"},
     ],
     "budget": 365000000,  # USD
     "fonti_dati": {}
    },

    {"nome": "un mondo a parte", "locations": ["opi", "pescasseroli"], "tipo": "film_ita",
     "actors": ["antonio albanese", "virginia raffaele"],
     "characters": ["michele cortese", "agnese"],
     "aliases": ["un mondo a parte"],
     "dates": {"global_start": "2023-01-01", "global_end": "2026-06-01"},
     "milestones": [
         {"date": "2024-03-28", "name": "Theatrical Release (Mar 2024)", "color": "#8B0000"},
         {"date": "2026-01-15", "name": "Streaming Release (Jan 2026)", "color": "#006400"},
     ],
     "budget": 9000000,  # EUR
     "fonti_dati": {}
    },

    {"nome": "rocco schiavone", "locations": ["aosta"], "tipo": "serie_ita",
     "actors": ["marco giallini"],
     "characters": ["rocco schiavone"],
     "aliases": ["schiavone", "rocco schiavone"],
     "dates": {},
     "milestones": [],
     "budget": None,
     "fonti_dati": {}
    },

    {"nome": "un passo dal cielo", "locations": ["braies", "san vito di cadore", "san candido"], "tipo": "serie_ita",
     "actors": ["terence hill", "daniele liotti", "enrico ianniello"],
     "characters": ["pietro thiene", "francesco neri", "vincenzo nappi"],
     "aliases": ["un passo dal cielo"],
     "dates": {"global_start": "2011-01-01", "global_end": "2026-06-01"},
     "milestones": [
         {"date": "2011-04-10", "name": "Season 1 Premiere - Terence Hill", "series": "Un Passo Dal Cielo 1", "color": "#1E90FF"},
         {"date": "2012-10-14", "name": "Season 2 Premiere - Terence Hill", "series": "Un Passo Dal Cielo 2", "color": "#1E90FF"},
         {"date": "2015-01-08", "name": "Season 3 Premiere - Terence Hill Finale", "series": "Un Passo Dal Cielo 3", "color": "#1E90FF"},
         {"date": "2017-01-17", "name": "Season 4 Premiere - Daniele Liotti Debut", "series": "Un Passo Dal Cielo 4", "color": "#FF8C00"},
         {"date": "2019-09-12", "name": "Season 5 Premiere - Daniele Liotti", "series": "Un Passo Dal Cielo 5", "color": "#FF8C00"},
         {"date": "2021-04-01", "name": "Season 6 Premiere - I Guardiani (Veneto Shift)", "series": "Un Passo Dal Cielo 6", "color": "#4B0082"},
         {"date": "2023-03-30", "name": "Season 7 Premiere - Giusy Buscemi Lead", "series": "Un Passo Dal Cielo 7", "color": "#4B0082"},
         {"date": "2025-01-09", "name": "Season 8 Premiere - Eco & Climate Focus", "series": "Un Passo Dal Cielo 8", "color": "#4B0082"},
     ],
     "budget": None,
     "fonti_dati": {}
    },

    {"nome": "benvenuti al sud", "locations": ["castellabate"], "tipo": "film_ita",
     "actors": ["claudio bisio", "alessandro siani", "angela finocchiaro"],
     "characters": ["alberto colombo", "mattia"],
     "aliases": ["benvenuti al sud"],
     "dates": {"global_start": "2008-01-01", "global_end": "2026-06-01"},
     "milestones": [
         {"date": "2009-09-01", "name": "Start of film shooting (Sep 2009)", "color": "#006400"},
         {"date": "2010-10-01", "name": "Theatrical Release (Oct 2010)", "color": "#8B0000"},
     ],
     "budget": 4500000,  # EUR
     "fonti_dati": {}
    },

    {"nome": "call me by your name", "locations": ["crema"], "tipo": "film_int",
     "actors": ["timothée chalamet", "armie hammer", "michael stuhlbarg"],
     "characters": ["elio", "oliver"],
     "aliases": ["call me by your name", "cmbyn"],
     "dates": {"global_start": "2014-01-01", "global_end": "2026-06-01"},
     "milestones": [
         {"date": "2016-05-01", "name": "Start of film shooting (May 2016)", "color": "#006400"},
         {"date": "2017-10-25", "name": "Theatrical Release abroad (Oct 2017)", "color": "#8B0000"},
         {"date": "2018-01-25", "name": "Theatrical Release in Italy (Jan 2018)", "color": "#1F4E79"},
     ],
     "budget": 3500000,  # USD
     "fonti_dati": {}
    },

    {"nome": "curon", "locations": ["curon venosta"], "tipo": "serie_ita",
     "actors": ["valeria bilello", "federico russo", "margherita morchio"],
     "characters": ["anna", "mauro", "daria", "thomas"],
     "aliases": ["curon"],
     "dates": {"global_start": "2018-06-10", "global_end": "2026-06-01"},
     "milestones": [
         {"date": "2020-06-10", "name": "Streaming Release (Jun 2020)", "color": "#006400"},
     ],
     "budget": None,
     "fonti_dati": {}
    },

    {"nome": "don matteo", "locations": ["gubbio", "spoleto"], "tipo": "serie_ita",
     "actors": ["terence hill", "nino frassica", "raoul bova"],
     "characters": ["don matteo", "cecchini", "don massimo"],
     "aliases": ["don matteo"],
     "dates": {"global_start": "2011-01-01", "global_end": "2026-06-01"},
     "milestones": [
         {"date": "2013-05-01", "name": "Start of film shooting (May 2011)", "color": "#006400"},
         {"date": "2014-01-09", "name": "Release on TV (Jan 2014-ongoing)", "color": "#8B0000"},
     ],
     "budget": None,
     "fonti_dati": {}
    },

    {"nome": "the twilight saga: new moon", "locations": ["montepulciano", "volterra"], "tipo": "film_int",
     "actors": ["kristen stewart", "robert pattinson", "taylor lautner"],
     "characters": ["bella", "edward", "jacob", "volturi"],
     "aliases": ["twilight", "new moon"],
     "dates": {"global_start": "2007-11-18", "global_end": "2026-06-01"},
     "milestones": [
         {"date": "2009-11-18", "name": "Theatrical Release (Nov 2009)", "color": "#8B0000"},
     ],
     "budget": 50000000,  # USD
     "fonti_dati": {}
    },

    {"nome": "i medici - masters of florence", "locations": ["pienza"], "tipo": "serie_int",
     "actors": ["richard madden", "dustin hoffman", "stuart martin"],
     "characters": ["cosimo de medici", "giovanni de medici", "lorenzo de medici"],
     "aliases": ["i medici", "medici", "masters of florence"],
     "dates": {"global_start": "2014-10-18", "global_end": "2026-06-01"},
     "milestones": [
         {"date": "2016-10-18", "name": "Season 1 (Oct 2016)", "color": "#006400"},
         {"date": "2018-10-23", "name": "Season 2 (Oct 2018)", "color": "#006400"},
         {"date": "2019-12-02", "name": "Season 3 (Dic 2019)", "color": "#006400"},
     ],
     "budget": None,
     "fonti_dati": {}
    },

    {"nome": "il giovane montalbano", "locations": ["ragusa", "santa croce camerina", "scicli"], "tipo": "serie_ita",
     "actors": ["michele riondino", "alessio vassallo", "andrea tidona"],
     "characters": ["salvo montalbano", "mimì augello", "fazio", "catarella", "livia"],
     "aliases": ["montalbano", "giovane montalbano", "commissario montalbano"],
     "dates": {"global_start": "2012-02-23", "global_end": "2015-12-31"},
     "milestones": [
         {"date": "2012-02-23", "name": "Debut - Il giovane Montalbano", "series": "Young Montalbano Era iniziale", "color": "#2E8B57"},
         {"date": "2012-03-01", "name": "Consolidamento serie e successo pubblico", "series": "Crescita popolarità", "color": "#3CB371"},
         {"date": "2015-10-01", "name": "Chiusura produzione serie", "series": "Fine prequel era", "color": "#6B8E23"}
     ],
     "budget": None,
     "fonti_dati": {}
    }
]

# === CARTELLA DI OUTPUT ===
output_dir = "_g4-2026-website/Film_Scheda_Json"
os.makedirs(output_dir, exist_ok=True)

# === GENERAZIONE AUTOMATICA DEI FILE JSON ===
for p in produzioni:
    filename = p["nome"].replace(" ", "-").replace(":", "").lower() + ".json"
    filepath = os.path.join(output_dir, filename)

    # aggiungo il campo locandina
    p["locandina"] = {
        "img": f"/assets/locandine/{filename.replace('.json', '.jpg')}",
        "alt": f"Locandina del film {p['nome']}"
    }

    # aggiungo fonti_dati dinamiche
    p["fonti_dati"] = {
        "istat": {
            "descrizione": "Indicatori comunali ISTAT/MiC-MiBACT (CIS, RGR)",
            "link": "https://www.istat.it/it/dati-analisi-e-prodotti"
        },
        "openstreetmap": {
            "descrizione": "Analisi dell’ecosistema commerciale locale (POI entro 5 km)",
            "link": "https://www.openstreetmap.org/"
        },
        "google_news": {
            "descrizione": "Articoli estratti tramite Google News API, analisi sentiment e topic modeling",
            "parole_chiave": [p["nome"], *p["locations"], "turismo", "economia locale"]
        },
        "reddit": {
            "descrizione": "Analisi del discorso della community tramite API PullPush",
            "subreddit": ["r/italy", "r/travel", "r/movies", "r/europe", "r/turismo"]
        },
        "youtube": {
            "descrizione": "Commenti ai video girati nelle location tramite YouTube Data API v3",
            "query": [p["nome"] + " " + loc for loc in p["locations"]]
        },
        "google_trends_wikipedia": {
            "descrizione": "Interesse informativo e comportamento di ricerca",
            "voci_wikipedia": p["locations"]
        },
        "getyourguide": {
            "descrizione": "Analisi dei tour e delle recensioni (topic modeling + sentiment)",
            "link": "https://www.getyourguide.com/"
        }
    }

    # salvo il JSON
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(p, f, indent=4, ensure_ascii=False)

print("JSON generati correttamente!")
