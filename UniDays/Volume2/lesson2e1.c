#include <stdio.h>

int main(void){
    //Declare
    int Num1, Num2, Sum;

    //Input
    printf("\nEnter the first number: ");
    scanf("%d", &Num1);
    printf("Enter the Second number: ");
    scanf("%d", &Num2);

    //Compute
    Sum = Num1 + Num2;

    //Output
    printf("The sum of %d & %d is %d!\n\n", Num1, Num2, Sum);
    
    return 0;
}