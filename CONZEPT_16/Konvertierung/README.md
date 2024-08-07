# Konvertierung

<a href="https://github.com/dwn10/C_C_C/blob/main/CONZEPT_16/Konvertierung/cnv.gif"><img src="https://github.com/dwn10/C_C_C/blob/main/CONZEPT_16/Konvertierung/cnv.gif" style="height: 80%; width:80%;"/></a>

## Zusammenfassung:

Das Programm stellt ein einfaches Tool zur Verfügung, um Werte zwischen verschiedenen Datentypen zu konvertieren.

- An den Festern kann mann zu verschiedenen Datentypen wechseln...

z.B:

- `Alpha` zu `Alpha`
- `Int` zu `Alpha`
- `BigInt` zu `Alpha`
- `Float` zu `Alpha`
- `Decimal` zu `Alpha`
- `Time` zu `Alpha`
- `Date` zu `Alpha`

- Dieser `Conzept-16-Code` demonstriert die Konvertierung zwischen verschiedenen Datentypen.

## Funktionsweise:

## EvtClickedButton:

- Diese Funktion wird ausgelöst, wenn ein Button geklickt wird.
- Sie identifiziert den Button anhand seines Namens (z.B. "ConvertAlpha2AlphaButton").

## SWITCH-Anweisung:

## Konvertierung zwischen verschiedenen Datentypen:

- Je nach Button-Name wird eine bestimmte Konvertierungsaktion durchgeführt:
- `ConvertAlpha2AlphaButton:` Überträgt den Inhalt eines Alpha-Felds in ein anderes und zeigt ihn in einem Label an.
- `ConvertInt2AlphaButton:` Wandelt eine Integer-Zahl (Int) in eine alphabetische Darstellung (Alpha) um und umgekehrt.
- `ConvertBig2AlphaButton:` Ähnlich wie ConvertInt2Alpha, aber für große Zahlen (BigInt).
- `Anzeige der Ergebnisse:` Die Ergebnisse der Konvertierungen werden in einem Zielfeld angezeigt.

- `Checkbox:` wenn an ist wird eine `1` gezeigt, wenn Sie aus ist wird eine `0` gezeigt.
- `Radiobutton` bei `Off` wird `False` angezeigt, bei `On` wird `True` angezeigt.

```C
  /* Dieser Code definiert ein Ereignis (EvtClickedCheckbox12), das ausgelöst wird,
wenn ein Kontrollkästchen (Checkbox12) angeklickt wird.
Je nach Zustand des Kontrollkästchens (aktiviert oder deaktiviert) wird
der Wert eines anderen Feldes (ConvertCheckBoxEins2NullZielField) auf "1" oder "0" gesetzt. */

sub EvtClickedCheckbox12
(aEvt :event;)// ConvertDate 1 o 0/
   : logic;
   {
   IF ($Checkbox12->wpCheckState =_WinStateChkChecked){
      $ConvertCheckBoxEins2NullZielField ->  WpCaption     # '1';
      }Else{
      $ConvertCheckBoxEins2NullZielField ->  WpCaption     # '0';

   }
   return(true);
 }

/*  Das Code definiert ein Ereignis (EvtClickedButton12), das ausgelöst wird,
wenn ein Radiobutton angeklickt wird. Je nach Zustand des Radiobuttons (angehakt oder nicht)
wird der Text eines Zielfeldes (ConvertCheckBoxTrue2FalseZielField) auf "True" oder "False" gesetzt. */

 sub EvtClickedButton12 //ConvertDate True to False /
    (
      aEvt        :event;   // Ereignis
     )
   : logic;
   {
   IF ($RadiobuttonOn->wpCheckState = _winStateChkChecked){
      $ConvertCheckBoxTrue2FalseZielField ->  WpCaption     # 'True';
      }Else{
      $ConvertCheckBoxTrue2FalseZielField ->  WpCaption     # 'False';
   }
   }

```

## CnvAI, CnvAB, CnvIA, CnvBA:

Dies sind integrierte Funktionen in `Conzept 16` zur Konvertierung zwischen verschiedenen Datentypen umgewandelt.

## Main-Funktion:

- Die Hauptfunktion, die ein Fenster mit dem Namen `"Konvertierung"` öffnet und die Interaktion mit dem Benutzer ermöglicht.
- Führt den Dialog aus und schließt ihn anschließend wieder.
