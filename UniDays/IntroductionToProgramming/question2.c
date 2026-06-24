/* Question 2 */

#include <stdio.h>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>

int main(void) {
    int i = 3, j = 10;
    printf("%d\n", i++);
    printf("%d\n", ++i);
    printf("%d\n", j--);
    printf("%d\n", --j);
    printf("%d\n", (--j + 2));
    printf("%d\n", (i-- + ++j)); 
}