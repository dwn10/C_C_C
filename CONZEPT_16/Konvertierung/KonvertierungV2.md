```C
-----------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------
 ## ##    ## ##   ###  ##  ### ##   ### ###  ### ##   #### ##              ##     ## ###
##   ##  ##   ##    ## ##  ##  ##    ##  ##   ##  ##  # ## ##             ###    ##   ##
##       ##   ##   # ## #     ##     ##       ##  ##    ##                 ##    ##
##       ##   ##   ## ##     ##      ## ##    ##  ##    ##                 ##    ## ###
##       ##   ##   ##  ##   ##       ##       ## ##     ##                 ##    ##   ##
##   ##  ##   ##   ##  ##  ##  ##    ##  ##   ##        ##                 ##    ##   ##
 ## ##    ## ##   ###  ##  # ####   ### ###  ####      ####               ####    ## ##
-----------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------
```

## Das Konzept 16 befasst sich mit der Konvertierung von Werten zwischen verschiedenen Datentypen,

- wie `Alpha` (Text), `Integer`, `BigInt`,
- `Float`, `Decimal`, `Time`, `Date`,
- `Checkbox`- und `Radiobutton`-Zuständen

## Hauptfunktionen:

`EvtClickedButton:`

- Diese Funktion verarbeitet Klickereignisse auf Schaltflächen.
- Je nach Name der angeklickten Schaltfläche werden Werte zwischen zwei Feldern konvertiert.
- Unterstützt Konvertierungen zwischen verschiedenen Datentypen (z. B. Alpha zu Integer, BigInt zu Alpha usw.).

`EvtClickedCheckbox1:`

- Reagiert auf Klicks auf ein Kontrollkästchen.
- Setzt den Wert eines anderen Feldes auf `"1"` (wenn das Kontrollkästchen aktiviert ist) oder `"0" `(wenn deaktiviert).

`EvtClickedButton1:`

- Verarbeitet Klicks auf einen `Radiobutton`.
- Setzt den Text eines Zielfeldes auf `"True"` (wenn der Radiobutton aktiviert ist) oder `"False"` (wenn deaktiviert).

`Hauptprogramm (Main):`

- Öffnet ein Dialogfenster mit dem Namen `"KonvertierungV2"`.
- Führt den Dialog aus (wartet auf Benutzerinteraktionen).
- Schließt das Dialogfenster nach Beendigung.

`Wichtige Hinweise:`

- Der Code verwendet spezielle Funktionen wie `CnvAI` `(Alpha to Integer)`, `CnvAB` `(Alpha to BigInt)`, etc. für die Konvertierungen.
- Die Verwendung von `SWITCH` ermöglicht die effiziente Verarbeitung verschiedener Schaltflächenklicks.

---

## CODE-ERKLÄRUNG

---

```C
// KonvertierungV:

@A+ // Beginnt die Deklaration globaler Variablen.
@C+ // Beginnt die Deklaration der Funktionen und Prozeduren.

//----------------------------------------------------------------------------
// ALPHA: Umwandlung von anderen Datentypen in den Alpha-Typ (String)
//----------------------------------------------------------------------------

// EvtClickedButton: Diese Funktion wird aufgerufen, wenn ein Button geklickt wird.
sub EvtClickedButton (aEvt : event;) : logic;  // 'aEvt' ist das Ereignisobjekt des Klicks
Local {
  tObj : Int; tCaption : Alpha; tObjName : Alpha; // Lokale Variablen für Objekt, Beschriftung und Namen
} {
  tObj      # aEvt:Obj;               // Abrufen des angeklickten Objekts
  tCaption  # tObj->WpCaption;        // Abrufen der Beschriftung des Objekts
  tObjName  # tObj->WpName;          // Abrufen des Namens des Objekts

  // Switch-Anweisung zur Unterscheidung der Buttons anhand ihres Namens
  SWITCH (tObjName) {

    // Umwandlung zwischen zwei Alpha-Feldern (Strings)
    CASE 'ConvertAlphatoAlphaButton' : {
      IF ($FieldAlphatoAlpha->WpCaption <> '') { 					// Wenn das Quellfeld nicht leer ist...
        $ConvertAlphatoAlphaZielField->WpCaption  # $FieldAlphatoAlpha->WpCaption;  	// Wert übertragen
        $FieldAlphatoAlpha->WpCaption             # '';                                 // Quellfeld leeren
      } ELSE {                                   					// Sonst (Quellfeld ist leer)
        $FieldAlphatoAlpha->WpCaption             # $ConvertAlphatoAlphaZielField->WpCaption;  // Wert zurück übertragen
        $ConvertAlphatoAlphaZielField->WpCaption  # '';                                 	// Zielfeld leeren
      }
    }

    // Umwandlung zwischen Integer und Alpha (Zahl zu String)
    CASE 'ConvertInttoAlphaButton' : {
      IF ($ConvertInttoAlphaZielField->WpCaptionInt <> 0) {  				// Wenn das Zielfeld eine Zahl enthält...
        $FieldInttoAlpha->WpCaption # CnvAI($ConvertInttoAlphaZielField->WpCaptionInt); // Umwandlung in String
        $ConvertInttoAlphaZielField->WpCaptionInt            # 0;                      	// Zielfeld leeren
      } ELSE {                                              				// Sonst (Zielfeld ist leer)
        $ConvertInttoAlphaZielField->WpCaptionInt            # CnvIA($FieldInttoAlpha->WpCaption); 	// String zu Zahl
        $FieldInttoAlpha->WpCaption                          # '';                      		// Quellfeld leeren
      }
    }

    	// (weitere CASE-Anweisungen für BigInt, Float, Decimal, Time, Date)

  } 	// Ende der SWITCH-Anweisung
} 	// Ende von EvtClickedButton

//------------------------------------------------------------------------------------
// EvtClickedCheckbox1: Setzt ein Feld auf "1" oder "0", je nach Zustand der Checkbox
//------------------------------------------------------------------------------------
sub EvtClickedCheckbox1 (aEvt :event;) : logic; {
  IF ($Checkbox1->wpCheckState = _WinStateChkChecked) {  	// Checkbox ist aktiviert
    $ConvertCheckBoxEins2NullZielField->WpCaption  # '1';
  } ELSE {                                            		// Checkbox ist deaktiviert
    $ConvertCheckBoxEins2NullZielField->WpCaption  # '0';
  }
  return(true);
}

//------------------------------------------------------------------------------------
// EvtClickedButton1: Setzt ein Feld auf "True" oder "False", je nach Zustand des Radiobuttons
//------------------------------------------------------------------------------------
sub EvtClickedButton1 (aEvt :event;) : logic; {
  IF ($RadiobuttonOn->wpCheckState = _winStateChkChecked) { 	// Radiobutton ist ausgewählt
    $RadioButtonTrue->WpCaption  # 'True';
  } ELSE {                                                	// Radiobutton ist nicht ausgewählt
    $RadioButtonTrue->WpCaption  # 'False';
  }
  return(true);
}

// Main: Hauptfunktion zum Öffnen und Ausführen des Dialogs
Main()
Local { This : Int; } {
  This # WinOpen('KonvertierungV2', _WinOpenDialog);  		// Dialog öffnen
  IF (This > 0) {
    WinDialogRun(This);                              		// Dialog ausführen
    WinClose(This);                                 		// Dialog schließen
  }
}

```
