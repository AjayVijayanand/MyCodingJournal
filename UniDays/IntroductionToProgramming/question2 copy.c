#include <stdlib.h>
#include <stdio.h>

void print_array(int a[], int arraysize);
int max_array(const int a[], int arraysize);

int main(void){
    int a[10] = {1, 2, 0, 0, 4, 5, 6, 9, 9, 17};

    print_array(a, 10);
    printf("The maxium number of the array is: %d\n", max_array(a, 10));
}

void print_array(int a[], int arraysize){
    printf("{");
    for (int x = 0; x < arraysize-1; x++){
        printf("%d, ", a[x]);
    }
    printf("%d}\n", a[arraysize-1]);
}

int max_array(const int a[], int arraysize){
    int max_value = a[0];
    for (int x = 1; x < arraysize; x++){
        if (max_value < a[x]){
            max_value = a[x];
        }
    }
    return max_value;
}