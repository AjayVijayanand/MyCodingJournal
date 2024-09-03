/* Experiment time! */

#include <stdio.h>

int main(void) {
    char c = 128; /* greater than max of 127 */
    printf("c = %d\n", c); 
    c = 129;
    printf("c = %d\n", c); 
    c = 255;
    printf("c = %d\n", c); 
    c = 256;
    printf("c = %d\n", c); 
    c = -129;
    printf("c = %d\n", c); 
    return 0;
}