/* Calculate and display the sum of two input values */          /* Changed Comment End and changed "difference" to "sum" */

#include <stdio.h>                                                      /* Changed "include" to "#inlcude" */

int main(void) {                                                        /* Changed "Main" to "main" */
    int Num1, Num2, Sum;                                                /* Changed "X" to "num1", "x" to "num2" and "sum" to "Sum" */
    printf("Enter First Number: ");                                     /* Added Prompt */
    scanf("%d", &Num1);                                                 /* Changed "& X" to "&X" */
    printf("Enter Second Number: ");                                    /* Added Prompt */
    scanf("%d", &Num2);                                                 /* Changed "& x" to "&x" and "%f" to "%d" */
    Sum = Num1 + Num2;                                                  /* Changed "X + x = sum" to "sum = X + x" */
    printf("The sum of %d and %d is %d\n", Num1, Num2, Sum);
    return 0;
}                                                                       /* Included "}" */