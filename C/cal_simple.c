#include <stdio.h>

// Función para imprimir el valor actual en la pantalla
void printPantalla(float valor)
{
    printf("%.2f\n", valor);
}

// Función para sumar dos números
float sumar(float num1, float num2)
{
    return num1 + num2;
}

// Función para restar dos números
float restar(float num1, float num2)
{
    return num1 - num2;
}

// Función para multiplicar dos números
float multiplicar(float num1, float num2)
{
    return num1 * num2;
}

// Función para dividir dos números
float dividir(float num1, float num2)
{
    if (num2 == 0)
    {
        printf("Error: división por cero.\n");
        return 0;
    }
    return num1 / num2;
}

// Función para calcular el módulo de dos números
float modulo(float num1, float num2)
{
    return (int)num1 % (int)num2;
}

// Función principal
int main()
{
    float num1, num2, resultado;
    char operacion;

    while (1)
    {
        // Imprimir el valor actual
        printPantalla(resultado);

        // Leer la operación del usuario
        printf("Introduzca la operación (+, -, *, /, %%): ");
        scanf(" %c", &operacion);

        // Leer el primer número
        printf("Introduzca el primer número: ");
        scanf("%f", &num1);

        // Leer el segundo número
        if (operacion != 'A' && operacion != 'C')
        {
            printf("Introduzca el segundo número: ");
            scanf("%f", &num2);
        }

        // Realizar la operación según el caracter introducido
        switch (operacion)
        {
        case '+':
            resultado = sumar(num1, num2);
            break;
        case '-':
            resultado = restar(num1, num2);
            break;
        case '*':
            resultado = multiplicar(num1, num2);
            break;
        case '/':
            resultado = dividir(num1, num2);
            break;
        case '%':
            resultado = modulo(num1, num2);
            break;
        case 'A':
            // Salir del programa
            return 0;
        default:
            printf("Operación no válida.\n");
        }
    }

    return 0;
}