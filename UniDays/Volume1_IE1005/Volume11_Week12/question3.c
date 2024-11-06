#include <stdlib.h>
#include <stdio.h>

void mystrcpy(char s[], char t[]);

int main(void){
    char s[] = "Hello";
    char t[] = "Hello";
    mystrcpy(s, t);
    return 0;
}

void mystrcpy(char s[], char t[]){
    int i = 0;
    while ((s[i] == t[i]) != '\0')
        i++;
}