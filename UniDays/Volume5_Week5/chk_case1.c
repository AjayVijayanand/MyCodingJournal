/* Check if user inputted char is lower case */

#include <stdio.h>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>

int main(void) {
    //Decleration
    char ch;

    //User Input
    printf("Enter Character: ");
    scanf("%c", &ch);

    //Computation & Output
    if (islower(ch)){
        printf("The character %c is lowercase!\n", ch);
    } else {
        printf("The character %c is NOT lowercase!\n", ch);
    }
}