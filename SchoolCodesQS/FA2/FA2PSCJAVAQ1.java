//Java Code for factorial of a number 
import java.util.*;

public class FA2PSCJAVAQ1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter your Number: ");
        int Num = input.nextInt();
        int Factorial = 1;    
        for (int x = 1; x <= Num; x++){
            Factorial = Factorial * x;
        }
        System.out.println("Result: " + Factorial);
    }
}