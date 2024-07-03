## neu Frame

`Name:` KonvertierungNeu `Caption:` KonvertierungsbefehleFrame

AreaLeft: 6 / AteaTop: 6 / AreaRight: 516 /
AreaBottom: 516 / AreaWidth: 510 / AreaHeight: 510

---

## Anordnung > Notebook

`Notebook1`

AreaLeft: 6 / AteaTop: 6 / AreaRight: 516 /
AreaBottom: 516 / AreaWidth: 510 / AreaHeight: 510

---

## Ausgabe > Label

Konvertierungsbefehle Datentypen

AreaLeft: 120 / AteaTop: 12 / AreaRight: 348 /
AreaBottom: 60 / AreaWidth: 228 / AreaHeight: 48

---

## Ausgabe > Label

`Name:` > `Caption:`

AlphaLabel `Alpha`
IntLabel `Int`
BigIntLabel `BigInt`
FloatLabel `Float`
DecimalLabel `Decimal`
TimeLabel `Time`
DateLabel `Date`

---

---

## Eingabe > Edit

`Name:` > `Caption:`

FieldAlpha2Alpha > 0,10
FieldInt2Alpha > 100
FieldBigInt2Alpha > 10
FieldFloat > 0,2
FieldDecimal > 0,50
FieldTime > 08:30:00,00
FieldDate > 15.05.2024

AreaLeft: 132 / AteaTop: 78 / AreaRight: 222 /
AreaBottom: 96 / AreaWidth: 90 / AreaHeight: 18

---

## Schaltflächen > Button

`Name:` Caption: Ereignisse: Special / `EvtClicked`

ConvertAlpha2AlphaButton `<<>>` \_Konvertierung:`EvtClickedButton`
ConvertInt2AlphaButton
ConvertBig2AlphaButton
ConvertFloat2AlphaButton
ConvertDecimal2AlphaButton
ConvertTime2AlphaButton
ConvertDatel2AlphaButton

AreaLeft: 234 / AteaTop: 78 / AreaRight: 324 /
AreaBottom: 96 / AreaWidth: 90 / AreaHeight: 18

---

## Eingabe > Edit

`Name:` `Caption:`

ConvertAlpha2AlphaZielField x
ConvertInt2AlphaZielField
ConvertBig2AlphaZielField
ConvertFloat2AlphaField
ConvertDecimal2AlphaZielField
ConvertTime2AlphaZielField
ConvertDate2AlphaZielField

AreaLeft: 336 / AteaTop: 78 / AreaRight: 426 /
AreaBottom: 96 / AreaWidth: 90 / AreaHeight: 18

---

---

## Schaltflächen > Checkbox

Checkbox1 Checkbox

---

## Eingabe > Edit

ConvertCheckBoxEins2NullZielField x

---

## Anordnung > GroupBox > Ereignisse

Groupbox1 > Checkbox > \_Konvertierung:EvtClickedCheckbox1

---

## Schaltflächen > Radiobutton

Name: RadiobuttonOff / Caption: `Off`
Name: RadiobuttonOn / Caption: `On`

AreaLeft: 30 / AteaTop: 30 / AreaRight: 114 /
AreaBottom: 54 / AreaWidth: 84 / AreaHeight: 24

---

---

