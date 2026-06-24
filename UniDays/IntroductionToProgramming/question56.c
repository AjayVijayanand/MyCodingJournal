#include <stdlib.h>
#include <stdio.h>


void print_matrix(int matrix[3][3]);
void addition_matrix(const int matrix1[3][3], const int matrix2[3][3], int result[3][3]);
void multiplication_matrix(const int matrix1[3][3], const int matrix2[3][3], int result[3][3]);

int main(void){
    int p[3][3] = {
        {1, 3, -4}, 
        {1, 1, -2}, 
        {-1, -2, 5}
    };
    int q[3][3] = {
        {8, 3, 0}, 
        {3, 10, 2}, 
        {0, 2, 6}
    };

    int r[3][3];

    printf("Matrix p:\n\n");
    print_matrix(p);

    printf("\n\nMatrix q:\n\n");
    print_matrix(q);

    printf("\n\nMatrix p + q:\n\n");
    addition_matrix(p, q, r);
    print_matrix(r);
    
    printf("\n\nMatrix p * q:\n\n");
    multiplication_matrix(p, q, r);
    print_matrix(r);
}

void print_matrix(int matrix[3][3]){
    int x, y;
    for (x = 0; x < 3; x++){
        for (y = 0; y < 3; y++) {
            printf("%5d", matrix[x][y]);
        }
        printf("\n");
    }
    printf("\n");
}

void addition_matrix(const int matrix1[3][3], const int matrix2[3][3], int result[3][3]){
    int  x, y;
    for (x = 0; x < 3; x++){
        for (y = 0; y < 3; y++) {
          result[x][y] = matrix1[x][y] + matrix2[x][y];
        }
    }
}

void multiplication_matrix(const int matrix1[3][3],const int matrix2[3][3], int result[3][3]){
    int x, y, z;
    for (x = 0; x < 3; x++){
        for (y = 0; y < 3; y++){
            result[x][y] = 0;
            for (z = 0; z < 3; z++){
                result[x][y] += matrix1[x][z] * matrix2[z][y]; 
            }
        }
    }
}
