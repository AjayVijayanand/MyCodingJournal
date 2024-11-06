/*
* Practical Test X
* Name: Vijay Anand Ajay
* Group: EE10
* Description: A Simple Math Quiz!
*/

#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>

int rand_range(int, int);
void digit_display(int, int, char);
int digit_num(int, int);

int main(void) {
    int num1, num2, 
    replace_numdigit1, replace_numdigit2,
    hint1, hint2, hint3, 
    replace_hintdigit1, replace_hintdigit2, replace_hintdigit3,
    digit1, digit2, exit;


    num1 = rand_range(1000, 9999);
    num2 = rand_range(1000, 9999);
    replace_numdigit1 = rand_range(1, 4);
    replace_numdigit2 = rand_range(1, 4); 

    printf("Number 1 and Number 2 are 4 digit integer. One of the digit of them is unknown. Guess the unknown numbers!\nThe number1 is ");
    digit_display(num1, replace_numdigit1, 'A');
    printf(". The number2 is ");
    digit_display(num1, replace_numdigit1, 'B');
    printf(".\n Hint 1: "); 
    digit_display(num1, replace_numdigit1, 'A');
    scanf("%d", &digit1, &digit2);

    return 0;
}

int rand_range(int lower_bound, int upper_bound){
    srand((unsigned) time(NULL));
    return (rand() % (upper_bound - lower_bound + 1)) + lower_bound;
}

void digit_display(int number, int position, char symbol){
    int pointer, digit_count = log10(number) + 1;
    for (pointer = 0; pointer < digit_count; pointer++){
        if (position == digit_count - pointer){
            printf("%c", symbol);
        } else {
            printf("%d", digit_num(number, digit_count - pointer));
        }
    }
}

int digit_num(int number, int position){
    number = number/pow(10, (position - 1));
    return number % 10;
}