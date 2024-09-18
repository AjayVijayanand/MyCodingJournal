/* Find the last side of side3 triangle */

#include <stdio.h>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>

int main(void) {
    //Decleration
    double side1, side2, side3, theta1, theta2, theta3;

    //User Input
    printf("Enter Side 1: ");
    scanf("%lf", &side1);
    printf("Enter Side 2: ");
    scanf("%lf", &side2);
    printf("Enter Angle between Side 1 and Side 2 (in degrees): ");
    scanf("%lf", &theta1);

    //Computation
    theta1 = theta1 * (M_PI/180);
    side3 = sqrt((side1 * side1) + (side2 * side2) - (2.00 * side1 * side2 * cos(theta1)));
    theta2 = asin((sin(theta1)*side1)/side3);
    theta3 = asin((sin(theta1)*side2)/side3);

    //Output
    printf("\n\nTriangle Specs: \n");
    printf("Side 1: %.2f\n", side1);
    printf("Side 2: %.2f\n", side2);
    printf("Side 3: %.2f\n\n", side3);

    //Extras
    theta1 = theta1 * (180/M_PI);
    theta2 = theta2 * (180/M_PI);
    theta3 = theta3 * (180/M_PI);
    printf("Angle between Side 1 and Side 2: %.2f°\n", theta1);
    printf("Angle between Side 2 and Side 3: %.2f°\n", theta2);
    printf("Angle between Side 3 and Side 1: %.2f°\n\n\n", theta3);
}