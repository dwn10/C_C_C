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
- [2.2 Durchführung der Wirtschaftlichkeitsanalyse inkl. Amortisationsrechnung.]()
- [2.3 Ermittlung von Anwendungsfällen inkl. Erstellung eines Anwendungsfall-Diagramms.]()
- [2.4 Erstellung einer erweiterten Ereignisgesteuerten Prozesskette.]()
- [2.5 Unterstützung des Fachbereichs beim Erstellen des Lastenhefts.]()

#### 3 Entwurf
- [3.1 Entwurf der Datenbank und der Anwendungsstruktur.]()
- [3.2 Entwurf der Benutzeroberfläche inkl. Erstellung von Mock-Ups.]()
- [3.3 Erstellung eines ER-Modells.]()
- [3.4 Entwurf der PDF auf Basis der Oberfläche.]()
- [3.5 Planung der Architektur inkl. Erstellung eines Komponentendiagramms.]()
- [3.6 Erstellung des Pflichtenhefts.]()

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
- [6.1 Erstellung des Benutzerhandbuchs.]()
- [6.2 Erstellung der Entwicklerdokumentation.]()

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

#### 2.3 Ermittlung von Anwendungsfällen inkl. Erstellung eines Anwendungsfall-Diagramms.

#### 2.4 Erstellung einer erweiterten Ereignisgesteuerten Prozesskette.

#### 2.5 Unterstützung des Fachbereichs beim Erstellen des Lastenhefts.



#### [Zustand:](https://website-h0nc5tb9m-pmndrs.vercel.app/zustand/introduction)
Es ist eine Bibliothek zur Zustandsverwaltung für React. Sie bietet eine einfache und minimalistische Möglichkeit, den Zustand in React-Anwendungen zu verwalten, ohne die Komplexität anderer robusterer Lösungen zur Zustandsverwaltung.

#### [Tanstack Query:](https://tanstack.com/query/v4/docs/framework/react/overview)
Es ist Teil des Tanstack-Ökosystems, das React Query und React Query Devtools umfasst. Es wird verwendet, um Abfragen und Aktualisierungen von Daten in React-Anwendungen effizient zu verwalten und die Verwaltung des Zustands im Zusammenhang mit dem Abrufen und Bearbeiten von Daten zu vereinfachen.

#### [Styled Components:](https://styled-components.com/)
Es ist eine Bibliothek für React, die es ermöglicht, CSS-Stile mit JavaScript-Syntax innerhalb von React-Komponenten zu schreiben. Sie erleichtert die Erstellung von Komponenten mit gekapselten und wiederverwendbaren Stilen, wodurch die Modularität und Wartbarkeit des Codes verbessert wird.

#### [React:](https://react.dev/learn/start-a-new-react-project)
Ist eine JavaScript-Bibliothek zum Erstellen von Benutzeroberflächen. Sie wurde von Facebook entwickelt und konzentriert sich auf die Erstellung wiederverwendbarer Komponenten, die ihren eigenen Zustand verwalten. React verwendet einen deklarativen Ansatz zur Erstellung von Benutzeroberflächen, was das Verständnis und die Wartung des Codes erleichtert.

#### [npm (Node Package Manager):](https://docs.npmjs.com/cli/v6/commands/npm-install)
Es ist der Standard-Paketmanager für die JavaScript-Laufzeitumgebung Node.js.

#### [Supabase:](https://supabase.com/)
 Ist eine Entwicklungsplattform, die gebrauchsfertige Backend-Dienste bereitstellt. Sie bietet eine PostgreSQL-Datenbank, Authentifizierung, Dateispeicherung und Serverless-Funktionen. Mit Supabase können Entwickler effizient Web- und mobile Anwendungen erstellen, ohne sich um die Einrichtung und Verwaltung des Backends kümmern zu müssen.

#### [PostgreSQL:](https://www.postgresql.org/)
Es handelt sich um ein relationales Datenbankmanagementsystem, das quelloffen und erweiterbar ist. Es ist bekannt für seine Robustheit, Skalierbarkeit und die Fähigkeit, große Datenmengen zu verarbeiten. Es wird häufig als Backend-Datenbank für verschiedene Anwendungen verwendet und bietet Unterstützung für komplexe Abfragen und Transaktionen.

#### [pgAdmin:](https://www.pgadmin.org/)
PostgreSQL-Tool
pgAdmin ist die beliebteste und funktionsreichste Open-Source-Plattform für die Entwicklung und Administration von PostgreSQL, der weltweit fortschrittlichsten Open-Source-Datenbank.

#### [React PDF:](https://react-pdf.org/)
Es ist eine Bibliothek, die die Generierung von PDF-Dokumenten in React-Anwendungen vereinfacht. Sie ermöglicht die dynamische Erstellung von PDF-Dokumenten mithilfe von React-Komponenten, was die Generierung von Berichten, Rechnungen oder anderen Dokumenten einfacher und vom Client aus steuerbarer macht.

Diese Technologien werden häufig in der modernen Webentwicklung eingesetzt und bieten effiziente und flexible Werkzeuge für die Erstellung von Benutzeroberflächen, die Verwaltung von Zuständen, die Manipulation von Daten und die Generierung von Dokumenten.

#### [UI-verse:](https://uiverse.io/)
Die größte Open-Source-Bibliothek für Benutzeroberflächen: HTML/CSS, Tailwind, React und Figma.

#### [PlantUML](https://plantuml.com/de/)
Ist ein äußerst vielseitiges Werkzeug, das die schnelle und unkomplizierte Erstellung einer Vielzahl von Diagrammen ermöglicht.

#### [Markdown editor](https://code.visualstudio.com/Docs/languages/markdown)
Ist eine leichtgewichtige Auszeichnungssprache, mit der du Texte einfach formatieren kannst. Du kannst Klartext schreiben und bearbeiten und dabei eine einfache Syntax verwenden, um Elemente wie Überschriften, Listen, Links und Fettdruck zu erstellen, die dann in HTML umgewandelt werden.

<a href="https://github.com/dwn10/C_C_C/blob/main/Documentation/PlantUML/secuence.plantuml" target="_blank">
  <img src="Documentation\img\diagram1.png" style="height: 80%; width:80%;"/>
</a>

>.[!NOTE].
> Esto es especial
