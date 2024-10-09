#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int istriangle(double a, double b, double c) {
    if (((a > 0) && (b > 0) && (c > 0)) && ((a+b) > c && (c+b) > a) && (a+c) > b) {
        printf("It is a triangle!\n");
        return 1;
    } else {
        printf("It is NOT a triangle!\n");
        return 0;
    }
}

double areatri(double a, double b, double c){
    double s, area;
    if (istriangle(a, b, c) == 1){
        s = (a + b + c)/2;
        area = sqrt((s*(s-a)*(s-b)*(s-c)));
        return area;
    } else {
        return 0;
    }
}

int main(void){
    printf("The area of the triangle = %.2f\n\n", areatri(5, 5, 6));
    printf("The area of the triangle = %.2f\n\n", areatri(5, 5, 8));
    printf("The area of the triangle = %.2f\n\n", areatri(0, 3, 4));
    printf("The area of the triangle = %.2f\n\n", areatri(4, 5, 1));
    return 0;
}