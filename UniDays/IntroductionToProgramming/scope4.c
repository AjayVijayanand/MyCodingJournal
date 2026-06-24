#include <stdio.h>

int a = 10;
int b = 12;
int ftn2(int a);
int ftn(int b);

int main(void) {
    int x = ftn(b);
    printf("main: %d\n", x);
    return 0;
}

int ftn(int b){
    b = a;
    printf("ftn: %d\n", b);
    return ftn2(a);
}

int ftn2(int a){
    int c = 13;
    printf("ftn2: %d\n", a + b);
    return ++a;
}