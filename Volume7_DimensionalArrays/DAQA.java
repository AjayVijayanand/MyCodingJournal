
import java.util.*;
public class DAQA {
    public static void main(String[] main){
        Scanner input = new Scanner(System.in);
        int[] Num = new int[10];
        for(int x = 0; x <= 9; x++){
            System.out.print("Enter Number: ");
            Num[x] = input.nextInt();
        }
        int Minimum = Num[0];
        int Maximum = Num[0];
        float Total = Num[0];
        for(int x = 1; x <= 9; x++){
            if (Num[x] > Maximum){
                Maximum = Num[x];
            }
            if (Num[x] < Minimum){
                Minimum = Num[x];
            }
            Total += Num[x];
        }
        System.out.println("Your Array: " + Arrays.toString(Num));
        System.out.println("Maximum: " + Maximum);
        System.out.println("Minimum: " + Minimum);
        System.out.println("Total: " + Total);
        System.out.println("Average: " + (Total/10));
    }
}
