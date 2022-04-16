import java.util.*;

public class Stack_Operations {
    public static void main(String[] args) {
        Stacks Stack = new Stacks();
        Scanner input = new Scanner(System.in);
        boolean exit = false;
        System.out.print("Enter Size of the Stack: ");
        int Size = input.nextInt();
        int[] S = new int[Size];
        int Top = -1;
        while (exit == false){
            System.out.print("Choices\n1. Push\n2. Pop\n3. Display\n4. Exit\nEnter Choice: ");
            int Choice = input.nextInt();
            switch (Choice) {
                case 1:
                    System.out.print("You have choosen: Push\nEnter Value to Push: ");
                    int Value = input.nextInt();
                    Top = Stack.push(S, Value, Top);
                    break;
                case 2: 
                    System.out.println("You have choosen: Pop");
                    Top = Stack.pop(S, Top);
                    break;
                case 3:
                    System.out.println("You have choosen: Display");
                    Stack.print(S, Top);
                    break;
                case 4:
                    exit = true;
                    break;
                default:
                    System.out.println("Enter Valid Option!");
                    break;
            }
        }
    }
}
