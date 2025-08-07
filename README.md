# 1 Python Einführungskurs

Dieses Repository enthält Materialien für einen einführenden Python-Programmierkurs mit Jupyter Notebooks und Python-Modulen, die grundlegende Programmierkonzepte abdecken.

## 1.1 Repository-Struktur

```
Python_Intro/
├── 01 ipynb/                    # Hauptverzeichnis für Kursmaterialien
│   ├── B000-launch.ipynb        # Kursstart/Einführungs-Notebook
│   ├── B030-Gemini-Colab.ipynb # Google Colab und Gemini Integration
│   ├── B100-Intro-Python_.ipynb # Haupt-Python-Einführungs-Notebook
│   ├── T100-Intro-Python_.ipynb # Tutorial/Übungs-Notebook
│   └── MyPackage/               # Python-Paket mit Kursmodulen
│       ├── Class_Auto.py        # Auto-Klassen-Beispiel für OOP-Konzepte
│       └── MyModul.py          # Hilfsfunktionen-Modul
```

## 1.2 Kursinhalte

### 1.2.1 Notebooks
- **B000-launch.ipynb**: Kurseinführung und Setup
- **B030-Gemini-Colab.ipynb**: Integration mit Google Colab und KI-Tools
- **B100-Intro-Python_.ipynb**: Umfassende Python-Einführung mit grundlegenden Konzepten
- **T100-Intro-Python_.ipynb**: Praktische Tutorials und Übungen

### 1.2.2 Python-Module
- **Class_Auto.py**: Objektorientiertes Programmierbeispiel mit einer Auto-Klasse
- **MyModul.py**: Sammlung von Hilfsfunktionen einschließlich:
  - `fib_r()`: Rekursiver Fibonacci-Sequenz-Generator
  - `swap_case()`: Funktion zur Groß-/Kleinschreibung-Umwandlung
  - `caesar()`: Caesar-Verschlüsselungsfunktion

## 1.3 Erste Schritte

### 1.3.1 Voraussetzungen
- Python 3.x installiert
- Jupyter Notebook oder JupyterLab
- Grundverständnis von Programmierkonzepten (hilfreich, aber nicht erforderlich)

### 1.3.2 Kurs ausführen
1. Dieses Repository klonen
2. Zum Verzeichnis `01 ipynb/` navigieren
3. Jupyter Notebook starten:
   ```bash
   jupyter notebook
   ```
4. Mit `B000-launch.ipynb` für die Kurseinführung beginnen
5. Die Notebooks der Reihe nach durcharbeiten

### 1.3.3 Verwendung der Python-Module
Das `MyPackage`-Verzeichnis enthält wiederverwendbare Python-Module, die importiert werden können:

```python
from MyPackage.Class_Auto import Auto
from MyPackage.MyModul import fib_r, swap_case, caesar

# Ein Auto-Objekt erstellen
mein_auto = Auto("BMW", "X5", "300 PS")
print(mein_auto)

# Hilfsfunktionen verwenden
print(fib_r(10))  # Fibonacci-Zahl
print(swap_case("Hallo Welt"))  # Groß-/Kleinschreibung umwandeln
print(caesar("Hallo", 3))  # Caesar-Verschlüsselung
```

## 1.4 Lernziele

Dieser Kurs behandelt grundlegende Python-Konzepte einschließlich:
- Grundlegende Syntax und Datentypen
- Kontrollstrukturen (Schleifen, Bedingungen)
- Funktionen und Module
- Objektorientierte Programmierung
- Dateienbearbeitung und Datenmanipulation
- Integration mit modernen Tools wie Google Colab
