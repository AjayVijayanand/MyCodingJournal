

public class Collections {
    public void push(int size, int[] Stack, int Value, int Top){
        if (Top == size - 1){
            System.out.println("Error: Overflow\nCannot Add a Value");
        } else {
            Top++;
            Stack[Top] = Value;
        }
    }

    public void pop(int size, int[] Stack, int Top){
        if (Top == size + 1){
            System.out.println("Error: Overflow\nCannot Add a Value");
        } else {
            Top--;
            Stack[Top] = 0;
        }
    }

    public void print(int size, int[] Stack){
        System.out.print("[");
        for (int x = 0; x < size - 1; x++){
            System.out.print(Stack[x] + ", ");
        }
        System.out.print(Stack[size-1] + "]");
    } 
}