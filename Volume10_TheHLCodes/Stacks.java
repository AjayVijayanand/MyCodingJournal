

public class Stacks {
    public void push(int[] Stack, int Value, int Top){
        if (Top == Stack.length - 1){
            System.out.println("Error: Overflow\nCannot Add a Value");
        } else {
            Top++;
            Stack[Top] = Value;
        }
    }

    public void pop(int[] Stack, int Top){
        if (Top == Stack.length + 1){
            System.out.println("Error: Empty\nCannot Pop a Value");
        } else {
            Top--;
            Stack[Top] = 0;
        }
    }

    public void print(int[] Stack, int Top){
        System.out.print("[");

        for (int x = Top - 1; x > 0; x--){
            System.out.print(Stack[x] + ", ");
        }
        System.out.println(Stack[0] + "]");
    } 
    
    public boolean isEmpty(int[] Stack){
        for (int x = Stack.length - 1; x >= 0; x--){
            if (Stack[x] != 0){
                return false;
            }
        }
        return true;
    } 
}
