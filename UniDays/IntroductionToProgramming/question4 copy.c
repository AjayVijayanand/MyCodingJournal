#include <stdlib.h>
#include <stdio.h>

void print_array(int a[], int arraysize);
int second(const int a[], int arraysize);

int main(void){
    int a[10] = {13, 25, 50, 40, 45, 251, 20, 151, 20, 17};

    print_array(a, 10);
    printf("The second maxium number of the array is: %d\n", second(a, 10));
}

void print_array(int a[], int arraysize){
    printf("{");
    for (int x = 0; x < arraysize-1; x++){
        printf("%d, ", a[x]);
    }
    printf("%d}\n", a[arraysize-1]);
}

int second(const int a[], int arraysize){
    int max_value, second_max;
    if (a[0] > a[1]){
        max_value = a[0];
        second_max = a[1];
    } else {
        max_value = a[1];
        second_max = a[0];
    }
    for (int x = 2; x < arraysize; x++){
        if (max_value <= a[x]){
            second_max = max_value;
            max_value = a[x];
        } else if (second_max <= a[x]){
            second_max = a[x];
        }
    }
    return second_max;
}