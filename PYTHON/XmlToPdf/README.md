# Streamlit-Webanwendung bereit, mit der Benutzer eine XML-Datei hochladen.

- Die enthaltenen Daten in einer Tabelle anzeigen und dann ausgewählte Zeilen als XML- oder PDF-Datei herunterladen können.

## Install & Start

<a href="https://github.com/dwn10/C_C_C/blob/main/PYTHON/XmlToPdf/XmlToPdf2.gif"><img src="https://github.com/dwn10/C_C_C/blob/main/PYTHON/XmlToPdf/XmlToPdf2.gif" style="height: 80%; width:80%;"/></a>

## Funktionsweise im Detail

<a href="https://github.com/dwn10/C_C_C/blob/main/PYTHON/XmlToPdf/XmlToPdf3.gif"><img src="https://github.com/dwn10/C_C_C/blob/main/PYTHON/XmlToPdf/XmlToPdf3.gif" style="height: 80%; width:80%;"/></a>

`process_xml(xml_file):`

- Diese Funktion liest und analysiert die hochgeladene XML-Datei, extrahiert relevante Daten und gibt diese als Pandas DataFrame zurück.

`create_xml_output(selected_data):`

- Aus den ausgewählten Daten `(Zeilen des DataFrames)` wird eine neue `XML-Struktur` erstellt und als String zurückgegeben, der zum Download bereit ist.

`create_pdf_output(selected_data):`

- Die ausgewählten Daten werden in einem `PDF-Dokument` formatiert, wobei die Spaltennamen als Überschriften und die Zeilenwerte als Tabellenzellen dargestellt werden. Das PDF wird als Bytes-Objekt zurückgegeben.

`main():`

- Konfiguriert die Streamlit-Seite mit Titel, Icon und Untertitel.
  - Ermöglicht das Hochladen einer XML-Datei.
  - Zeigt die Daten der hochgeladenen Datei in einer Tabelle an.
  - Ermöglicht die Auswahl mehrerer Zeilen.

## Stellt zwei Buttons bereit:

`"Download XML":`

- Wenn Zeilen ausgewählt wurden, wird die create_xml_output Funktion aufgerufen und der Download gestartet.
  `"Download PDF":`
- Ähnlich wie beim XML-Download, ruft aber create_pdf_output auf.

```C
Zeigt Warnmeldungen an, wenn versucht wird herunterzuladen, ohne Zeilen auszuwählen.
Wichtige Bibliotheken
```

- `streamlit:` Zur Erstellung der interaktiven Webanwendung.
- `pandas:` Zur Datenverarbeitung und Tabellenanzeige.
- `xml.etree.ElementTree:` Zum Lesen und Schreiben von XML-Daten.
- `fpdf:` Zum Erstellen von PDF-Dokumenten.
- `io:` Zur Arbeit mit Bytes-Objekten (für den Download).
