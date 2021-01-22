//Java Code for printing first 50 even numbers (except multiples of 10)
import java.util.*;

public class FA2PSCJAVAQ3 {
    public static void main(String[] args) {
        int c = 1;
        int x = 2;
        System.out.println("This code will print the first 50 even numbers (except multiples of 10)");
        while (c <= 50){
            if (x % 10 == 0){
                x = x + 2;
                c = c + 1;
                continue;
            } 
            System.out.println(x); 
            x = x + 2;
            c = c + 1;
        }
    }
}