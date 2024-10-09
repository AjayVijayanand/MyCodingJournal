#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double repay(int);

int main(void){
    printf("%lf\n", repay(12));
    printf("%lf\n", repay(365));
    return 0;
}

double repay(int n) {
    double sum = 1.0;
    for (int i = 1; i <= n; i++)
        sum = sum*(1 + 1.0/n);
    return sum;
}