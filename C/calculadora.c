#include <stdio.h>

int main()
{
    float numeroActual = 0.0;
    float resultado = 0.0;
    char operacion;

    while (1)
    {
        // Mostrar el número actual
        printf("%f\n", numeroActual);

        // Leer la entrada del usuario
        scanf(" %c", &operacion);

        // Procesar la entrada
        switch (operacion)
        {
        case '+':
            resultado = suma(numeroActual, resultado);
            break;
        case '-':
            resultado = resta(numeroActual, resultado);
            break;
        case '*':
            resultado = multiplicacion(numeroActual, resultado);
            break;
        case '/':
            resultado = division(numeroActual, resultado);
            break;
        case '%':
            resultado = modulo(numeroActual, resultado);
            break;
        case 'C':
            numeroActual = 0.0;
            resultado = 0.0;
            break;
        case 'D':
            numeroActual = borrarUltimoDigito(numeroActual);
            break;
        case '+/-':
            numeroActual = cambioSigno(numeroActual);
            break;
        case '=':
            mostrarResultado(resultado);
            break;
        }
    }

    return 0;
}

// Definición de las funciones...