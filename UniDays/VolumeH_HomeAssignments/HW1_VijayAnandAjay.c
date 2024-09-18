/*  Home Assignment 1
*   Name: Vijay Anand Ajay
*   Group: EE10
*   Description: Finding the circumfurence, area of a circle and volume, surface area of a sphere 
*   with a user inputed radius
*/

//Include libraries
#include <stdio.h>

#define P_CONST 3.14159                                             //Defining a Macro with a constant value

int main(void) {
    //Declaration
    double radius,                                                  //Input Variables 
    circumference, area,                                            //Output Variables for a Circle
    volume, surface_area;                                           //Output Variables for a Sphere

    //User Input (with a validation rule)
    radius = 0;
    while (radius <= 0){
        printf("Input the radius of the circle: ");
        scanf("%lf", &radius);
        if (radius <= 0) {
            printf("Enter a valid radius!\n");
        }
    }

    //Computation
    //Calculation for a Circle
    circumference = 2 * P_CONST * radius;                           //Calculating the circumference: C = 2 * π * r
    area = P_CONST * radius * radius;                               //Calculating the Area: A = π * r^2

    //Calculation for a Sphere
    volume = 4.0/3.0 * P_CONST * radius * radius * radius;          //Calculating the Volume: V = 4/3 * π * r^3
    surface_area = 4.0 * P_CONST * radius * radius;                 //Calculating the circumference: S = 4 * π * r^2

    //Output
    printf("\n\n\n\nRadius                          =      %.3f\n", radius);
    printf("Circumference of a Circle       =      %.3f\n", circumference);
    printf("Area of a Circle                =      %.3f\n", area);
    printf("Volume of a Sphere              =      %.3f\n", volume);
    printf("Surface Area of a Sphere        =      %.3f\n\n\n\n", surface_area);
    return 0;
}