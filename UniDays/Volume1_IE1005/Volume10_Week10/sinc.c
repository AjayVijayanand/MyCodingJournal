#include <stdio.h>
#include <stdlib.h>
#include <math.h> 

double sinc(double);

int main(void){

    double start_point, end_point, x, interval;

    printf("Enter start point and end point: ");
    scanf("%lf %lf", &start_point, &end_point);
    interval = (end_point - start_point)/20;

    printf("    x               sinc(x)\n");
    for(x = start_point; x <= end_point; x += interval){
            printf("%12lf    %12lf\n", x, sinc(x));
    }

}

double sinc(double x){

    if (x == 0) return 1.0;
    return sin(x)/x;

}