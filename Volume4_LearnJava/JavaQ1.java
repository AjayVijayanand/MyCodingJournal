
import java.util.Scanner;

public class JavaQ1 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("Enter 1st Number:");
        int x = input.nextInt();
        System.out.println("Enter 2nd Number:");
        int y = input.nextInt();
        System.out.println("Sum: " + (x + y));
        if(x > y){
            if(x == y){
                System.out.println("They are equal");
            } else{
                System.out.println("The largest is: " + x);
            }
        } else {
            if(x == y){
                System.out.println("They are equal");
            }else{
                System.out.println("The largest is: " + y);
            }
        }
    }
}

