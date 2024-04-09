#include <stdio.h>

// Función para sumar dos números
float suma(float num1, float num2)
{
    return num1 + num2;
}

// Función para restar dos números
float resta(float num1, float num2)
{
    return num1 - num2;
}

// Función para multiplicar dos números
float multiplicacion(float num1, float num2)
{
    return num1 * num2;
}

// Función para dividir dos números
float division(float num1, float num2)
{
    return num1 / num2;
}

// Función para calcular el módulo de dos números
float modulo(float num1, float num2)
{
    return (int)num1 % (int)num2;
}

// Función para cambiar el signo del número
float cambioSigno(float num)
{
    return -num;
}

// Función para borrar el último dígito
float borrarUltimoDigito(float num)
{
    return (int)num / 10;
}

// Función para imprimir el resultado
void imprimirResultado(float resultado)
{
    printf("%0.2f\n", resultado);
}

// Función principal
int main()
{
    float num1, num2, resultado;
    char operacion;

    // Bucle para realizar operaciones hasta que el usuario ingrese 'S'
    while (operacion != 'S')
    {
        // Mostrar el menú de operaciones
        printf("\nSeleccione una operación:\n");
        printf("+ para sumar\n");
        printf("- para restar\n");
        printf("* para multiplicar\n");
        printf("/ para dividir\n");
        printf("%% para calcular el módulo\n");
        // printf("+/- para cambiar el signo\n");
        printf("DEL para borrar el último dígito\n");
        printf("S para salir\n");

        // Obtener la operación
        scanf(" %c", &operacion);

        // Obtener el primer número
        printf("Ingrese el primer número: ");
        scanf("%f", &num1);

        // Obtener el segundo número
        printf("Ingrese el segundo número: ");
        scanf("%f", &num2);

        // Realizar la operación seleccionada
        switch (operacion)
        {
        case '+':
            resultado = suma(num1, num2);
            break;
        case '-':
            resultado = resta(num1, num2);
            break;
        case '*':
            resultado = multiplicacion(num1, num2);
            break;
        case '/':
            if (num2 == 0)
            {
                printf("Error: División por cero.\n");
            }
            else
            {
                resultado = division(num1, num2);
            }
            break;
        case '%':
            resultado = modulo(num1, num2);
            break;
        // case '+/-':
        // resultado = cambioSigno(num1);
        // break;
        case 'D':
            resultado = borrarUltimoDigito(num1);
            break;
        case 'S':
            printf("Saliendo...\n");
            break;
        default:
            printf("Operación no válida.\n");
        }

        // Imprimir el resultado
        if (operacion != 'S' && operacion != 'D')
        {
            imprimirResultado(resultado);
        }
    }

    return 0;
}