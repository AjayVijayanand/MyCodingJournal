public class Queue{
  public void enQueue(int[] Que, int F, int R, int Val, int Size){
    if (R == Size - 1){
      System.out.println("Error: Overflow\nCannot enQueue a Value");
    } else if (F == -1){
      R = 0;
      F = 0;
      Que[R] = Val;
      System.out.println("Value EnQueued");
    } else {
      R++;
      Que[R] = Val;
      System.out.println("Value EnQueued");
    }
  }
  
  public void deQueue(int[] Que, int F, int R){
    if (F == -1){
      System.out.println("Error: Nothing Found\nCannot DeQueue a Value");
    } else if (F == R){
      Que[F] = 0;
      R = -1;
      F = -1;
      System.out.println("Value DeQueued");
    } else {
      Que[F] = 0;
      F++;
      System.out.println("Value DeQueued");
    }
  }
  
  public void print(int[] Que, int F, int R){
    System.out.print("[");
    for (int x = R - 1; x > F; x--){
      System.out.print(Que[x] + ", ");
    }
    System.out.println(Que[F] + "]");
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
