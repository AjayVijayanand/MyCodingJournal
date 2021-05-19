
import java.util.*;
public class DAQ{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int[] Numbers = new int[10];
        int Total = 0;
        for(int x = 0; x <= 9; x++){
            System.out.print("Enter Number: ");
            Numbers[x] = input.nextInt();
            Total = Total + Numbers[x];
        }
        System.out.println("Array: " + Arrays.toString(Numbers));
        System.out.println("Sum Total of Array Elements: " + Total);
    }
}