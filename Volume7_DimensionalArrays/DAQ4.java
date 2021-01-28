import java.util.*;
public class DAQ2{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int[] Num = new int[10];
        int[] Rev = new int[10];
        for(int x = 0; x <= 9; x++){
            System.out.print("Enter Number: ");
            Num[x] = input.nextInt();
            if (x % 2 != 0){
                Rev[x-1] = Num[x];
                Rev[x] = Num[x-1];
            }
        }
        System.out.println("Your Array: " + Arrays.toString(Num));
        System.out.println("Revised Array: " + Arrays.toString(Rev));
    }
}