```C
// _KonvertierungNeu
@A+
@C+

 /* Das Programm öffnet ein Dialogfenster namens "KonvertierungNeu"
 und führt es aus. Wenn das Fenster erfolgreich geöffnet wurde (Rückgabewert > 0),
 wird es nach der Ausführung geschlossen.*/
Main()
Local { This : Int ; }{
  This # WinOpen( 'KonvertierungNeu', _WinOpenDialog );
  IF ( This > 0 ) {
    WinDialogRun( This );
    WinClose( This );
  }
}

-----------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------
 ## ##    ## ##   ###  ##  ### ##   ### ###  ### ##   #### ##              ##     ## ###            ## ##    ## ##   ### ##   ### ###
##   ##  ##   ##    ## ##  ##  ##    ##  ##   ##  ##  # ## ##             ###    ##   ##           ##   ##  ##   ##   ##  ##   ##  ##
##       ##   ##   # ## #     ##     ##       ##  ##    ##                 ##    ##                ##       ##   ##   ##  ##   ##
##       ##   ##   ## ##     ##      ## ##    ##  ##    ##                 ##    ## ###            ##       ##   ##   ##  ##   ## ##
##       ##   ##   ##  ##   ##       ##       ## ##     ##                 ##    ##   ##           ##       ##   ##   ##  ##   ##
##   ##  ##   ##   ##  ##  ##  ##    ##  ##   ##        ##                 ##    ##   ##           ##   ##  ##   ##   ##  ##   ##  ##
 ## ##    ## ##   ###  ##  # ####   ### ###  ####      ####               ####    ## ##             ## ##    ## ##   ### ##   ### ###
-----------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------

// _Konvertierung
@A+
@C+
//----------------------------------------------------------------------------
//  ALPHA
//----------------------------------------------------------------------------

/* Dieses Code behandelt ein Click-Ereignis (EvtClickedButton) in einer Anwendung.
Es identifiziert das angeklickte Objekt (tObj) und reagiert spezifisch auf einen Button namens
'ConvertAlpha2AlphaButton'.

Wenn das Eingabefeld ($FieldAlpha2Alpha) nicht leer ist, wird sein Inhalt in ein Zielfeld
($ConvertAlpha2AlphaZielField) und ein Ausgabe-Label ($OutputLabel1) kopiert und anschließend gelöscht.

Ist das Eingabefeld leer, wird der Inhalt des Zielfelds in das Eingabefeld und das Ausgabe-Label kopiert
und aus dem Zielfeld gelöscht. */

sub EvtClickedButton
(
  aEvt                  : event;        // Ereignis
)
: logic;
Local {
  tObj : Int ; tCaption : Alpha ; tObjName : Alpha ;
  tTestAlpha : Alpha ; tTestInt : Int ; tTestBigInt : BigInt ; tTestFloat : Float ;
  tTestDecimal : Decimal ; tTestTime : time ; tTestDate : Date ;
}{
  tObj      # aEvt:Obj;
  tCaption  # tObj->WpCaption;
  tObjName  # tObj->WpName;
  SWITCH ( tObjName ) {
    CASE 'ConvertAlpha2AlphaButton' : {
      ///tTest # $FieldAlpha2Alpha->WpCaption;
      IF ( $FieldAlpha2Alpha->WpCaption <> ''  ) {
        $ConvertAlpha2AlphaZielField->WpCaption # $FieldAlpha2Alpha->WpCaption;
        $OutputLabel1->WpCaption                # $FieldAlpha2Alpha->WpCaption;
        $FieldAlpha2Alpha->WpCaption            # '';
      } ELSE {
        $FieldAlpha2Alpha->WpCaption            # $ConvertAlpha2AlphaZielField->WpCaption;
        $OutputLabel1->WpCaption                # $ConvertAlpha2AlphaZielField->WpCaption;
        $ConvertAlpha2AlphaZielField->WpCaption # '';
      }

    } // ConvInt2Alpha
    CASE 'ConvertInt2AlphaButton' : { // (i)  ConvertInt2Alpha + Label + Field + Button  ConvertInt2AlphaZielField
      tTestInt # $FieldInt2Alpha->WpCaptionInt;
      IF ( $FieldInt2Alpha->WpCaptionInt <> 0  ) {
        $ConvertInt2AlphaZielField->WpCaption # CnvAI( $FieldInt2Alpha->WpCaptionInt );
        $OutputLabel1->WpCaption              # CnvAI( $FieldInt2Alpha->WpCaptionInt );
        $FieldInt2Alpha->WpCaptionInt         # 0;
      } ELSE {
        $FieldInt2Alpha->WpCaptionInt         # CnvIA( $ConvertInt2AlphaZielField->WpCaption );
        $OutputLabel1->WpCaption              # $ConvertInt2AlphaZielField->WpCaption;
        $ConvertInt2AlphaZielField->WpCaption # '';
      }

    } // ConvertBigInt2AlphaButton
    CASE 'ConvertBig2AlphaButton' : {  // (i)   ConvertBig2Alpha + Label + Field + Button  ConvertBig2AlphaZielField
      tTestBigInt # $FieldBigInt2Alpha->WpCaptionBigInt;
      IF ( $FieldBigInt2Alpha->WpCaptionBigInt <> 0\b ) {
        $ConvertBig2AlphaZielField->WpCaption # CnvAB( $FieldBigInt2Alpha->WpCaptionBigInt );
        $OutputLabel1->WpCaption              # CnvAB( $FieldBigInt2Alpha->WpCaptionBigInt );
        $FieldBigInt2Alpha->WpCaptionBigInt   # 0\b;
      } ELSE {
        $FieldBigInt2Alpha->WpCaptionBigInt   # CnvBA( $ConvertBig2AlphaZielField->WpCaption );
        $OutputLabel1->WpCaption              # $ConvertBig2AlphaZielField->WpCaption;
        $ConvertBig2AlphaZielField->WpCaption # '';
      }

     } // ConvertFloat2AlphaButton
    CASE 'ConvertFloat2AlphaButton' : {  // (i)   ConvertFloat2Alpha + Label + Field + Button  ConvertFloat2AlphaZielField
      tTestFloat # $FieldFloat->WpCaptionFloat;
      IF ( $FieldFloat->WpCaptionFloat <>  0.0 ) {
        $ConvertFloat2AlphaField->WpCaption     # CnvAF( $FieldFloat->WpCaptionFloat );
        $OutputLabel1->WpCaption                # CnvAF( $FieldFloat->WpCaptionFloat );
        $FieldFloat->WpCaptionFloat             # 0.0;
      } ELSE {
        $FieldFloat->WpCaptionFloat             # CnvFA( $ConvertFloat2AlphaField->WpCaption );
        $OutputLabel1->WpCaption                # $ConvertFloat2AlphaField->WpCaption;
        $ConvertFloat2AlphaField->WpCaption     # '';
      }

    } // ConvertDecimal2AlphaButton
    CASE 'ConvertDecimal2AlphaButton' : {  // (i)   ConvertDecimal2Alpha + Label + Field + Button  ConvertDecimal2AlphaZielField
      tTestDecimal # $FieldDecimal->WpCaptionDecimal;
      IF ( $FieldDecimal->WpCaptionDecimal <>  0\m ) {
        $ConvertDecimal2AlphaZielField->WpCaption   # CnvAM( $FieldDecimal->WpCaptionDecimal );
        $OutputLabel1->WpCaption                    # CnvAM( $FieldDecimal->WpCaptionDecimal );
        $FieldDecimal->WpCaptionDecimal             # 0\m;
      } ELSE {
        $FieldDecimal->WpCaptionDecimal             # CnvMA( $ConvertDecimal2AlphaZielField->WpCaption );
        $OutputLabel1->WpCaption                    # $ConvertDecimal2AlphaZielField->WpCaption;
        $ConvertDecimal2AlphaZielField->WpCaption   # '';
      }

    } // ConvertTime2AlphaButton
    CASE 'ConvertTime2AlphaButton' : {  // (i)   ConvertTime2Alpha + Label + Field + Button  ConvertTime2AlphaZielField
      tTestTime # $FieldTime->WpCaptionTime;
      IF ( $FieldTime->WpCaptionTime <>  00:00:00.0 ) {
        $ConvertTime2AlphaZielField->WpCaption    # CnvAT( $FieldTime->WpCaptionTime );
        $OutputLabel1->WpCaption                  # CnvAT( $FieldTime->WpCaptionTime );
        $FieldTime->WpCaptionTime                 # 00:00:00.0;
      } ELSE {
        $FieldTime->WpCaptionTime                 # CnvTA( $ConvertTime2AlphaZielField->WpCaption );
        $OutputLabel1->WpCaption                  # $ConvertTime2AlphaZielField->WpCaption;
        $ConvertTime2AlphaZielField->WpCaption    # '';
      }

    } // ConvertDatel2AlphaButton
    CASE 'ConvertDatel2AlphaButton' : {  // (i)   ConvertDatel2Alpha + Label + Field + Button  ConvertDate2AlphaZielField
      tTestDate # $FieldDate->WpCaptionDate;
      IF ( $FieldDate->WpCaptionDate <>  0.0.0 ) {
        $ConvertDate2AlphaZielField->WpCaption    # CnvAD( $FieldDate->WpCaptionDate );
        $OutputLabel1->WpCaption                  # CnvAD( $FieldDate->WpCaptionDate );
        $FieldDate->WpCaptionDate                 # 0.0.0;
      } ELSE {
        $FieldDate->WpCaptionDate                 # CnvDA( $ConvertDate2AlphaZielField->WpCaption );
        $OutputLabel1->WpCaption                  # $ConvertDate2AlphaZielField->WpCaption;
        $ConvertDate2AlphaZielField->WpCaption    # '';
      }
    }
  } // SWITCH
} // EvtClickedButton

//----------------------------------------------------------------------------
//  INT
//----------------------------------------------------------------------------
sub EvtClickedButtonPage2
(
  aEvt                  : event;        // Ereignis
)
: logic;
Local {
  tObj : Int ; tCaption : Alpha ; tObjName : Alpha ;
  tTestAlpha : Alpha ; tTestInt : Int ; tTestBigInt : BigInt ; tTestFloat : Float ;
  tTestDecimal : Decimal ; tTestTime : time ; tTestDate : Date ;
}{
  tObj      # aEvt:Obj;
  tCaption  # tObj->WpCaption;
  tObjName  # tObj->WpName;
  SWITCH ( tObjName ) {
    CASE 'ConvertAlpha2IntButtonS2' : {
      ///tTest # $FieldAlpha2Alpha->WpCaption;
      IF ( $FieldAlpha2Int->WpCaption <> ''  ) {
        $ConvertInt2IntZielFieldS2->WpCaptionInt  # CnvIA( $FieldAlpha2Int->WpCaption );
        $FieldAlpha2Int->WpCaption                # '';
      } ELSE {
        $FieldAlpha2Int->WpCaption                # CnvAI( $ConvertInt2IntZielFieldS2->WpCaptionInt );
        $ConvertInt2IntZielFieldS2->WpCaptionInt  # 0;
      }

    } // ConvInt2Int
    CASE 'ConvertInt2IntButton' : { // (i)  ConvertInt2Int + Label + Field + Button  ConvertInt2IntZielField
      //tTestInt # $FieldInt2Alpha->WpCaptionInt;
      IF ( $FieldInt2Int->WpCaptionInt <> 0  ) {
        $ConvertInt2IntZielField->WpCaptionInt       #  $FieldInt2Int->WpCaptionInt;
        $FieldInt2Int->WpCaptionInt                  # 0;
      } ELSE {
        $FieldInt2Int->WpCaptionInt                  #  $ConvertInt2IntZielField->WpCaptionInt ;
        $ConvertInt2IntZielField->WpCaptionInt       # 0;
      }

    } // ConvertBig2IntButton
    CASE 'ConvertBig2IntButton' : {  // (i)   ConvertBig2Int + Label + Field + Button  ConvertBig2IntZielField
      IF ( $FieldBigInt2Int->WpCaptionBigInt <> 0\b ) {
        $ConvertBig2IntZielField->WpCaptionInt       # CnvIB( $FieldBigInt2Int->WpCaptionBigInt );
        $FieldBigInt2Int->WpCaptionBigInt           # 0\b;
      } ELSE {
        $FieldBigInt2Int->WpCaptionBigInt           # CnvBI( $ConvertBig2IntZielField->WpCaptionInt );
        $ConvertBig2IntZielField->WpCaptionInt      # 0;
      }

     } // ConvertFloat2IntButton
    CASE 'ConvertFloat2IntButton' : {  // (i)   ConvertFloatInt + Label + Field + Button  ConvertFloat2IntZielField

      IF ( $FieldFloat2Int->WpCaptionFloat <>  0.0 ) {
        $ConvertFloat2IntZielField->WpCaptionInt      # CnvIF( $FieldFloat2Int->WpCaptionFloat );
        $FieldFloat2Int->WpCaptionFloat               # 0.0;
      } ELSE {
        $FieldFloat2Int->WpCaptionFloat               # CnvFI( $ConvertFloat2IntZielField->WpCaptionInt );
        $ConvertFloat2IntZielField->WpCaptionInt      # 0;
      }

    } // ConvertDecimal2IntButton
    CASE 'ConvertDecimal2IntButton' : {  // (i)   ConvertDecimal2Int + Label + Field + Button  ConvertDecimal2IntZielField
      tTestDecimal # $FieldDecimal2Int->WpCaptionDecimal;
      IF ( $FieldDecimal2Int->WpCaptionDecimal <>  0\m ) {
        $ConvertDecimal2IntZielField->WpCaptionInt      # CnvIM( $FieldDecimal2Int->WpCaptionDecimal );
        $FieldDecimal2Int->WpCaptionDecimal             # 0\m;
      } ELSE {
        $FieldDecimal2Int->WpCaptionDecimal             # CnvMI( $ConvertDecimal2IntZielField->WpCaptionInt );
        $ConvertDecimal2IntZielField->WpCaptionInt      # 0;
      }

    } // ConvertTime2IntButton
    CASE 'ConvertTime2IntButton' : {  // (i)   ConvertTime2Int + Label + Field + Button  ConvertTime2IntZielField
      IF ( $FieldTime2Int->WpCaptionTime <>  00:00:00.0 ) {
        $ConvertTime2IntZielField->WpCaptionInt        # CnvIT( $FieldTime2Int->WpCaptionTime );
        $FieldTime2Int->WpCaptionTime                  # 00:00:00.0;
      } ELSE {
        $FieldTime2Int->WpCaptionTime                  # CnvTI( $ConvertTime2IntZielField->WpCaptionInt );
      }

    } // ConvertDatel2IntButton
    CASE 'ConvertDatel2IntButton' : {  // (i)   ConvertDatel2Int + Label + Field + Button  ConvertDate2IntZielField

      IF ( $FieldDate2Int->WpCaptionDate <>  0.0.0 ) {
        $ConvertDate2IntZielField->WpCaptionInt         # CnvID( $FieldDate2Int->WpCaptionDate );
        $FieldDate2Int->WpCaptionDate                   # 0.0.0;
      } ELSE {
        $FieldDate2Int->WpCaptionDate                   # CnvDI( $ConvertDate2IntZielField->WpCaptionInt );
      }
    }
  } // SWITCH
} // EvtClickedButton

//----------------------------------------------------------------------------
//  BIGINT
//----------------------------------------------------------------------------
sub EvtClickedButtonPage3
(
  aEvt                  : event;        // Ereignis
)
: logic;
Local {
  tObj : Int ; tCaption : Alpha ; tObjName : Alpha ;
  tTestAlpha : Alpha ; tTestInt : Int ; tTestBigInt : BigInt ; tTestFloat : Float ;
  tTestDecimal : Decimal ; tTestTime : time ; tTestDate : Date ;
}{
  tObj      # aEvt:Obj;
  tCaption  # tObj->WpCaption;
  tObjName  # tObj->WpName;
  SWITCH ( tObjName ) {
    CASE 'ConvertAlpha2BigIntButtonS3' : {
      IF ( $FieldAlpha2BigInt->WpCaption <> ''  ) {
        $ConvertAlpha2BigIntZielFieldS3->WpCaptionBigInt  # CnvBA( $FieldAlpha2BigInt->WpCaption );
        $FieldAlpha2BigInt->WpCaption                     # '';
      } ELSE {
        $FieldAlpha2BigInt->WpCaption                     # CnvAB( $ConvertAlpha2BigIntZielFieldS3->WpCaptionBigInt );
        $ConvertAlpha2BigIntZielFieldS3->WpCaptionBigInt  # 0\b;
      }

    } // ConvInt2BigInt
    CASE 'ConvertInt2BigIntButtonS3' : {
      IF ( $FieldInt2BigInt->WpCaptionInt <> 0  ) {
        $ConvertInt2BigIntZielField->WpCaptionBigInt       #  $FieldInt2BigInt->WpCaptionInt;
        $FieldInt2BigInt->WpCaptionInt                     # 0;
      } ELSE {
        $FieldInt2BigInt->WpCaptionInt                     #  $ConvertInt2BigIntZielField->WpCaptionBigInt ;
        $ConvertInt2BigIntZielField->WpCaptionBigInt       # 0\b;
      }

    } // ConvertBigInt2BigIntButtonS3
    CASE 'ConvertBigInt2BigIntButtonS3' : {
      IF ( $FieldBigInt2BigInt->WpCaptionBigInt <> 0\b ) {
        $ConvertBigIng2BigIntZielField->WpCaptionBigInt     #  $FieldBigInt2BigInt->WpCaptionBigInt ;

        $FieldBigInt2BigInt->WpCaptionBigInt                # 0\b;
      } ELSE {
        $FieldBigInt2BigInt->WpCaptionBigInt                #  $ConvertBigIng2BigIntZielField->WpCaptionBigInt ;
        $ConvertBigIng2BigIntZielField->WpCaptionBigInt     # 0\b;
      }

     } // ConvertFloat2BigIntButtonS3
    CASE 'ConvertFloat2BigIntButtonS3' : {

      IF ( $FieldFloat2BigInt->WpCaptionFloat <>  0.0 ) {
        $ConvertFloat2BigIntZielField->WpCaptionBigInt      # CnvBF( $FieldFloat2BigInt->WpCaptionFloat );
        $FieldFloat2BigInt->WpCaptionFloat                  # 0.0;
      } ELSE {
        $FieldFloat2BigInt->WpCaptionFloat                  # CnvFB( $ConvertFloat2BigIntZielField->WpCaptionBigInt );
        $ConvertFloat2BigIntZielField->WpCaptionBigInt      # 0\b;
      }

    } // ConvertDecimal2BigIntButtonS3
    CASE 'ConvertDecimal2BigIntButtonS3' : {
      IF ( $FieldDecimal2BigInt->WpCaptionDecimal <>  0\m ) {
        $ConvertDecimal2BigIntZielField->WpCaptionBigInt      # CnvBM( $FieldDecimal2BigInt->WpCaptionDecimal );
        $FieldDecimal2BigInt->WpCaptionDecimal                # 0\m;
      } ELSE {
        $FieldDecimal2BigInt->WpCaptionDecimal                # CnvMB( $ConvertDecimal2BigIntZielField->WpCaptionBigInt );
        $ConvertDecimal2BigIntZielField->WpCaptionBigInt      # 0;
      }

    } // ConvertTime2BigIntButtonS3
    CASE 'ConvertTime2BigIntButtonS3' : {
      IF ( $ConvertTime2BigIntZielField->WpCaptionBigInt <>  0\b ) {
        $FieldTime2BigInt->WpCaptionTime                      # CnvTB( $ConvertTime2BigIntZielField->WpCaptionBigInt, true );
        $ConvertTime2BigIntZielField->WpCaptionBigInt         # 0\b;
      } ELSE {
        $ConvertTime2BigIntZielField->WpCaptionBigInt         # CnvBT( $FieldTime2BigInt->WpCaptionTime );
        $FieldTime2BigInt->WpCaptionTime                      # 00:00:00;
      }


    } // ConvertDatel2BigIntButtonS3
    CASE 'ConvertDatel2BigIntButtonS3' : {

      IF ( $FieldDate2BigInt->WpCaptionDate <>  0.0.0 ) {
        $ConvertDate2BigIntZielField->WpCaptionBigInt        # CnvBD( $FieldDate2BigInt->WpCaptionDate );
        $FieldDate2BigInt->WpCaptionDate                     # 0.0.0;
      } ELSE {
        $FieldDate2BigInt->WpCaptionDate                     # CnvDB( $ConvertDate2BigIntZielField->WpCaptionBigInt, true );
      }
    }
  } // SWITCH
} // EvtClickedButton

//----------------------------------------------------------------------------
//  FLOAT
//----------------------------------------------------------------------------
sub EvtClickedButtonPage4
(
  aEvt                  : event;        // Ereignis
)
: logic;
Local {
  tObj : Int ; tCaption : Alpha ; tObjName : Alpha ;
  tTestAlpha : Alpha ; tTestInt : Int ; tTestBigInt : BigInt ; tTestFloat : Float ;
  tTestDecimal : Decimal ; tTestTime : time ; tTestDate : Date ;
}{
  tObj      # aEvt:Obj;
  tCaption  # tObj->WpCaption;
  tObjName  # tObj->WpName;
  SWITCH ( tObjName ) { // ConvAlpha2Float
    CASE 'ConvertAlpha2FloatButtonS4' : {
      IF ( $FieldAlpha2Float->WpCaption <> '' ) {
        $ConvertAlpha2FloatZielFieldS4->WpCaptionFloat  # CnvFA( $FieldAlpha2Float->WpCaption );
        $FieldAlpha2Float->WpCaption                    # '';
      } ELSE {
        $FieldAlpha2Float->WpCaption                    # CnvAF( $ConvertAlpha2FloatZielFieldS4->WpCaptionFloat );
        $ConvertAlpha2FloatZielFieldS4->WpCaptionFloat  # 0\f;
      }

    } // ConvInt2Float
    CASE 'ConvertInt2FloatButtonS4' : {
      IF ( $FieldInt2Float->WpCaptionInt <> 0 ) {
        $ConvertInt2FloatZielFieldS4->WpCaptionFloat   #  CnvFI( $FieldInt2Float->WpCaptionInt );
        $FieldInt2Float->WpCaptionInt                  # 0;
      } ELSE {
        $FieldInt2Float->WpCaptionInt                  #  CnvIF ($ConvertInt2FloatZielFieldS4->WpCaptionFloat ) ;
        $ConvertInt2FloatZielFieldS4->WpCaptionFloat   # 0\f;
      }

    } // ConvertBigInt2Float
    CASE 'ConvertBigInt2FloatButtonS4' : {
      IF ( $FieldBigInt2Float->WpCaptionBigInt <> 0\b ) {
        $ConvertBigIng2FloatZielFieldS4->WpCaptionFloat    # CnvFB( $FieldBigInt2Float->WpCaptionBigInt );

        $FieldBigInt2Float->WpCaptionBigInt                # 0;
      } ELSE {
        $FieldBigInt2Float->WpCaptionBigInt                #  CnvBF( $ConvertBigIng2FloatZielFieldS4->WpCaptionFloat ) ;
        $ConvertBigIng2FloatZielFieldS4->WpCaptionFloat    # 0\f;
      }

     } // ConvertFloat2Float
    CASE 'ConvertFloat2FloatButtonS4' : {

      IF ( $FieldFloat2Float->WpCaptionFloat <>  0.0\f ) {
        $ConvertFloat2FloatZielFieldS4->WpCaptionFloat      # $FieldFloat2Float->WpCaptionFloat ;
        $FieldFloat2Float->WpCaptionFloat                   # 0.0;
      } ELSE {
        $FieldFloat2Float->WpCaptionFloat                   # $ConvertFloat2FloatZielFieldS4->WpCaptionFloat ;
        $ConvertFloat2FloatZielFieldS4->WpCaptionFloat      # 0\f;
      }

    } // ConvertDecimal2Float
    CASE 'ConvertDecimal2FloatButtonS4' : {
      IF ( $FieldDecimal2Float->WpCaptionDecimal <>  0.0\m ) {
        $ConvertDecimal2FloatZielFieldS4->WpCaptionFloat      # CnvFM( $FieldDecimal2Float->WpCaptionDecimal );
        $FieldDecimal2Float->WpCaptionDecimal                 # 0.0\m;
      } ELSE {
        $FieldDecimal2Float->WpCaptionDecimal                 # CnvMF( $ConvertDecimal2FloatZielFieldS4->WpCaptionFloat );
        $ConvertDecimal2FloatZielFieldS4->WpCaptionFloat      # 0.0\f;
      }

    } // ConvertTime2Float
      CASE 'ConvertTime2FloatButtonS4' : {
      IF ( $FieldTime2Float->WpCaptionTime  <> 00:00:00 ) {
         $ConvertTime2FloatZielFieldS4->wpCaption           # 'Ungültige Parameter';
      }

    }
 // ConvertDate2Float
       CASE 'ConvertDatel2FloatButtonS4' : {
        IF ( $FieldDate2Float->wpCaptionDate <> 0.0.0 ){
        $ConvertDate2FloatZielFieldS4->WpCaption         # 'Ungültige Parameter';
      }
    }
  } // SWITCH
} // EvtClickedButton

//----------------------------------------------------------------------------
//  DECIMAL
//----------------------------------------------------------------------------
sub EvtClickedButtonPage5
(
  aEvt                  : event;        // Ereignis
)
: logic;
Local {
  tObj : Int ; tCaption : Alpha ; tObjName : Alpha ;
  tTestAlpha : Alpha ; tTestInt : Int ; tTestBigInt : BigInt ; tTestFloat : Float ;
  tTestDecimal : Decimal ; tTestTime : time ; tTestDate : Date ;
}{
  tObj      # aEvt:Obj;
  tCaption  # tObj->WpCaption;
  tObjName  # tObj->WpName;
  SWITCH ( tObjName ) { // ConvAlpha2Decimal
    CASE 'ConvertAlpha2DecimalButtonS5' : {
      IF ( $FieldAlpha2Decimal->WpCaption <> '' ) {
        $ConvertAlpha2DecimalZielFieldS5->WpCaptionDecimal  # CnvMA( $FieldAlpha2Decimal->WpCaption );
        $FieldAlpha2Decimal->WpCaption                      # '';
      } ELSE {
        $FieldAlpha2Decimal->WpCaption                      # CnvAM( $ConvertAlpha2DecimalZielFieldS5->WpCaptionDecimal );
        $ConvertAlpha2DecimalZielFieldS5->WpCaptionDecimal  # 0.0\m;
      }

    } // ConvInt2Decimal
    CASE 'ConvertInt2DecimalButtonS5' : {
      IF ( $FieldInt2Decimal->WpCaptionInt <> 0 ) {
        $ConvertInt2DecimalZielFieldS5->WpCaptionDecimal   #  CnvMI ($FieldInt2Decimal->WpCaptionInt ) ;
        $FieldInt2Decimal->WpCaptionInt                    # 0;
      } ELSE {
        $FieldInt2Decimal->WpCaptionInt                    #  CnvIM ($ConvertInt2DecimalZielFieldS5->WpCaptionDecimal ) ;
        $ConvertInt2DecimalZielFieldS5->WpCaptionDecimal   # 0.0\m;
      }

    } // ConvertBigInt2Decimal
    CASE 'ConvertBigInt2DecimalButtonS5' : {
      IF ( $FieldBigInt2Decimal->WpCaptionBigInt <> 0\b ) {
        $ConvertBigIng2DecimalZielFieldS5->WpCaptionDecimal     # CnvMB( $FieldBigInt2Decimal->WpCaptionBigInt );
        $FieldBigInt2Decimal->WpCaptionBigInt                   # 0;
      } ELSE {
        $FieldBigInt2Decimal->WpCaptionBigInt                   #  CnvBM( $ConvertBigIng2DecimalZielFieldS5->WpCaptionDecimal ) ;
        $ConvertBigIng2DecimalZielFieldS5->WpCaptionDecimal     # 0.0\m;
      }

     } // ConvertFloat2Decimal
    CASE 'ConvertFloat2DecimalButtonS5' : {

      IF ( $FieldFloat2Decimal->WpCaptionFloat <>  0.0\f ) {
        $ConvertFloat2DecimalZielFieldS5->WpCaptionDecimal      # CnvMF( $FieldFloat2Decimal->WpCaptionFloat ) ;
        $FieldFloat2Decimal->WpCaptionFloat                     # 0.0;
      } ELSE {
        $FieldFloat2Decimal->WpCaptionFloat                     # CnvFM( $ConvertFloat2DecimalZielFieldS5->WpCaptionDecimal ) ;
        $ConvertFloat2DecimalZielFieldS5->WpCaptionDecimal      # 0\m;
      }

    } // ConvertDecimal2Decimal
    CASE 'ConvertDecimal2DecimalButtonS5' : {
      IF ( $FieldDecimal2Decimal->WpCaptionDecimal <>  0.0\m ) {
        $ConvertDecimal2DecimalZielFieldS5->WpCaptionDecimal      # $FieldDecimal2Decimal->WpCaptionDecimal ;
        $FieldDecimal2Decimal->WpCaptionDecimal                   # 0.0\m;
      } ELSE {
        $FieldDecimal2Decimal->WpCaptionDecimal                   # $ConvertDecimal2DecimalZielFieldS5->WpCaptionDecimal ;
        $ConvertDecimal2DecimalZielFieldS5->WpCaptionDecimal      # 0.0\m;
      }

    } // ConvertTime2Decimal
    CASE 'ConvertTime2DecimalButtonS5' : {
      IF ( $FieldTime2Decimal->WpCaptionTime  <> 00:00:00 ) {
         $ConvertTime2DecimalZielFieldS5->wpCaption           # 'Ungültige Parameter';
      }

    }
    // ConvertDate2Decimal
    CASE 'ConvertDatel2DecimalButtonS5' : {
      IF ( $FieldDate2Decimal->wpCaptionDate <> 0.0.0 ){
          $ConvertDate2DecimalZielFieldS5->WpCaption  # 'Ungültige Parameter';
      }
    }
  } // SWITCH
} // EvtClickedButton

//----------------------------------------------------------------------------
// TIME
//----------------------------------------------------------------------------
sub EvtClickedButtonPage6
(
  aEvt                  : event;        // Ereignis
)
: logic;
Local {
  tObj : Int ; tCaption : Alpha ; tObjName : Alpha ;
  tTestAlpha : Alpha ; tTestInt : Int ; tTestBigInt : BigInt ; tTestFloat : Float ;
  tTestDecimal : Decimal ; tTestTime : time ; tTestDate : Date ;
}{
  tObj      # aEvt:Obj;
  tCaption  # tObj->WpCaption;
  tObjName  # tObj->WpName;
  SWITCH ( tObjName ) { // ConvAlpha2Time
    CASE 'ConvertAlpha2TimeButtonS6' : {
      IF ( $FieldAlpha2Time->WpCaption <> '' ) {
        $ConvertAlpha2TimelZielFieldS6->WpCaptionTime  # CnvTA( $FieldAlpha2Time->WpCaption );
        $FieldAlpha2Time->WpCaption                    # '';
      } ELSE {
        $FieldAlpha2Time->WpCaption                    # CnvAT( $ConvertAlpha2TimelZielFieldS6->WpCaptionTime );
        $ConvertAlpha2TimelZielFieldS6->WpCaptionTime  # 0:0:0;
      }

    } // ConvInt2Time
    CASE 'ConvertInt2TimeButtonS6' : {
      IF ( $FieldInt2Time->WpCaptionInt <> 0 ) {
        $ConvertInt2TimelZielFieldS6->WpCaptionTime     #  CnvTI ( $FieldInt2Time->WpCaptionInt ) ;
        $FieldInt2Time->WpCaptionInt                    # 0;
      } ELSE {
        $FieldInt2Time->WpCaptionInt                    #  CnvIT ( $ConvertInt2TimelZielFieldS6->WpCaptionTime ) ;
        $ConvertInt2TimelZielFieldS6->WpCaptionTime     # 0:0:0;
      }

    } // ConvertBigInt2Time
    CASE 'ConvertBigInt2TimeButtonS6' : {
      IF ( $FieldBigInt2Time->WpCaptionBigInt <> 0\b ) {
        $ConvertBigIng2TimelZielFieldS6->WpCaptionTime     # CnvTB( $FieldBigInt2Time->WpCaptionBigInt, False );
        $FieldBigInt2Time->WpCaptionBigInt                 # 0;
      } ELSE {
        $FieldBigInt2Time->WpCaptionBigInt                 #  CnvBT( $ConvertBigIng2TimelZielFieldS6->WpCaptionTime ) ;
        $ConvertBigIng2TimelZielFieldS6->WpCaptionTime     # 0:0:0;
     }

    } // ConvertFloat2Time
    CASE 'ConvertFloat2TimeButtonS6' : {
      IF ( $FieldFloat2Time->wpCaptionFloat  <> 0.0\f ) {
         $ConvertFloat2TimelZielFieldS6->wpCaption       # 'Ungültige Parameter';

      }
    } // ConvertDecimal2Time
    CASE 'ConvertDecimal2TimeButtonS6' : {
      IF ( $FieldDecimal2Time->wpCaptionDecimal  <> 0\m) {
          $ConvertDecimal2TimelZielFieldS6->WpCaption     # 'Ungültige Parameter';
      }

    } // ConvertTime2Time
    CASE 'ConvertTime2TimeButtonS6' : {
      IF ( $FieldTime2Time->WpCaptionTime <> 0:0:0) {
        $ConvertTime2TimelZielFieldS6->WpCaptionTime     # $FieldTime2Time->WpCaptionTime  ;
        $FieldTime2Time->wpCaptionTime                   # 0:0:0;
      } ELSE {
        $FieldTime2Time->WpCaptionTime                   # $ConvertTime2TimelZielFieldS6->WpCaptionTime ;
        $ConvertTime2TimelZielFieldS6->WpCaptionTime     # 0:0:0;
    }
  }
 // ConvertDate2Time
   CASE 'ConvertDatel2TimeButtonS6' : {
     IF ( $FieldDate2Time->wpCaptionDate <> 0.0.0 ){
          $ConvertDate2TimelZielFieldS6->WpCaption    # 'Ungültige Parameter';
      }
    }
  } // SWITCH
} // EvtClickedButton
//----------------------------------------------------------------------------
// DATE
//----------------------------------------------------------------------------
sub EvtClickedButtonPage7
(
  aEvt                  : event;        // Ereignis
)
: logic;
Local {
  tObj : Int ; tCaption : Alpha ; tObjName : Alpha ;
  tTestAlpha : Alpha ; tTestInt : Int ; tTestBigInt : BigInt ; tTestFloat : Float ;
  tTestDecimal : Decimal ; tTestTime : time ; tTestDate : Date ;
}{
  tObj      # aEvt:Obj;
  tCaption  # tObj->WpCaption;
  tObjName  # tObj->WpName;
  SWITCH ( tObjName ) { // ConvAlpha2Date
    CASE 'ConvertAlpha2DateButtonS7' : {
      IF ( $FieldAlpha2Date->WpCaption  <> ''  ) {
        $ConvertAlpha2DatelZielFieldS7->WpCaptionDate       # CnvDA( $FieldAlpha2Date->WpCaption );
        $FieldAlpha2Date->WpCaption                         # '';
      } ELSE {
        $FieldAlpha2Date->WpCaption                         # CnvAD( $ConvertAlpha2DatelZielFieldS7->WpCaptionDate );
        $ConvertAlpha2DatelZielFieldS7->WpCaptionDate       # 0.0.0;
      }

    }// ConvInt2Date
    CASE 'ConvertInt2DateButtonS7' : {
      IF ( $FieldInt2Date->WpCaptionInt <> 0 ) {
        $ConvertInt2DatelZielFieldS7->WpCaptionDate     # CnvDI( $FieldInt2Date->WpCaptionInt ) ;
        $FieldInt2Date->WpCaptionInt                    # 0;
      } ELSE {
        $FieldInt2Date->WpCaptionInt                    # CnvID( $ConvertInt2DatelZielFieldS7->WpCaptionDate ) ;
        $ConvertInt2DatelZielFieldS7->WpCaptionDate     # 0.0.0;
      }

    } // ConvertBigInt2Date
    CASE 'ConvertBigInt2DateButtonS7' : {
    //tTestDate # $ConvertBigIng2DatelZielFieldS7->WpCaptionDate ;
      IF ( $FieldBigInt2Date->WpCaptionBigInt <> 0 ) {
        $ConvertBigIng2DatelZielFieldS7->WpCaptionDate     # CnvDB( $FieldBigInt2Date->WpCaptionBigInt, true ) ;
        $FieldBigInt2Date->WpCaptionBigInt                 # 0;
      } ELSE {
        $FieldBigInt2Date->WpCaptionBigInt                 # CnvBD( $ConvertBigIng2DatelZielFieldS7->WpCaptionDate ) ;
        $ConvertBigIng2DatelZielFieldS7->WpCaptionDate     # 0.0.0;
      }

    } // ConvertFloat2Date
    CASE 'ConvertFloat2DateButtonS7' : {
      IF ( $FieldFloat2Date->wpCaptionFloat  <> 0.0\f ) {
         $ConvertFloat2DatelZielFieldS7->wpCaption        # 'Ungültige Parameter';
      }

    } // ConvertDecimal2Date
    CASE 'ConvertDecimal2DateButtonS7' : {
      IF ( $FieldDecimal2Date->wpCaptionDecimal  <> 0.0\m) {
          $ConvertDecimal2DatelZielFieldS7->WpCaption     # 'Ungültige Parameter';
      }

    } // ConvertTime2Date
    CASE 'ConvertTime2DateButtonS7' : {
    IF ( $FieldTime2Date->wpCaptionTime <> 0:0:0){
      $ConvertTime2DatelZielFieldS7->wpCaption            # 'Ungültige Parameter';
    }

  }// ConvertDate2Date
    CASE 'ConvertDatel2DateButtonS7' : {
    IF ( $FieldDate2Date->wpCaptionDate <> 0.0.0 ) {
      $ConvertDate2DatelZielFieldS7->WpCaptionDate     # $FieldDate2Date->wpCaptionDate;
      $FieldDate2Date->WpCaptionDate                   # 0.0.0;
    } ELSE {
      $FieldDate2Date->wpCaptionDate                   # $ConvertDate2DatelZielFieldS7->WpCaptionDate;
      $ConvertDate2DatelZielFieldS7->WpCaptionDate     # 0.0.0;
      }
    }


  } // SWITCH
} // EvtClickedButton

//------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------
// EvtClickedCheckbox (ALPHA)   1 o 0
//------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------

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
 } // EvtClickedCheckbox


 //------------------------------------------------------------------------------------
 // EvtClickedCheckbox (INT)
 //------------------------------------------------------------------------------------
 sub EvtClickedCheckbox13
(aEvt :event;)// ConvertDate 1 o 0/
   : logic;
   {
   IF ($Checkbox13->wpCheckState =_WinStateChkChecked){
      $ConvertCheckBoxEins2NullZielFieldS2 ->  WpCaption     # '1';
      }Else{
      $ConvertCheckBoxEins2NullZielFieldS2 ->  WpCaption     # '0';

   }
   return(true);
 }


 //------------------------------------------------------------------------------------
 // EvtClickedCheckbox (BIGINT)
 //------------------------------------------------------------------------------------
 sub EvtClickedCheckbox14
(aEvt :event;)// ConvertDate 1 o 0/
   : logic;
   {
   IF ($Checkbox14->wpCheckState =_WinStateChkChecked){
      $ConvertCheckBoxEins2NullZielFieldS3 ->  WpCaption     # '1';
      }Else{
      $ConvertCheckBoxEins2NullZielFieldS3 ->  WpCaption     # '0';

   }
   return(true);
 }

 //------------------------------------------------------------------------------------
 // EvtClickedCheckbox (FLOAT)
 //------------------------------------------------------------------------------------
 sub EvtClickedCheckbox15
(aEvt :event;)// ConvertDate 1 o 0/
   : logic;
   {
   IF ($Checkbox15->wpCheckState =_WinStateChkChecked){
      $ConvertCheckBoxEins2NullZielFieldS4 ->  WpCaption     # '1';
      }Else{
      $ConvertCheckBoxEins2NullZielFieldS4 ->  WpCaption     # '0';

   }
   return(true);
 }

 //------------------------------------------------------------------------------------
 // EvtClickedCheckbox (DECIMAL)
 //------------------------------------------------------------------------------------
 sub EvtClickedCheckboxS5
(aEvt :event;)// ConvertDate 1 o 0/
   : logic;
   {
   IF ($Checkbox16->wpCheckState =_WinStateChkChecked){
      $ConvertCheckBoxEins2NullZielFieldS5 ->  WpCaption     # '1';
      }Else{
      $ConvertCheckBoxEins2NullZielFieldS5 ->  WpCaption     # '0';

   }
   return(true);
 }

 //------------------------------------------------------------------------------------
 // EvtClickedCheckbox (TIME)
 //------------------------------------------------------------------------------------
 sub EvtClickedCheckboxS6
(aEvt :event;)// ConvertDate 1 o 0/
   : logic;
   {
   IF ($Checkbox17->wpCheckState =_WinStateChkChecked){
      $ConvertCheckBoxEins2NullZielFieldS6 ->  WpCaption     # '1';
      }Else{
      $ConvertCheckBoxEins2NullZielFieldS6 ->  WpCaption     # '0';

   }
   return(true);
 }

 //------------------------------------------------------------------------------------
 // EvtClickedCheckbox (DATE)
 //------------------------------------------------------------------------------------
 sub EvtClickedCheckboxS7
(aEvt :event;)// ConvertDate 1 o 0/
   : logic;
   {
   IF ($Checkbox18->wpCheckState =_WinStateChkChecked){
      $ConvertCheckBoxEins2NullZielFieldS7 ->  WpCaption     # '1';
      }Else{
      $ConvertCheckBoxEins2NullZielFieldS7 ->  WpCaption     # '0';

   }
   return(true);
 }


 //------------------------------------------------------------------------------------
 //------------------------------------------------------------------------------------
 // EvtClicked (ALPHA)  True to False
 //------------------------------------------------------------------------------------
 //------------------------------------------------------------------------------------

/*  Das Code-Snippet definiert ein Ereignis (EvtClickedButton12), das ausgelöst wird,
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

  //------------------------------------------------------------------------------------
  // EvtClicked (INT)
  //------------------------------------------------------------------------------------
 sub EvtClickedButtonS2 //ConvertDate True to False /
    (
      aEvt        :event;   // Ereignis
     )
   : logic;
   {
   IF ($RadiobuttonOnS2->wpCheckState = _winStateChkChecked){
      $ConvertCheckBoxTrue2FalseZielFieldS2 ->  WpCaption     # 'True';
      }Else{
      $ConvertCheckBoxTrue2FalseZielFieldS2 ->  WpCaption     # 'False';
   }
   }

  //------------------------------------------------------------------------------------
  // EvtClicked (BIGINT)
  //------------------------------------------------------------------------------------
 sub EvtClickedButtonS3 //ConvertDate True to False /
    (
      aEvt        :event;   // Ereignis
     )
   : logic;
   {
   IF ($RadiobuttonOnS3->wpCheckState = _winStateChkChecked){
      $ConvertCheckBoxTrue2FalseZielFieldS3 ->  WpCaption     # 'True';
      }Else{
      $ConvertCheckBoxTrue2FalseZielFieldS3 ->  WpCaption     # 'False';
   }
   }
  //------------------------------------------------------------------------------------
  // EvtClicked (FLOAT)
  //------------------------------------------------------------------------------------
 sub EvtClickedButtonS4 //ConvertDate True to False /
    (
      aEvt        :event;   // Ereignis
     )
   : logic;
   {
   IF ($RadiobuttonOnS4->wpCheckState = _winStateChkChecked){
      $ConvertCheckBoxTrue2FalseZielFieldS4 ->  WpCaption     # 'True';
      }Else{
      $ConvertCheckBoxTrue2FalseZielFieldS4 ->  WpCaption     # 'False';
   }
   }
  //------------------------------------------------------------------------------------
  // EvtClicked (DECIMAL)
  //------------------------------------------------------------------------------------
 sub EvtClickedButtonS5 //ConvertDate True to False /
    (
      aEvt        :event;   // Ereignis
     )
   : logic;
   {
   IF ($RadiobuttonOnS5->wpCheckState = _winStateChkChecked){
      $ConvertCheckBoxTrue2FalseZielFieldS5 ->  WpCaption     # 'True';
      }Else{
      $ConvertCheckBoxTrue2FalseZielFieldS5 ->  WpCaption     # 'False';
   }
   }
 //------------------------------------------------------------------------------------
 // EvtClicked (TIME)
 //------------------------------------------------------------------------------------
 sub EvtClickedButtonS6 //ConvertDate True to False /
    (
      aEvt        :event;   // Ereignis
     )
   : logic;
   {
   IF ($RadiobuttonOnS6->wpCheckState = _winStateChkChecked){
      $ConvertCheckBoxTrue2FalseZielFieldS6 ->  WpCaption     # 'True';
      }Else{
      $ConvertCheckBoxTrue2FalseZielFieldS6 ->  WpCaption     # 'False';
   }
   }
 //------------------------------------------------------------------------------------
 // EvtClicked (TIME)
 //------------------------------------------------------------------------------------
 sub EvtClickedButtonS7 //ConvertDate True to False /
    (
      aEvt        :event;   // Ereignis
     )
   : logic;
   {
   IF ($RadiobuttonOnS7->wpCheckState = _winStateChkChecked){
      $ConvertCheckBoxTrue2FalseZielFieldS7 ->  WpCaption     # 'True';
      }Else{
      $ConvertCheckBoxTrue2FalseZielFieldS7 ->  WpCaption     # 'False';
   }


  return(true);
} // EvtClicked

 /* Main ----------------------------------------------------------------*/
Main()
Local { This : Int ; }{
  This # WinOpen( 'Konvertierung', _WinOpenDialog );
  IF ( This > 0 ) {
    WinDialogRun( This );
    WinClose( This );
  }
}



```
