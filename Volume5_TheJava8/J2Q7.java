//Java Code to print maximum out of 3 user entered numbers (using nested if condition)
import java.util.*;

public class J2Q7 {
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
                System.out.println("The largest is: " + num1 + ". This is Number 1.");
            } else if (num1 == num3){
                System.out.println("The largest is: " + num1 + ". Both Number 1 and Number 3 are Equal!");
            } else {
                System.out.println("The largest is: " + num3 + ". This is Number 3.");
            }
        } else if (num1 < num2){
            if(num2 > num3){
                System.out.println("The largest is: " + num2 + ". This is Number 2.");
            } else if (num2 == num3){
                System.out.println("The largest is: " + num2 + ". Both Number 2 and Number 3 are Equal!");
            } else {
                System.out.println("The largest is: " + num3 + ". This is Number 3.");
            }
        } else if (num1 == num2){
            if (num1 == num3){
                System.out.println("All 3 Numbers are equal!");
            } else if (num1 > num3){
                System.out.println("The largest is: " + num1 + ". Both Number 1 and Number 2 are Equal!");
            } else {
                System.out.println("The largest is: " + num3 + ". This is Number 3.");
            }
        }
    }
}