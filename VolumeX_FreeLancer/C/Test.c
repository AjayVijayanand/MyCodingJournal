#include <stdio.h>

int main() {
    int Num;
    printf("Enter Number: ");
    scanf("%d", &Num);
    if (Num % 2 == 0) {
        printf("%d is Even!", Num);
    } else {
        printf("%d is Odd!", Num);
    }
    return 0;
}