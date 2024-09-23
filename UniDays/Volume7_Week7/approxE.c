#include <stdlib.h>
#include <stdio.h>


int factorial (long num){
    if (num == 0){
        return 1;
    } else {
        return num * factorial(num-1);
    }
}

int main(void){
    int n = 0, limit;
    double sum = 0;

    printf("Enter Iteration: ");
    scanf("%d", &limit);
    while (n < limit){
        sum += (double) 1/factorial(n);
        n++;
    }

    printf("%lf\n", sum);
}