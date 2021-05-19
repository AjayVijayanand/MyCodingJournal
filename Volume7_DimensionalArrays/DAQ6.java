
import java.util.*;
public class DAQ6{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int[] Num = new int[10];
        for(int x = 0; x <= 9; x++){
            System.out.print("Enter Number: ");
            Num[x] = input.nextInt();
        }
        boolean Found = false;
        System.out.print("What Number do you want to search: ");
        int Search = input.nextInt();
        System.out.println("Your Array: " + Arrays.toString(Num));
        System.out.println("Element Searche: " + Search);
        for(int x = 0; x <= (Num.length - 1); x++){
            if (Num[x] == Search){
                System.out.println("Element found at Index: " + x);
                Found = true;
            }
        }
        if(!Found){
            System.out.println("Element not found!");
        }
    }
}