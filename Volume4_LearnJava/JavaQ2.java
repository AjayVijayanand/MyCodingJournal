package Volume4_LearnJava;
import java.util.Scanner;

public class JavaQ2 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("Enter 1st Number:");
        int x = input.nextInt();
        System.out.println("Enter 2nd Number:");
        int y = input.nextInt();
        System.out.println("Enter 3rd Number:");
        int z = input.nextInt();
        if(x > y){
            if(x > z){
                System.out.println("The largest is: " + x);
            } else if (x == z){
                System.out.println("The largest is: " + x + " and " + z + ". Both x and z are Equal!");
            } else {
                System.out.println("The largest is: " + z);
            }
        } else if (x < y){
            if(y > z){
                System.out.println("The largest is: " + y);
            } else if (y == z){
                System.out.println("The largest is: " + y + " and " + z + ". Both y and z are Equal!");
            } else {
                System.out.println("The largest is: " + z);
            }
        } else if (x == y){
            if (x == z){
                System.out.println("All 3 numbers are equal!");
            } else if (x > z){
                System.out.println("The largest is: " + x + " and " + y + ". Both x and y are Equal!");
            } else {
                System.out.println("The largest is: " + z);
            }
        }
    }
}

