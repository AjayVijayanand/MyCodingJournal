#include <stdio.h>
#include <math.h>

int main(void) {
    double V, R1, R2, R3, I;
    printf("Input Voltage: ");
    scanf("%lf", &V);
    printf("Input Resistance of Resistor 1: ");
    scanf("%lf", &R1);
    printf("Input Resistance of Resistor 2: ");
    scanf("%lf", &R2);
    printf("Input Resistance of Resistor 3: ");
    scanf("%lf", &R3);
    if (R1 + R2 + R3 == 0) {
        printf("Error! Division by Zero!");
    } else {
        I = V/(R1+R2+R3);
    }
    printf("Current: %lf\n", I);
    return 0;
}