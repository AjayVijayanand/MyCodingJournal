//Java Code to check if user entered number is prime or has factors
package Volume5_TheJava8;
import java.util.*;

public class J2Q8 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter Number: ");
        int num = input.nextInt();
        int Factors = 0;
        for (int x = 2; x < num; x++){
            if (num % x == 0){
                Factors = Factors + 1;
            }
        }
        if(Factors == 0){
            System.out.println("Number is a Prime");
        } else{
            System.out.println("Number is Not A Prime. It has this many factors: " + (Factors + 2));
        }
    }
}