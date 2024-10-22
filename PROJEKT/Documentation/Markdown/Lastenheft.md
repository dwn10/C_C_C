# Lastenheft für das Inventarsystem mit React und Supabase
#### 1. Einleitung
Dieses Dokument beschreibt die Anforderungen an ein neues Web Inventarsystem für die SOFTWEAVER GmbH. Das aktuelle System ist nicht webbasiert und kann nur von einem PC aus verwaltet werden, was zu Einschränkungen bei der Flexibilität und dem Zugriff führt. Das neue System soll diese Einschränkungen beseitigen und eine effiziente Verwaltung von Produkten, Lagerbeständen und Ressourcen ermöglichen.

#### 2. Anforderungen

#### 2.1 Funktionale Anforderungen

| Anforderung | Priorität | Beschreibung |
|---|---|---| 
| Benutzerauthentifizierung | Muss | Das System muss eine sichere Benutzerauthentifizierung mit verschiedenen Rollen (z. B. Administrator, Mitarbeiter) ermöglichen. |
| Produktverwaltung | Muss | Das System muss die Verwaltung von Produktinformationen wie Name, Code, Beschreibung, Kategorie, Preis, Lagerbestand und Bilder ermöglichen. |
| Bestandsverwaltung | Muss | Das System muss die Verwaltung des Lagerbestands in Echtzeit ermöglichen, einschließlich Zugängen, Abgängen und Warnungen bei niedrigem Bestand. |
| Lieferantenmanagement | Muss | Das System muss die Verwaltung von Lieferanteninformationen ermöglichen, einschließlich Kontaktinformationen, Historie von Käufen und Bestellungen. |
| Berichtsgenerierung | Muss | Das System muss die Generierung von anpassbaren Berichten im PDF-Format ermöglichen, z. B. über den aktuellen Lagerbestand, die Bewegungshistorie und Verkäufe. |
| API-Integration | Kann | Das System kann optional die Integration mit externen Diensten über APIs ermöglichen, z. B. zur Synchronisierung von Daten mit ERP- oder E-Commerce-Plattformen. |
| Responsive Design | Muss | Das System muss auf verschiedenen Geräten (Desktop, Tablet, Smartphone) optimal dargestellt werden. |
| Intuitive Benutzeroberfläche | Muss | Das System muss eine benutzerfreundliche und intuitive Oberfläche bieten, die eine einfache Navigation und Bedienung ermöglicht. |
| Suche und Filterung | Muss | Das System muss eine erweiterte Suche und Filterung von Produkten ermöglichen. |
| Echtzeitaktualisierung | Muss | Das System muss Aktualisierungen des Lagerbestands in Echtzeit anzeigen. |
| Automatische Warnmeldungen | Muss | Das System muss automatische Warnmeldungen bei niedrigem oder fehlendem Lagerbestand generieren. |

#### 2.2 Nicht-funktionale Anforderungen

| Anforderung | Priorität | Beschreibung |
|---|---|---|
| Leistung | Muss | Das System muss eine gute Leistung und schnelle Ladezeiten aufweisen. |
| Sicherheit | Muss | Das System muss sensible Daten schützen und die Datenintegrität gewährleisten. |
| Skalierbarkeit | Kann | Das System sollte skalierbar sein, um zukünftiges Wachstum und zusätzliche Anforderungen zu bewältigen. |
| Zuverlässigkeit | Muss | Das System muss zuverlässig und stabil funktionieren. |
| Wartbarkeit | Muss | Der Systemcode muss gut dokumentiert und leicht zu warten sein. |

---
# Pflichtenheft

#### 1. Einleitung
Dieses Dokument beschreibt die Anforderungen an das zu entwickelnde Webinventarsystem für die SOFTWEAVER GmbH. Es basiert auf dem Projektantrag und den Ergebnissen der Analysephase. Das Dokument dient als Grundlage für die Implementierung und definiert die Funktionen, Qualitätsmerkmale und Rahmenbedingungen des Systems.

#### 2. Ziele
Das neue Inventarsystem soll folgende Ziele erreichen:

- **Optimierung der Bestandsverwaltung:** Verbesserung der Transparenz und Kontrolle über den Lagerbestand, Reduzierung von Kosten und Vermeidung von Verlusten.
- **Fundierte Entscheidungen:** Bereitstellung präziser Daten für strategische Entscheidungen in Einkauf, Verkauf und Produktion.
- **Effizienzsteigerung:** Automatisierung von Prozessen und Reduzierung manueller Eingriffe.
- **Skalierbarkeit:** Flexibilität und Anpassungsfähigkeit an zukünftige Anforderungen und Unternehmenswachstum.
- **Sicherheit und Zuverlässigkeit:** Schutz sensibler Daten und Sicherstellung der Datenintegrität.

#### 3. Anforderungen

#### 3.1 Funktionale Anforderungen
Die funktionalen Anforderungen beschreiben die Funktionen, die das System erfüllen muss.

