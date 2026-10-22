# 🚀 Antigravity Custom Skills Suite

Willkommen im Repository für **benutzerdefinierte Fähigkeiten (Custom Skills)** des **Antigravity**-Assistenten. 
Diese Sammlung umfasst ein Set hochspezialisierter Agenten und Rollen, die den gesamten Lebenszyklus der Softwareentwicklung abdecken – von der Architekturplanung über UI-Design und SEO bis hin zu Testing, Sicherheit und Bereitstellung.

## ⚙️ Globale Installation und Konfiguration

Es gibt zwei Hauptwege, um diese Skills in deiner Antigravity-Umgebung zu laden:

### Option 1: Globale native Installation (Empfohlen)
Damit die Skills in **jedem Projekt** auf deiner Festplatte automatisch verfügbar sind:
1. Kopiere alle Ordner dieses Repositories (z. B. `000-der-planer`, `01-der-architekt`, `00-skills-ersteller`, usw.).
2. Füge sie in das globale Stammverzeichnis für Antigravity-Anpassungen ein:
   ```
   C:\Users\<Benutzer>\.gemini\config\plugins\custom-skills\skills\
   ```
   *(Falls der Ordner `custom-skills/skills` noch nicht existiert, erstelle ihn).*
3. Nach dem Kopieren erkennt Antigravity die `SKILL.md`-Dateien jedes Ordners automatisch anhand ihres Frontmatters. Ein Neustart ist nicht erforderlich.

### Option 2: Projektbezogene Installation (Lokal / Workspace)
Wenn du diese Skills nur in einem bestimmten Projekt verwenden möchtest:
1. Erstelle im Wurzelverzeichnis deines Projekts einen Ordner namens `.agents/skills/`.
2. Kopiere die gewünschten Skill-Ordner in dieses Verzeichnis.
3. Antigravity priorisiert und verwendet sie ausschließlich, während dieser Arbeitsbereich geöffnet ist.

### Option 3: Registrierung über `skills.json` (Plugin / Shared)
Wenn du dieses Repository an seinem ursprünglichen Pfad (`DEV/Skills-Agents`) belassen und lediglich verknüpfen möchtest:
1. Erstelle oder bearbeite die Datei `skills.json` unter `C:\Users\<Benutzer>\.gemini\config\skills.json`.
2. Füge den Pfad dieses Repositories zum Array `entries` hinzu:
   ```json
   {
     "entries": [
       { "path": "C:/Users/<Benutzer>/Documents/DEV/Skills-Agents" }
     ]
   }
   ```

---