//Java Code to print maximum out of 3 user entered numbers (using nested if condition)
import java.util.*;

public class FA2PSCJAVAQ7 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter 1st Number:");
        int num1 = input.nextInt();
        System.out.println("Enter 2nd Number:");
        int num2 = input.nextInt();
        System.out.println("Enter 3rd Number:");
        int num3 = input.nextInt();
        if(num1 > num2){
            if(num1 > num3){
                System.out.println("The largest is: " + num1);
            } else if (num1 == num3){
                System.out.println("The largest is: " + num1 + " and " + num3 + ". Both num1 and num3 are Equal!");
            } else {
                System.out.println("The largest is: " + num3);
            }
        } else if (num1 < num2){
            if(num2 > num3){
                System.out.println("The largest is: " + num2);
            } else if (num2 == num3){
                System.out.println("The largest is: " + num2 + " and " + num3 + ". Both num2 and num3 are Equal!");
            } else {
                System.out.println("The largest is: " + num3);
            }
        } else if (num1 == num2){
            if (num1 == num3){
                System.out.println("All 3 numbers are equal!");
            } else if (num1 > num3){
                System.out.println("The largest is: " + num1 + " and " + num2 + ". Both num1 and num2 are Equal!");
            } else {
                System.out.println("The largest is: " + num3);
            }
        }
    }
}