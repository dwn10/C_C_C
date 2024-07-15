# Taschenrechner

- Einfacher Taschenrechner mit grafischer Oberfläche

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
  - Zusätzlich wird eine `Historie` der Berechnung in einer Liste `(LastLineDataList)` gespeichert.
