public class Queue{
  public void enQueue(int[] Que, int F, int R, int Val, int Size){
    if (R == Size - 1){
      System.out.println("Error: Overflow\nCannot enQueue a Value");
    } else if (F == -1){
      R = 0;
      F = 0;
      Que[R] = Val;
    } else {
      R++;
      Q[R] = Val;
    }
  }
  
  public void deQueue(int[] Que, int F, int R){
    if (F == -1){
      System.out.println("Error: Nothing Found\nCannot DeQueue a Value");
    } else if (F == R){
      Que[F] = 0;
      R = -1;
      F = -1;
    } else {
      Que[F] = 0;
      F++;
    }
  }
  
  public void print(int[] Que, int F, int R){
    System.out.print("[");
    for (int x = R - 1; x > F; x--){
      System.out.print(Stack[x] + ", ");
    }
    System.out.println(Stack[F] + "]");
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
