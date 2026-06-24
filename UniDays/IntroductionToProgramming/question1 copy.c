#include <stdlib.h>
#include <stdio.h>

int main(void){

    int n[10] = {18, 3, 15, 7, 11, 9, 13, 5, 17, 1};
    printf("Element         Value         Histogram\n");
    for (int x = 0; x < 10; x++){
        printf("%-16d%-14d", x, n[x]);
        for (int y = 0; y < n[x]; y++){
            printf("*");
        }
        printf("\n");
    }
    return 0;
}