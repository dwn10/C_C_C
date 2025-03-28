<p align="center">
  <a href="https://github.com/dwn10/C_C_C/blob/main/PROJEKT/Documentation/Markdown/README.md#inventarsystem" target="_blank">Dokumentation</a> •
  <a href="https://github.com/dwn10/C_C_C/blob/main/PROJEKT/Documentation/Markdown/User.md#benutzerhandbuch" target="_blank">Benutzerdokumentation</a> •
  <a href="https://github.com/dwn10/C_C_C/blob/main/PROJEKT/Documentation/Markdown/DiagrammeIMG.md#diagramme" target="_blank">Diagramme</a> •
  <a href="https://github.com/dwn10/C_C_C/blob/main/PROJEKT/Documentation/Markdown/Links.md#projektlinks-und-ressourcen" target="_blank">Projektlinks</a>
</p>

### Entwicklerdokumentation
Dieses webbasierte Inventarsystem basiert auf einer modernen Architektur, die die Leistungsfähigkeit von React im Frontend mit der Flexibilität von Supabase im Backend kombiniert.
React, eine JavaScript-Bibliothek, ermöglicht den Aufbau einer dynamischen, schnellen und intuitiven Benutzeroberfläche, die das Benutzererlebnis verbessert. Supabase hingegen, eine BaaS-Plattform (Backend as a Service), bietet alle notwendigen Tools für das Backend, einschliesslich einer robusten Datenbank, eines sicheren Authentifizierungssystems und skalierbarer Speicheroptionen.
Diese Kombination von Technologien führt zu einem effizienten, robusten und einfach zu wartenden webbasierten Inventarsystem.

#### Frontend (React):
- React wird verwendet, um eine intuitive und responsive Benutzeroberfläche zu erstellen.
- TanStack Query wird verwendet, um Serveranfragen zu stellen und Daten zu verwalten.
- TanStack Table erleichtert die Anzeige von Daten in Tabellen.
- React-pdf ermöglicht die Generierung von Berichten im PDF-Format.

#### Backend (Supabase):
- Supabase stellt die Backend-Infrastruktur bereit, einschließlich der PostgreSQL-Datenbank.
- Supabase verwaltet auch die Authentifizierung und Autorisierung von Benutzern.
- Die Dateispeicherung erfolgt über Supabase.

#### Hauptfunktionen:
- **Produktverwaltung:** Produkte registrieren, ändern, suchen und filtern.
- **Bestandsverwaltung:** Echtzeit-Bestandskontrolle, Warnungen bei niedrigem Lagerbestand.
- **Lieferantenverwaltung:** Registrierung und Verwaltung von Lieferanteninformationen.
- **Berichtsgenerierung:** Erstellung von benutzerdefinierten Berichten im PDF-Format.
- **API-Integration:** Verbindung mit externen Diensten zur Datensynchronisierung.

## Ein "Inventar"-Projekt mit React und Supabase in Visual Studio Code erstellen:
#### Schritt 1: Umgebung vorbereiten

