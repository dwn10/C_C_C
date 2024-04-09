def suma(a, b):
  return a + b

def resta(a, b):
  return a - b

def multiplicacion(a, b):
  return a * b

def division(a, b):
  if b == 0:
    return "No se puede dividir por 0"
  else:
    return a / b

def porcentaje(a, b):
  return (a / 100) * b

def salir():
  print("¡Hasta la próxima!")
  exit()

while True:
  print("\n**Calculadora básica**")
  print("+. Suma")
  print("-. Resta")
  print("*. Multiplicación")
  print("/. División")
  print("%. Porcentaje")
  print("s. Salir\n")

  opcion = input("Elige una opción: ")

  if opcion == "+":
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))
    resultado = suma(a, b)
    print(f"El resultado de la suma es: {resultado}")
    print("**********************************")
  elif opcion == "-":
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))
    resultado = resta(a, b)
    print(f"El resultado de la resta es: {resultado}")
    print("**********************************")

  elif opcion == "*":
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))
    resultado = multiplicacion(a, b)
    print(f"El resultado de la multiplicación es: {resultado}")
    print("**********************************")

  elif opcion == "/":
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))
    resultado = division(a, b)
    print(f"El resultado de la división es: {resultado}")
    print("**********************************")

  elif opcion == "%":
    a = float(input("Introduce el número: "))
    b = float(input("Introduce el porcentaje: "))
    resultado = porcentaje(a, b)
    print(f"El resultado del porcentaje es: {resultado}")
    print("**********************************")

  elif opcion == "s":
    salir()

  else:
    print("Opción no válida. Inténtalo de nuevo.")

""" El código proporcionado es una calculadora básica en Python que ofrece las siguientes operaciones:

Suma
Resta
Multiplicación
División
Cálculo de porcentaje
El código también incluye una función para salir del programa.

Las funciones de la calculadora son:

suma(a, b): Suma dos números y devuelve el resultado.
resta(a, b): Resta dos números y devuelve el resultado.
multiplicacion(a, b): Multiplica dos números y devuelve el resultado.
division(a, b): Divide dos números y devuelve el resultado. Si el divisor es 0, la función devuelve el mensaje "No se puede dividir por 0".
porcentaje(a, b): Calcula el porcentaje de un número y devuelve el resultado.
El código funciona de la siguiente manera:

Se muestra un menú con las opciones disponibles.
El usuario elige una opción.
Si la opción es válida, se solicitan los datos necesarios para realizar la operación.
Se llama a la función correspondiente para realizar la operación.
Se muestra el resultado de la operación.
Se vuelve a mostrar el menú.  """