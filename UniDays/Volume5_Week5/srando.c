/* Example on the use of srand() */
#include <stdio.h>
#include <stdlib.h>
#include <time.h> //Library for time()
int main(void) {
    srand((unsigned) time(NULL));
    printf("Three random integers are:\n%d %d %d\n", rand(),rand(),rand());
    return 0;
}