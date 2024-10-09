#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double repay(int n) {
    double sum = 1.0;
    for (int i = 1; i <= n; i++)
        sum = sum*(1 + 1.0/n);
    return sum;
}

int main(void){
    printf("%.1f\n", repay(12));
    printf("%.1f\n", repay(365));
    return 0;
}