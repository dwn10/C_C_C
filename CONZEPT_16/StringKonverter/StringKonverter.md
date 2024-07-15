```C
// _StringCnv

@A+
@C+

//*-----------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------
//   ## ##    ## ##   ###  ##  ### ##   ### ###  ### ##   #### ##              ##     ## ###
//  ##   ##  ##   ##    ## ##  ##  ##    ##  ##   ##  ##  # ## ##             ###    ##   ##
//  ##       ##   ##   # ## #     ##     ##       ##  ##    ##                 ##    ##
//  ##       ##   ##   ## ##     ##      ## ##    ##  ##    ##                 ##    ## ###
//  ##       ##   ##   ##  ##   ##       ##       ## ##     ##                 ##    ##   ##
//  ##   ##  ##   ##   ##  ##  ##  ##    ##  ##   ##        ##                 ##    ##   ##
//   ## ##    ## ##   ###  ##  # ####   ### ###  ####      ####               ####    ## ##
//-------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------*//

//----------------------------------------------------------------------------
//  StrToOEM
//----------------------------------------------------------------------------
sub EvtClicked
(
  aEvt                  : event;        // Ereignis
)
: logic;
local {
    tobj : Int ; tCaption : Alpha ; tObjName : Alpha ;
}
{


  tobj      # aEvt:Obj;        // (i)  Convert	FieldAlpha1 + Button  Convert	ZielFieldToOEM
  tCaption  # tObj->wpcaption;
  tObjName  # tObj->wpName;
  SWITCH ( tObjName ) {
    CASE 'StrToOEMButton' : { // Konvertiert das Feld FieldAlpha1 in OEM-Codierung und zeigt das Ergebnis in ZielFieldToOEM an
      IF ( $FieldAlpha1->wpCaption <> '' ) {
        $ZielFieldToOEM->wpCaption                    # StrCnv($FieldAlpha1->wpCaption , _StrToOEM);
        $FieldAlpha1->wpCaption                       # '';
      }
    }
    CASE 'StrToANSIButton' : {
      IF ( $FieldAlpha2->wpCaption <> '' ) {
        $ZielFieldToANSI->wpCaption                   # StrCnv($FieldAlpha2->wpCaption , _StrToANSI);
        $FieldAlpha2->wpCaption                       # '';
      }
    }
    CASE 'StrToHTMLButton' : {
      IF ( $FieldAlpha3->wpCaption <> '' ) {
        $ZielFieldToHTML->wpCaption                   # StrCnv($FieldAlpha3->wpCaption , _StrToHTML);
        $FieldAlpha3->wpCaption                       # '';
      }
    }
    CASE 'StrToOEMButton' : {
      IF ( $FieldAlpha4->wpCaption <> '' ) {
        $ZielFieldToURI->wpCaption                    # StrCnv($FieldAlpha4->wpCaption , _StrToURI);
        $FieldAlpha4->wpCaption                       # '';
      }
    }
    CASE 'StrToUTF8Button' : {
      IF ( $FieldAlpha5->wpCaption <> '' ) {
        $ZielFieldToUTF8->wpCaption                    # StrCnv($FieldAlpha5->wpCaption , _StrToUTF8);
        $FieldAlpha5->wpCaption                        # '';
      }
    }
    CASE 'StrToBase64Button' : {
      IF ( $FieldAlpha6->wpCaption <> '' ) {
        $ZielFieldToBase64->wpCaption                  # StrCnv($FieldAlpha6->wpCaption , _StrToBase64);
        $FieldAlpha6->wpCaption                        # '';
      }
    }
    CASE 'StrFromOEMButton' : {
      IF ( $FieldAlpha7->wpCaption <> '' ) {
        $ZielFieldFromOEM->wpCaption                   # StrCnv($FieldAlpha7->wpCaption , _StrFromOEM);
        $FieldAlpha7->wpCaption                        # '';
      }
    }
    CASE 'StrFromANSIButton' : {
      IF ( $FieldAlpha8->wpCaption <> '' ) {
        $ZielFieldFromANSI->wpCaption                  # StrCnv($FieldAlpha8->wpCaption , _StrFromANSI);
        $FieldAlpha8->wpCaption                        # '';
      }
    }
    CASE 'StrFromHTMLButton' : {
      IF ( $FieldAlpha9->wpCaption <> '' ) {
        $ZielFieldToHTML->wpCaption                    # StrCnv($FieldAlpha9->wpCaption , _StrFromHTML);
        $FieldAlpha9->wpCaption                        # '';
      }
    }
    CASE 'StrFromURIButton' : {
      IF ( $FieldAlpha10->wpCaption <> '' ) {
        $ZielFieldToURI->wpCaption                     # StrCnv($FieldAlpha10->wpCaption , _StrFromURI);
        $FieldAlpha10->wpCaption                       # '';
      }
    }
    CASE 'StrFromUTF8Button' : {
      IF ( $FieldAlpha11->wpCaption <> '' ) {
        $ZielFieldToUTF8->wpCaption                    # StrCnv($FieldAlpha11->wpCaption , _StrFromUTF8);
        $FieldAlpha11->wpCaption                       # '';
      }
    }
    CASE 'StrFromBase64Button' : {
      IF ( $FieldAlpha12->wpCaption <> '' ) {
        $ZielFieldToBase64->wpCaption                  # StrCnv($FieldAlpha12->wpCaption , _StrFromBase64);
        $FieldAlpha12->wpCaption                       # '';
      }
    }
    CASE 'StrUpperButton' : {
      IF ( $FieldAlpha13->wpCaption <> '' ) {
        $ZielFieldToUpper->wpCaption                   # StrCnv($FieldAlpha13->wpCaption , _StrUpper);
        $FieldAlpha13->wpCaption                       # '';
      }
    }
    CASE 'StrUpper1252Button' : {
      IF ( $FieldAlpha14->wpCaption <> '' ) {
        $ZielFieldToUpper1252->wpCaption               # StrCnv($FieldAlpha14->wpCaption , _StrUpper1252);
        $FieldAlpha14->wpCaption                       # '';
      }
    }
    CASE 'StrLowerButton' : {
      IF ( $FieldAlpha15->wpCaption <> '' ) {
        $ZielFieldToLower->wpCaption                   # StrCnv($FieldAlpha15->wpCaption , _StrLower);
        $FieldAlpha15->wpCaption                       # '';
      }
    }
    CASE 'StrLower1252Button' : {
      IF ( $FieldAlpha16->wpCaption <> '' ) {
        $ZielFieldToLower1252->wpCaption               # StrCnv($FieldAlpha16->wpCaption , _StrLower1252);
        $FieldAlpha16->wpCaption                       # '';
      }
    }
    CASE 'StrUmlautButton' : {
      IF ( Field$Alpha17->wpCaption <> '' ) {
        $ZielFieldToUmlaut->wpCaption                  # StrCnv($FieldAlpha17->wpCaption , _StrUmlaut);
        $FieldAlpha17->wpCaption                       # '';
      }
    }
    CASE 'StrLetterButton' : {
      IF ( $FieldAlpha18->wpCaption <> '' ) {
        $ZielFieldToLetter->wpCaption                  # StrCnv($FieldAlpha18->wpCaption , _StrLetter);
        $FieldAlpha18->wpCaption                       # '';
      }
    }
    CASE 'StrLetterExtButton' : {
      IF ( $FieldAlpha19->wpCaption <> '' ) {
        $ZielFieldToLetterExt->wpCaption               # StrCnv($FieldAlpha19->wpCaption , _StrLetterExt);
        $FieldAlpha19->wpCaption                       # '';
      }
    }
    CASE 'StrSoundex1Button' : {
      IF ( $FieldAlpha20->wpCaption <> '' ) {
        $ZielFieldToSoundex1->wpCaption                # StrCnv($FieldAlpha20->wpCaption , _StrSoundex1);
        $FieldAlpha20->wpCaption                       # '';
      }
    }
    CASE 'StrSoundex2Button' : {
      IF ( $FieldAlpha21->wpCaption <> '' ) {
        $ZielFieldSoundex2->wpCaption                  # StrCnv($FieldAlpha21->wpCaption , _StrSoundex2);
        $FieldAlpha21->wpCaption                       # '';
      }
    }
    CASE 'StrNameReorderButton' : {
      IF ( $FieldAlpha22->wpCaption <> '' ) {
        $ZielFieldNameReorder->wpCaption               # StrCnv($FieldAlpha22->wpCaption , _StrNameReorder);
        $FieldAlpha22->wpCaption                       # '';
      }
    }
    CASE 'StrNameNoFirstButton' : {
      IF ( $FieldAlpha23->wpCaption <> '' ) {
        $ZielFieldNameNoFirst->wpCaption               # StrCnv($FieldAlpha23->wpCaption ,_StrNameReorder | _StrNameNoFirst);
        $FieldAlpha23->wpCaption                       # '';
      }
    }
    CASE 'StrNameNoDoubleButton' : {
      IF ( $FieldAlpha24->wpCaption <> '' ) {
        $ZielFieldNameNoDouble->wpCaption              # StrCnv($FieldAlpha24->wpCaption ,_StrNameReorder | _StrNameNoDouble);
        $FieldAlpha24->wpCaption                       # '';
      }
    }
    }
{
  return(true);
}

}


Main()
Local { This : Int ; }{
  This # WinOpen( 'StringCnv', _WinOpenDialog );
  IF ( This > 0 ) {
    WinDialogRun( This );
    WinClose( This );
  }
}
```
