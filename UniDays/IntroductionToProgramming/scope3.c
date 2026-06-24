#include <stdio.h>

int a = 1, b = 2, c = 3;
int fun(void);

int main(void) {
    int i;
    double d;
    d = 33.7;
    for (i = 1; i <= 5; i++) {
        printf("funmain1: %3d\n", fun());
        printf("funmain2: %3d %3d %3d\n", a, b, c);
    }
    printf("%f\n", d);
    return 0;
}

int fun(void) {
    int b, c;
    double d;
    static int cnt = 1;
    printf("fun: %3d\n", cnt++);
    a = b = c = 4;
    d = 50.0;
    return a + b + c;
}