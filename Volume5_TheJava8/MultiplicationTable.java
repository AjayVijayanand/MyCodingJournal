//Java Code to print multiplication table of a user entered number 
import java.util.*;

public class J2Q4 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter Number for the multiplication table: ");
        int Num = input.nextInt();
        for(int x = 1; x <= 10; x++){
            System.out.println(Num + " * " + x + " = " + (Num * x));
        }
    }
}