#include <stdio.h>

int main(void){
    int i = 32; /* outer block scope */
    printf("Within the outer block: i = %d\n", i);
    { /* begin inner block */
        int i, j; /* inner block scope */
        printf("Within the inner block: \n");
        for (i = 0, j = 10; i <= 10; i++, j--)
            printf("i = %2d, j = %2d\n", i, j);
    } /* end inner block */
    printf("Within the outer block: i = %d\n", i);
    return 0;
}