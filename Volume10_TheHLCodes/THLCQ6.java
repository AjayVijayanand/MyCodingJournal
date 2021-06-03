import java.util.*;

public class THLCQ6{
  public static void main(String[] args){
    Queue Q = new Queue();
    Scanner input = new Scanner(System.in);
    boolean exit = false;
    int F = -1;
    int R = -1;
    System.out.print("Enter Size of Queue: ");
    int Size = input.nextInt();
    int[] Queues = new int[Size];
    while (exit == false){
      System.out.println(F);
      System.out.println(R);
      System.out.print("Choices\n1. EnQueue\n2. DeQueue\n3. Display\n4. Exit\nEnter Choice: ");
      int Choice = input.nextInt();
      switch (Choice) {
        case 1:
          System.out.print("You have choosen: EnQueue\nEnter Value to EnQueue: ");
          int Value = input.nextInt();
          Q.enQueue(Queues, F, R, Value, Size);
          if (R == Size - 1){
            continue;
          } else if (F == -1){
            R = 0;
            F = 0;
          } else {
            R++;
          }
          break;
        case 2: 
          System.out.println("You have choosen: DeQueue");
          Q.deQueue(Queues, F, R);
          if (F == -1){
            continue;
          } else if (F == R){
            R = -1;
            F = -1;
          } else {
            F++;
          }
          break;
        case 3:
          System.out.println("You have choosen: Display");
          Q.print(Queues, F, R);
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
