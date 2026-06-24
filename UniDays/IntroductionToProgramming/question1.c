/* Question 1 */

#include <stdio.h>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>

int main(void) {
    int x = 3, y = 4, z = 10;
    printf("(a) x + y/z*x = %d\n", x + y/z*x);
    printf("(b) x * -(y+z) = %d\n", x*-(y+z));
    printf("(c) x %% (z/y) = %d\n", x%(z/y));
    printf("(d) y %% x + 1.5/x = %.2f\n", y%x +1.5/x);
    printf("(e) x/2 + 3.5 = %.2f\n", x/2 + 3.5);
    printf("(f) (double) x/2 + 3.5 = %.2f\n", (double)x/2 + 3.5);
    printf("(g) x/2.0 + 3.5 = %.2f\n", x/2.0 + 3.5);
}