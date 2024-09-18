#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
    int i = 0, diceval = 0;
    srand((unsigned) time(NULL));
    while (i < 100) {
        printf("Dice Value (%d): %d\n", i+1, rand()%6+1);
        i++;
    }
}