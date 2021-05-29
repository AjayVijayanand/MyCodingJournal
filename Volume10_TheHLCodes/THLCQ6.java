import java.util.*;

public class THLCQ6{
  public static void main(String[] args){
    Queue Q = new Queue();
    Scanner input = new System.in();
    boolean exit = false;
    int F = -1;
    int R = -1;
    System.out.print("Enter Size of Queue: ");
    Size = input.nextInt();
    int[] Queues = new int[Size];
    while (exit == false){
      System.out.print("Choices\n1. EnQueue\n2. DeQueue\3. Display\n4. Exit\nEnter Choice: ");
      Choice = input.nextInt();
      switch (Choice) {
        case 1:
          System.out.print("You have choosen: EnQueue\nEnter Value to EnQueue: ");
          Value = input.intNext();
          enQueue(Queues, F, R, Value, Size);
          System.out.println("Value EnQueued");
          break;
        case 2: 
          System.out.println("You have choosen: DeQueue");
          deQueue(Queues, F, R);
          System.out.println("Value DeQueued");
          break;
        case 3:
          System.out.println("You have choosen: Display");
          print(Queues, F, R);
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
