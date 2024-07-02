```C
// _Konvertierung
@A+
@C+


sub EvtClickedButton
(
  aEvt                  : event;        // Ereignis
)
: logic;
Local {
  tObj : Int ; tCaption : Alpha ; tObjName : Alpha ;
  tTestAlpha : Alpha ; tTestInt : Int ; tTestBigInt : BigInt ; tTestFloat : Float ;
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
    } // Conv2Alpha
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
    } // ConvertInt2AlphaButton
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

  } // SWITCH //

  return(true);
}


Main()
Local { This : Int ; }{
  This # WinOpen( 'Konvertierung', _WinOpenDialog );
  IF ( This > 0 ) {
    WinDialogRun( This );
    WinClose( This );
  }
}

```
