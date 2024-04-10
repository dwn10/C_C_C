unit Main;

interface

uses
  Forms, Unit1 in 'Unit1.pas' { Add your unit here if needed };

type
  TForm1 = class(TForm)
    procedure ButtonClick(Sender: TObject);
    procedure ClearButton(Sender: TObject);
    procedure EqualsButton(Sender: TObject);
  private
    FNumber1, FNumber2: string; { Strings to store operands }
    FOperator: Char;           { Character to store operator }
    Label1: TLabel;
  public
    { Published constructor }
  end;

var
  Form1: TForm1;

implementation

{$R *.dfm}

procedure TForm1.ButtonClick(Sender: TObject);
begin
  // Get the button caption (number)
  FNumber1 := FNumber1 + (Sender as TButton).Caption;
  Label1.Caption := FNumber1; // Update displayed number
end;

procedure TForm1.ClearButton(Sender: TObject);
begin
  // Clear all stored values and displayed number
  FNumber1 := '';
  FNumber2 := '';
  FOperator := #0;  // Null character for operator
  Label1.Caption := '';
end;

procedure TForm1.EqualsButton(Sender: TObject);
var
  Result: Double;
begin
  // Convert strings to doubles for calculation
  FNumber2 := Label1.Caption; // Capture current displayed number
  case FOperator of
    '+': Result := StrToFloat(FNumber1) + StrToFloat(FNumber2);
    '-': Result := StrToFloat(FNumber1) - StrToFloat(FNumber2);
    '*': Result := StrToFloat(FNumber1) * StrToFloat(FNumber2);
    '/': Result := StrToFloat(FNumber1) / StrToFloat(FNumber2);
  end;

  // Display the result and clear stored values
  Label1.Caption := FloatToStr(Result);
  FNumber1 := '';
  FNumber2 := '';
  FOperator := #0;
end;

begin
  Application.Initialize;
  Application.CreateForm(TForm1, Form1);
  Application.Run;
end.
