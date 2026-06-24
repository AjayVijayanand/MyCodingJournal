#include <stdio.h>

void drawwidth(int, char);
void drawheight(int, int);

int main(void){
    drawwidth(10, '+');
    drawheight(10, 5);
    drawwidth(10, '-');
}

void drawwidth(int width, char symbol){

    int w;

    printf("*");
    for (w = 0; w < width - 2; w++)
        printf("%c", symbol);
    printf("*\n");

}

void drawheight(int width, int height){

    int w, h;

    for (h = 0; h < height - 2; h++){
        printf("|");
        for (w = 0; w < width - 2; w++){
           printf(" ");
        }
        printf("|\n");
    }

}

