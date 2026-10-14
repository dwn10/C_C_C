# C_C_C - Mehrsprachiges Entwicklungs- & Projektrepository

<p align="center">
  <strong>Language:</strong>
  <a href="README.md">Español</a> |
  <a href="README.en.md">English</a> |
  <a href="README.de.md">Deutsch</a>
</p>

Willkommen im **C_C_C** Repository. Dieses Projekt vereint eine vielfältige Sammlung von Anwendungen, Lernmodulen, Business-Tools und strukturierter technischer Dokumentation über verschiedene Programmiersprachen und Technologieumgebungen hinweg (**C**, **CONZEPT 16**, **Java**, **Python**, **React/Supabase** und **YEET**).

---

## 📑 Inhaltsverzeichnis

- [Projektstruktur](#-projektstruktur)
- [Modulübersicht](#-modulübersicht)
  - [1. C (Programmiersprache C)](#1-c-programmiersprache-c)
  - [2. CONZEPT 16](#2-conzept-16)
  - [3. JAVA](#3-java)
  - [4. PROJEKT (Inventarsystem)](#4-projekt-inventarsystem)
  - [5. PYTHON](#5-python)
  - [6. YEET (Vectorsoft)](#6-yeet-vectorsoft)
- [Verwendete Technologien](#-verwendete-technologien)
- [Installations- und Bedienungsanleitung](#-installations--und-bedienungsanleitung)
- [Autor](#-autor)

---

## 📁 Projektstruktur

```text
C_C_C/
├── C/                     # Taschenrechner und arithmetische Algorithmen in C und Python
├── CONZEPT_16/            # Module und GUIs auf der CONZEPT 16 Unternehmensplattform
│   ├── Konvertierung/     # Datentypkonvertierung (Alpha, Int, Float, Date, Time etc.)
│   ├── StringKonverter/   # Erweiterte Textverarbeitung und Zeichensätze (OEM, UTF-8 etc.)
│   └── Taschenrechner/    # Grafischer Taschenrechner mit Berechnungshistorie
├── JAVA/                  # Desktop-Anwendungen in Java (Swing & Maven)
│   ├── CRUD/              # Produktverwaltungssystem (Dateibasiert / Lokale Datenbank)
│   └── Calculator/        # Interaktiver Taschenrechner mit Swing-GUI
├── PROJEKT/               # Dokumentation und Architekturentwurf für das Inventarsystem
│   └── Documentation/     # Technische Spezifikationen (Dev, User, Lastenheft, UML, ERD, PDF)
├── PYTHON/                # Microservices und interaktive Web-Tools mit Streamlit
│   ├── E-Rechnung/        # XRechnung-Generator und Validator für das deutsche System
│   ├── Leitweg-ID/        # Leitweg-ID Generator & Prüfsummenvalidierung für Behörden
│   ├── Taschenrechner/    # Python-Rechnermodul
│   └── XmlToPdf/          # Dynamischer XML-Viewer mit Export nach PDF und gefiltertem XML
├── YEET/                  # Low-Code-Dokumentation und Prototypen (Vectorsoft YEET)
│   ├── Documentation/     # Offizielles Handbuch im PDF-Format
│   └── README.md          # Anleitungen zur Scanner-Integration (Barcode / QR-Code)
├── README.md              # Hauptdokumentation des Repositorys (Spanisch)
├── README.en.md           # Englische Dokumentation
└── README.de.md           # Deutsche Dokumentation
```

---

## 🔍 Modulübersicht

### 1. C (Programmiersprache C)
* **Zweck:** Grundlagen der prozeduralen Programmierung, Binärarithmetik und Konsolen-Ein-/Ausgabe.
* **Wichtige Dateien:**
  * `calculadora.c`, `calculator.c`, `taschenrechner.c`: Taschenrechner-Implementierungen mit Grundrechenarten (+, -, *, /, %), Ziffernlöschung und Vorzeichenwechsel.
  * `cal_simple.c`, `tasch_simple.c`: Schlanke Versionen für die schnelle Konsolenausführung.
  * `calculadora.py`, `taschenrechner.py`: Äquivalente Python-Skripte zum direkten Vergleich zwischen kompilierten und interpretierten Sprachen.
  * Vorkompilierte `.exe`-Binärdateien für Windows.

### 2. CONZEPT 16
* **Zweck:** Entwicklung grafischer Benutzeroberflächen (GUI) und ereignisgesteuerte Logik auf der relationalen Entwicklungsplattform **CONZEPT 16** (Vectorsoft).
* **Teilprojekte:**
  * **`Konvertierung/`:** Interaktives Tool zur Konvertierung verschiedener Datentypen (`Alpha`, `Int`, `BigInt`, `Float`, `Decimal`, `Time`, `Date` sowie Checkbox-Werte).
  * **`StringKonverter/`:** Texttransformationen und Kodierungskonvertierungen (`OEM`, `ANSI`, `HTML`, `URI`, `UTF-8`, `Base64`), Groß-/Kleinschreibung, Namensumordnung und Behandlung deutscher Umlaute.
  * **`Taschenrechner/`:** Vollständiger GUI-Taschenrechner mit Ausgabefeld, Funktionstasten und persistenter Historienliste (`LastLineDataList`).

### 3. JAVA
* **Zweck:** Objektorientierte Programmierung mit Java Swing-Komponenten und Maven-Projektverwaltung.
* **Teilprojekte:**
  * **`CRUD/` (`pryArchivos`):** Produkt- und Bestandsverwaltung mit Benutzeroberflächen (`FrmGestionProductos`, `FrmProductos`), strukturierter Speicherung in Textdateien und Datenbankanbindung.
  * **`Calculator/`:** Desktop-Taschenrechner aufgebaut mit `JFrame`, `JPanel` und Ereignisbehandlung über `ActionListener`.

### 4. PROJEKT (Inventarsystem)
* **Zweck:** Umfassende technische Dokumentation und Softwarearchitektur für ein vollwertiges **Inventarsystem** auf Basis von **React** (Frontend) und **Supabase / PostgreSQL** (Backend).
* **Dokumentationsbestandteile:**
  * **`Markdown/`:**
    * `README.md`: Projektphasen, Meilensteine und methodischer Überblick.
    * `Dev.md`: Entwicklerhandbuch, VS-Code-Konfiguration, Datenbankschemata und API-Aufrufe.
    * `User.md`: Benutzerdokumentation für den täglichen Betriebsablauf.
    * `Lastenheft.md`: Anforderungskatalog und Funktionsumfang.
    * `DB-Inventar.md`: Tabellendefinitionen, Relationen, Indizes und Constraints in Supabase/PostgreSQL.
    * `UML-Diagramme.md` & `DiagrammeIMG.md`: Anwendungsfalldiagramme, Prozessketten (eEPK) und Architekturübersichten.
    * `Links.md`: Ressourcen, Dokumentationslinks und Projekttools.
  * **`PDF/`:** Projektabschluss-Präsentation (`Präsentation_D-Paz.pdf`).

### 5. PYTHON
* **Zweck:** Interaktive Web-Anwendungen und Automatisierungstools auf Basis des **Streamlit**-Frameworks.
* **Teilprojekte:**
  * **`E-Rechnung/`:** Erstellung und Validierung elektronischer Rechnungen im Standard **XRechnung** (XML/JSON) mit automatischer Steuerberechnung und Leitweg-ID-Prüfung.
  * **`Leitweg-ID/`:** Offizieller Leitweg-ID-Generator und Validator für öffentliche Auftraggeber in Deutschland (Bundesland-Codes, Postleitzahlen und Prüfzifferberechnung).
  * **`XmlToPdf/`:** Analyse von XML-Dateien mit tabellarischer Darstellung in DataFrames und Export gefilterter Datensätze als formatierte PDF- oder XML-Dateien.
  * **`Taschenrechner/`:** Rechner-Skript in Python.

### 6. YEET (Vectorsoft)
* **Zweck:** Technische Anleitungen und Integrationsbeispiele für die Low-Code-Plattform **YEET** von Vectorsoft.
* **Besonderheiten:**
  * JavaScript-Logik (`UI Logic`) zur Anbindung von Barcode- und QR-Code-Scannern über die Kamera.
  * Echtzeitsynchronisation zwischen Tabellenkomponenten (`yTable`) und OData-Entitäten (`apiObject.odata.odataEntityRead`).
  * Vollständiges Referenzhandbuch in `Yeet-Doku-Web.pdf`.

---

## 🛠 Verwendete Technologien

| Kategorie | Technologien / Sprachen |
| :--- | :--- |
| **Programmiersprachen** | C, Java (JDK 8+), Python 3.8+, JavaScript, SQL, CONZEPT 16 |
| **Frameworks & Bibliotheken** | Streamlit, Pandas, Java Swing, Maven, React, TanStack Query |
| **Datenbanken & Backend** | Supabase, PostgreSQL, OData |
| **Standards & Dateiformate** | XRechnung, XML, JSON, PDF |
| **Entwicklungstools** | VS Code, NetBeans, Git |

---

## 🚀 Installations- und Bedienungsanleitung

### 🐍 Python-Anwendungen (Streamlit)
Zum Starten der Webanwendungen im Verzeichnis `PYTHON/` (z. B. `E-Rechnung`, `Leitweg-ID` oder `XmlToPdf`):

```bash
# 1. In das jeweilige Verzeichnis wechseln
cd PYTHON/E-Rechnung   # oder PYTHON/Leitweg-ID bzw. PYTHON/XmlToPdf

# 2. Abhängigkeiten installieren
pip install -r requirements.txt

# 3. Anwendung starten
streamlit run app.py
```

### ☕ Java-Anwendungen
* Öffnen des entsprechenden Projektordners (`JAVA/CRUD` oder `JAVA/Calculator`) in einer Java-IDE (NetBeans, IntelliJ IDEA oder Eclipse).
* Für `JAVA/CRUD` das Projekt mit Maven erstellen:
  ```bash
  mvn clean install
  ```

### ⚡ C-Programme
* Unter Windows können die vorkompilierten `.exe`-Dateien im Ordner `C/` direkt ausgeführt werden.
* Zur manuellen Kompilierung mit GCC:
  ```bash
  gcc calculadora.c -o calculadora.exe
  ./calculadora.exe
  ```

---

## 👤 Autor

* **D. Paz** ([@dwn10](https://github.com/dwn10))
* Repository: [https://github.com/dwn10/C_C_C](https://github.com/dwn10/C_C_C)
