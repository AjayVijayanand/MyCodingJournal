//Java Code to read 10 numbers from user and count and print how many are even and odd
import java.util.*;

public class FA2PSCJAVAQ5 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        int EvenNo = 0;
        int OddNo = 0;
        for (int x = 1; x <= 10; x++){
            System.out.println("Enter Number to check whether its Even or Odd: ");
            int Num = input.nextInt();
            if (Num % 2 == 0){
                EvenNo++;
            } else {
                OddNo++;
            }
        }
        System.out.println("Number of Even Numbers: " + EvenNo);
        System.out.println("Number of Odd Numbers: " + OddNo);
    }
}