// Taschenrechner
@A+
@C+

///////////////////////////
sub EvtChanced ( aEvt : event; )  : logic;  // Ereignis
Local { tObj : Int ; tInhalt : Alpha ;}{
  tObj # aEvt:Obj;
  tInhalt # tObj->WpCaption;

  return(true);
}
///////////////////////////
sub EvtClickedButton
(
  aEvt              : event;                  // Ereignis
)
: logic;
Local { tObj : Int ; tInhalt : Alpha ;}{
  tObj # aEvt:Obj;
  tInhalt # tObj->WpCaption;
  return(true);
}

Main()
Local { This : Int ; }{
  This # WinOpen('Taschenrechner', _WinOpenDialog);
  IF ( This > 0 ){
    WinDialogRun( This );
    WinClose( This );
  }
}
------------------------------
------------------------------

)
: logic;
Local { tObj : Int; tCaption : Alpha; tObjName:
Alpha; tWert1 : Int; TWert2: Int; tMerkerLabelLast: Alpha; }{

  tObj        # aEvt:Obj;
  tCaptation  # tObj->WpCaption;
  tObjName    # tObj->WpName;

  SWITCH ( tObjName ){
    CASE 'ZahlButton1' : {
      $OutputLabel->WpCaption # $OutputLabel->WpCaption + tCaption;
    }
    CASE 'ZahlButton2' : {
      $OutputLabel->WpCaption # $OutputLabel->WpCaption + tCaption;
    }
    CASE 'ZahlButton3' : {
      $OutputLabel->WpCaption # $OutputLabel->WpCaption + tCaption;
    }
    CASE 'ZahlButton4' : {
      $OutputLabel->WpCaption # $OutputLabel->WpCaption + tCaption;
    }
    CASE 'ZahlButton5' : {
      $OutputLabel->WpCaption # $OutputLabel->WpCaption + tCaption;
    }
    CASE 'ZahlButton6' : {
      $OutputLabel->WpCaption # $OutputLabel->WpCaption + tCaption;
    }
    CASE 'ZahlButton7' : {
      $OutputLabel->WpCaption # $OutputLabel->WpCaption + tCaption;
    }
    CASE 'ZahlButton8' : {
      $OutputLabel->WpCaption # $OutputLabel->WpCaption + tCaption;
    }
    CASE 'ZahlButton9' : {
      $OutputLabel->WpCaption # $OutputLabel->WpCaption + tCaption;
    }
    CASE 'ZahlButton0' : {
      $OutputLabel->WpCaption # $OutputLabel->WpCaption + tCaption;
    }

    // Buttons | Komma , +, -, *, /, +-
    CASE 'ButtonKomma' : {
      $OutputLabel->WpCaption # $OutputLabel->WpCaption + tCaption;
    }

    CASE 'ButtonPlus' : {
      $MerkerLabelLast->WpCaption # $OutputLabel->WpCaption;

      IF ( $MerkerLabelVZ->WpCaption = '+' ){
        tWert1 # CnvIA( $MerkerLabellast->WpCaption);
        tWert2 # CnvIA( $OutputLabel->WpCaption);
        tMerkerLabelLast # $MerkerLabelLast->WpCaption;
        $OutputLabel->WpCaption # tMerkerLabellast +
        $MerkerLabelVZ->WpCaption +
        $OutputLabel->WpCaption +
        '=' + CnvAI( tWert1 + tWert2 );
      }
      $MerkerLabelVZ->WpCaption # '+';
    }
}
}
##
CASE 'ButtonPlus' : {
  // Store the current displayed value in a variable
  tWert1 := CnvIA($OutputLabel->WpCaption);

  // If the previous operation was also addition, perform the addition
  IF ($MerkerLabelVZ->WpCaption = '+') THEN
    tWert2 := CnvIA($MerkerLabelLast->WpCaption);  // Use previous value
    $OutputLabel->WpCaption := CnvAI(tWert1 + tWert2);  // Update output with sum
  ELSE
    // Store the current displayed value for future addition
    $MerkerLabelLast->WpCaption := $OutputLabel->WpCaption;
  END;

  // Update the operator marker
  $MerkerLabelVZ->WpCaption := '+';
}

