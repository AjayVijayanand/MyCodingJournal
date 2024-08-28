/* Solution of a*x^2 + b*x + c = 0 */

/* Headers */
#include <stdio.h>
#include <math.h>

/* Main Code */
int main(void) {
    double a, b, c, d, root1, root2, realpart, imaginarypart;                          /* Declare Variables */
    /* Input Values! */
    printf("Input the coefficient, a: ");
    scanf("%lf", &a);
    printf("Input the coefficient, b: ");
    scanf("%lf", &b);
    printf("Input the coefficient, c: ");
    scanf("%lf", &c);
    /* Calculate the Discriminant */
    d = b*b-4*a*c;
    /* Computate the answers! */
    printf("\n");
    if (a == 0) {                                                                     /* Linear Equation */
        printf("0 = %.2f*x + %.2f\n", b, c);
        printf("\n");
        printf("This is a linear equation!\n");
        printf("There is only 1 Real Root!\n");
        printf("The Root: %.2f\n", -c/b);
    } else {
        printf("0 = %.2f*x^2 + %.2f*x + %.2f\n", a, b, c);
        printf("\n");  
        if (d > 0) {                                                                   /* 2 Real Distinct Root */
            printf("There are 2 Distinct Real roots!\n");
            root1 = (- b + sqrt(d))/(2*a);
            root2 = (- b - sqrt(d))/(2*a);
            printf("First root: %.2f\n", root1);
            printf("Second root: %.2f\n", root2);
        } else if (d == 0) {                                                            /* 1 Real Repeated Root */
            printf("There is only 1 Real Repeated Root!\n");
            printf("The root: %.2f\n", -b/(2*a));
        } else {                                                                        /* 2 Complex Roots */
            printf("There are 2 Distinct Complex Roots!\n");
            realpart = (-b)/(2*a);
            imaginarypart = sqrt(-d)/(2*a);
            printf("First root: %.2f + %.2fi\n", realpart, imaginarypart);
            printf("Second root: %.2f - %.2fi\n", realpart, imaginarypart);
        }
    }
    return 0;
    /* End Code! */
}