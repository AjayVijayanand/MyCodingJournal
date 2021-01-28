import java.util.*;
public class DAQ2{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int[] Num = new int[10];
        int[] Rev = new int[10];
        for(int x = 0; x <= 9; x++){
            System.out.print("Enter Number: ");
            Num[x] = input.nextInt();
            Rev[9-x] = Num[x];
        }
        System.out.println("Your Array: " + Arrays.toString(Num));
        System.out.println("Revised Array: " + Arrays.toString(Rev));
    }
}