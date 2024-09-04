/* Question 3 */

#include <stdio.h>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>

int main(void) {
    int x = 10, y = 2, z = 3;

    printf("   Expression     Equivalent to     Result    \n");
    printf("--------------------------------------------\n");

    x = 10, y = 2, z = 3;
    x += y;
    printf("     x += y         x = x + y        x=%d\n", x);

    x = 10, y = 2, z = 3;
    x %= z;
    printf("     x %%= z         x = x %% z        x=%d\n", x);

    x = 10, y = 2, z = 3;
    y /= z;
    printf("     y /= z         y = y / z        y=%d\n", y);

    x = 10, y = 2, z = 3;
    y *= x/y;
    printf("    y *= x/y       y = y * x/y       y=%d\n", y);

    x = 10, y = 2, z = 3;
    x %= x/(y+z);
    printf("  x %%= x/(y+z)   x = x %% x/(y+z)     x=%d\n", x);
}