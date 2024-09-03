/* Distance travelled by a particle falling under gravity.*/

#include <stdio.h>
#define ACCEL 9.81                                                                //Pre-defined Constant

int main(void) {
    //Decleration
    double time = 0,                                                              //Initialised Variable
    initial_velocity, max_time, interval,                                         //User Inputable Variables
    distance;                                                                     //Result Variable

    //User Input
    printf("Enter your Initial Velocity: ");
    scanf("%lf", &initial_velocity);
    printf("Enter your Maximum Time Travelled: ");
    scanf("%lf", &max_time);
    printf("Enter your Time Interval: ");
    scanf("%lf", &interval);

    //Computation + Output
    printf("Time Elapsed    Distance Travelled\n" );
    printf("----------------------------------\n" );
    while (time <= max_time) {
        distance = (initial_velocity * time) + (0.5 * ACCEL * time * time);        //Calculation
        printf("%7.2f %19.2f\n", time, distance);                                  //Output
        time = time + interval;                                                    //Loop Condition Increment
    }
    return 0;
}