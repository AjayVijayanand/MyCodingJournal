public class Stacks {
    public boolean isEmpty(int[] Stack){
        for (int x = Stack.length - 1; x >= 0; x--){
            if (Stack[x] != 0){
                return false;
            }
        }
        return true;
    } 

    public int push(int[] Stack, int Value, int Top){
        if (Top == Stack.length - 1){
            System.out.println("Error: Overflow\nCannot Add a Value");
        } else {
            Top++;
            Stack[Top] = Value;
            System.out.println("Value Pushed");
        }
        return Top;
    }

    public int pop(int[] Stack, int Top){
        if (Top == -1){
            System.out.println("Error: Empty\nCannot Pop a Value");
        } else {
            Top--;
            Stack[Top] = 0;
            if(Top == 0){
                Top = -1;
            }
            System.out.println("Value Poped");
        }
        return Top;
    }

    public void print(int[] Stack, int Top){
        if(Top == -1){
            System.out.println("[" + Stack[0] + "]");
        }else {
            System.out.print("[");
            for (int x = Top; x > 0; x--){
                System.out.print(Stack[x] + ", ");
            }
            System.out.println(Stack[0] + "]");
        }
    } 
}
