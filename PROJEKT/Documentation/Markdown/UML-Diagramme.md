
# Diagramme
___
**Entity-Relationship-Model**

# Inventar DB

### Table structure

**firma**

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **name** | TEXT | not null  |  | |
| **währungssymbol** | TEXT | not null  |  | |
| **iduseradmin** | BIGINT | not null  | firma_iduseradmin_fk | |


**firmazuordnen**

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **id_firma** | BIGINT | not null  | firmazuordnen_id_firma_fk | |
| **id_user** | BIGINT | not null  | asignarempresa_id_user_fk | |


**kategorien**

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **beschreibung** | TEXT | not null  |  | |
| **color** | TEXT | not null  |  | |
| **id_firma** | BIGINT | not null  | kategorien_id_firma_fk | |


**kardex**

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **datum** | DATE | not null  |  | |
| **typ** | TEXT | not null  |  | |
| **id_user** | BIGINT | not null  | kardex_id_user_fk | |
| **id_producto** | BIGINT | not null  | kardex_id_produkt_fk | |
| **anzahl** | BLOB | not null  |  | |
| **id_firma** | BIGINT | not null  | kardex_id_firma_fk | |
| **details** | TEXT | not null  |  | |
| **status** | BIGINT | not null , default: 1 |  | |


**marke**

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **beschreibung** | TEXT | not null  |  | |
| **id_firma** | BIGINT | not null  | marke_id_firma_fk | |


**modul**

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **name** | TEXT | not null  |  | |
| **check** | BOOLEAN | not null , default: false |  | |


**berechtigungen**

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **id_user** | BIGINT | not null  | berechtigungen_id_user_fk | |
| **id_modul** | BIGINT | not null  | berechtigungen_id_modul_fk | |


**produkte**

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **beschreibung** | TEXT | not null  |  | |
| **id_marke** | BIGINT | not null  | produkte_id_marke_fk | |
| **aktueller _lagerbestand** | NUMERIC | not null  |  | |
| **mindestbestand** | NUMERIC | not null  |  | |
| **barcode** | TEXT | not null  |  | |
| **interner_code** | TEXT | not null  |  | |
| **verkaufspreis** | NUMERIC | not null  |  | |
| **kaufpreis** | NUMERIC | not null  |  | |
| **id_kategorie** | BIGINT | not null  | produkte_id_kategorie_fk | |
| **id_firma** | BIGINT | not null  | produkte_id_firma_fk | |


**users**

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **namen** | TEXT | not null , default: generic |  | |
| **nr_doc** | TEXT | not null , default: - |  | |
| **telefon** | TEXT | not null , default: - |  | |
| **adresse** | TEXT | not null , default: - |  | |
| **datum_reg** | DATE | not null  |  | |
| **status** | TEXT | not null , default: activ |  | |
| **typuser** | TEXT | not null  |  | |
| **idauth** | TEXT | not null  |  | |
| **typdoc** | TEXT | not null , default: - |  | |
| **email** | TEXT | not null , default: - |  | |

# PlantUML Diagramme
### Ablaufdiagramm
// !theme superhero-outline // !theme crt-green
```plantuml

@startuml

!theme crt-green
!include <C4/C4_Context>
title Ablaufdiagramm - Inventarsystem D.Paz

start

:Benutzername und Passwort eingeben;
:Benutzer validieren;

if (Ist der Benutzer gültig?) then (ja)
  :Hauptmenü anzeigen;
  :Option auswählen;
  switch (Option)
    case (Produkt hinzufügen)
      :Produktdaten eingeben;
      :Produkt in der Datenbank speichern;
    case (Produkt löschen)
      :Zu löschendes Produkt auswählen;
      :Produkt aus der Datenbank löschen;
    case (Produkt aktualisieren)
      :Zu aktualisierendes Produkt auswählen;
      :Neue Produktdaten eingeben;
      :Produkt in der Datenbank aktualisieren;
    case (Inventar anzeigen)
      :Produktliste anzeigen;
    case (Beenden)
      :Sitzung beenden;
  endswitch
  :Zurück zum Hauptmenü;
else (nein)
  :Fehlermeldung anzeigen;
  :Zurück zur Anmeldung;
endif

stop

@enduml

```

### Usecase Diagramm
```plantuml

@startuml

!theme crt-green
!include <C4/C4_Context>
title Usecase Diagramm

left to right direction

Actor "Administrator" as admin
Actor "Benutzer" as user

Rectangle Inventar_System {
  admin -- (Anmelden)
  (Anmelden) <. (Login validieren) : include
  (Anmelden) <.. (Passwort wiederherstellen) : extends
  (Login validieren) <. (DB abfragen) : include
  (Passwort wiederherstellen) <. (DB abfragen) : include

  admin -- (Benutzer verwalten)
  admin -- (Produkte verwalten)
  admin -- (Berichte generieren)

  user -- (Inventar abfragen)
  (Inventar abfragen) <. (DB abfragen) : include
  user -- (Produktanfrage stellen)
  (Produktanfrage stellen) <. (DB abfragen) : include
}

@enduml

```

### Gantt Diagramm
```plantuml

@startgantt

!theme superhero
!include <C4/C4_Context>
title Gantt Diagramm

[Analyse und Design] requires 12 days
then [Entwurf] requires 12 days
then [Implementierung inkl. Tests] requires 41 days
then [Abnahme und Einführung] requires 5 days
then [Dokumentation] requires 10 days
@endgantt

```

### Projekt
```plantuml

@startsalt

!theme superhero
!include <C4/C4_Context>
title Projekt
{
{T

+ << Technologie >>       | << Beschreibung >>

+ Frontend                | <<>> 
++ React
+++ Zustand               | Zustandsverwaltung   
+++ TanStack              |  Devtool   
+++ ReactChart            | Diagrammerstellung
+++ Styled Components     | CSS-Style mit JavaScript-Syntax     
  
+ Backend                 | <<>>   
++ Supabase     
+++ Konsole SQL       
+++ Triggers Functions    
+++ UserAuth   
+++ Tabellendiagramm  
}
}
@endsalt

```


