
import java.util.*;
public class ArrayAddElementInt{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int[] Num = {1, 2, 3, 4, 5, 6, 8, 9, 0};
        int Index = 0;
        System.out.println("Your Array: " + Arrays.toString(Num));
        System.out.print("Enter Number To add: ");
        int Element = input.nextInt();
        for(int x = 0; x <= Num.length - 1; x++){
            if (Num[Index] < Element){
              Index = x;
            }
        }
        int x;
        for(x = Num.length - 2; x >= Index; x--){
            Num[x + 1] = Num[x];
        }
        Num[x + 1] = Element;
        System.out.println("Your Array: " + Arrays.toString(Num));
    }
}