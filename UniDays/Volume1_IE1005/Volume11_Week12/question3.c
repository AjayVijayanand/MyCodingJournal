#include <stdlib.h>
#include <stdio.h>

void mystrcpy(char s[], char t[]);

int main(void){
    char org[] = "Programming";
    char cpy[100];
    mystrcpy(org, cpy);
    printf("%s\n", org);
    printf("%s\n", cpy);
    return 0;
}

void mystrcpy(char s[], char t[]){
    int i = 0;
    while ((s[i] = t[i]) != '\0')
        i++;
}