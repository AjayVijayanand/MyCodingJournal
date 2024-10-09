#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float scale(float Number, int Power){
    return Number * pow(10, Power);
}

int main(void){
    printf("%.1f\n", scale(2.5, 2));
    return 0;
}