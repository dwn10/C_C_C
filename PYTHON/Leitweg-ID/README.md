# Leitweg-ID Generator

Eine Streamlit-Anwendung zur Generierung und Validierung von Leitweg-IDs für deutsche Behörden.

## Funktionen

- Generierung von Leitweg-IDs nach dem offiziellen Standard
- Validierung von Bundesland-Codes
- Überprüfung deutscher Postleitzahlen
- Automatische Berechnung der Prüfziffer
- Kopieren der generierten ID in die Zwischenablage
- Benutzerfreundliche Weboberfläche

## Installation

1. Stellen Sie sicher, dass Python 3.8 oder höher installiert ist
2. Klonen Sie das Repository:
```bash
git clone [repository-url]
cd Leitweg-ID
```

3. Installieren Sie die erforderlichen Pakete:
```bash
pip install -r requirements.txt
```

## Verwendung

1. Starten Sie die Anwendung:
```bash
streamlit run app.py
```

2. Öffnen Sie einen Webbrowser und navigieren Sie zu:
- Lokal: http://localhost:8501
- Netzwerk: http://[ihre-ip-adresse]:8501

## Eingabefelder

- **Bundesland-Code (2 Stellen)**: z.B. 05 für Nordrhein-Westfalen
- **Postleitzahl (5 Stellen)**: Deutsche PLZ zur Validierung
- **Regierungsbezirk (1 Stelle)**: Optional
- **Landkreis (2 Stellen)**: Optional
- **Gemeindekennzahl (3, 4 oder 7 Stellen)**: Pflichtfeld
- **Feinadressierung (max. 30 Zeichen)**: Optional

## Technische Details

- **Prüfziffer-Berechnung**: Implementiert nach dem Modulo-97-Verfahren
- **Caching**: Effiziente Zwischenspeicherung für Validierungen
- **API-Integration**: Validierung von Postleitzahlen über externe API
- **Responsive Design**: Optimiert für Desktop und Mobile

## Abhängigkeiten

- Python 3.8+
- Streamlit 1.41.1
- Requests 2.31.0
- Python-dateutil 2.9.0
- Pytz 2024.2
- Regex 2023.12.25

## Lizenz

MIT License
