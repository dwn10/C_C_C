# E-Rechnung Generator
### Test Version D.Paz

Eine Streamlit-Anwendung zur Erstellung und Verwaltung von elektronischen Rechnungen (E-Rechnung) im XRechnung-Format, kompatibel mit dem deutschen E-Rechnungssystem.

## Funktionen

- Erstellung von elektronischen Rechnungen im XRechnung-Format
- Leitweg-ID Validierung
- Speicherung im XML- und JSON-Format
- Anzeige vorhandener Rechnungen
- Validierung von XML-Rechnungen
- Automatische Berechnung von Mehrwertsteuer und Gesamtbeträgen

## Installation

1. Stellen Sie sicher, dass Python 3.8 oder höher installiert ist
2. Klonen Sie das Repository:
```bash
git clone [repository-url]
cd E-Rechnung
```

3. Installieren Sie die Abhängigkeiten:
```bash
pip install -r requirements.txt
```

## Verwendung

1. Starten Sie die Anwendung:
```bash
streamlit run app.py
```

2. Zugriff über Ihren Browser:
- Lokal: http://localhost:8501
- Netzwerk: http://[ihre-ip]:8501

## Funktionalitäten

### 1. Rechnungserstellung
- Lieferanten- und Kundendaten
- Integration mit Leitweg-ID
- Automatische Steuerberechnung
- XML-Generierung nach XRechnung-Standard

### 2. Rechnungsanzeige
- Liste aller erstellten Rechnungen
- Vollständige Details in Tabellenform
- Zugriff auf XML- und JSON-Dateien

### 3. Rechnungsprüfung
- Validierung der XML-Struktur
- Überprüfung der Leitweg-ID
- Prüfung der Pflichtfelder

## Dateistruktur

- `app.py`: Hauptanwendung
- `rechnungen/`: Verzeichnis für Rechnungen
  - `*.xml`: Rechnungen im XRechnung-Format
  - `*.json`: Rechnungsdaten im JSON-Format

## Abhängigkeiten

- Python 3.8+
- Streamlit 1.41.1
- Pandas 2.1.4
- Requests 2.31.0
- Python-dateutil 2.9.0
- Pytz 2024.2
- lxml 5.1.0

## Support

Für Problemmeldungen oder Verbesserungsvorschläge erstellen Sie bitte ein Issue im Repository.

---

Entwickelt zur Vereinfachung der elektronischen Rechnungsstellung im deutschen System
