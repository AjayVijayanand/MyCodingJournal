/* Solution of a*x*x + b*x + c = 0 */
#include <stdio.h>
#include <math.h>
int main(void) {
    double a, b, c, d, root1, root2, realpart, imaginarypart;
    printf("Input the coefficient, a: ");
    scanf("%lf", &a);
    printf("Input the coefficient, b: ");
    scanf("%lf", &b);
    printf("Input the coefficient, c: ");
    scanf("%lf", &c);
    d = b*b-4*a*c;
    if (a == 0) {                                                                      /* Linear Equation */
        printf("There is only 1 root!");
        printf("The Root: %4.3f", -c/b);
    } else {
        if (d > 0) {                                                                   /* 2 Real Distinct Root */
            printf("There are 2 distinct roots!!");
            root1 = (- b + sqrt(d))/(2*a);
            root2 = (- b - sqrt(d))/(2*a);
            printf("First root: %4.3f\n", root1);
            printf("Second root: %4.3f\n", root2);
        } else if (d == 0) {                                                            /* 1 Real Root */
            printf("There is only 1 root!\n");
            printf("The root: %4.3f\n", -b/(2*a));
        } else {                                                                        /* 2 Complex Roots */
            printf("There are Complex Roots!\n");
            realpart = (-b)/(2*a);
            imaginarypart = sqrt(-d)/(2*a);
            printf("First root: %4.3f + %4.3fi \n", realpart, imaginarypart);
            printf("Second root: %4.3f - %4.3fi \n", realpart, imaginarypart);
        }
    }
    return 0;
}