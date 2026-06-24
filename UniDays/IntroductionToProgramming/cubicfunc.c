#include <stdio.h>
#include <math.h>

#define N 100000

double cubic_function(double);
double riemann_sum(double, double);
double a, b, c, d;

int main(void){
    double high_bound, low_bound;

    printf("Input the coefficient, a, b, c and d: ");
    scanf("%lf %lf %lf %lf", &a, &b, &c, &d);
    printf("Enter Higher Bound and Lower Bound: ");
    scanf("%lf %lf", &low_bound, &high_bound);

    printf("%lf\n", riemann_sum(low_bound, high_bound));

}

double cubic_function(double x){
    return (a*x*x*x) + (b*x*x) + (c*x) + d;
}

double riemann_sum(double p, double q){
    double sub_interval, i, sum;

    sub_interval = (q - p)/N;

    for (i = 0; i < N - 1; i++){
        sum += cubic_function(p + (i * sub_interval)) * sub_interval;
    }

    return sum;
}

