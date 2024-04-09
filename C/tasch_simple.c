#include <stdio.h>

// Funktion zum Drucken des aktuellen Werts auf dem Bildschirm
void printPantalla(float wert)
{
    printf("%.2f\n", wert);
}

// Funktion zum Addieren von zwei Zahlen
float summe(float num1, float num2)
{
    return num1 + num2;
}

// Funktion zum Subtrahieren von zwei Zahlen
float differenz(float num1, float num2)
{
    return num1 - num2;
}

// Funktion zum Multiplizieren von zwei Zahlen
float produkt(float num1, float num2)
{
    return num1 * num2;
}

// Funktion zum Dividieren von zwei Zahlen
float quotient(float num1, float num2)
{
    if (num2 == 0)
    {
        printf("Fehler: Division durch Null.\n");
        return 0;
    }
    return num1 / num2;
}

// Funktion zum Berechnen des Moduls von zwei Zahlen
float modulo(float num1, float num2)
{
    return (int)num1 % (int)num2;
}

// Hauptfunktion
int main()
{
    float num1, num2, ergebnis;
    char operation;

    while (1)
    {
        // Drucken des aktuellen Werts
        printPantalla(ergebnis);

        // Einlesen der Operation vom Benutzer
        printf("Geben Sie die Operation ein (+, -, *, /, %%): ");
        scanf(" %c", &operation);

        // Einlesen der ersten Zahl
        printf("Geben Sie die erste Zahl ein: ");
        scanf("%f", &num1);

        // Einlesen der zweiten Zahl
        if (operation != 'A' && operation != 'C')
        {
            printf("Geben Sie die zweite Zahl ein: ");
            scanf("%f", &num2);
        }

        // Ausführen der Operation gemäß dem eingegebenen Zeichen
        switch (operation)
        {
        case '+':
            ergebnis = summe(num1, num2);
            break;
        case '-':
            ergebnis = differenz(num1, num2);
            break;
        case '*':
            ergebnis = produkt(num1, num2);
            break;
        case '/':
            ergebnis = quotient(num1, num2);
            break;
        case '%':
            ergebnis = modulo(num1, num2);
            break;
        case 'A':
            // Beenden des Programms
            return 0;
        default:
            printf("Ungültige Operation.\n");
        }
    }

    return 0;
}