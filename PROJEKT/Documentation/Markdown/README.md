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
    frontend: ["React", "TanStack Query"],
    backend: ["Supabase", "PostgreSQL"],
    devTool: ["VS-Code"],
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
- [4.1 Hauptfunktionen des Systems entwickeln.](#41-hauptfunktionen-des-systems-entwickeln)
- [4.2 Verwendung von Supabase Realtime-Funktionen.](#42-verwendung-von-supabase-realtime-funktionen)
- [4.3 Implementierung des Logins.](#43-implementierung-des-logins)
- [4.4 Verwendung von React-pdf zur Erstellung von PDF-Berichten.](#44-verwendung-von-react-pdf-zur-erstellung-von-pdf-berichten)
- [4.5 Speicherung von Kaufpreisinformationen in der Supabase-Datenbank.](#45-speicherung-von-kaufpreisinformationen-in-der-supabase-datenbank)
- [4.6 Verwendung von APIs, um eine Verbindung zu den externen Diensten herzustellen.](#46-verwendung-von-apis-um-eine-verbindung-zu-den-externen-diensten-herzustellen)
- [4.7 Implementierung der Oberfläche der Webanwendung.](#47-implementierung-der-oberfl%C3%A4che-der-webanwendung)
- [4.8 Verwendung von Funktionen zur Berechnung von Leistungskennzahlen.](#48-verwendung-von-funktionen-zur-berechnung-von-leistungskennzahlen)

#### 5 Abnahme und Einführung
- [5.1 Code-Review.](#51-code-review)
- [5.2 Abnahme durch den Fachbereich.](#52-abnahme-durch-den-fachbereich)
- [5.3 Erfolgskontrolle in der Fachabteilung.](#53-erfolgskontrolle-in-der-fachabteilung)
- [5.4 Deployment der Anwendung.](#54-deployment-der-anwendung)

#### 6 Dokumentation
- [6.1 Erstellung des Benutzerhandbuchs.](#61-erstellung-des-benutzerhandbuchs)
- [6.2 Erstellung der Entwicklerdokumentation.](#62-erstellung-der-entwicklerdokumentation)

#### 1 Projektplanung
Dieses Kapitel beschreibt die umfassende Planung des Projekts, die die Auswahl einer geeigneten Entwicklungsmethode und die Identifizierung der für die Durchführung erforderlichen Ressourcen umfasst.

#### 1.1 Projektphasen
Diese Abschlussarbeit wird nach dem [Wasserfallmodell](https://github.com/dwn10/C_C_C/blob/main/PROJEKT/Documentation/Markdown/DiagrammeIMG.md#wasserfallmodell-phasen) entwickelt. Die Gesamtzeit, die der IT-Spezialist für die Entwicklung der Anwendung aufwenden kann, ist auf 80 Stunden begrenzt. Tabelle 1 zeigt im Detail, wie diese 80 Stunden auf die verschiedenen Phasen des Wasserfallmodells verteilt sind. [weitere Details](https://github.com/dwn10/C_C_C/blob/main/PROJEKT/Documentation/Markdown/UML-Diagramme.md#projektphasen)


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
| Abnahme und Erfolgskontrolle | Zwei Mitarbeiter:innen der Personalabteilung | 3 h | 50 € * 2 = 100 € | 500 € |
| Migration der Daten | Ein:e Mitarbeiter:in der Personalabteilung | 7,6 h | 50 € | 380 € |
|  |  |  |  | **3.180 €** |

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

$$
\displaystyle \frac{4.593 \ {\text{min/Jahr}}}{60 \ } \times 50 \ {€/h} \approx 13.779 \ {€ / Jahr}
$$

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

#### 3.2 Entwurf der Benutzeroberfläche inkl. Erstellung von [Mock-Ups.](https://github.com/dwn10/C_C_C/blob/main/PROJEKT/Documentation/Markdown/DiagrammeIMG.md#mock-ups)
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
Diese Komponente stellt eine Benutzeroberfläche zur Erstellung von PDF-Berichten bereit, die Informationen wie den Benutzer, die Produktbeschreibung, die Art der Bewegung (Eingabe oder Ausgabe), die Menge, das Datum und den aktuellen Lagerbestand enthalten.

#### 3.5 Planung der Architektur inkl. Erstellung eines [Komponentendiagramms.](https://github.com/dwn10/C_C_C/blob/main/PROJEKT/Documentation/Markdown/DiagrammeIMG.md#komponentendiagramm)

**Hauptkomponenten:**
**Benutzeroberfläche (Frontend):**

- Entwickelt mit React.
- Bietet eine intuitive und responsive Oberfläche für die Benutzerinteraktion.
- **Hauptkomponenten:**
    - Produktverwaltung (Registrierung, Suche, Aktualisierung).
    - Bestandsverwaltung (Visualisierung, Warnungen, Bewegungen).
    - Lieferantenverwaltung (Registrierung, Historie, Bewertung).
    - Berichtsgenerierung (Anpassung, Export).
    - Authentifizierung und Zugriffskontrolle.
- Anpassbares Design für verschiedene Geräte (Desktop, Tablets, Mobilgeräte).

**API (Backend):**
- Implementiert mit Supabase.
- Bietet eine REST-API für die Kommunikation zwischen Frontend und Datenbank.
- **Funktionalitäten:**
    - Authentifizierung und Autorisierung von Benutzern.
    - Datenzugriff (Lesen und Schreiben).
    - Speicherung von Produktbildern.
    - Integration mit externen Diensten (optional).

**Datenbank:**
- PostgreSQL (bereitgestellt von Supabase).
- **Speichert Informationen über:**
    - Produkte (Name, Code, Beschreibung, Kategorie, Preis, Lagerbestand, Bilder).
    - Produktkategorien.
    - Produktmarken.
    - Benutzer (Rollen, Berechtigungen).
    - Lagerbewegungen (Einträge, Ausgänge, Lagerbestand).
    - Lieferanten.

**Authentifizierung:**
- Supabase Auth.
- Verwaltet die Authentifizierung und Autorisierung von Benutzern.
- Weist Rollen und Berechtigungen zu.

**Dateispeicher:**
- Supabase Storage.
- Speichert Produktbilder.

**Berichtsgenerierung:**- React-pdf.
- Generiert Berichte im PDF-Format.
- Ermöglicht die Anpassung und den Export von Berichten.

#### 3.6 Erstellung des [Pflichtenhefts.](https://github.com/dwn10/C_C_C/blob/main/PROJEKT/Documentation/Markdown/Lastenheft.md#pflichtenheft)
Dieses Dokument beschreibt die Anforderungen an das zu entwickelnde Webinventarsystem für die SOFTWEAVER GmbH. Es basiert auf dem Projektantrag und den Ergebnissen der Analysephase. Das Dokument dient als Grundlage für die Implementierung und definiert die Funktionen, Qualitätsmerkmale und Rahmenbedingungen des Systems.

#### 4 Implementierung inkl. Tests
Dieser Abschnitt beschreibt die Implementierung der Produktverwaltung. Der Fokus liegt auf den CRUD-Operationen (Erstellen, Lesen, Aktualisieren, Löschen). Für die Umsetzung werden React (Frontend) und Supabase (Backend) verwendet.

#### 4.1 [Hauptfunktionen des Systems entwickeln.](https://github.com/dwn10/C_C_C/blob/main/PROJEKT/Documentation/Markdown/Dev.md#ein-inventar-projekt-mit-react-und-supabase-in-visual-studio-code-erstellen)
Die Entwicklung des Inventarsystems konzentriert sich auf die Erstellung einer robusten, skalierbaren und benutzerfreundlichen Webanwendung unter Verwendung von React für das Frontend und Supabase für das Backend.

**Hauptfunktionen:**

- **Produktverwaltung**
- **Bestandsverwaltung**
- **Berichtsgenerierung**
- **API-Integration (optional)**
- **Sicherheit und Zugriffskontrolle**

**Entwicklung**

Der Entwicklungsprozess wird die folgenden Phasen durchlaufen:

- **Analyse und Design:** Detaillierte Definition der Anforderungen, Design der Datenbank und Struktur der Anwendung.
- **Frontend-Entwicklung:** Erstellung der Benutzeroberfläche mit React.
- **Backend-Entwicklung:** Konfiguration von Supabase, Erstellung von Tabellen, Funktionen und Sicherheitsrichtlinien.
- **Integration:** Verbindung des Frontends mit dem Backend über die Supabase-API.
- **Implementierung von Funktionen:** Entwicklung der Hauptfunktionen des Systems.
- **Tests und Optimierung:** Umfassende Tests, um die Qualität und Leistung des Systems sicherzustellen.
- **Implementierung:** Bereitstellung des Systems in einer Produktionsumgebung.

#### 4.2 Verwendung von Supabase Realtime-Funktionen.

**Vorteile der Verwendung von Supabase Realtime:**
- **Erhöhte Effizienz:**
Echtzeit-Updates ermöglichen es den Benutzern, fundierte Entscheidungen auf der Grundlage genauer und aktueller Daten zu treffen.

- **Verbesserte Produktivität:**
Die Automatisierung von Aufgaben und Echtzeit-Benachrichtigungen entlasten das Personal, sodass es sich auf andere wichtige Aufgaben konzentrieren kann.

- **Reduzierung von Fehlern:**
Die Echtzeit-Synchronisierung von Daten minimiert das Risiko von Fehlern, die durch veraltete Informationen verursacht werden.

- **Verbesserte Benutzererfahrung:**
Die dynamische und interaktive Benutzeroberfläche bietet den Benutzern eine ansprechendere und effizientere Erfahrung.

#### 4.3 [Implementierung des Logins.](https://github.com/dwn10/C_C_C/blob/main/PROJEKT/Documentation/Markdown/Dev.md#login)
Die Implementierung der Anmeldung wird Supabase Auth zur Authentifizierung der Benutzer verwenden. Es wird ein Anmeldeformular erstellt, in dem die Benutzer ihre Anmeldeinformationen (E-Mail und Passwort) eingeben. Beim Absenden des Formulars überprüft Supabase Auth, ob die Anmeldeinformationen gültig sind.

Zusätzlich werden weitere Sicherheitsmaßnahmen implementiert, wie z. B. der Schutz vor Brute-Force-Angriffen und die Validierung sicherer Passwörter.

#### 4.4 Verwendung von React-pdf zur Erstellung von [PDF-Berichten.](https://github.com/dwn10/C_C_C/blob/main/PROJEKT/Documentation/Markdown/Dev.md#pdf-bericht)
React-pdf bietet die Möglichkeit, individuelle und visuell ansprechende Berichte mit Inventardaten zu erstellen, wie z. B. den aktuellen Lagerbestand, die Historie der Bewegungen, Verkäufe und Einkäufe, unter anderem.

Diese Berichte können in Echtzeit generiert werden, was den Benutzern aktuelle und genaue Informationen für die Entscheidungsfindung liefert. Darüber hinaus erleichtert React-pdf die Integration der Berichte in die Benutzeroberfläche des Systems, sodass Benutzer schnell und einfach darauf zugreifen können. Die Möglichkeit, die Berichte im PDF-Format zu exportieren, erleichtert auch deren Speicherung, Druck und Verteilung.

#### 4.5 Speicherung von Kaufpreisinformationen in der Supabase-Datenbank.
Die Kaufinformationen werden in der Datenbank unter Verwendung separater Tabellen für "Produkte", "Lieferanten" und "Einkäufe" gespeichert. Die Tabelle "Produkte" enthält detaillierte Informationen zu jedem Produkt, einschließlich des Einkaufspreises. 

Die Tabelle "Lieferanten" speichert die Informationen der Lieferanten, wie Name, Kontakt und Adresse. Die Tabelle "Einkäufe" zeichnet jede Einkaufstransaktion auf, einschließlich Datum, Lieferant, gekaufte Produkte, Mengen und Gesamtkosten. Fremdschlüssel werden verwendet, um die Tabellen zu verknüpfen und die Datenintegrität zu gewährleisten.

#### 4.6 Verwendung von APIs, um eine Verbindung zu den externen Diensten herzustellen.
APIs werden verwendet, um das Inventarsystem mit externen Diensten wie ERP- oder E-Commerce-Plattformen zu verbinden. Dies ermöglicht die Synchronisierung von Daten wie Produktinformationen, Preisen und Lagerbeständen zwischen dem Inventarsystem und den externen Plattformen.

Darüber hinaus bietet die Integration mit externen Diensten über APIs Flexibilität und Skalierbarkeit für das System, indem die Verbindung mit verschiedenen Datenquellen und die Automatisierung von Aufgaben ermöglicht wird.

#### 4.7 Implementierung der [Oberfläche der Webanwendung.](https://github.com/dwn10/C_C_C/blob/main/PROJEKT/Documentation/Markdown/DiagrammeIMG.md#system-nav)
Die Benutzeroberfläche der Webanwendung wird mit React entwickelt, wobei wiederverwendbare Komponenten und ein responsives Design verwendet werden, das sich an verschiedene Geräte anpasst (Desktop, Tablets und Mobilgeräte).

Es wird eine klare und intuitive Navigation zwischen den verschiedenen Bereichen des Systems implementiert, wie z. B. Produktverwaltung, Inventar, Lieferanten und Berichte. Es werden Bibliotheken wie TanStack Query verwendet, um Anfragen an den Server zu stellen, und TanStack Table, um die Daten in interaktiven Tabellen anzuzeigen.

Besonderes Augenmerk wird auf die Benutzererfahrung gelegt, mit einem optisch ansprechenden Design und einer benutzerfreundlichen Oberfläche.

#### 4.8 Verwendung von Funktionen zur Berechnung von Leistungskennzahlen.
Die Funktionen in Supabase können die Berechnung von wichtigen Leistungsindikatoren automatisieren. Beispielsweise können Funktionen erstellt werden, um den Gesamtwert des Inventars, den Lagerumschlag, die Kosten der verkauften Produkte und die Bruttogewinnmarge zu berechnen.

Diese Funktionen können so programmiert werden, dass sie regelmäßig oder in Echtzeit ausgeführt werden, wodurch aktuelle Informationen über die Leistung des Inventars bereitgestellt werden.

Die Ergebnisse dieser Funktionen können in Dashboards oder Berichten angezeigt werden, was die Analyse und Entscheidungsfindung erleichtert.

#### 5 Abnahme und Einführung

#### 5.1 Code-Review.
Um die Qualität und Wartbarkeit des Inventarsystems zu gewährleisten, wird die Codeüberprüfung ein wesentlicher Prozess in der Entwicklung sein. Es wird ein Peer-Review-Ansatz implementiert, bei dem die Entwickler ihren Code gegenseitig überprüfen, um Fehler zu erkennen, die Lesbarkeit zu verbessern und die Konformität mit den Codierungsstandards sicherzustellen.

Statische Codeanalyse-Tools werden verwendet, um die Identifizierung häufiger Probleme zu automatisieren, und die Diskussion und der Wissensaustausch zwischen den Entwicklern werden gefördert. Die Codeüberprüfung wird auch als Gelegenheit dienen, mögliche Verbesserungen im Design und in der Architektur des Systems zu identifizieren.

#### 5.2 Abnahme durch den Fachbereich.
Die Abnahme und Präsentation des Webinventarsystems erfolgte durch eine interaktive Demonstration mit der Personalabteilung. Die Webanwendung wurde vorgestellt, ihre Funktionalität erläutert und die Fragen des Teams beantwortet. Es wurden verschiedene Anwendungsszenarien simuliert, wie z. B. die Registrierung neuer Produkte, die Aktualisierung des Lagerbestands, die Generierung von Berichten und die Benutzerverwaltung.

Der Schwerpunkt lag auf der Benutzerfreundlichkeit, Effizienz und Sicherheit des Systems. Das Team hatte die Möglichkeit, die Anwendung zu testen, Fragen zu stellen und Feedback zu geben.

Die Vorschläge wurden gesammelt und Anpassungen vorgenommen, um sicherzustellen, dass das System die Erwartungen und Anforderungen der Abteilung erfüllt. Schließlich wurde die Genehmigung zur Implementierung des Webinventarsystems erteilt.

#### 5.3 Erfolgskontrolle in der Fachabteilung.
Der Projekterfolg wird kontinuierlich bewertet, indem der Fortschritt in Bezug auf die definierten Ziele und Zeitvorgaben verfolgt wird. Es werden Projektmanagement-Tools eingesetzt, um den Fortschritt zu überwachen, potenzielle Hindernisse zu identifizieren und die termingerechte Lieferung des Systems sicherzustellen.

#### 5.4 Deployment der Anwendung.
Die Bereitstellung der Anwendung erfolgt in einer Produktionsumgebung, die über das Internet zugänglich ist. Zum Hosten der React-Anwendung wird ein Cloud-Hosting-Dienst wie Ionos oder Vercel verwendet.

Die PostgreSQL-Datenbank und die Authentifizierungs- und Speicherfunktionen werden von Supabase bereitgestellt. Für die Anwendung wird eine benutzerdefinierte Domain konfiguriert und zur Gewährleistung der Kommunikationssicherheit ein SSL-Zertifikat verwendet.

Es werden Caching-Strategien und Leistungsoptimierungen implementiert, um ein reibungsloses Benutzererlebnis zu gewährleisten. Vor der endgültigen Inbetriebnahme werden umfassende Tests in der Produktionsumgebung durchgeführt. Der Bereitstellungsprozess wird dokumentiert, um zukünftige Updates und die Wartung der Anwendung zu erleichtern.

#### 6 Dokumentation

#### 6.1 Erstellung des [Benutzerhandbuchs.](https://github.com/dwn10/C_C_C/blob/main/PROJEKT/Documentation/Markdown/User.md#benutzerhandbuch)
Das Benutzerhandbuch wurde zum einfachen Verständnis entwickelt und enthält Screenshots und Beispiele, die jeden Schritt veranschaulichen. Die wichtigsten Funktionen des Systems, wie die Produktregistrierung, die Bestandsverwaltung und die Berichterstellung, werden detailliert beschrieben.

Darüber hinaus werden Informationen über den Zugriff auf das System, die Navigation in der Benutzeroberfläche und die Ausführung gängiger Aufgaben bereitgestellt.

#### 6.2 Erstellung der [Entwicklerdokumentation.](https://github.com/dwn10/C_C_C/blob/main/PROJEKT/Documentation/Markdown/Dev.md#ein-inventar-projekt-mit-react-und-supabase-in-visual-studio-code-erstellen)
Die Entwicklerdokumentation dient als Leitfaden für das Inventarsystem.
Sie beschreibt detailliert die Projektstruktur, die Hauptfunktionen, die verwendeten APIs sowie die durchgeführten Unit- und Integrationstests.
Zur besseren Veranschaulichung der Beziehungen zwischen den Komponenten werden Klassen- und Sequenzdiagramme verwendet.
Diese Dokumentation wird bei jeder Änderung am Quellcode aktualisiert, um ihre Genauigkeit und ihren Nutzen zu gewährleisten.

#### Schlussfolgerung
Dieses Projekt schlägt die Entwicklung eines modernen und effizienten Inventarsystems unter Verwendung von React und Supabase vor. Ziel ist es, die Mängel des aktuellen Systems zu beheben, das nur von einem PC aus verwaltet werden kann, was die Flexibilität und den Zugriff auf Informationen einschränkt.

Das neue System wird eine intuitive und reaktionsschnelle Benutzeroberfläche bieten, auf die von verschiedenen Geräten aus zugegriffen werden kann. Es ermöglicht eine detaillierte Produktverwaltung, Echtzeit-Bestandskontrolle, Lieferantenmanagement und Berichtsgenerierung.

Zu den erwarteten Vorteilen der Implementierung des neuen Systems gehören die Optimierung der Bestandsverwaltung, die Verbesserung der Entscheidungsfindung, die Steigerung der Effizienz, Skalierbarkeit, Sicherheit und Zuverlässigkeit.

Insgesamt zielt das Projekt darauf ab, die Art und Weise, wie Unternehmen ihre Lagerbestände verwalten, zu verbessern, indem es ein robustes, effizientes und benutzerfreundliches Werkzeug bereitstellt.