#include <stdio.h>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>

int main(void) {
    int height, width, count1, count2;
    printf("Enter two integers for height and width: ");
    scanf("%d %d", &height, &width);
    for(count1 = 0; count1 < height; count1++){
        for (count2 = 0; count2 < width; count2++){
            if (count1 == 0 || count1 == height - 1){
                printf("=");
            } else {
                if (count2 == 0 || count2 == width - 1){
                    printf("*");
                } else {
                    printf(" ");
                }
            }
        }
        printf("\n");
    }
}