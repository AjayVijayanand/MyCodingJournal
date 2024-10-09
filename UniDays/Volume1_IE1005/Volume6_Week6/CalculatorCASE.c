#include <stdlib.h>
#include <stdio.h>

int main(void){
    //Decleration
    double number1, number2; 
    char operator;

    //User Input
    printf("\n\nWelcome to the calculator!\n\n");
    printf("Enter two numbers and an operator in the form\n");
    printf("\n[Number1] [Operator] [Number 2]\n\n");
    printf("Enter the expression: ");
    scanf("%lf %c %lf", &number1, &operator, &number2);

    //Computation & Output
    switch (operator) {
        case '+':
            printf("\n\n%.2f %c %.2f = %.2f\n", number1, operator, number2, number1+number2);
            break;
        case '-':
            printf("\n\n%.2f %c %.2f = %.2f\n", number1, operator, number2, number1-number2);
            break;
        case '*':
            printf("\n\n%.2f %c %.2f = %.2f\n", number1, operator, number2, number1*number2);
            break;
        case '/':
            if (number2 == 0) {
                printf("\n\nDivison by Zero! The Result is UNDEFINED!\n");
            } else {
                printf("\n\n%.2f %c %.2f = %.2f\n", number1, operator, number2, number1/number2);
            }
            break;
        default:
            printf("\n\nAn Error has occured\n");
            break;
    }

    return 0;
}
