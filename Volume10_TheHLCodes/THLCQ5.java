import java.util.*;

public class THLCQ5 {
    public static void main(String[] args) {
        Stacks Stack = new Stacks();
        Scanner input = new System.in()
        boolean exit = false;
        int F = -1;
        int R = -1;
        System.out.print("Enter Size of Queue: ");
        Size = input.nextInt();
        int[] S = new int[Size];
        while (exit == false){
            System.out.print("Choices\n1. Push\n2. Pop\3. Display\n4. Exit\nEnter Choice: ");
            Choice = input.nextInt();
            switch (Choice) {
                case 1:
                    System.out.print("You have choosen: Push\nEnter Value to Push: ");
                    Value = input.intNext();
                    Stack.enQueue(S, Value, Size);
                    System.out.println("Value Pushed");
                    break;
                case 2: 
                    System.out.println("You have choosen: Pop");
                    Stack.deQueue(S, Size);
                    System.out.println("Value Poped");
                    break;
                case 3:
                    System.out.println("You have choosen: Display");
                    Stack.print(S, Size);
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
