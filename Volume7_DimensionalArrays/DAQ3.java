import java.util.*;
public class DAQ2{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int[] Num = new int[10];
        int[] Rev = new int[10];
        for(int x = 0; x <= 9; x++){
            System.out.print("Enter Number: ");
            int Number = input.nextInt();
            Num[x] = Number;
            if (x < 5){
                Rev[x+5] = Number;
            } else {
                Rev[x-5] = Number;
            }
        }
        System.out.println("Your Array: " + Arrays.toString(Num));
        System.out.println("Revised Array: " + Arrays.toString(Rev));
    }
}