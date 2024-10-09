/* program style.c for IE1005 hands-on        */
/* Name: Ajay Vijay Anand                     */
/* Group: E010                                */
/* Date: 11/09/2024                           */

#include <stdio.h>
#define PI_CONST 3.14159

int main(void) { 
  /* declaration */
  double radius, area, circumference;

  /* get the input */
  printf("Enter the radius of the circle: ");
  scanf("%lf", &radius);

  /* compute area and circumference */
  circumference = 2.0 * radius * PI_CONST;
  area = PI_CONST * radius * radius;

  /* display the results */
  printf("Radius of circle        = %.2f\n", radius);
  printf("Area of circle          = %.2f\n", area);
  printf("Circumference of circle = %.2f\n", circumference);

  return 0;
}