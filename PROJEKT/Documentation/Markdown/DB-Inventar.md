# Inventar DB

## Table structure

### firma

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **name** | TEXT | not null  |  | |
| **währungssymbol** | TEXT | not null  |  | |
| **iduseradmin** | BIGINT | not null  | firma_iduseradmin_fk | |


### firmazuordnen

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **id_firma** | BIGINT | not null  | firmazuordnen_id_firma_fk | |
| **id_user** | BIGINT | not null  | asignarempresa_id_usuario_fk | |


### kategorien

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **beschreibung** | TEXT | not null  |  | |
| **color** | TEXT | not null  |  | |
| **id_firma** | BIGINT | not null  | kategorien_id_firma_fk | |


### kardex

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


### marke

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **beschreibung** | TEXT | not null  |  | |
| **id_firma** | BIGINT | not null  | marke_id_firma_fk | |


### modul

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **name** | TEXT | not null  |  | |
| **check** | BOOLEAN | not null , default: false |  | |


### berechtigungen

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **id** | BIGINT | 🔑 PK, not null , autoincrement |  | |
| **id_user** | BIGINT | not null  | berechtigungen_id_user_fk | |
| **id_modul** | BIGINT | not null  | berechtigungen_id_modul_fk | |


### produkte

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


### users

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




