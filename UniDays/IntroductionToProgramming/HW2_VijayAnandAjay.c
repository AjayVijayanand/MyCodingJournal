/*  Home Assignment 2
*   Name: Vijay Anand Ajay
*   Group: EE10
*   Description: Finding the Common Factors of 3 three-digit whole numbers - A user inputed number, 
*   a randomly generated number(with a non-last zero digit) and a number that is reversed from the second number.
*/

//Include libraries
#include <stdio.h>
#include <stdlib.h>
#include <time.h> 


//Declaring Functions
int random_number_generator(void);                                          //Function that generates a random 3 digit number
int reversed_number_generator(int);                                         //Function that generates the reverse of a number
int find_smallest_number(int, int, int);                                    //Function that finds the smallest number among the 3 numbers - To make the code more efficient
void display_common_factors(int, int, int);                                 //Function that finds and displays the common factors for 3 numbers and how many common factors



//Main Body
int main(void){
    //Initialise Variables
    int user_number = 0,                                                    //User Inputed Number 
    randomly_generated_number,                                              //Number generated randomly
    reversed_number;                                                        //Reversed - Number generated randomly

    //User Input + Validation
    while ( (user_number <= 99) || (user_number >= 1000) ){
        printf("Enter a three-digit whole number: ");
        scanf("%d", &user_number);
        if ( (user_number <= 99) || (user_number >= 1000) ) {
            printf("Enter a valid three-digit whole number!!!\n");
        }
    }

    randomly_generated_number = random_number_generator();                      //Calling the function to generate a random number
    reversed_number = reversed_number_generator(randomly_generated_number);     //Calling the function to reverse the randomly generated number

    //Displaying the randomly generated number and the reverse of that number
    printf("The second number is %d.\n", randomly_generated_number);
    printf("The third number is %d.\n", reversed_number);

    //Output
    display_common_factors(user_number, randomly_generated_number, reversed_number);    //Calling the function to get and display the common factors

    return 0;

}



//Function that generates a random 3 digit number
int random_number_generator(void){
    //Initialise Variables
    int generated_number = 10;
    srand((unsigned) time(NULL));

    //Computation
    while ( generated_number % 10 == 0 ){
        //Generate a random number from 0 to 899 and then adding 100 to the value to get a range from 100 to 999 (inclusive)
        generated_number = ( rand() % 900 ) + 100;   
    }                           

    //Output
    return generated_number;
}

//Function that generates the reverse of a number
int reversed_number_generator(int number){
    //Initialise Variables
    int reversed_number = 0, 
    remainder; 

    //Computation
    while (number != 0){
        remainder = number % 10;    
        reversed_number = ( reversed_number * 10 ) + remainder;
        number = number / 10;
    }

    //Output
    return reversed_number;
}

//Function that finds the smallest number among the 3 numbers - this is to make the code more efficient
int find_smallest_number(int number1, int number2, int number3){
    //Initialise Variable
    int smallest_number = number1;

    //Computation
    if (smallest_number > number2) {
        smallest_number = number2;
    }
    if (smallest_number > number3) {
        smallest_number = number3;
    }

    //Output
    return smallest_number;
}

//Function that finds and displays the common factors for 3 numbers and how many common factors are there
void display_common_factors(int number1, int number2, int number3){
    //Initialise Variables
    int max_possible_common_factor = find_smallest_number(number1, number2, number3),
    possible_factor, 
    factor_counter = 0;

    //Computation
    printf("Common factors for %d %d %d\n", number1, number2, number3);
    for (possible_factor = 1; possible_factor <= max_possible_common_factor; possible_factor++) {
        if ((number1 % possible_factor == 0) && (number2 % possible_factor == 0) && (number3 % possible_factor == 0)){
            printf("%d\n", possible_factor);    //Output - Prints all the Common Factors of the 3 numbers
            factor_counter++;
        }
    }

    //Output - The number of Common Factors for the 3 numbers
    printf("There are(is) %d common factor(s) of %2d, %2d, and %2d\n", factor_counter, number1, number2, number3);
}

