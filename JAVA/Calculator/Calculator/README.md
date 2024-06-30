# Taschenrechner in Java mit Swing

Der Code erstellt einen einfachen Taschenrechner als grafische Anwendung (GUI) in Java mithilfe der Swing-Bibliothek. Hier die Hauptfunktionen und Komponenten:

<a href=".\Calculator\calculator.gif"><img src=".\Calculator\calculator.gif" style="height: 80%; width:80%;"/></a>

## Hauptkomponenten:

- 'JFrame (Taschenrechner):' Das Hauptfenster der Anwendung.
- 'JPanel (contentPane):' Ein Panel zur Organisation der Elemente im Fenster.
- 'JTextField (txtPantalla):' Ein Textfeld zur Anzeige von Zahlen und Ergebnissen.
- 'JButtons:' Zahlentasten '(0-9)', Operationstasten '(+, -, x, /)', eine Kommataste '(.)', eine Löschtaste '(C)' und eine Gleichheitstaste '(=)'.

## Funktionsweise:

- 'Oberfläche:' Die Oberfläche des Taschenrechners wird mit dem Textfeld und den verschiedenen Tasten aufgebaut.
- 'Eingabe:' Wenn Zahlentasten gedrückt werden, werden die entsprechenden Zahlen im Textfeld angezeigt.
- 'Operationen:' Operationstasten '(+, -, \*, /)' speichern die aktuelle Zahl und die gewählte Operation.
- 'Berechnung:' Die Gleichheitstaste '(=)' löst die Berechnung aus. Das Programm verwendet die gespeicherten Zahlen und die Operation, um das Ergebnis zu ermitteln. Das Ergebnis wird im Textfeld angezeigt.
- 'Löschen:' Die Löschtaste '(C)' setzt das Textfeld zurück.

## Variablen:

'numero1', 'numero2': Speichern die eingegebenen Zahlen.
'resultado:' Speichert das Ergebnis einer Berechnung.
'operacion:' Speichert die gewählte Rechenoperation '(+, -, \*, /)'.

## Ereignisbehandlung (ActionListener):

Jede Taste hat einen ActionListener, der auf Klicks reagiert. Die ActionListener für die Zahlentasten fügen die Zahl dem Textfeld hinzu. Die ActionListener für die Operationstasten speichern die aktuelle Zahl und die Operation. Der ActionListener der Gleichheitstaste führt die Berechnung durch und zeigt das Ergebnis an.

## Hauptmethode (main):

Die 'main-Methode' startet die Anwendung, indem sie eine Instanz des Taschenrechners erstellt und sichtbar macht.
