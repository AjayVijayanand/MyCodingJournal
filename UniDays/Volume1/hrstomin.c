/*
 * Converts hours to minutes.
 */

#include <stdio.h>
#define HR_TO_MIN  60       /* number of minutes in an hour */

int main(void)
{
  double hours,                  /* input - in hours */
         minutes;                /* output - in minutes */

  /* Read in the hours. */
  printf("Enter the time in hours > ");
  scanf ("%lf", &hours);

  /* Convert hours to minutes. */
  minutes = hours + HR_TO_MIN;

  /* Display minutes. */
  printf("The time in minutes is %lf\n\n", minutes);

  return 0;
}