#include <stdio.h>
int main(void) {
    int number1, number2, number3, number4, smaller;
    printf("Enter the first integer: ");
    scanf("%d", &number1);
    printf("Enter the second integer: ");
    scanf("%d", &number2);
    printf("Enter the third integer: ");
    scanf("%d", &number3);
    printf("Enter the fourth integer: ");
    scanf("%d", &number4);
    smaller = number1;
    if (smaller > number2){
        smaller = number2;
    }
    if (smaller > number3) {
        smaller = number3;
    }
    if (smaller > number4) {
        smaller = number4;
    }
    printf("%d is the smaller integer.", smaller);
    return 0;
}