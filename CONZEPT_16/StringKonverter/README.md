# StringCnv mit Conzept16:

<a href="#"><img src="#" style="height: 80%; width:80%;"/></a>

## Allgemeines

- Der vorgestellte Code definiert eine grafische Benutzeroberfläche, die verschiedene Textoperationen ermöglicht. Dazu gehören Konvertierungen zwischen Kodierungen `(OEM, ANSI, HTML, URI, UTF-8, Base64)`, Zeichenkettenmanipulation `(Groß-/Kleinschreibung, Umlaute, Buchstaben, Klang, Namensumordnung)` und andere Funktionen im Zusammenhang mit der Textverarbeitung.

## Subroutine EvtClicked

- `Funktion:` Bearbeitet das Ereignis des Klickens auf eine Schaltfläche in der Benutzeroberfläche.

## Variablen:

- `tobj:` ID des gedrückten Objekts (Schaltfläche).
- `tCaption:` Beschriftung der gedrückten Taste.
- `tObjName:` Name der gedrückten Taste.

## Konversionslogik

- Der Code enthält mehrere Fälle innerhalb eines SWITCH, um verschiedene Arten von Textkonvertierungen zu behandeln. Jeder Fall entspricht einer Taste in der Benutzeroberfläche und führt eine bestimmte Konvertierung mit der Funktion StrCnv mit den entsprechenden Parametern durch.

## Grundstruktur der Fälle:

- Prüft, ob das Eingabefeld Text enthält.
- Wenn das Feld nicht leer ist, wird die Konvertierung mit der Funktion StrCnv und dem entsprechenden Konvertierungstyp durchgeführt.
- Das Ergebnis der Konvertierung wird dem Ausgabefeld zugewiesen.
- Das Eingabefeld wird gelöscht.

## Beispielfälle

- CASE `'StrToOEMButton':` Konvertiert den Text aus dem Feld `FieldAlpha1` in das `OEM-Format` und weist ihn dem Feld `ZielFieldToOEM` zu.
- CASE `'StrUpperButton':` Konvertiert den Text aus dem Feld `FieldAlpha2` in `Großbuchstaben` und weist ihn dem Feld `ZielFieldToUpper` zu.
- CASE `'StrNameReorderButton':` Ordnet den Namen im Feld `FieldAlpha3` neu und weist ihn dem Feld `ZielFieldNameReorder` zu.
