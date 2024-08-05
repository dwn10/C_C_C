## Neu Frame erstellen

`Name:` TaschenrechnerNeu `Caption:` Frame `[Frame1]`

```C
    - AreaLeft: 6 / AreaTop: 6 / AreaRight: 516 /
    - AreaBottom: 516 / AreaWidth: 510 / AreaHeight: 510
```

---

## Ausgabe > Label

`InputField` `Edit`

```C
    - AreaLeft: 120 / AreaTop: 12 / AreaRight: 348 /
    - AreaBottom: 60 / AreaWidth: 228 / AreaHeight: 48
```

---

## Schaltflächen > Button

`Name:` Caption: Ereignisse: Special / `EvtClickedButton`

- `ZahlButton0` `Button[0]` \_Konvertierung:`EvtClickedButton`
- `ZahlButton1` `Button[1]`
- `ZahlButton2` `Button[2]`
- `ZahlButton3` `Button[3]`
- `ZahlButton4` `Button[4]`
- `ZahlButton5` `Button[5]`
- `ZahlButton6` `Button[6]`
- `ZahlButton7` `Button[7]`
- `ZahlButton8` `Button[8]`
- `ZahlButton9` `Button[9]`
- `ButtonKomma` `Button[,]`

- `ButtonClearAll` `Button[CE]`
- `ButtonPlus` `Button[+]`
- `ButtonSubtraktion` `Button[-]`
- `ButtonMultiplikation` `Button[*]`
- `ButtonDivision` `Button[/]`
- `ButtonEreignis` `Button[=]`

```C
  - AreaLeft: 234 / AreaTop: 78 / AreaRight: 324 /
  - AreaBottom: 96 / AreaWidth: 90 / AreaHeight: 18
```

## Ausgabe > Label

`OutputLabel` `Label`

```C
    - AreaLeft: 120 / AreaTop: 12 / AreaRight: 348 /
    - AreaBottom: 60 / AreaWidth: 228 / AreaHeight: 48
```

## Ausgabe > Label

- `MerkerLabelLast` `Label[b]`
- `MerkerLabelVZ` `Label[a]`

```C
    - AreaLeft: 120 / AreaTop: 12 / AreaRight: 348 /
    - AreaBottom: 60 / AreaWidth: 228 / AreaHeight: 48
```

## Ansicht > DataList

- `LastLineDataList` `DataList`

```C
    - AreaLeft: 120 / AreaTop: 12 / AreaRight: 348 /
    - AreaBottom: 60 / AreaWidth: 228 / AreaHeight: 48
```

---

