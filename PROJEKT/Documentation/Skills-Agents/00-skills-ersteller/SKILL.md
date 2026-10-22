---
name: 00-skills-ersteller
description: Eine spezialisierte Fähigkeit zur Erstellung neuer Skills für das Antigravity-System unter Gewährleistung dualer Synchronisation und Best Practices.
---

# Skill-Ersteller (Skills Creator) 🛠️✨

Diese Fähigkeit fungiert als Assistent und Leitfaden für die Erstellung neuer Fähigkeiten (Skills) innerhalb der Antigravity-Umgebung. Ihr Ziel ist es sicherzustellen, dass alle neuen Skills einer kohärenten Struktur folgen, präzise dokumentiert sind, korrekt im System synchronisiert werden und Best Practices einhalten.

## Struktur eines Skills

Jeder Skill muss in einem eigenen Ordner liegen und mindestens eine `SKILL.md`-Datei enthalten.

- **Skill-Verzeichnis/**: Deskriptiver Name in Kleinbuchstaben mit Bindestrichen und Nummerierung, falls zutreffend (z. B. `17-neue-faehigkeit` oder `00-skills-ersteller`).
    - **SKILL.md**: Die Hauptdatei, welche die Logik und Metadaten des Skills definiert.
    - **references/**: (PFLICHT BEI BEISPIELEN) Zusätzliche Dokumentation, Vorlagen oder `BEISPIEL.md`-Dateien. Niemals lose Beispieldateien im Wurzelverzeichnis des Skills ablegen.
    - **scripts/**: (Optional) Enthält Skripte (Python, Node, Bash), die der Skill ausführen kann.
    - **assets/**: (Optional) Bilder, Icons oder statische Ressourcen.

## Kritische Regeln für Erstellung und Synchronisation

**KRITISCH**: Skills *müssen* gleichzeitig an **zwei Orten** erstellt oder aktualisiert werden. Der Benutzer verwaltet seinen Code in einem Git-Repository, der Agent liest die Skills jedoch aus seiner globalen Konfiguration.

1. **Internes Agenten-Verzeichnis**: `C:\Users\.gemini\config\plugins\custom-skills\skills\` (Hier liest der Agent sie nativ).
2. **Repository-Verzeichnis des Benutzers**: `C:\Users\Documents\DEV\Skills-Agents\` (Hier versioniert der Benutzer sie mit Git).

Beim Erstellen oder Bearbeiten eines Skills:
- Wende Änderungen **stets auf beide Pfade** an (entweder über PowerShell-Befehle wie `Copy-Item -Recurse` oder durch gleichzeitiges Schreiben an beiden Speicherorten).
- Wenn du eine Beispieldatei erstellst, stelle sicher, dass der Ordner `references/` (in beiden Pfaden) existiert und speichere sie darin ab.

## Die Datei SKILL.md

Die Datei `SKILL.md` gliedert sich in zwei kritische Abschnitte:

### 1. YAML Frontmatter (Metadaten)
Ganz am Anfang der Datei, abgegrenzt durch `---`. Das System verwendet diesen Block zur Indizierung und Entscheidung, wann der Skill geladen wird.

- `name`: Eindeutiger Bezeichner (stimmt in der Regel mit dem Ordnernamen überein, z. B. `00-skills-ersteller`).
- `description`: **KRITISCH**. Eine präzise Beschreibung in der dritten Person, die erklärt, was der Skill tut und wann er relevant ist. Muss relevante Schlüsselwörter enthalten.

### 2. Markdown-Hauptteil (Anweisungen)
Nach dem Frontmatter folgen die detaillierten Verhaltensanweisungen für den Agenten. Hier wird Schritt für Schritt beschrieben, wie sich der Agent verhalten soll, wenn dieser Skill aktiv ist.

## Workflow zur Erstellung eines Skills

1. **Zweck definieren**: Welches Problem löst der Skill?
2. **Namen wählen**: Ein klarer und konsistenter Ordnername.
3. **YAML verfassen**: Sicherstellen, dass die `description` hochgradig präzise ist.
4. **Instruktionen formulieren**: Spezifische Angaben zu den Werkzeugen, die der Agent nutzen soll, und dem einzuhaltenden Tonfall.
5. **Erstellen und Synchronisieren**: Schreibe die Dateien in das interne Agenten-Verzeichnis UND in das Arbeitsverzeichnis des Benutzers (`Skills-Agents`). Denke daran, Beispiele in den Ordner `references/` zu legen.
6. **Katalog aktualisieren (`README.md`)**: Trage den neuen Skill in der entsprechenden Kategorie der `README.md` ein (oder erstelle die Datei neu, falls sie fehlt).

## Dokumentation und Aktualisierung des Katalogs (`README.md`)

Jedes Mal, wenn ein neuer Skill erstellt wird oder wenn der Benutzer eine strukturierte Dokumentation/Auditierung des Repositories anfordert:

1. **Überprüfung des Vorhandenseins**:
   - Prüfen, ob die Datei `README.md` im Wurzelverzeichnis des Repositories (`DEV/Skills-Agents/README.md`) existiert.
   - **Falls nicht vorhanden**: Neu von Grund auf generieren, inklusive Einleitung, globalen Installationsanweisungen und thematischem Katalog.
   - **Falls vorhanden**: Chirurgisch bearbeiten, um den neuen Skill in die passende Sektion einzufügen, ohne bestehende Einträge zu beschädigen oder Duplikate zu erzeugen.

2. **Katalogisierungsregeln**:
   - **Nummerierte Exklusivität**: Nur offizielle Skills mit numerischem Präfix registrieren (z. B. `000-...`, `001-...`, `0b-...`, `36-...`, `88-...`), Entwürfe oder unnummerierte Hilfsordner ignorieren, sofern nicht anders angewiesen.
   - **Einordnung in die korrekte Kategorie**: Den Skill unter Einhaltung der numerischen Sequenz in die entsprechende thematische Gruppe einfügen:
     - 🧠 *Core & Orchestrierung* (z. B. `000`, `00`, `0`, `19`, `88`)
     - 🧭 *Fase 0: Strategie, Business & Entdeckung* (z. B. `0b`)
     - 🏗️ *Software Engineering & Architektur* (z. B. `001`, `01`, `02a`, `02b`, `03`, `04`, `05`, `06`, `11`, `17`, `22`, `33`, `36`)
     - 🎨 *Frontend-Design, UI & Komponenten* (z. B. `02c`, `02d`, `08`, `12`, `14`, `15`, `16`, `23`, `24`, `24b`)
     - ⚖️ *Recht & Compliance* (z. B. `13`, `13b`, `13c`)
     - 💸 *Zahlungen & Monetarisierung* (z. B. `25`, `26`, `28`)
     - 🌍 *SEO, Wachstum & Lokalisierung* (z. B. `07`, `09`, `10`, `10b`, `10c`, `27`)
     - 🔐 *Sicherheit & Cyber-Defense* (z. B. `31`, `31a`, `31b`, `32`)
     - 🤖 *Fortgeschrittene KI & Dienstprogramme* (z. B. `18`, `20`, `21`, `30`, `34`, `35`)
   - **Standard-Eintragsformat**:
     `- **`[ordnername]`**: [Prägnante Zusammenfassung des Zwecks und der wichtigsten Werkzeuge].`
   - **Dateihygiene**: Datei sauber halten, ohne redundante Leerzeilen am Ende des Dokuments.

---
*Hinweis: Halte die Beschreibungen präzise und achte stets auf die strikte duale Synchronisation zwischen dem Arbeitsbereich und der globalen Antigravity-Konfiguration.*
