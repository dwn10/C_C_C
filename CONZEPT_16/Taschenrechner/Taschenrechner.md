```C
// _Taschenrechner
@A+
@C+

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
```
