<p align="center">
  <a href="https://github.com/dwn10/C_C_C/blob/main/PROJEKT/Documentation/Markdown/Dev.md#ein-inventar-projekt-mit-react-und-supabase-in-visual-studio-code-erstellen" target="_blank">Entwicklerdokumentation</a> •
  <a href="https://github.com/dwn10/C_C_C/blob/main/PROJEKT/Documentation/Markdown/User.md#benutzerhandbuch" target="_blank">Benutzerdokumentation</a> •
  <a href="https://github.com/dwn10/C_C_C/blob/main/PROJEKT/Documentation/Markdown/DiagrammeIMG.md#diagramme" target="_blank">Diagramme</a> •
  <a href="https://github.com/dwn10/C_C_C/blob/main/PROJEKT/Documentation/Markdown/Links.md#projektlinks-und-ressourcen" target="_blank">Projektlinks</a>
</p>

# Inventarsystem

mit React und Supabase

#### Verwendete Technologien:

```javascript
const Project = {
  code: ["HTML", "CSS", "Javascript", "SQL"],
  technologies: {
    devTool: ["VS-Code", "Supabase"],
  },
};
```

#### 1 Projektplanung
- [1.1 Projektphasen.](#11-projektphasen)
- [1.2 Ressourcenplanung.](#12-ressourcenplanung)
- [1.3 Entwicklungsprozess.](#13-entwicklungsprozess)

#### 2 Analyse und Design
- [2.1 Durchführung der Ist-Analyse.](#21-durchführung-der-ist-analyse)
- [2.2 Durchführung der Wirtschaftlichkeitsanalyse inkl. Amortisationsrechnung.](#22-durchf%C3%BChrung-der-wirtschaftlichkeitsanalyse-inkl-amortisationsrechnung)
- [2.3 Ermittlung von Anwendungsfällen inkl. Erstellung eines Anwendungsfall-Diagramms.](#23-ermittlung-von-anwendungsf%C3%A4llen-inkl-erstellung-eines-anwendungsfall-diagramms)
- [2.4 Erstellung einer erweiterten Ereignisgesteuerten Prozesskette.](#24-erstellung-einer-erweiterten-ereignisgesteuerten-prozesskette)
- [2.5 Unterstützung des Fachbereichs beim Erstellen des Lastenhefts.](#25-unterst%C3%BCtzung-des-fachbereichs-beim-erstellen-des-lastenhefts)

#### 3 Entwurf
- [3.1 Entwurf der Datenbank und der Anwendungsstruktur.](#31-entwurf-der-datenbank-und-der-anwendungsstruktur)
- [3.2 Entwurf der Benutzeroberfläche inkl. Erstellung von Mock-Ups.](#32-entwurf-der-benutzeroberfl%C3%A4che-inkl-erstellung-von-mock-ups)
- [3.3 Erstellung eines ER-Modells.](#33-erstellung-eines-er-modells)
- [3.4 Entwurf der PDF auf Basis der Oberfläche.](#34-entwurf-der-pdf-auf-basis-der-oberfl%C3%A4che)
- [3.5 Planung der Architektur inkl. Erstellung eines Komponentendiagramms.](#35-planung-der-architektur-inkl-erstellung-eines-komponentendiagramms)
- [3.6 Erstellung des Pflichtenhefts.](#36-erstellung-des-pflichtenhefts)

#### 4 Implementierung inkl. Tests
- [4.1 Hauptfunktionen des Systems entwickeln.]()
- [4.2 Verwendung von Supabase Realtime-Funktionen.]()
- [4.3 Implementierung des Logins.]()
- [4.4 Verwendung von React-pdf zur Erstellung von PDF-Berichten.]()
- [4.5 Speicherung von Kaufpreisinformationen in der Supabase-Datenbank.]()
- [4.6 Verwendung von APIs, um eine Verbindung zu den externen Diensten herzustellen.]()
- [4.7 Implementierung der Oberfläche der Webanwendung.]()
- [4.8 Verwendung von Funktionen zur Berechnung von Leistungskennzahlen.]()

#### 5 Abnahme und Einführung
- [5.1 Code-Review.]()
- [5.2 Abnahme durch den Fachbereich.]()
- [5.3 Erfolgskontrolle in der Fachabteilung.]()
- [5.4 Deployment der Anwendung.]()

#### 6 Dokumentation
- [6.1 Erstellung des Benutzerhandbuchs.](https://github.com/dwn10/C_C_C/blob/main/PROJEKT/Documentation/Markdown/User.md#benutzerhandbuch)
- [6.2 Erstellung der Entwicklerdokumentation.](https://github.com/dwn10/C_C_C/blob/main/PROJEKT/Documentation/Markdown/Dev.md#ein-inventar-projekt-mit-react-und-supabase-in-visual-studio-code-erstellen)

#### 1 Projektplanung
Dieses Kapitel beschreibt die umfassende Planung des Projekts, die die Auswahl einer geeigneten Entwicklungsmethode und die Identifizierung der für die Durchführung erforderlichen Ressourcen umfasst.

#### 1.1 Projektphasen
Diese Abschlussarbeit wird nach dem Wasserfallmodell entwickelt. Die Gesamtzeit, die der IT-Spezialist für die Entwicklung der Anwendung aufwenden kann, ist auf 80 Stunden begrenzt. Tabelle 1 zeigt im Detail, wie diese 80 Stunden auf die verschiedenen Phasen des Wasserfallmodells verteilt sind.


| Phase                     | Zeit |
| ------------------------ | ---- |
| Analyse und Design      | 12 h |
| Entwurf                 | 12 h |
| Implementierung inkl. Tests | 41 h |
| Abnahme und Einführung  | 5 h  |
| Dokumentation            | 10 h |
| **GESAMT**              | **80 h** |

#### 1.2 Ressourcenplanung
Für dieses Projekt wurde eine Strategie zur Kostenminimierung gewählt, bei der die Verwendung von kostenlosen und Open-Source-Ressourcen priorisiert wurde. Die Ressourcenplanung, die unter [detailliert](#zustand) beschrieben ist, wurde in vier Kategorien unterteilt:

- [**Personal:**]() Entwicklung Team.
- [**Hardware:**]() Laptop, Monitor.
- [**Software:**]() Es wurde vorrangig auf kostenlose Software gesetzt, um Lizenzkosten zu vermeiden.

Bei der Entwicklung der Webanwendung wurden die folgenden Open-Source-Tools verwendet:

- [**Framework React:**](#react) Zur Erstellung der Benutzeroberfläche.
- [**Supabase:**](#supabase) Als Backend-Plattform.
- [**PostgreSQL:**](#postgresql) Als Datenbankmanagementsystem.

Diese Strategie ermöglichte es, das Projekt effizient und mit einem optimierten Budget zu entwickeln.

#### Diagrammen und Dokumentation
- [**PlantUML:**](#plantuml) Zur Erstellung von Diagrammen.
- [**Markdown editor:**](#markdown) Dokumentation.

#### 1.3 Entwicklungsprozess
Um eine organisierte Struktur zu gewährleisten, wurde ein klarer Entwicklungsprozess definiert. Dem Wasserfallmodell folgend, wie in Abschnitt [1.1](#11-projektphasen) Projektphasen beschrieben, erwies sich dieser Ansatz als besonders geeignet für die Bedürfnisse dieser Industrie- und Handelskammer.

#### 2 Analyse und Design
Die Anfangsphase des Wasserfallmodells konzentriert sich auf die Analyse. In dieser Phase wird eine umfassende Analyse durchgeführt, um die Projektaufgaben gründlich zu verstehen. Anschließend wird die wirtschaftliche Machbarkeit bewertet und der Personalbedarf in einem Pflichtenheft dokumentiert.

#### 2.1 Durchführung der Ist-Analyse
Die aktuelle Situation der SOFTWEAVER GmbH besteht derzeit darin, dass ein Inventarsystem nur von einem PC aus verwaltet werden kann.
Das bedeutet, dass es keinen zentralen Zugriff oder eine flexible Nutzung von verschiedenen Geräten oder Standorten gibt.

Dies führt zu erschwertem Informationszugriff, verzögerter Entscheidungsfindung und potenziellen Fehlern im Lagerbestand. Die mangelnde Flexibilität behindert die Mobilität und Reaktionsfähigkeit der Mitarbeiter, was zu verpassten Geschäftschancen führen kann. Zudem ist das System nicht in der Lage, die Vielfalt der Hardware zu verwalten, was zu Schwierigkeiten bei der Nachverfolgung und Kontrolle führt.

Die Einführung eines neuen Inventarsystems würde eine zentrale und strukturierte Registrierung aller Geräte wie PCs, Tablets und Smartphones ermöglichen. Dies würde die Transparenz erhöhen, die Bestandskontrolle verbessern und eine effizientere Entscheidungsfindung ermöglichen. Auf diese Weise würde das neue System dazu beitragen, die Herausforderungen der aktuellen Situation zu meistern und das Mobilitätsmanagement des Unternehmens zu optimieren.

#### 2.2 Durchführung der Wirtschaftlichkeitsanalyse inkl. Amortisationsrechnung
Die wirtschaftliche Analyse beinhaltet die Bewertung der Durchführbarkeit des Projekts aus finanzieller Sicht. Dazu wurden die Projektkosten erhoben und mit der daraus resultierenden Zeitersparnis verglichen, wodurch die Amortisationszeit berechnet werden konnte.

Um die wirtschaftliche Tragfähigkeit des Projekts zu bewerten, wurde eine umfassende Kostenanalyse durchgeführt, die sowohl die Entwicklungskosten als auch die Kosten für die in Abschnitt [1.2](#12-ressourcenplanung), Ressourcenplanung, aufgeführten Ressourcen umfasst. Aufgrund der Vertraulichkeit der Gehälter wurden zur Schätzung der Personalkosten Standardstundensätze verwendet, die von der Personalabteilung in Zusammenarbeit mit einem Abteilungsleiter festgelegt wurden.

Die Kostenplanung für das Projekt berücksichtigt verschiedene Stundensätze:

- Mitarbeiter:innen (Personal/IT): 35 € pro Stunde
- Auszubildende: 10 € pro Stunde

Zusätzlich fallen pro Stunde 15 € für Ressourcen und Lizenzen an. Um die Übersichtlichkeit in Tabelle 2 zu gewährleisten, wurden diese Kosten bereits in die Stundensätze integriert.  Somit ergeben sich folgende effektive Stundensätze:

- Mitarbeiter:innen (Personal/IT): 50 € pro Stunde (35 € + 15 €)
- Auszubildende: 25 € pro Stunde (10 € + 15 €)

Als Basis für die Berechnung der Personalkosten dient eine 38-Stunden-Woche. Ein Personentag (PT) entspricht demnach 7,6 Stunden bzw. 456 Minuten.

| Vorgang | Mitarbeiter | Zeit | Kosten pro Stunde | Kosten |
|---|---|---|---|---|
| Entwicklungskosten | Ein Auszubildender der IT | 80 h | 25 € | 2.000 € |
| Erstellung des Lastenheftes | Zwei Mitarbeiter:innen der Personalabteilung | 2 h | 50 € * 2 = 100 € | 200 € |
| Pull-Requests (PRs) abnehmen | Ein:e Mitarbeiter:in der IT-Abteilung | 2 h | 50 € | 100 € |
| Abnahme und Erfolgskontrolle | Zwei Mitarbeiter:innen der Personalabteilung | 3 h | 50 € * 2 = 100 € | 300 € |
| Migration der Daten | Ein:e Mitarbeiter:in der Personalabteilung | 7,6 h | 50 € | 380 € |
|  |  |  |  | **2.980 €** |

#### Amortisationsrechnung

Die Amortisationszeit wird berechnet, indem die Projektkosten (2.350 €) mit der Zeitersparnis verglichen werden, die in der Personalabteilung bei der Berechnung der Weihnachtsgratifikationen erzielt wird. Diese Berechnung basiert auf Daten aus Vorjahren und konzentriert sich auf die Prozesse, die durch die Projektumsetzung optimiert werden. Aufgaben, die keine Zeitersparnis mit sich bringen, wie z. B. die Beantwortung von telefonischen Anfragen zu den Gratifikationen, werden bei der Berechnung nicht berücksichtigt.

| Vorgang | Anzahl pro Jahr | Zeit vorher pro Vorgang | Zeit nachher pro Vorgang | Einsparung pro Jahr |
|---|---|---|---|---|
| Inventar-Aktualisierung | 12 | 360 min | 0 min | 4.320 min |
| Registrierung neuer Geräte | 6 | 10 min | 5 min | 30 min |
| Zuweisung von Geräten an Mitarbeiter | 5 | 15 min | 5 min | 50 min |
| Kontrolle der Excel-Datei durch zweite Person | 1 | 228 min | 60 min | 168 min |
| Erstellung von Inventarberichten | 1 | 30 min | 5 min | 25 min |
|  |  |  |  | **4.593 min** |


Durch die Zeiteinsparung von 4.593 Minuten pro Jahr ließen sich die jährlich gesparten Kosten
berechnen

` 4.593 min/Jahr
........................... ×50 €/h ≈ 13.779 €/Jahr
      60 

#### 2.3 Ermittlung von Anwendungsfällen inkl. Erstellung eines [Anwendungsfall-Diagramms.](https://github.com/dwn10/C_C_C/blob/main/PROJEKT/Documentation/Markdown/DiagrammeIMG.md#usecase-diagramm)
Ein weiterer Schritt der Analysephase war die Darstellung der wichtigsten fachlichen Anwendungsfälle. Dafür wurde mithilfe der Unified Modeling Language (UML).

- **Aktionen des Administrators:**
Der Administrator kann sich anmelden, wobei die Aktionen "Login validieren" und optional "Passwort wiederherstellen" inkludiert sind. Beide Aktionen beinhalten Datenbankabfragen.
Der Administrator kann Benutzer verwalten, Produkte verwalten und Berichte generieren.

- **Aktionen des Benutzers:**
Der Benutzer kann das Inventar abfragen und eine Produktanfrage stellen. Beide Aktionen beinhalten Datenbankabfragen.

#### 2.4 Erstellung einer erweiterten Ereignisgesteuerten [Prozesskette.](https://github.com/dwn10/C_C_C/blob/main/PROJEKT/Documentation/Markdown/DiagrammeIMG.md#ablaufdiagramm)
Prozessablauf eines Inventarsystems. Nach Eingabe von Benutzername und Passwort erfolgt eine Validierung. Ist der Benutzer gültig, wird das Hauptmenü angezeigt, in dem der Benutzer zwischen verschiedenen Optionen wählen kann:

- **Produkt hinzufügen:** Produktdaten eingeben und in der Datenbank speichern.
- **Produkt löschen:** Zu löschendes Produkt auswählen und aus der Datenbank löschen.
- **Produkt aktualisieren:** Zu aktualisierendes Produkt auswählen, neue Daten eingeben und in der Datenbank aktualisieren.
- **Inventar anzeigen:** Produktliste anzeigen.
- **Beenden:** Sitzung beenden.

Nach jeder Aktion kehrt der Benutzer zum Hauptmenü zurück. Ist der Benutzer ungültig, wird eine Fehlermeldung angezeigt und der Benutzer muss sich erneut anmelden.

#### 2.5 Unterstützung des Fachbereichs beim Erstellen des [Lastenhefts.](https://github.com/dwn10/C_C_C/blob/main/PROJEKT/Documentation/Markdown/Lastenheft.md#lastenheft-f%C3%BCr-das-inventarsystem-mit-react-und-supabase)
Die Analysephase gipfelte in der Erstellung einer Anforderungsspezifikation in Zusammenarbeit mit der Personalabteilung. Diese Spezifikation, die die Grundlage für die technische Umsetzung bildet, umfasst alle technischen Anforderungen des Projekts.

Anhand des Anwendungsfalldiagramms und der Gespräche mit der Personalabteilung wurden die technischen Anforderungen für die Webanwendung mithilfe der MoSCoW-Methode erfasst, dokumentiert und priorisiert. Diese Methode klassifiziert die Anforderungen nach ihrer Wichtigkeit in vier Kategorien: Muss haben, Sollte haben, Könnte haben und Wird nicht haben.

#### 3 Entwurf
In der Entwurfsphase, die auf die Analyse folgte, entstanden konkrete Pläne für die Architektur, das Datenmodell und die Benutzeroberflächen der Anwendung.  Parallel dazu wurden  Qualitätssicherungsmaßnahmen definiert und ein Pflichtenheft erarbeitet, welches die technischen Spezifikationen zur Umsetzung der im Lastenheft beschriebenen fachlichen Anforderungen enthielt.

#### 3.1 Entwurf der [Datenbank](https://github.com/dwn10/C_C_C/blob/main/PROJEKT/Documentation/Markdown/DiagrammeIMG.md#table-structure) und der Anwendungsstruktur.
Das System verfolgt Produkte mit vollständigen Details, einschließlich Kategorien, Marken und Preisen. Darüber hinaus zeichnet das "Kardex" alle Inventarbewegungen auf, bietet einen Transaktionsverlauf und ermöglicht eine Analyse des Produktflusses.

- **firma:** Speichert Informationen über das Unternehmen, einschließlich Name, Währungssymbol und ID des Administratorbenutzers.
- **firmazuordnen:** Ordnet Benutzer Firmen zu.
- **kategorien:** Definiert Produktkategorien mit Beschreibung und Farbe.
- **kardex:** Registriert Inventarbewegungen (Einträge, Ausgänge) mit Datum, Typ, Benutzer, Produkt, Menge, Details und Status.
- **marke:** Speichert Informationen über die Marken der Produkte.
- **modul:** Scheint mit Berechtigungen oder Modulen des Systems zusammenzuhängen, mit einem Namen und einem Status ("check").
- **berechtigungen:** Weist Benutzern Berechtigungen in Bezug auf die Module zu.
- **produkte:** Enthält detaillierte Informationen zu den Produkten, einschließlich Beschreibung, Marke, Lagerbestand, Mindestbestand, Codes, Preisen und Kategorie.
- **users:** Speichert Informationen der Systembenutzer.

#### 3.2 Entwurf der Benutzeroberfläche inkl. Erstellung von Mock-Ups.
Für die Gestaltung benutzerfreundlicher Oberflächen wurden in Zusammenarbeit mit der Personalabteilung Mockups erstellt. Ein Mockup ist die visuelle Darstellung eines Designentwurfs.

Zur Erstellung dieser Mockups wurde die Software Figma verwendet. Anhand von Anwendungsfällen wurden die notwendigen Oberflächen für Login, Produktverwaltung etc. ermittelt.

Das Design umfasst beispielsweise die Farbgestaltung und Positionierung bestimmter Elemente.  Zusätzlich wurden wiederkehrende Elemente wie Logo und Navigationsleiste in Kopf- und Fußzeile integriert. Das erste Mockup zeigt die Benutzeroberfläche für die Zugangsverwaltung zur Plattform.

#### 3.3 Erstellung eines [ER-Modells.](https://github.com/dwn10/C_C_C/blob/main/PROJEKT/Documentation/Markdown/DiagrammeIMG.md#tabellenmodell)

**Haupt Entitäten:**

- **firma (1):** Unternehmen mit Name und Währung. Jedes Unternehmen hat einen Administrator (Benutzer).
- **benutzer (n):** Benutzer mit Name, Kontaktinformationen, Registrierungsdatum, Typ und ID.
- **produkte (n):** Produkt mit Beschreibung, Marke, Lagerbestand, Barcodes, Preis, Kategorie und Unternehmen.
- **kategorien (n):** Produktkategorie mit Beschreibung, Farbe und zugehörigem Unternehmen.
- **marke (n):** Produktmarke mit Beschreibung und zugehörigem Unternehmen.

**Beziehungen:**

- **firmazuordnen (n:n):** Ordnet Benutzer Unternehmen zu. Ein Benutzer kann zu mehreren Unternehmen gehören und ein Unternehmen kann mehrere Benutzer haben.
- **kardex (n):** Inventaraufzeichnung mit Datum, Transaktionstyp, Benutzer, Produkt, Menge, Unternehmen, Details und Status.
- **berechtigungen (n:n):** Verwaltet Benutzerberechtigungen. Ordnet Benutzer Systemmodulen zu. Ein Benutzer kann auf mehrere Module zugreifen und ein Modul kann für mehrere Benutzer zugänglich sein.

#### 3.4 Entwurf der PDF auf Basis der Oberfläche.

#### 3.5 Planung der Architektur inkl. Erstellung eines [Komponentendiagramms.](https://github.com/dwn10/C_C_C/blob/main/PROJEKT/Documentation/Markdown/DiagrammeIMG.md#komponentendiagramm)


#### 3.6 Erstellung des Pflichtenhefts.


