#include <stdio.h>

void f1(int, int, int);
void f2(int, int, int*);
int main(void)
{
int x = 1, y = 2, z = 0;
int* p = &z;
printf("z = %d\n", z);
f1(x, y, z);
printf("z = %d\n", z);
f2(x, y, p);
printf("z = %d", z);
return 0;
}

void f1(int x, int y, int z)
{
z = x + y;
}
void f2(int x, int y, int* p)
{
*p = x + y;
}