import java.util.*;

public class THLCQ5 {
    public static void main(String[] args) {
        Stacks Stack = new Stacks();
        int[] Num = new int[5];
        System.out.println(Stack.isEmpty(Num));
        Stack.push(Num, 5, -1);
        Stack.pop(Num, 5);
        Stack.print(Num, 5);
        System.out.println(Stack.isEmpty(Num));
    }
}