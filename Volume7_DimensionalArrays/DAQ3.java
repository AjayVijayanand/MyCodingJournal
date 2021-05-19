
import java.util.*;
public class DAQ3{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int[] Num = new int[10];
        int[] Rev = new int[10];
        for(int x = 0; x <= 9; x++){
            System.out.print("Enter Number: ");
            int Number = input.nextInt();
            Num[x] = Number;
            Rev[x] = Number;
        }
        for(int x = 0; x <= 9; x++){
            if (x % 2 == 1 && x != 9){
                Rev[8-x] = Num[x];
            }
        }
        System.out.println("Your Array: " + Arrays.toString(Num));
        System.out.println("Revised Array: " + Arrays.toString(Rev));
    }
}