``` C
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
```

------------------------------
``` C
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
```
------------------------------
##
``` C
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
```
##
``` C
// Konvertierung
@A+
@C+
sub EvtClickedButton
(
aEvt    :event; // Ereignis
)
: logic;
Local {
  tObj  : Int ; obj tCaption  :  Alpha  ; tObjName  :   Alpha  ;
  tTestAlpha : Alpha  ;  tTestInt  :  Int  ;  tTestBigInt  :  BigInt ;
}(
  tObj        #  aEvt:Obj;
  tCaption    #  tObj->WpCaption;
  tObjName    #  tObj->WpName;
SWITCH (tObjlName) {
  CASE 'ConvertAlpha2AlphaButton': (
  //tTest # $FieldAlpha2Alpha->WpCaption;
  IF ( $FieldAlpha2Alpha->WpCaption <> '' ) {
    $ConvertAlpha2AlphaZielField->WpCaption # $FieldAlpha2Alpha->WpCaption;
    $OutputLabell->lWpCaption               # $FieldAlpha2Alpha->WpCaption;
    $FieldAlpha2Alpha->WpCaption            # '';
} ELSE {
    $FieldAlpha2Alpha->WpCaption            # $ConvertAlpha2AlphaZielField->WpCaption;
    $OutputLabell->WpCaption                # $ConvertAlpha2AlphaZielField->WpCaption;
    $FieldAlpha2Alpha->pCaption:
    $ConvertAlpha2AlphaZielField->WpCaption  # '';
}
}




// Conv2Aipha
CASE ConvertInt2AlphaButton FieldInt2Alpha->WpCaptionInt: TestInt
: // (1) ConvertInt2Alpha + Label + Field + Button Convertint2AlphaZielField
IF (FieldInt2Alpha->MpCaptionInt <> 0) [
$OutputLabell->WpCaption FieldInt2Alpha->WpCaptionInt
$ConvertInt2AlphaZielField->pCaption CnvAI (SFieldInt2Alpha->apCaptionInt):
# CnvAI (FieldInt2Alpha->pCaptionInt):
#0:
#CnvIA( ConvertInt2AlphaZielField->@pCaption);
# $ConvertInt2AlphaZielField->FpCaption:

}
} ELSE {
}
FieldInt2Alpha->SpCaptionInt OutputLabell->WpCaption
Convert.Int2AlphaZielField->pCaption:
}// ConvertInt2AlphaButton
CASE ConvertBig2AlphaButton': { // (1) ConvertBig2Alpha Label Field Button ConvertBig2AlphaZiel Field
TestBigInt FieldBigInt2Alpha->WpCaptionBigInt:
IF (FieldBigInt2Alpha->RpCaptionBigInt <> b) {
$ConvertBig2AlphaZielField->RpCaption CnvAB(FieldBigInt2Alpha->RpCaptionBigInt); CnvAB(FieldBigInt2Alpha->apCaptionBigInt):
$OutputLabell->WpCaption
FieldBigInt2Alpha->WpCaptionBigInt } ELSE ( 0\b:
FieldBigInt2Alpha->WpCaptionBigInt
OutputLabell->WpCaption ConvertBig2AlphaZielField->pCaption:
ChvBA( ConvertBig2AlphaZielField->pCaption):
ConvertBig2AlphaZielField->pCaption:
}
// SWITCH //
return(true);
Main()
Local (This: Int ){
This
WinOpen('Konvertierung", WinOpenDialog);
IF (This > 0) {
WinDialogRun (This);
WinClose (This);
}
} 
```
