/* Temperature Conversion from Celcius to Fahrenheit. */

#include <stdio.h>
int main(void) {
    //Decleration
    double celcius,                                              //User Inputable Variable
    fahrenheit;                                                  //Result Variable

    printf("Welcome to the temperature Convertor\n");

    //User Input
    printf("Enter your Temperature in Celcius to convert to Fahrenheit: ");
    scanf("%lf", &celcius);

    //Computation
    fahrenheit = ((float)9/5) * celcius + 32;

    //Output
    printf("%.2lf°C = %.2lf°F\n", celcius, fahrenheit);
    return 0;
}