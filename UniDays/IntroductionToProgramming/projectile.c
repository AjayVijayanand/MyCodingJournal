#include <stdio.h>
#include <math.h>

#define CONST_G 9.81

void instruct(void);
double flighttime(double, double, double);
double flightht(double, double, double);

int main(void){
    double distance, velocity, angle, time, height;

    instruct();
    scanf("%lf %lf %lf", &distance, &velocity, &angle);

    time = flighttime(distance, velocity, angle);
    height = flightht(velocity, angle, time);

    printf("Distance to target: %.2fm\n", distance);
    printf("Initial Velocity: %.2fm/s\n", velocity);
    printf("Angle of Elevation: %.2fradians\n", angle);
    printf("Time of flight: %.2fs\n", time);
    printf("Height of flight: %.2fm\n", height);

    return 0;
}

void instruct(void){
    printf("Enter the Distance to target (in meters), Initial Velocity (in meters per second) and Angle of Elevation (in radians): ");
}

double flighttime(double dist, double vel, double theta){
    return (dist)/(vel*cos(theta));
}

double flightht(double vel, double theta, double time){
    return (vel * sin(theta) * time) - ((CONST_G * time * time)/2) ;
}