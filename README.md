
# Python Einführungskurs

# 1 📋 Übersicht

Dieses Repository enthält Materialien für einen Python-Einführungskurs auf Deutsch mit interaktiven Jupyter Notebooks und Übungsdatensätzen.

# 2 🗂️ Repository-Struktur

```
Python_Intro/
├── 01_notebook/                    # Jupyter Notebooks
│   ├── B101_Intro_Python.ipynb     # Python-Grundlagen (Basis)
│   ├── T101_Intro_Python.ipynb     # Python-Grundlagen (Tutorial)
│   └──X101_Exkurse_Python.ipynb   # Exkurse & Vertiefungen
├── 02_daten/                       # Übungsdatensätze
│   ├── titanic.csv / .xlsx         # ML-Datensatz
│   ├── Kundendaten.json / .xlsx    # JSON- und Excel-Beispieldaten
│   ├── chinook.db                  # SQLite-Datenbank (Musik)
│   ├── northwind.db                # SQLite-Datenbank (Handel)
│   └── weitere Dateien...          # CSV, TXT, LOG-Dateien
├── 03_skript/                      # Dokumentation und Kursskript
│   └── PY Skript V3.pdf            # Kursskript
├── 04_modul/                       # Wiederverwendbare Python-Module
│   ├── my_modul.py                 # Hilfsfunktionen (fib_r, caesar, swap_case)
│   ├── class_auto.py               # OOP-Beispielklasse
│   └── inspect_modul.py            # Modul-Inspektion und Analyse
├── LICENSE                         # MIT-Lizenz
└── README.md                       # Diese Datei
```

# 3 📋 Verfügbare Kursmaterialien

## 3.1 **01_notebook/** - Jupyter Notebooks

| Notebook | Typ | Beschreibung |
|----------|-----|--------------|
| `B101_Intro_Python.ipynb` | Basis | Python-Grundlagen — Hauptnotebook für den Kurs |
| `T101_Intro_Python.ipynb` | Tutorial | Tutorial-Version mit Schritt-für-Schritt-Anleitungen |
| `X101_Exkurse_Python.ipynb` | Exkurs | Vertiefende Themen und Exkurse |

## 3.2 **02_daten/** - Übungsdatensätze

**CSV/Datenbank-Dateien:**
- `titanic.csv` / `titanic.xlsx` - Titanic-Passagierdaten für ML-Übungen
- `demofile.csv` - Allgemeine CSV-Demonstrationsdatei
- `urls.csv` - URL-Liste für Web-Scraping-Übungen
- `chinook.db` - SQLite-Datenbank (Musikshop) für SQL-Übungen
- `northwind.db` - SQLite-Datenbank (Handelsunternehmen) für SQL-Übungen

**Excel/JSON-Dateien:**
- `Kundendaten.json` - Kundendaten im JSON-Format
- `Kundendaten.xlsx` - Kundendaten in Excel-Format
- `Wasserfall.xlsx` - Excel-Datei für Wasserfalldiagramme

**Text/Log-Dateien:**
- `datei_in.txt` - Textdatei für Datei-I/O-Übungen
- `logdatei` - Log-Datei für Parsing-Übungen

## 3.3 **03_skript/** - Dokumentation

- `PY Skript V3.pdf` - Kursskript (PDF-Version)

## 3.4 **04_modul/** - Python-Module

Wiederverwendbare Python-Module, die in den Notebooks importiert werden:

| Modul | Beschreibung |
|-------|--------------|
| `my_modul.py` | Hilfsfunktionen: Fibonacci (`fib_r`), Caesar-Chiffre (`caesar`), String-Manipulation (`swap_case`) |
| `class_auto.py` | OOP-Beispielklasse `Auto` für Objektorientierungs-Übungen |
| `inspect_modul.py` | Modul-Inspektion und Analyse mit `inspect` |

# 4 🛠️ Technisches Setup

**Systemvoraussetzungen:**
- Browser mit Internet-Zugang
- Google-Account
- Google Colab (keine lokale Installation erforderlich)

# 5 ⚖️ Lizenzen

Der **Quellcode** steht unter der [MIT License](./LICENSE).       

Die **Kursmaterialien** können frei verwendet, modifiziert und weiterverbreitet werden, soweit keine abweichenden Rechte Dritter oder gesonderten Lizenzhinweise angegeben sind.   

**Northwind SQLite-Datenbank**: basiert auf Microsofts Northwind-Beispieldatenbank. Die hier verwendete SQLite-Version stammt aus dem Projekt `jpwhite3/northwind-SQLite3` und steht unter der MIT License (Copyright © 2016 JP White); siehe [`Licence NorthwindDB.md`](./02_daten/Licence%20NorthwindDB.md). Microsofts SQL-Server-Samples, einschließlich Northwind/Pubs, stehen ebenfalls unter MIT License (Copyright Microsoft Corporation).   

**Chinook SQLite-Datenbank**: stammt aus dem Projekt `lerocha/chinook-database` und steht unter der MIT License (Copyright © 2008-2024 Luis Rocha); siehe [`Licence ChinookDB.md`](./02_daten/Licence%20ChinookDB.md).   
