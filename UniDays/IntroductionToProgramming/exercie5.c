#include <stdio.h>
int main(void) {
    int i;
    for (i = 0; i < 5; i++) {
        static int x = 10, y = 0;
        printf("x = %d, y = %d\n", x++, y++);
    }
    return 0;
}