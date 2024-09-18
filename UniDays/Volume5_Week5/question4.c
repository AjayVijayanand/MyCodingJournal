/* Question 4 */

#include <stdio.h>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>

int main(void) {
 //Question 4(a)
    int i = -15, j = 5;
    double x = -1.5, y = 4.0;
    char ch = 'a'; 
    printf("(i) abs(i+2*j) = %d\n", abs(i+2*j));
    printf("(ii) fabs(x) = %.2f\n", fabs(x));
    printf("(iii) ceil(x+y) = %.2f\n", ceil(x+y));
    printf("(iv) floor(x+y) = %.2f\n", floor(x+y));

    //Question 4(b)
    printf("(i) isalnum(5) = %d\n", isalnum(5));
    printf("(ii) isalnum('5') = %d\n", isalnum('5'));
    printf("(iii) isalpha('A') = %d\n", isalpha('A'));
    printf("(iv) isalpha(65) = %d\n", isalpha(65));
    printf("(v) isupper(ch) = %d\n", isupper(ch));
    printf("(vi) isdigit(ch) = %d\n", isdigit(ch));
    return 0;
}