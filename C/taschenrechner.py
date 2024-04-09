def summe(a, b):
  return a + b

def differenz(a, b):
  return a - b

def multiplikation(a, b):
  return a * b

def division(a, b):
  if b == 0:
    return "Keine Division durch 0 möglich"
  else:
    return a / b

def prozent(a, b):
  return (a / 100) * b

def beenden():
  print("¡Hasta la próxima!")
  exit()

while True:
  print("\n**Grundrechner**")
  print("+. Addition")
  print("-. Subtraktion")
  print("*. Multiplikation")
  print("/. Division")
  print("%. Prozent")
  print("b. Beenden\n")

  option = input("Wähle eine Option: ")

  if option == "+":
    a = float(input("Gib die erste Zahl ein: "))
    b = float(input("Gib die zweite Zahl ein: "))
    ergebnis = summe(a, b)
    print(f"Das Ergebnis der Addition ist: {ergebnis}")
    print("**********************************")
  elif option == "-":
    a = float(input("Gib die erste Zahl ein: "))
    b = float(input("Gib die zweite Zahl ein: "))
    ergebnis = differenz(a, b)
    print(f"Das Ergebnis der Subtraktion ist: {ergebnis}")
    print("**********************************")

  elif option == "*":
    a = float(input("Gib die erste Zahl ein: "))
    b = float(input("Gib die zweite Zahl ein: "))
    ergebnis = multiplikation(a, b)
    print(f"Das Ergebnis der Multiplikation ist: {ergebnis}")
    print("**********************************")

  elif option == "/":
    a = float(input("Gib die erste Zahl ein: "))
    b = float(input("Gib die zweite Zahl ein: "))
    ergebnis = division(a, b)
    print(f"Das Ergebnis der Division ist: {ergebnis}")
    print("**********************************")

  elif option == "%":
    a = float(input("Gib die Zahl ein: "))
    b = float(input("Gib den Prozentsatz ein: "))
    ergebnis = prozent(a, b)
    print(f"Das Ergebnis des Prozentsatzes ist: {ergebnis}")
    print("**********************************")

  elif option == "b":
    beenden()

  else:
    print("Ungültige Option. Bitte versuche es erneut.")