- **Produktverwaltung:**
Muss: Erfassung detaillierter Produktinformationen (Name, Code, Beschreibung, Kategorie, Preis, Lagerbestand, Bilder).
Muss: Ermöglichen einer erweiterten Produktsuche und -filterung.
Muss: Aktualisierung von Produktinformationen in Echtzeit.
Sollte: Flexible Kategorisierung und Kennzeichnung von Produkten.

- **Bestandsverwaltung:**
    - **Muss:** Echtzeit-Anzeige des verfügbaren Lagerbestands.
    - **Muss:** Automatische Warnmeldungen bei niedrigem Lagerbestand.
    - **Sollte:** Erfassung und Historie aller Lagerbewegungen (Zugänge, Abgänge, Umbuchungen).
    - **Kann:** Automatische Berechnung von Lagerkosten.

- **Lieferantenmanagement:**
    - **Sollte:** Registrierung und Verwaltung von Lieferanteninformationen.
    - **Kann:** Historie von Käufen und Bestellungen.
    - **Kann:** Leistungsbewertung von Lieferanten.

- **Berichtsgenerierung:**
    - **Muss:** Generierung von anpassbaren Berichten (Lagerbestand, Bewegungshistorie, Verkäufe).
    - **Muss:** Export von Berichten im PDF-Format.
    - **Kann:** Grafische Darstellung von Daten in Diagrammen und Tabellen.

- **API-Integration:**
    - **Kann:** Integration mit externen Diensten (ERP, E-Commerce) zur Datensynchronisation.
    - **Kann:** Anreicherung von Produktinformationen mit externen Daten.

- **Sicherheit und Zugangskontrolle:**
    - **Muss:** Benutzerauthentifizierung und -autorisierung mit Rollenzuweisung (Administrator, Mitarbeiter).
    - **Muss:** Berechtigungssystem für verschiedene Aktionen (Lesen, Schreiben, Löschen).
    - **Sollte:** Protokollierung relevanter Benutzeraktionen (Audit-Trail).

#### 3.2 Nicht-funktionale Anforderungen
Die nicht-funktionalen Anforderungen beschreiben die Qualitätsmerkmale des Systems.

- **Benutzerfreundlichkeit:**
    - **Muss:** Das System muss intuitiv und einfach zu bedienen sein, auch für unerfahrene Benutzer.
    - **Sollte:** Die Benutzeroberfläche muss konsistent und ergonomisch gestaltet sein.

- **Leistung:**
    - **Muss:** Das System muss schnell und effizient arbeiten, auch bei großen Datenmengen.
    - **Sollte:** Die Antwortzeiten müssen kurz sein, insbesondere bei kritischen Funktionen.

- **Zuverlässigkeit:**
    - **Muss:** Das System muss stabil und zuverlässig funktionieren und Datenverlust vermeiden.
    - **Sollte:** Das System muss eine hohe Verfügbarkeit aufweisen.

- **Skalierbarkeit:**
    - **Sollte:** Das System muss in der Lage sein, mit wachsenden Datenmengen und Benutzerzahlen umzugehen.
    - **Kann:** Die Architektur des Systems muss eine einfache Erweiterung und Anpassung ermöglichen.

- **Sicherheit:**
    - **Muss:** Das System muss sensible Daten vor unbefugtem Zugriff schützen.
    - **Muss:** Die Datenintegrität muss gewährleistet sein.

#### 4. Systemarchitektur
- **Frontend:** React mit TypeScript, TanStack Query und TanStack Table.
- **Backend:** Supabase (PostgreSQL, Authentifizierung, Storage).
- **Berichtsgenerierung:** React-pdf.

#### 5. Benutzeroberfläche
- Modernes und responsives Design, optimiert für verschiedene Endgeräte.
- Klare Navigationsstruktur und intuitive Benutzerführung.
- Konsistente Gestaltung und übersichtliche Darstellung der Informationen.

#### 6. Testen
- Umfassende Tests während der Entwicklung (Unit-Tests, Integrationstests).
- Abschließende Abnahmetests durch den Fachbereich.

#### 7. Dokumentation
- **Muss:** Erstellung eines Benutzerhandbuchs.
- **Sollte:** Erstellung einer technischen Dokumentation für Entwickler.

#### 8. Wartung und Support
- Regelmäßige Wartung und Updates des Systems.
- Bereitstellung von Support für Benutzer.

#### 9. Glossar
- **API:** Application Programming Interface
- **ERP:** Enterprise Resource Planning
- **Frontend:** Benutzeroberfläche
- **Backend:** Server-seitige Logik
- **Supabase:** Open-Source Backend-as-a-Service Plattform
- **React:** JavaScript-Bibliothek zur Erstellung von Benutzeroberflächen

#### 10. Anhang
- **Anforderungsspezifikation**
- **Gantt-Diagramm**
- **ER-Modell**
- **Komponentendiagramm**
- **Mock-ups**