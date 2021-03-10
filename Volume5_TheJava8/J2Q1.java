//Java Code for factorial of a number 
//int - max accurate factorial for num: 13, Values which is not zero = 33
//long - max accurate factorial for num: 20, Values which is not zero = 65
package Volume5_TheJava8;
import java.util.*;

public class J2Q1 {
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