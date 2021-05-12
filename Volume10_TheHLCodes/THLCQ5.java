import java.util.*;

public class THLCQ5 {
    public static void push(int size, int[] Stack, int Value, int Top){
        if (Top == size - 1){
            System.out.println("Error: Overflow\nCannot Add a Value");
        } else {
            Top++;
            Stack[Top] = Value;
        }
    }

    public static void pop(int size, int[] Stack, int Top){
        if (Top == size + 1){
            System.out.println("Error: Overflow\nCannot Add a Value");
        } else {
            Top--;
            Stack[Top] = 0;
        }
    }

    public static void print(int size, int[] Stack){
        System.out.print("[");
        for (int x = 0; x < size; x++){
            System.out.print(Stack[x] + ", ");
        }
        System.out.print("]");
    } 

    public static void main(String[] args) {
        int[] Num = {6, 6, 6, 6, 6};
        push(5, Num, 5, -1);
        pop(5, Num, 5);
        print(5, Num);
    }
}