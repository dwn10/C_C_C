# Taschenrechner mit Conzept 16

- Taschenrechner mit grafischer Benutzeroberfläche `(GUI)`.
- Er reagiert auf Klick-Ereignisse von Schaltflächen `(Zahlen, Operatoren, etc.)` und führt entsprechende Aktionen aus.
- Zusätzlich wird eine `Historie` der Berechnung in einer Liste `(LastLineDataList)` gespeichert.

## Funktionen:

- `EvtChanged(aEvt):` Diese Funktion reagiert auf Ereignisse (z.B. Tastendrücke), ermittelt das auslösende Objekt und seinen Inhalt.
- `EvtClickedButton(aEvt):` Die Kernfunktion, die auf Klicks auf Buttons reagiert. Abhängig vom Button werden Zahlen eingegeben, mathematische Operationen durchgeführt oder das Ergebnis berechnet und angezeigt.

## Funktionsweise:

- `Benutzeroberfläche (UI):` Das Programm erstellt eine einfache grafische Oberfläche mit einem Eingabefeld `(OutputLabel)` zur Anzeige der Zahlen und des Ergebnisses, Buttons für Zahlen `(0-9)` und Rechenoperationen `(+, -, *, /)`, sowie spezielle Buttons `(Komma, Vorzeichenwechsel, Löschen)`.

- `Zahleneingabe:` Klicks auf die Zahlenbuttons hängen die jeweilige Ziffer an den aktuellen Inhalt des Eingabefeldes an. Das Komma wird ebenfalls hinzugefügt.

- `Rechenoperationen:`

  - Beim Klick auf einen Operator `(+, -, \*, /)` wird die bisherige Eingabe in einer Hilfsvariable `(MerkerLabelLast)` gespeichert.
  - Das Eingabefeld wird geleert.
  - Der Operator wird in einer weiteren Hilfsvariable `(MerkerLabelVZ)` vermerkt.

- `Ergebnisberechnung:`

  - Beim Klick auf `"="` wird der aktuelle Wert im Eingabefeld als zweite Zahl geholt.
  - Basierend auf dem gespeicherten Operator `(MerkerLabelVZ)` wird die entsprechende Berechnung durchgeführt `(Addition, Subtraktion, Multiplikation oder Division)`.
  - Das Ergebnis wird als String formatiert und im Eingabefeld angezeigt.

  ***

  ## EXTRA

  ***

## Variablen:

- `tObj:` ID der gedrückten Taste.
- `tCaption:` Bezeichnung der gedrückten Taste.
- `tObjName:` Name der gedrückten Taste.
- `tWert1`, `tWert2:` Numerische Werte für Berechnungen `(Typ Float)`.
- `tMerkerLabelLast:` Speichert die letzte numerische Eingabe.
- `tLabelVZ:` Speichert den gewählten mathematischen Operator `(+, -, \*, /)`.
- `tLastInput:` Speichert die letzte numerische Eingabe vor dem Operator.
- `tLineCount:` Zähler für Zeilen in einer Liste für den Berechnungsverlauf.
- `tErg:` Ergebnis der Operation (nicht im gezeigten Code verwendet).
- `tSuccess:` Gibt den Erfolg einer Operation im Zusammenhang mit der Verlaufsliste.

## Logik:

- `Bildschirm löschen:` Wenn der letzte Operator `'='` war, löschen Sie den Bildschirm und den Akkumulator.
- `Numerische Tasten verarbeiten:` Verkettet die gedrückte Ziffer mit dem Inhalt des Displays.
- `Operatortasten verarbeiten:` Speichert den Operator, löscht das Display und speichert den vorherigen Wert in einem Akkumulator.
- `Gleichheitszeichen (=) verarbeiten:` Führt die Berechnung gemäß dem gespeicherten Operator durch, zeigt das Ergebnis und einer Verlaufsliste an.
- `Alles löschen-Taste verarbeiten:` Löscht die Verlaufsliste.
