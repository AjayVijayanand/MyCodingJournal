#include <stdio.h>
#include <math.h>

int main(void){
    double sum, product;
    sum = 0;
    product = 0;
    int num1, num2;
    printf("Enter Number 1: ");
    scanf("%d", &num1);
    printf("Enter Number 2: ");
    scanf("%d", &num2);
    sum = num1 + num2;
    product = num1 * num2;
    printf("\nSum of the 2 Numbers is: %lf", sum);
    printf("\nProduct of the 2 Numbers is: %lf\n", product);
}