```C
// _Taschenrechner
@A+
@C+
//*-----------------------------------------------------------------------------------------
//-----------------------------------------------------------------------------------------
//   ## ##    ## ##   ###  ##  ### ##   ### ###  ### ##   #### ##              ##     ## ###
//  ##   ##  ##   ##    ## ##  ##  ##    ##  ##   ##  ##  # ## ##             ###    ##   ##
//  ##       ##   ##   # ## #     ##     ##       ##  ##    ##                 ##    ##
//  ##       ##   ##   ## ##     ##      ## ##    ##  ##    ##                 ##    ## ###
//  ##       ##   ##   ##  ##   ##       ##       ## ##     ##                 ##    ##   ##
//  ##   ##  ##   ##   ##  ##  ##  ##    ##  ##   ##        ##                 ##    ##   ##
//   ## ##    ## ##   ###  ##  # ####   ### ###  ####      ####               ####    ## ##
//-----------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------*//
//////////////////
sub EvtChanged( aEvt : event; )  : logic; // Funktion: Bearbeitet das Ereignis der Änderung eines Objekts in der Benutzeroberfläche.
Local { tObj : Int ; tInhalt : Alpha ; }{

  tObj # aEvt:Obj; // tObj: ID des geänderten Objekts.
    tInhalt # tObj->WpCaption;

  return(true);
}
/////////////////
sub EvtClickedButton
(
  aEvt                  : event;        // Ereignis
)
: logic;
Local {
  tObj : Int ; tCaption : Alpha ; tObjName : Alpha ;
  tWert1 : Float ; tWert2 : Float ; tMerkerLabelLast : Alpha ; tLabelVZ : Alpha ; tLastInput : Alpha ;
  tLineCount  : Int ; tErg : Int ;  tSuccess : Logic ;
}{

  tObj      # aEvt:Obj;
  tCaption  # tObj->WpCaption;
  tObjName  # tObj->WpName;

  // Endsumme leeren?
  IF ( $MerkerLabelVZ->WpCaption = '=' ) {
    $MerkerLabelVZ->WpCaption # '';
    $OutputLabel->WpCaption   # ''; // (i) Sonst muss ein Clear erfolgen, hier der automatismus;)
  }

  SWITCH ( tObjName ) {
    CASE 'ZahlButton1' : {
      $OutputLabel->WpCaption # $OutputLabel->WpCaption +  tCaption;
    }
    CASE 'ZahlButton2' : {
      $OutputLabel->WpCaption # $OutputLabel->WpCaption +  tCaption;
    }
    CASE 'ZahlButton3' : {
      $OutputLabel->WpCaption # $OutputLabel->WpCaption +  tCaption;
    }
    CASE 'ZahlButton4' : {
      $OutputLabel->WpCaption # $OutputLabel->WpCaption +  tCaption;
    }
    CASE 'ZahlButton5' : {
      $OutputLabel->WpCaption # $OutputLabel->WpCaption +  tCaption;
    }
    CASE 'ZahlButton6' : {
      $OutputLabel->WpCaption # $OutputLabel->WpCaption +  tCaption;
    }
    CASE 'ZahlButton7' : {
      $OutputLabel->WpCaption # $OutputLabel->WpCaption +  tCaption;
    }
    CASE 'ZahlButton8' : {
      $OutputLabel->WpCaption # $OutputLabel->WpCaption +  tCaption;
    }
    CASE 'ZahlButton9' : {
      $OutputLabel->WpCaption # $OutputLabel->WpCaption +  tCaption;
    }
    CASE 'ZahlButton0' : {
      $OutputLabel->WpCaption # $OutputLabel->WpCaption +  tCaption;
    }

    // Buttons | Komma , +, - , *, /, +-
    CASE 'ButtonKomma' : {
      $OutputLabel->WpCaption # $OutputLabel->WpCaption +  tCaption;
    }

    CASE 'ButtonPlus' : {
      $MerkerLabelLast->WpCaption # $OutputLabel->WpCaption; // Bisherige Eingabe sichern
      $OutputLabel->WpCaption     # '';                      // Letzte Eingabe leeren
      $MerkerLabelVZ->WpCaption   # '+';
    }
    CASE 'ButtonSubtraktion' : {
      $MerkerLabelLast->WpCaption # $OutputLabel->WpCaption; // Bisherige Eingabe sichern
      $OutputLabel->WpCaption     # '';                      // Letzte Eingabe leeren
      $MerkerLabelVZ->WpCaption   # '-';
    }
    CASE 'ButtonMultiplikation' : {
      $MerkerLabelLast->WpCaption # $OutputLabel->WpCaption; // Bisherige Eingabe sichern
      $OutputLabel->WpCaption     # '';                      // Letzte Eingabe leeren
      $MerkerLabelVZ->WpCaption   # '*';
    }
    CASE 'ButtonDivision' : {
      $MerkerLabelLast->WpCaption # $OutputLabel->WpCaption; // Bisherige Eingabe sichern
      $OutputLabel->WpCaption     # '';                      // Letzte Eingabe leeren
      $MerkerLabelVZ->WpCaption   # '/';
    }
    CASE 'ButtonPlusMinus' : {
      $OutputLabel->WpCaption # $OutputLabel->WpCaption + tCaption;
    }



    CASE 'ButtonClearAll' : {
      WinLstDatLineRemove( $LastLineDataList, _WinLstDatLineAll );
    }
    CASE 'ButtonEreignis' : {
      tLabelVZ          # $MerkerLabelVZ->WpCaption;
      tWert1            # CnvFA( $MerkerLabelLast->WpCaption );
      tWert2            # CnvFA( $OutputLabel->WpCaption );
      tMerkerLabelLast  # $MerkerLabelLast->WpCaption;
      tLastInput        # $OutputLabel->WpCaption;
      SWITCH ( tLabelVZ ) {
        CASE '+' : {
          $OutputLabel->WpCaption # tMerkerLabelLast + tLabelVZ + tLastInput + ' = ' + CnvAF( tWert1 + tWert2 );
        }
      }

      SWITCH ( tLabelVZ ) {
        CASE '-' : {
          $OutputLabel->WpCaption # tMerkerLabelLast + tLabelVZ + tLastInput + ' = ' + CnvAF( tWert1 - tWert2 );
        }
      }

      SWITCH ( tLabelVZ ) {
        CASE '*' : {
          $OutputLabel->WpCaption # tMerkerLabelLast + tLabelVZ + tLastInput + ' = ' + CnvAF( tWert1 * tWert2 );
        }
      }

      SWITCH ( tLabelVZ ) {
        CASE '/' : {
          $OutputLabel->WpCaption # tMerkerLabelLast + tLabelVZ + tLastInput + ' = ' + CnvAF( tWert1 / tWert2 );
        }
      }
      // SWITCH ..
      $MerkerLabelVZ->WpCaption   # '=';
      $MerkerLabelLast->WpCaption # '';

      tLineCount # WinLstDatLineInfo( $LastLineDataList, _WinLstDatInfoCount );
      tLineCount # WinLstDatLineAdd( $LastLineDataList, tLineCount + 1, _WinLstDatLineLast );
      tSuccess   # WinLstCellSet( $LastLineDataList, $OutputLabel->WpCaption, 2, _WinLstDatLineLast );


    }
    // Buttons |
  } // SWITCH ...
  return(true);
}


SUB Test1(){}

Main()
Local { This : Int ; }{
  This # WinOpen( 'Taschenrechner', _WinOpenDialog );
  IF ( This > 0 ) {
    WinDialogRun( This );
    WinClose( This );
  }
}
```
