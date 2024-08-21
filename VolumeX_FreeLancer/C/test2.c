#include <stdio.h>

int main() {
    int myNum, prod;
    printf("Enter Number: ");
    scanf("%d", &myNum);
    for(int x = 1; x <= myNum; x++){
        prod = myNum * x;
        printf("%d * %d = %d\n", myNum, x, prod);
    };
    return 0;
}