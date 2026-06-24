#include <stdio.h>

int main() {
    int myNum;
    printf("Enter Number: ");
    scanf("%d", &myNum);
    if (myNum % 2 == 0){
        printf("%d is Even!\n", myNum);
    } else {
        printf("%d is Odd!\n", myNum);
    }
    return 0;
}