//Java Code to check if user entered number is prime or has factors
import java.util.*;

public class FA2PSCJAVAQ8 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int num = 40;
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