#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double repay(int);

int main(void){
    printf("Charge per year: $%lf\n", repay(1));
    printf("Charge per month: $%lf\n", repay(12));
    printf("Charge per day: $%lf\n", repay(365));
    printf("Charge per hour: $%lf\n", repay(365*24));
    return 0;
}

double repay(int n) {
    double sum = 1.0;
    for (int i = 1; i <= n; i++)
        sum = sum*(1 + 1.0/n);
    return sum;
}