- **Node.js und npm installieren:** Lade die neueste Version von Node.js von der offiziellen Website (https://nodejs.org/) herunter und installiere sie. npm wird zusammen mit Node.js installiert.
- **Visual Studio Code installieren:** Lade Visual Studio Code von der offiziellen Website (https://code.visualstudio.com/) herunter und installiere es.
- **React-Erweiterung für VS Code installieren:** Öffne VS Code und suche im Marketplace nach der Erweiterung "Reactjs code snippets". Installiere sie, um das Schreiben von React-Code zu vereinfachen.

___
#### Schritt 2: React-Projekt erstellen

- **Terminal öffnen:** Öffne in VS Code das integrierte Terminal (Ansicht > Terminal).
- **Anwendung erstellen:** Verwende Create React App, um ein neues Projekt zu generieren:

```bash
# Terminal
npx create-react-app inventar
````

```bash
cd inventar
```

- **Anwendung starten:** Führe den folgenden Befehl aus, um den Entwicklungsserver zu starten:
```bash
npm run dev
```
___
#### Schritt 3: Supabase konfigurieren

- **Supabase-Konto erstellen:** Gehe zur Supabase-Website (https://supabase.com/) und erstelle ein kostenloses Konto.
- **Neues Projekt erstellen:** Erstelle im Supabase-Dashboard ein neues Projekt und wähle die Region, die deinem Standort am nächsten liegt.
- **Anmeldeinformationen abrufen:** Im Abschnitt "Project Settings" > "API" findest du die URL und den API-Schlüssel. Speichere diese Informationen, da du sie benötigst, um deine React-Anwendung mit Supabase zu verbinden.

___
#### Schritt 4: Supabase-Bibliothek installieren

- **Supabase-Client installieren:** Führe in deinem Projektterminal den folgenden Befehl aus:

```bash
npm install @supabase/supabase-js
```
___
#### Schritt 5: Anwendung mit Supabase verbinden

- **Datei für die Konfiguration erstellen:** Erstelle eine Datei namens supabaseClient.js im Stammverzeichnis deines Projekts (z. B. in src/supabaseClient.js).
- **Client initialisieren:** Füge den folgenden Code zur Datei supabaseClient.js hinzu und ersetze your-project-url und your-anon-key durch deine eigenen Anmeldeinformationen:

```js
 JavaScript
import { createClient } from '@supabase/supabase-js'

const supabaseUrl = 'your-project-url'
const supabaseAnonKey = 'your-anon-key'

export const supabase = createClient(supabaseUrl, supabaseAnonKey)

```
___
#### Schritt 6: Datenbank entwerfen

- **Zugriff auf den SQL-Editor:** Gehen Sie im Supabase-Dashboard zum Abschnitt `"SQL-Editor"`.
- **Tabelle "produkte" erstellen:** Führen Sie den folgenden SQL-Code aus, um eine 
Tabelle zum Speichern der Produktinformationen zu erstellen:

```sql
SQL
create table produkte (
id bigint generated by default as identity primary key,
name text not null,
beschreibung text,
menge integer not null,
preis numeric(10, 2) not null
);
```
___
#### Schritt 7: Benutzeroberfläche erstellen

- **Komponenten erstellen:** Erstelle React-Komponenten für die verschiedenen Teile deiner Anwendung, wie z.B.:

    - **Produktliste:** Um die Liste der Produkte anzuzeigen.
    - **ProduktHinzufügen:** Ein Formular zum Hinzufügen neuer Produkte.
    - **ProduktBearbeiten:** Ein Formular zum Bearbeiten bestehender Produkte.
- **Supabase-Bibliothek verwenden:** Verwende in deinen Komponenten die im Schritt 5 erstellte `supabase`-Instanz, um mit der Datenbank zu interagieren. Du kannst zum Beispiel `supabase.from('produkte').select() verwenden`, um die Produktliste abzurufen.

___
#### Schritt 8: Funktionen hinzufügen

- **CRUD implementieren:** Implementiere die CRUD-Operationen (Erstellen, Lesen, Aktualisieren, Löschen), um die Produkte in deinem Inventar zu verwalten.
- **Authentifizierung hinzufügen:** Wenn du den Zugriff auf deine Anwendung kontrollieren möchtest, kannst du die Authentifizierungsfunktionen von Supabase verwenden.
- **Zusätzliche Funktionen hinzufügen:** Du kannst deiner Anwendung weitere Funktionen hinzufügen, wie z.B. Produktsuche, Filter usw.

#### Beispiel für die Komponente Produktliste:

```js

import React, { useState, useEffect } from 'react';
import { supabase } from './supabaseClient';

function Produktliste() {
  const [produkte, setProdukte] = useState([]);

  useEffect(() => {
    const produkteAbrufen = async () => {
      const { data, error } = await supabase
        .from('produkte')
        .select('*');


      if (error) {
        console.error('Fehler beim Abrufen der Produkte:', error);
      } else {
        setProdukte(data);
      }
    };

    produkteAbrufen();
  }, []);

  return (
    <ul>
      {produkte.map((produkt) => (
        <li key={produkt.id}>
          {produkt.name} - {produkt.anzahl} Einheiten
        </li>
      ))}
    </ul>
  );
}

export default Produktliste;

```

## Kernpunkte des Projekts:

#### Teil der Datenbankstruktur

```sql

-- Produkte
CREATE TABLE
  public.produkte (
    id bigint NOT NULL,
    beschreibung text NOT NULL,
    idmarke bigint,
    bestand numeric,
    mindestbestand numeric,
    strichcode text,
    interner_code text,
    verkaufspreis numeric,
    einkaufspreis numeric,
    id_kategorie bigint,
    id_firma bigint
  );

ALTER TABLE public.produkte OWNER TO postgres;

ALTER TABLE public.produkte
ALTER COLUMN id
ADD GENERATED BY DEFAULT AS IDENTITY (
  SEQUENCE NAME public.produkte_id_seq START
  WITH
    1 INCREMENT BY 1 NO MINVALUE NO MAXVALUE CACHE 1
);

ALTER TABLE ONLY public.produkte
ADD CONSTRAINT produkte_pkey PRIMARY KEY (id);

ALTER TABLE ONLY public.produkte
ADD CONSTRAINT produkte_id_kategorie_fkey FOREIGN KEY (id_kategorie) REFERENCES public.kategorien (id);

ALTER TABLE ONLY public.produkte
ADD CONSTRAINT produkte_id_firma_fkey FOREIGN KEY (id_firma) REFERENCES public.firma (id) ON DELETE CASCADE;

ALTER TABLE ONLY public.produkte
ADD CONSTRAINT produkte_idmarke_fkey FOREIGN KEY (idMarke) REFERENCES public.marke (id);

CREATE POLICY "Löschberechtigung für Benutzer basierend auf Benutzer-ID aktivieren" ON public.produkte FOR DELETE TO authenticated USING ((id = id));

CREATE POLICY "Einfügen nur für authentifizierte Benutzer aktivieren" ON public.produkte FOR INSERT TO authenticated
WITH
  CHECK (true);

CREATE POLICY "Lesezugriff für alle Benutzer aktivieren" ON public.produkte FOR
SELECT
  USING (true);

CREATE POLICY "Aktualisierung für Benutzer basierend auf E-Mail aktivieren" ON public.produkte
FOR UPDATE
  TO authenticated USING ((id = id))
WITH
  CHECK ((id = id));

```

Die Tabelle **"Produkte"** speichert Informationen über die Produkte, einschließlich:

- **id:** Eindeutige Kennung des Produkts (autoinkrementell).
- **beschreibung:** Textuelle Beschreibung des Produkts.
- **id_marke:** Kennung der Marke des Produkts.
- **stock:** Aktuelle Menge im Inventar.
- **aktueller _lagerbestand:** Mindestmenge, die im Inventar vorhanden sein muss.
- **barcode:** Barcode des Produkts.
- **interner_code:** Interne Produktcode.
- **verkaufspreis:** Verkaufspreis des Produkts.
- **kaufpreis:** Einkaufspreis des Produkts.
- **id_kategorie:** Kennung der Kategorie des Produkts.
- **id_firma:** Kennung des Unternehmens, zu dem das Produkt gehört.

**Einschränkungen:**

- **produkte_pkey:** Definiert die Spalte "id" als Primärschlüssel, um sicherzustellen, dass jedes Produkt eine eindeutige Kennung hat.
- **produkte_id_Kategorie_fkey:** Definiert einen Fremdschlüssel, der die Spalte "id_Kategorie" mit der Tabelle "Kategorien" verknüpft.
- **produkte_id_Firma_fkey:** Definiert einen Fremdschlüssel, der die Spalte **"id_Firma"** mit der Tabelle **"Firma"** verknüpft und festlegt, dass beim Löschen eines Unternehmens auch die zugehörigen Produkte gelöscht werden (ON DELETE CASCADE).
- **produkte_idMarke_fkey:** Definiert einen Fremdschlüssel, der die Spalte **"id_marke"** mit der Tabelle **"Marke"** verknüpft.

**Zugriffsrichtlinien:**

- **"Enable delete for users based on user_id":** Ermöglicht authentifizierten Benutzern das Löschen von Produkten.
- **"Enable insert for authenticated users only":** Ermöglicht nur authentifizierten Benutzern das Einfügen neuer Produkte.
- **"Enable read access for all users":** Ermöglicht allen Benutzern das Lesen der Produktinformationen.
- **"Enable update for users based on email":** Ermöglicht authentifizierten Benutzern das Aktualisieren der Produktinformationen.

Dieser Code erstellt eine Tabelle zum Speichern von Produktinformationen mit den erforderlichen Beziehungen zu anderen Tabellen und definiert Zugriffsrichtlinien, um zu steuern, wer Daten in der Tabelle lesen, einfügen, aktualisieren und löschen darf.

___
#### Users Zugriffsrichtlinien:

```sql

ALTER TABLE public.users OWNER TO postgres;

ALTER TABLE public.users
ALTER COLUMN id
ADD GENERATED BY DEFAULT AS IDENTITY (
  SEQUENCE NAME public.users_id_seq START
  WITH
    1 INCREMENT BY 1 NO MINVALUE NO MAXVALUE CACHE 1
);

ALTER TABLE ONLY public.users
ADD CONSTRAINT users_pkey PRIMARY KEY (id);

CREATE POLICY "Enable delete for users based on user_id" ON public.users FOR DELETE TO authenticated USING ((id = id));

CREATE POLICY "Enable insert for authenticated users only" ON public.users FOR INSERT TO authenticated
WITH
  CHECK (true);

CREATE POLICY "Enable read access for all users" ON public.users FOR
SELECT
  USING (true);

CREATE POLICY "Enable update for users based on email" ON public.users
FOR UPDATE
  TO authenticated USING ((id = id))
WITH
  CHECK ((id = id));

```

- Erlaubt authentifizierten Benutzern das Löschen von Benutzern, wenn die IDs übereinstimmen.
- Erlaubt nur authentifizierten Benutzern das Einfügen von Benutzern.
- Erlaubt allen Benutzern das Lesen der Informationen aus der Tabelle.
- Erlaubt authentifizierten Benutzern das Aktualisieren von Informationen, wenn die IDs übereinstimmen.

Zusammenfassend lässt sich sagen, dass dieser Code eine Tabelle zum Speichern von Benutzerinformationen mit verschiedenen Attributen erstellt und Zugriffsrichtlinien konfiguriert, um die Einfüge-, Lese-, Aktualisierungs- und Löschoperationen von Daten zu steuern.

___
#### Triggers

```sql
-- Trigger

CREATE TRIGGER trigger_aktualisiere_bestand
AFTER INSERT ON public.kardex FOR EACH ROW
EXECUTE FUNCTION public.aktualisiere_bestand();

CREATE TRIGGER trigger_berechtigungen
AFTER INSERT ON public.benutzer FOR EACH ROW
EXECUTE FUNCTION public.insert_berechtigungen();

CREATE TRIGGER trigger_standardwerte
AFTER INSERT ON public.firma FOR EACH ROW
EXECUTE FUNCTION public.insert_standardwerte();

```

Dieser Code definiert drei "Trigger" (Auslöser) in einer Datenbank. Trigger sind Aktionen, die automatisch ausgeführt werden, wenn bestimmte Ereignisse eintreten:

- **trigger_aktualisiere_bestand:** Dieser Trigger wird nach jeder Einfügung (AFTER INSERT) in der Tabelle kardex aktiviert. Seine Funktion ist die Ausführung der Funktion aktualisiere_bestand(), welche den Produktbestand basierend auf dem neuen Eintrag im Kardex aktualisiert.

- **trigger_berechtigungen:** Dieser Trigger wird nach jeder Einfügung (AFTER INSERT) in der Tabelle users aktiviert. Seine Funktion ist die Ausführung der Funktion insert_berechtigungen(), einem neuen Benutzer die Standardberechtigungen zuweist.

- **trigger_standardwerte:** Dieser Trigger wird nach jeder Einfügung (AFTER INSERT) in der Tabelle Firma aktiviert. Seine Funktion ist die Ausführung der Funktion insert_standardwerte(), die Standardwerte oder -daten konfiguriert, wenn ein neue Firma im System angelegt wird.

Diese Trigger automatisieren Aufgaben im Zusammenhang mit der Bestandsverwaltung, den Benutzerberechtigungen und der anfänglichen Konfiguration von Firmen und gewährleisten so die Integrität und Konsistenz der Datenbank.

___
#### CRUD Produkte

```js

// Definiert eine Reihe von Funktionen für die Interaktion mit einer Datenbank (Supabase)
// und die Verwaltung von Produktinformationen.

import { supabase } from "../index";
import Swal from "sweetalert2";
const tabelle = "produkte";

export async function ProdukteEinfuegen(p) {
  try {
    const { error } = await supabase.rpc("produkteEinfuegen", p);
    if (error) {
      console.log("parameter", p);
      console.log("parameter", error.message);
      Swal.fire({
        icon: "error",
        title: "Ups...",
        text: error.message,
        footer: '<a href="">Neue Beschreibung hinzufügen</a>',
      });
    }
  } catch (error) {
    throw error;
  }
}

export async function ProdukteAnzeigen(p) {
  try {
    const { data } = await supabase.rpc("produkteAnzeigen", {
      _id_firma: p._id_firma,
    });
    return data;
  } catch (error) {}
}

export async function ProdukteLoeschen(p) {
  try {
    const { error } = await supabase.from("produkte").delete().eq("id", p.id);
    if (error) {
      alert("Fehler beim Löschen", error);
    }
  } catch (error) {
    alert(error.error_description || error.message + " Produkte löschen");
  }
}

export async function ProdukteBearbeiten(p) {
  try {
    const { error } = await supabase.from("produkte").update(p).eq("id", p.id);
    if (error) {
      alert("Fehler beim Bearbeiten des Produkts", error);
    }
  } catch (error) {
    alert(error.error_description || error.message + " Kategorien bearbeiten");
  }
}

export async function ProdukteSuchen(p) {
  try {
    const { data } = await supabase.rpc("produkteSuchen", {
      _id_firma: p.id_firma,
      suchbegriff: p.beschreibung,
    });
    return data;
  } catch (error) {}
}

// BERICHTE //
export async function ReportLagerbestandAlleProdukte(p) {
  const { data, error } = await supabase
    .from(tabelle)
    .select()
    .eq("id_firma", p.id_firma);
  if (error) {
    return;
  }
  return data;
}

export async function ReportLagerbestandProProdukt(p) {
  const { data, error } = await supabase
    .from(tabelle)
    .select()
    .eq("id_firma", p.id_firma)
    .eq("id", p.id);
  if (error) {
    return;
  }
  return data;
}

export async function ReportLagerbestandUnterMinimum(p) {
  const { data, error } = await supabase.rpc("reportprodukteunterminimum", p); geändert

  if (error) {
    return;
  }
  return data;
}

export async function ReportKardexEinAusgang(p) {
  const { data, error } = await supabase.rpc("kardexunternehmenanzeigen", p);
  if (error) {
    return;
  }
  return data;
}

export async function ReportInventarBewertung(p) {
  const { data, error } = await supabase.rpc("inventarbewertung", p);

  if (error) {

    return;
  }
  return data;
}

```
**Hauptfunktionen:**

- **ProdukteEinfuegen(p):** Fügt ein neues Produkt in die Datenbank ein. Wenn während des Einfügens ein Fehler auftritt, wird dem Benutzer über SweetAlert2 eine Fehlermeldung angezeigt.
- **ProduktAnzeigen(p):** Ruft eine Liste von Produkten aus der Datenbank ab, wahrscheinlich gefiltert nach _id_firma.
- **ProdukteLoeschen(p):** Löscht ein Produkt anhand seiner ID aus der Datenbank. Zeigt bei einem Fehler eine Warnmeldung an.
- **ProduktBearbeiten(p):** Aktualisiert die Informationen eines Produkts in der Datenbank. Zeigt bei einem Fehler eine Warnmeldung an.
- **ProduktSuchen(p):** Sucht nach Produkten in der Datenbank, unter Verwendung von _id_firma und einer Beschreibung als Suchkriterien.

**Berichtsfunktionen:**

- **ReportLagerbestandAlleProdukte(p):** Ruft einen Bericht über den Lagerbestand aller Produkte eine Firma ab.
- **ReportLagerbestandProProdukt(p):** Ruft einen Bericht über den Lagerbestand eines bestimmten Produkts eine Firma ab.
- **ReportLagerbestandUnterMinimum(p):** Ruft einen Bericht über die Produkte ab, deren Lagerbestand unter dem Minimum liegt, unter Verwendung einer in der Datenbank gespeicherten Funktion namens "reportprodukteunterminimum".
- **ReportKardexEinAusgang(p):** Ruft einen Bericht über den Kardex von Wareneingang und -ausgang der Produkte eine Firma ab, unter Verwendung einer in der Datenbank gespeicherten Funktion namens "zeigekardexfirma".
- **ReportInventarBewertung(p):** Ruft einen Bericht über die Inventarbewertung eine Firma ab, unter Verwendung einer in der Datenbank gespeicherten Funktion namens "inventarbewertung".

___
#### App.jsx
Dies ist die Hauptstruktur der Anwendung in React.

```js

import { MyRoutes, Light, Dark, AuthContextProvider } from "./index";

import { createContext, useState } from "react";
import { ThemeProvider } from "styled-components";
import { ReactQueryDevtools } from "@tanstack/react-query-devtools";

export const ThemeContext = createContext(null);
function App() {
  const [themeuse, setTheme] = useState("dark");
  const theme = themeuse === "light" ? "light" : "dark";
  const themeStyle = theme === "light" ? Light : Dark;

  return (
    <>
      <ThemeContext.Provider value={{ theme, setTheme }}>
        <ThemeProvider theme={themeStyle}>
          <AuthContextProvider>
            <MyRoutes />
            <ReactQueryDevtools initialIsOpen={true} />
          </AuthContextProvider>
        </ThemeProvider>
      </ThemeContext.Provider>
    </>
  );
}

export default App;

```

**Importe:**

- **MyRoutes:** Enthält die Routen der Anwendung und definiert, wie zwischen verschiedenen Bildschirmen navigiert wird.
- **Light, Dark:** Sind wahrscheinlich Objekte, die Style für helle bzw. dunkle Themes definieren.
- **AuthContextProvider:** Eine Komponente, die Authentifizierungskontext bereitstellt und die Verwaltung des Benutzerzugriffs ermöglicht.
- **createContext, useState:** React Hooks zum Erstellen von Kontext und Verwalten von Zuständen.
- **ThemeProvider:** Komponente von styled-components zum Anwenden von Themes auf die Anwendung.
- **ReactQueryDevtools:** Entwicklungswerkzeuge für die Bibliothek react-query, die die Verwaltung asynchroner Daten erleichtert.

**Theme-Kontext:**

- **ThemeContext:** Es wird ein Kontext erstellt, um das Theme der Anwendung (hell oder dunkel) zu verwalten.
- **useState("dark"):** Zu Beginn wird das Theme auf "dunkel" gesetzt.

**Hauptfunktion App:**

- **themeuse, setTheme:** Zustand zur Steuerung des aktuellen Themes.
- **theme:** Variable, die das anzuwendende Theme definiert ("light" oder "dark").
- **themeStyle:** Das dem aktuellen Theme entsprechende Stilobjekt wird ausgewählt.
- Es werden die Komponenten innerhalb von Kontext-Providern gerendert:
    - **ThemeContext.Provider:** Stellt das aktuelle Theme und die Funktion zum Ändern des Themes für die gesamte Anwendung bereit.
    - **ThemeProvider:** Wendet das ausgewählte Theme auf die Komponenten an.
    - **AuthContextProvider:** Stellt den Authentifizierungskontext bereit.

- **MyRoutes:** Rendert die Routen der Anwendung.
- **ReactQueryDevtools:** Aktiviert die Entwicklungswerkzeuge für react-query.

Zusammenfassend konfiguriert dieser Code eine React-Anwendung mit austauschbaren Themes (hell/dunkel), Authentifizierungsverwaltung und Entwicklungswerkzeugen für die Datenverwaltung.

___
#### Login
Dieser Code stellt eine ziemlich Standard-Anmeldemaske mit einigen zusätzlichen Funktionen wie Formularvalidierung und Themenverwaltung dar. Die Hauptlogik konzentriert sich auf die Benutzerauthentifizierung und die Navigation.

```js

import styled from "styled-components";
import {
  Btnsave,
  v,
  useAuthStore,
  InputText,
  useUsersStore,
  Spinner,
  SpinnerLoader,
  RegistrierenAdmin,
  supabase,
  FooterLogin,
 
} from "../../index";
import {Device} from "../../styles/breakpoints"
import stars from "../../assets/starsVarias.svg";
import { useMutation } from "@tanstack/react-query";
import { useContext, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { useForm } from "react-hook-form";
import LogoImg from "../../assets/LogoImg.svg";
import logo from "../../assets/inventarlogo.png";
import { MdOutlineInfo } from "react-icons/md";
import { ThemeContext } from "../../App";
export function LoginTemplate() {
  const { setTheme, theme } = useContext(ThemeContext);
  setTheme("light")
  const { insertUser } = useUsersStore();
  const { signInWithEmail } = useAuthStore();
  const [state, setState] = useState(false);
  const [email, setemail] = useState("");
  const [pass, setPass] = useState("");
  const [stateStartseite, setStateStartseite] = useState(false);
  const navigate = useNavigate();
  const mutation = useMutation({
    mutationFn: async () => {
      const p = {
        email: "d-paz@gmail.com",
        pass: "The1080",
      };
      await insertUser(p);
    },
  });
  const {
    register,
    formState: { errors },
    handleSubmit,
    watch,
  } = useForm();
  async function start(data) {
    const response = await signInWithEmail({
      email: data.email,
      pass: data.pass,
    });
    if (response) {
      navigate("/");
    } else {
      setStateStartseite(!stateStartseite);
    }
  }

  return (
    <Container imgbackground={v.hintergrundbild}>
      <div className="contentLogo">
        <img src={logo}></img>
        <span>InventarPRO</span>
      </div>
      <div className="bannerseite">
        <img src={LogoImg}></img>
      </div>

      <div className="contentCard">
        <div className="card">
          {state && <RegistrierenAdmin setState={() => setState(!state)} />}

          <Titel>InventarPRO</Titel>
          {stateStartseite && (
            <TextStateStartseite>falsche Daten</TextStateStartseite>
          )}
          <span className="hilfe">
            {" "}
            Sie können ein neues Konto erstellen oder <br></br>eines bei Ihrem Arbeitgeber beantragen
            <MdOutlineInfo />
          </span>
          <p className="ausspruch">Kontrollieren Sie Ihr Inventar.</p>
          <form onSubmit={handleSubmit(start)}>
            <InputText icon={<v.iconemail />}>
              <input
                className="form__field"
                onChange={(e) => setemail(e.target.value)}
                type="text"
                placeholder="email"
                {...register("email", {
                  required: true,
                })}
              />
              <label className="form__label">email</label>
              {errors.email?.type === "required" && <p>Erforderliches Feld</p>}
            </InputText>
            <InputText icon={<v.iconpass />}>
              <input
                className="form__field"
                onChange={(e) => setPass(e.target.value)}
                type="password"
                placeholder="password"
                {...register("pass", {
                  required: true,
                })}
              />
              <label className="form__label">pass</label>
              {errors.pass?.type === "required" && <p>Erforderliches Feld</p>}
            </InputText>
            <ContainerBtn>
              <Btnsave Titel="start" bgcolor="#fc6b32" />
              <Btnsave
                funcion={() => setState(!state)}
                Titel="Benutzerkonto erstellen"
                bgcolor="#ffffff"
              />
            </ContainerBtn>
          </form>
        </div>
        <FooterLogin />
      </div>
    </Container>
  );

```
```css
}
const Container = styled.div`
  background-size: cover;
  height: 100vh;
  display: grid;
  grid-template-columns: 1fr;
  align-items: center;
  justify-content: center;
  text-align: center;
  background-color: #262626;
  @media ${Device.tablet} {
    grid-template-columns: 1fr 2fr;
  }
  .contentLogo {
    position: absolute;
    top: 15px;
    font-weight: 700;
    display: flex;
    left: 15px;
    align-items: center;
    color: #fff;

    img {
      width: 50px;
    }
  }
  .square {
    transition: cubic-bezier(0.4, 0, 0.2, 1) 0.6s;
    position: absolute;
    height: 100%;
    width: 100%;
    bottom: 0;
    transition: 0.6s;
  }

  .bannerseite {
    background-color: #fc6b32;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    img {
      width: 80%;
    }
  }
  .contentCard {
    grid-column: 2;
    background-color: #ffffff;
    background-image: url(${stars});
    background-size: cover;
    z-index: 100;
    position: relative;
    gap: 30px;
    display: flex;
    padding: 20px;
    box-shadow: 8px 5px 18px 3px rgba(0, 0, 0, 0.35);
    justify-content: center;
    width: auto;
    height: 100%;
    width: 100%;
    align-items: center;
    flex-direction: column;
    justify-content: space-between;
    .card {
      padding-top: 80px;
      width: 100%;
      @media ${Device.laptop} {
        width: 50%;
      }
    }
    .version {
      color: #727272;
      text-align: start;
    }
    .contentImg {
      width: 100%;
      display: flex;
      justify-content: center;

      img {
        width: 40%;

        animation: float 1.5s ease-in-out infinite alternate;
      }
    }
    .ausspruch {
      color: #fc6c32;
      font-size: 1.5rem;
      font-weight: 700;
      margin-bottom:30px;
    }
    .hilfe {
      position: absolute;
      top: 15px;
      right: 15px;
      color: #8d8d8d;
      font-size: 15px;
      font-weight: 500;
    }
    &:hover {
      .contentsvg {
        top: -100px;
        opacity: 1;
      }
      .square {
        transform: rotate(37deg) rotateX(5deg) rotateY(12deg) rotate(3deg)
          skew(2deg) skewY(1deg) scaleX(1.2) scaleY(1.2);
        color: red;
      }
    }
  }
  @keyframes float {
    0% {
      transform: translate(0, 0px);
    }
    50% {
      transform: translate(0, 15px);
    }
    100% {
      transform: translate(0, -0px);
    }
  }
`;
const Titel = styled.span`
  font-size: 3rem;
  font-weight: 700;
`;
const ContainerBtn = styled.div`
  margin-top: 15px;
  display: flex;
  justify-content: center;
`;
const textStateStartseite = styled.p`
  color: #fc7575;
`;

```

**React-Komponente namens LoginTemplate**
Die React-Komponente LoginTemplate zeigt eine Anmeldemaske für eine Webanwendung (namens InventarPRO) an.

**Funktionalität:**

- **Anmelden:** Ermöglicht Benutzern die Anmeldung mit ihrer E-Mail-Adresse und ihrem Passwort. Verwendet die Funktion `signInWithEmail` aus einem `useAuthStore` (ein State-Store für die Authentifizierung), um den Benutzer zu authentifizieren. Bei erfolgreicher Anmeldung wird der Benutzer zur Hauptseite (/) weitergeleitet. Bei Misserfolg wird eine Fehlermeldung angezeigt.
- **Konto erstellen:** Verfügt über eine Schaltfläche zum Erstellen eines neuen Kontos. Es scheint, dass eine Komponente `RegistrienAdmin` bedingt angezeigt wird.
- **Benutzerspeicherung:** Enthält eine Funktion insertUser aus einem useUsersStore.
- **Formularvalidierung:** Verwendet `react-hook-form`, um das Anmeldeformular zu verwalten und zu validieren. Erfordert, dass die Felder für E-Mail und Passwort ausgefüllt werden.
- **Anwendungsthema:** Verwendet einen `ThemeContext`, um das Anwendungsthema auf `"light"` (hell) zu setzen.

**Benutzeroberfläche:**

- **Design:** Verwendet `styled-components`, um die Vorlage zu gestalten. Das Design ist responsiv und passt sich an verschiedene Bildschirmgrößen an (mit `Breakpoints`).
- **Elemente:** Enthält ein Logo, ein Formular mit Feldern für E-Mail und Passwort, Schaltflächen zum Anmelden und Konto erstellen sowie eine Meldung "Daten inkorrekt", die bei fehlgeschlagener Anmeldung angezeigt wird.
- **Bilder:** Verwendet Hintergrundbilder, ein Warenkorb-Bild und ein Logo.
- **Animationen:** Verfügt über eine "Schwebe"-Animation für ein Bild.

**Abhängigkeiten:**

- **styled-components:** Zum Stylen der Komponenten.
- **@tanstack/react-query:** Zum Verwalten von Mutationen (wie insertUser).
- **react-router-dom:** Für die Navigation zwischen Seiten.
- **react-hook-form:** Für die Formularverwaltung und -validierung.

**Benutzerdefinierte Komponenten:**

Der Code verwendet mehrere benutzerdefinierte Komponenten:

- Btnsave
- InputText
- RegistrierenAdmin
- Spinner
- SpinnerLoader
- FooterLogin

___
#### AdminRegistrierung
Komponente bietet eine Oberfläche zur Registrierung neuer Administratorbenutzer mit Feldvalidierung.

```js

import { useEffect, useState } from "react";
import styled from "styled-components";
import { v } from "../../../styles/variables";
import {
  InputText,
  Spinner,
  useOperations,
  Btnsave,
  useUsersStore,
  useKategorienStore,useAuthStore,
} from "../../../index";
import { useForm } from "react-hook-form";
import { CirclePicker } from "react-color";
import Emojipicker from "emoji-picker-react";
import { MdAlternateEmail } from "react-icons/md";
import { RiLockPasswordLine } from "react-icons/ri";
import { useMutation } from "@tanstack/react-query";
import { useNavigate } from "react-router-dom";
export function RegistrierenAdmin({ state, setState }) {
  const { insertUserAdmin } = useUsersStore();
  const { signInWithEmail } = useAuthStore();
  const navigate = useNavigate();
  const {
    register,
    formState: { errors },
    handleSubmit,
  } = useForm();
  const mutation = useMutation({
    mutationFn: async (data) => {
      const p = {
        email: data.email,
        pass:data.pass,
        Typuser:"admin"
      }; 
      const dt =   await insertUserAdmin(p);
      if (dt) {
        navigate("/");
      } else {
        setStateStart(!stateStart);
      }
    },
  });
  return (
    <Container>
        <ContentClose >
          <span onClick={setState}>x</span>
        </ContentClose>
      <section className="subcontainer">

      
      <div className="headers">
        <section>
          <h1>User registrieren</h1>
        </section>

      
      </div>

      <form className="form" onSubmit={handleSubmit(mutation.mutateAsync)}>
        <section>
          <article>
            <InputText icon={<MdAlternateEmail />}>
              <input  className="form__field"
                style={{ textTransform: "lowercase" }}
                type="text"
                placeholder="email"
                {...register("email", {
                  required: true,
                  pattern: /^[^\s@]+@[^\s@]+\.[^\s@]+$/i,
                })}
              />
               <label className="form__label">email</label>
              {errors.email?.type === "pattern" && (
                <p>Das E -Mail -Format ist falsch</p>
              )}
              {errors.email?.type === "required" && <p>Erforderliches Feld</p>}
            </InputText>
          </article>
          <article>
            <InputText icon={<RiLockPasswordLine />}>
              <input  className="form__field"
                type="text"
                placeholder="pass"
                {...register("pass", {
                  required: true,
                })}
              />
 <label className="form__label">pass</label>
              {errors.pass?.type === "required" && <p>Erforderliches Feld</p>}
            </InputText>
          </article>
          <div className="btnspeichernContent">
            <Btnsave
              icon={<v.iconspeichern />}
              titel="speichern"
              bgcolor="#ff7556"  
            />
          </div>
        </section>
      </form>
      </section>
    </Container>
  );

```
```css
}
const Container = styled.div`
  position: absolute;
  height: 100%;
  width: 100%;
  top: 0;
  left: 0;
  border-radius: 20px;
  background: #fff;
  box-shadow: -10px 15px 30px rgba(10, 9, 9, 0.4);
  padding: 13px 36px 20px 36px;
  z-index: 100;
  display:flex;

  align-items:center;
.subcontainer{
  width: 100%;
}

  .headers {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;

    h1 {
      font-size: 20px;
      font-weight: 500;
    }
    span {
      font-size: 20px;
      cursor: pointer;
    }
   
  }
  .form {
    section {
      gap: 20px;
      display: flex;
      flex-direction: column;
      .colorContainer {
        .colorPickerContent {
          padding-top: 15px;
          min-height: 50px;
        }
      }
    }
  }
`;

const ContentClose =styled.div`
  position:absolute;
  top:0;
  right:0;
  font-size:33px;
  margin:30px;
  cursor: pointer;
`

```

**Funktionalität:**
- **Registrierungsformular:** Die Komponente verwendet react-hook-form zur Verwaltung des Formulars, welches Felder für E-Mail und Passwort beinhaltet.
- **Validierung:** Es wird validiert, ob die E-Mail ein gültiges Format hat und beide Felder ausgefüllt sind.
- **Benutzeranlage:** Beim Absenden des Formulars wird eine Mutation von @tanstack/react-query verwendet, um die Funktion insertUserAdmin aus dem useUsersStore aufzurufen.
- **Automatische Anmeldung:** Wenn die Benutzeranlage erfolgreich ist, wird der Benutzer zur Startseite ("/") weitergeleitet, um sich automatisch anzumelden.
- **Fehlerbehandlung:** Falls die Benutzeranlage fehlschlägt, wird der Status der Komponente (über setStateStart) aktualisiert, um eine Fehlermeldung anzuzeigen.
- **Style:** Die Komponente verwendet styled-components, um die Style des Formulars zu definieren, einschließlich des Hauptcontainers, der Überschriften, der Eingabefelder und des Speicherbuttons.

**Verwendete Bibliotheken:**
- **React:** Zum Erstellen der Benutzeroberfläche.
- **styled-components:** Zum Stylen der Komponente.
- **react-hook-form:** Zur Verwaltung des Formulars und der Validierung.
- **@tanstack/react-query:** Zum Durchführen der Mutation zur Benutzeranlage.
- **react-router-dom:** Zum Weiterleiten des Benutzers nach der Registrierung.
- **Weitere:** Es werden weitere Bibliotheken für spezifische Elemente wie Icons (react-icons), einen Farbwähler (react-color) und einen Emoji-Wähler (emoji-picker-react) verwendet.

___
#### Personal Registrierung
Diese Komponente bietet eine Oberfläche zur Erfassung oder Bearbeitung von persönlichen Daten, einschließlich der Verwaltung von Berechtigungen. Sie verwendet verschiedene Werkzeuge und Techniken zur Zustandsverwaltung, Benutzerinteraktion, Datenspeicherung und Darstellung der Informationen.

```js

import { useEffect, useState } from "react";
import styled from "styled-components";
import { v } from "../../../styles/variables";
import {
  InputText,
  Spinner,
  useOperations,
  Btnsave,
  useUsersStore,
  useKategorienStore,
  Selector,
  useProdukteStore,
  useMarkeStore,
  ListGeneric,
  Btnfilter,
  RegistrierenMarke,
  RegistrierenKategorien,
  ListModul,
  TypuserData,
  TypDocData,
  useGlobalStore,
  useBerechtigungenStore,
} from "../../../index";
import { useForm } from "react-hook-form";
import { CirclePicker } from "react-color";
import Emojipicker from "emoji-picker-react";
import { useFirmaStore } from "../../../store/FirmaStore";
import { Device } from "../../../styles/breakpoints";
import { useQuery } from "@tanstack/react-query";
import { queryClient } from "../../../main";
import { QueryCache } from "@tanstack/react-query";

export function RegistrierenPersonal({
  onClose,
  dataSelect,
  action,
  setdataSelect,
}) {
  const { insertUser, edituser } = useUsersStore();
  const { dataFirma } = useFirmaStore();
  const [stateMarke, setStateMarke] = useState(false);
  const [stateKategorie, setStateKategorie] = useState(false);
  const [openRegisterMarke, SetopenRegisterMarke] = useState(false);
  const [openRegisterKategorie, SetopenRegisterKategorie] = useState(false);
  const [subaction, setaction] = useState("");
  const { datamodules } = useGlobalStore();
  const [checkboxs, setCheckboxs] = useState([]);
  const [Typuser, setTypuser] = useState({
    icon: "",
    beschreibung: "mitarbeiter",
  });
  const [TypDoc, setTypDoc] = useState({ icon: "", beschreibung: "idNr" });
  const { dataBerechtigungenEdit, zeigenBerechtigungenEdit } = useBerechtigungenStore();

  const { isLoading } = useQuery({
    queryKey: ["zeigenBerechtigungenedit", { id_user: dataSelect.id }],
    queryFn: () => zeigenBerechtigungenEdit({ id_user: dataSelect.id }),
    enabled: dataSelect.id != null,
  });

  const {
    register,
    formState: { errors, isDirty },
    handleSubmit,
    watch,
  } = useForm();
  async function insert(data) {
    if (action === "Edit") {
      const p = {
        id: dataSelect.id,
        names: data.names,
        nro_doc: data.nrodoc,
        telefon: data.telefon,
        adresse: data.adresse,
        estado: "activo",
        Typuser: Typuser.beschreibung,
        TypDoc: TypDoc.beschreibung,
       
      };
      await edituser(p, checkboxs, dataFirma.id);
      // refetch()
      onClose();
    } else {
      const p = {
        names: data.names,
        email: data.email,
        nrodoc: data.nrodoc,
        telefon: data.telefon,
        adresse: data.adresse,
        estado: "activo",
        Typuser: Typuser.beschreibung,
        TypDoc: TypDoc.beschreibung,
        id_Firma: dataFirma.id,
      };
      const parametrosAuth = {
        email: data.email,
        pass: data.pass,
      };
      await insertUser(parametrosAuth, p, checkboxs);

      onClose();
    }
  }
  useEffect(() => {
    if (action === "Edit") {
      setTypDoc({icon: "", beschreibung: dataSelect.TypDoc})
      setTypuser({
        icon: "",
        beschreibung: dataSelect.Typuser,
      })
      
    }
  }, []);
  if (isLoading) {
    return <span>charging...</span>;
  }
  return (
    <Container>
      <div className="sub-container">
        <div className="headers">
          <section>
            <h1>
              {action == "Edit" ? "Edit personal" : "Registrieren personal"}
            </h1>
          </section>

          <section>
            <span onClick={onClose}>x</span>
          </section>
        </div>
        <form className="form" onSubmit={handleSubmit(insert)}>
          <section className="section1">
            <article>
              <InputText icon={<v.iconname />}>
                <input 
               
                  disabled={action === "Edit" ? true : false}
                  className={action==="Edit"?"form__field disabled":"form__field"}
                  defaultValue={dataSelect.email}
                  type="text"
                  placeholder=""
                  {...register("email", {
                    required: action==="Edit"?false:true,
                  })}
                />
                <label className="form__label">email</label>

                {errors.email?.type === "required" && <p>Erforderliches Feld</p>}
              </InputText>
            </article>
            {action != "Edit" ? (
              <article>
                <InputText icon={<v.iconpass />}>
                  <input
                    className="form__field"
                    defaultValue={dataSelect.pass}
                    type="text"
                    placeholder=""
                    {...register("pass", {
                      required: true,
                    })}
                  />
                  <label className="form__label">pass</label>

                  {errors.pass?.type === "required" && <p>Erforderliches Feld</p>}
                </InputText>
              </article>
            ) : null}

            <article>
              <InputText icon={<v.iconname />}>
                <input
                  className="form__field"
                  defaultValue={dataSelect.names}
                  type="text"
                  placeholder=""
                  {...register("names", {
                    required: true,
                  })}
                />
                <label className="form__label">names</label>

                {errors.names?.type === "required" && <p>Erforderliches Feld</p>}
              </InputText>
            </article>
            <ContainerSelector>
              <label>Typ doc: </label>
              <Selector
                state={stateMarke}
                color="#fc6027"
                text1="🎴"
                text2={TypDoc.beschreibung}
                funcion={() => setStateMarke(!stateMarke)}
              />

              {stateMarke && (
                <ListGeneric
                  bottom="-260px"
                  scroll="scroll"
                  setState={() => setStateMarke(!stateMarke)}
                  data={TypDocData}
                  funcion={(p) => setTypDoc(p)}
                />
              )}

              {subaction}
            </ContainerSelector>

            <article>
              <InputText icon={<v.iconstock />}>
                <input
                  className="form__field"
                  defaultValue={dataSelect.nro_doc}
                  type="number"
                  placeholder=""
                  {...register("nrodoc", {
                    required: true,
                  })}
                />
                <label className="form__label">Nro. doc</label>

                {errors.nrodoc?.type === "required" && <p>Erforderliches Feld</p>}
              </InputText>
            </article>
            <article>
              <InputText icon={<v.iconstockminimum />}>
                <input
                  step="0.01"
                  className="form__field"
                  defaultValue={dataSelect.telefon}
                  type="text"
                  placeholder=""
                  {...register("telefon", {
                    required: true,
                  })}
                />
                <label className="form__label">telefon</label>

                {errors.telefon?.type === "required" && <p>Erforderliches Feld</p>}
              </InputText>
            </article>
            <article>
              <InputText icon={<v.iconbarcode />}>
                <input
                  className="form__field"
                  defaultValue={dataSelect.adresse}
                  type="text"
                  placeholder=""
                  {...register("adresse", {
                    required: true,
                  })}
                />
                <label className="form__label">adresse</label>

                {errors.adresse?.type === "required" && (
                  <p>Erforderliches Feld</p>
                )}
              </InputText>
            </article>
          </section>
          <section className="section2">
            <ContainerSelector>
              <label>Typ: </label>
              <Selector
                state={stateKategorie}
                color="#fc6027"
                text1="👷‍♂️"
                text2={Typuser.beschreibung}
                funcion={() => setStateKategorie(!stateKategorie)}
              />

              {stateKategorie && (
                <ListGeneric
                  bottom="-150px"
                  scroll="scroll"
                  setState={() => setStateKategorie(!stateKategorie)}
                  data={TypuserData}
                  funcion={(p) => setTypuser(p)}
                />
              )}
            </ContainerSelector>
            Berechtigungen:🔑
            <ListModul
              action={action}
              setCheckboxs={setCheckboxs}
              checkboxs={checkboxs}
              Typuser={Typuser}
            />
            {/* {checkboxs.map((item, index) => {
              if (item.check) {
                return <span>{item.name}</span>;
              } else {
                return null;
              }
            })} */}
          </section>
          <div className="btnspeichernContent">
            <Btnsave
              icon={<v.iconspeichern />}
              titulo="Speichern"
              bgcolor="#EF552B"
            />
          </div>
        </form>
      </div>
    </Container>
  );

```

```css
}
const Container = styled.div`
  transition: 0.5s;
  top: 0;
  left: 0;
  position: fixed;
  background-color: rgba(10, 9, 9, 0.5);
  display: flex;
  width: 100%;
  min-height: 100vh;
  align-items: center;
  justify-content: center;
  z-index: 1000;

  .sub-container {
    overflow-y: auto;
    overflow-x: hidden;
    height: 90vh;

    &::-webkit-scrollbar {
      width: 6px;
      border-radius: 10px;
    }
    &::-webkit-scrollbar-thumb {
      background-color: #484848;
      border-radius: 10px;
    }
    width: 100%;
    max-width: 90%;
    border-radius: 20px;
    background: ${({ theme }) => theme.bgtotal};
    box-shadow: -10px 15px 30px rgba(10, 9, 9, 0.4);
    padding: 13px 36px 20px 36px;
    z-index: 100;

    .headers {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;

      h1 {
        font-size: 20px;
        font-weight: 500;
      }
      span {
        font-size: 20px;
        cursor: pointer;
      }
    }
    .form {
      display: grid;
      grid-template-columns: 1fr;
      gap: 15px;
      @media ${Device.tablet} {
        grid-template-columns: repeat(2, 1fr);
      }
      section {
        gap: 20px;
        display: flex;
        flex-direction: column;
      }
      .btnspeichernContent {
        display: flex;
        justify-content: end;
        grid-column: 1;
        @media ${Device.tablet} {
          grid-column: 2;
        }
      }
    }
  }
`;

const ContainerSelector = styled.div`
  display: flex;
  gap: 10px;
  align-items: center;
  position: relative;
`;

```

**Hauptfunktionalität:**

- **Formular:** Die Komponente verwendet react-hook-form zur Verwaltung eines Formulars mit Feldern wie E-Mail, Passwort, Namen, Dokumententyp, Dokumentennummer, Telefon und Adresse.
- **Status:** Verwendet useState zur Verwaltung des Status verschiedener Elemente der Benutzeroberfläche, wie z. B. der Sichtbarkeit von Auswahlfeldern, des Benutzertyps, des Dokumententyps und der ausgewählten Berechtigungen.
- **Datenspeicherung:** Interagiert mit verschiedenen Stores (Datenspeichern) wie useUsersStore, useFirmaStore, useGlobalStore und useBerechtigungenStore, um auf Daten zuzugreifen und Aktionen wie das Einfügen oder Bearbeiten von Benutzern durchzuführen.
- **Datenabfragen:** Verwendet @tanstack/react-query, um asynchrone Abfragen durchzuführen, z. B. um die Berechtigungen eines Benutzers abzurufen.
- **Style:** Verwendet styled-components, um die Style der Komponente zu definieren.
- **Benutzerdefinierte Komponenten:** Verwendet benutzerdefinierte Komponenten wie InputText, Selector, ListGeneric, Btnsave, ListModuls usw., um die Benutzeroberfläche zu erstellen.
- **Externe Bibliotheken:** Verwendet externe Bibliotheken wie react-color (für eine Farbauswahl), emoji-picker-react (für eine Emoji-Auswahl) und react-hook-form (für die Formularverwaltung).

**Workflow:**

- **Initialisierung:** Beim Laden der Komponente werden die Daten initialisiert, wenn ein bestehender Benutzer bearbeitet wird.
- **Formular:** Der Benutzer interagiert mit dem Formular, um Daten einzugeben oder zu ändern.
- **Auswahlfelder:** Der Benutzer kann den Dokumententyp und den Benutzertyp auswählen.
- **Berechtigungen:** Der Benutzer kann dem Benutzer über die Komponente ListModuls Berechtigungen zuweisen.
- **Speichern:** Beim Klicken auf die Schaltfläche "Speichern" wird das Formular validiert und die Funktion einfügen aufgerufen, um die Daten zu speichern.
- **Einfügen/Bearbeiten:** Die Funktion einfügen ermittelt, ob ein neuer Benutzer eingefügt oder ein bestehender bearbeitet wird, und führt die entsprechende Aktion mithilfe der Funktionen des useUsersStore aus.

___
#### UserAuth
Dieser Code erstellt einen Mechanismus zur Verwaltung des Authentifizierungsstatus eines Benutzers in einer React-Anwendung, die Supabase verwendet. Die Komponente `AuthContextProvider` ist dafür zuständig, Änderungen in der Authentifizierung zu überwachen und den Benutzerstatus zu aktualisieren, während die Funktion `UserAuth` es den Komponenten ermöglicht, auf die Informationen des authentifizierten Benutzers zuzugreifen.

```js

import { createContext, useContext, useEffect, useState } from "react";
import { supabase } from "../index";
const AuthContext = createContext();
export const AuthContextProvider = ({ children }) => {
  const [user, setUser] = useState([]);
  useEffect(() => {
    const { data: authListener } = supabase.auth.onAuthStateChange(
      async (event, session) => {
        if (session?.user == null) {
          setUser(null);
        } else {
          setUser(session?.user);
          console.log("event", event);
          console.log("session USER", session?.user);
        }
      }
    );
    return () => {
      authListener.subscription;
    };
  }, []);

  return (
    <AuthContext.Provider value={{ user }}>{children}</AuthContext.Provider>
  );
};
export const UserAuth = () => {
  return useContext(AuthContext);
};
// Dieser Code definiert einen Kontext-Provider in React,
// um die Benutzerauthentifizierung mit Supabase zu verwalten.

```

**Importe:** Importiere die benötigten Funktionen von React `createContext`, `useContext`, `useEffect`, `useState` und die Supabase-Instanz `(supabase)` aus einer externen Datei.

**Kontext:** Erstelle einen Authentifizierungskontext `AuthContext` mit `createContext`. Dieser Kontext speichert die Informationen des authentifizierten Benutzers.

**Kontextanbieter:** Definiere eine Komponente `AuthContextProvider`, die Folgendes tut:

- Verwende den Hook `useState`, um die Benutzerinformationen (user) in einem lokalen Zustand zu speichern, der initial leer ist (`[]`).
- Verwende den Hook `useEffect`, um einen Supabase-Authentifizierungslistener `supabase.auth.onAuthStateChange` einzurichten. Dieser Listener wird ausgeführt, wenn sich der Authentifizierungsstatus ändert (Anmeldung, Abmeldung usw.).

**Innerhalb des Listeners:**
    - Wenn eine aktive Sitzung vorhanden ist `session?.user`, aktualisiere den Status `user` mit den Benutzerinformationen und protokolliere die Informationen in der Konsole.
    - Wenn keine aktive Sitzung vorhanden ist `session?.user == null`, setze den Status `user` auf `null`.
- Gib die Komponente `AuthContext.Provider` zurück, die den Wert des Kontexts `(user)` an alle untergeordneten Komponenten weitergibt.

**Kontextzugriffsfunktion:** Definiere eine Funktion `UserAuth`, die den Hook `useContext` verwendet, um von jeder untergeordneten Komponente aus auf den Wert des Kontexts `(user)` zuzugreifen.

___
#### PDF-Bericht

```js
import { NavLink, Outlet } from "react-router-dom";
import styled from "styled-components";
export function ReportTemplate() {
  return (
    <Container>
      <PageContainer>
        <Content>
          <Outlet/>
        </Content>
        <Sidebar>
          <SidebarSection>
            <SidebarTitle>Aktueller Lagerbestand</SidebarTitle>
            <SidebarItem to="aktueller-lagerbestand-nach-produkt">
              Nach Produkt
            </SidebarItem>
            <SidebarItem to="aktueller-bestand-alles">Alle</SidebarItem>
            <SidebarItem to="lagerbestand-niedrig-minimum">unter dem Minimum</SidebarItem>
          </SidebarSection>
          <SidebarSection>
          <SidebarTitle>Ein- und Ausgänge</SidebarTitle>
          <SidebarItem to="kardex-eingaenge-ausgaenge">Nach Produkt</SidebarItem>
          </SidebarSection>
          <SidebarSection>
          <SidebarTitle to="ss">Geschätzt</SidebarTitle>
          <SidebarItem to="bestandsbewertet">Alle</SidebarItem>
          </SidebarSection>
        </Sidebar>
      </PageContainer>
    </Container>
  );
}
```
```css
const Content = styled.div`
  padding: 20px;
  border-radius: 8px;
  margin: 20px;
  flex: 1;
`;
const PageContainer = styled.div`
  display: flex;
  flex-direction: column;
  max-width: 1200px;
  justify-content: center;
  width: 100%;
  @media (min-width: 768px) {
    flex-direction: row;
  }
`;
const Container = styled.div`
  min-height: 100vh;
  padding: 15px;
  width: 100%;
  color: ${({ theme }) => theme.text};
`;
const Sidebar = styled.div`
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  @media (min-width: 768px) {
    width: 250px;
    order: 2;
  }
`;
const SidebarSection = styled.div`
  margin-bottom: 20px;
  border-radius: 10px;
  border: 2px solid ${({ theme }) => theme.color2};
  padding: 12px;
`;
const SidebarTitle = styled.h3`
  margin-bottom: 20px;
  font-size: 1.2em;
`;
const SidebarItem = styled(NavLink)`
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px;
  border-radius: 12px;
  cursor: pointer;
  margin: 5px 0;
  padding: 0 5%;
  text-decoration: none;
  color: ${(props) => props.theme.text};
  height: 60px;
  &:hover {
    color: ${(props) => props.theme.colorSubtitle};
  }
  &.active {
    background: ${(props) => props.theme.bg6};
    border: 2px solid ${(props) => props.theme.bg5};
    color: ${(props) => props.theme.color1};
    font-weight: 600;
  }
`;

```

**ReportTemplate:** Eine Vorlage für den Berichtsbereich einer Anwendung

**Struktur:**
- **Seitenleiste:** Enthält eine Liste von Links zu verschiedenen Berichtsarten, gruppiert in Abschnitten (aktueller Lagerbestand, Ein- und Ausgänge, etc.).
- **Inhalt:** Ein Bereich, in dem der ausgewählte Bericht angezeigt wird.

**Funktionalität:**
- Verwendet react-router-dom für die Navigation zwischen den verschiedenen Berichten.
- Outlet rendert die Komponente des spezifischen Berichts basierend auf der aktuellen Route.
- Verwendet styled-components zur Gestaltung der Vorlage, einschließlich der Seitenleiste, des Inhalts und der Links.
- Das Design ist responsiv und passt sich an verschiedene Bildschirmgrößen an.