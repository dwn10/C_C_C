#include <stdio.h>

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
    return num1 / num2;
}

// Funktion zum Berechnen des Moduls von zwei Zahlen
float modulo(float num1, float num2)
{
    return (int)num1 % (int)num2;
}

// Funktion zum Ändern des Vorzeichens der Zahl
float vorzeichenwechsel(float num)
{
    return -num;
}

// Funktion zum Löschen der letzten Ziffer
float letzteZifferLoeschen(float num)
{
    return (int)num / 10;
}

// Funktion zum Drucken des Ergebnisses
void ergebnisDrucken(float ergebnis)
{
    printf("%0.2f\n", ergebnis);
}

// Hauptfunktion
int main()
{
    float num1, num2, ergebnis;
    char operation;

    // Schleife, um Operationen auszuführen, bis der Benutzer 'B' eingibt
    while (operation != 'B')
    {
        // Menü mit Operationen anzeigen
        printf("\nWählen Sie eine Operation:\n");
        printf("+ zum Addieren\n");
        printf("- zum Subtrahieren\n");
        printf("* zum Multiplizieren\n");
        printf("/ zum Dividieren\n");
        printf("%% zum Berechnen des Moduls\n");
        // printf("+/- zum Ändern des Vorzeichens\n");
        printf("DEL(D) zum Löschen der letzten Ziffer\n");
        printf("B zum Beenden\n");

        // Einlesen der Operation
        scanf(" %c", &operation);

        // Einlesen der ersten Zahl
        printf("Geben Sie die erste Zahl ein: ");
        scanf("%f", &num1);

        // Einlesen der zweiten Zahl
        printf("Geben Sie die zweite Zahl ein: ");
        scanf("%f", &num2);

        // Ausführen der gewählten Operation
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
            if (num2 == 0)
            {
                printf("Fehler: Division durch Null.\n");
            }
            else
            {
                ergebnis = quotient(num1, num2);
            }
            break;
        case '%':
            ergebnis = modulo(num1, num2);
            break;
        // case '+/-':
        //     ergebnis = vorzeichenwechsel(num1);
        //     break;
        case 'D':
            ergebnis = letzteZifferLoeschen(num1);
            break;
        case 'B':
            printf("Beenden...\n");
            break;
        default:
            printf("Ungültige Operation.\n");
        }

        // Drucken des Ergebnisses
        if (operation != 'B' && operation != 'D')
        {
            ergebnisDrucken(ergebnis);
        }
    }

    return 0;
}