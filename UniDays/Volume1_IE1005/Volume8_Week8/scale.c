#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double scale(double, int);

int main(void){
    double number;
    int power;
    printf("Enter a (Real) Number: ");
    scanf("%lf", &number);
    printf("Enter a Scale Power (integer number): ");
    scanf("%d", &power);
    printf("%.1f\n", scale(number, power));
    return 0;
}

double scale(double Number, int Power){
    return Number * pow(10, Power);
}