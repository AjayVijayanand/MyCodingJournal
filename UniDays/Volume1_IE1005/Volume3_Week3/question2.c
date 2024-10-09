#include <stdio.h>
int main(void) {                                        /* line 1 */
    
    int number1, number2, smaller;                      /* line 2 - (i) */
    
    printf("Enter the first integer: ");                /* line 3 - (iii) */
    scanf("%d", &number1);                              /* line 4 - (ii) */
    printf("Enter the second integer: ");               /* line 5 - (iii) */
    scanf("%d", &number2);                              /* line 6 - (ii) */
    
    if (number1 > number2){                             /* line 7 - (iv) */
        smaller = number2;                              /* line 8 - (v) */
    } else {                                            /* line 9 - (iv) */
        smaller = number1;                              /* line 10 - (v) */
    }

    printf("%d is the smaller integer.", smaller);      /* line 11 - (iii) */
    return 0;
} 