//AP & GP
import java.util.*;
import java.lang.*;

public class JavaQ4{
    public static void main(String[] args){
        int Range;
        double a;
        double d;
        double r;
        double Result;
        Scanner input = new Scanner(System.in);
        System.out.println("Looking into the Progressions...\nYour Choices:Enter your Choice: ");
        int Choice = input.nextInt();
        switch (Choice){
            case 1:
                System.out.println("You have choosen: Arithmetic Progression");
                System.out.println("a + (n - 1) * d");
                System.out.println("Enter a");
                a = input.nextDouble();
                System.out.println(a + " + (n - 1) * d");
                System.out.println("Enter d");
                d = input.nextDouble();
                System.out.println(a + " + (n - 1) * " + d);
                System.out.println("Enter Range");
                Range = input.nextInt();
                for (int n = 1; n <= (Range - 1); n++){
                    Result = a + ((n - 1) * d);
                    System.out.print(Result + ", ");
                }
                Result = a + ((Range - 1) * d);
                System.out.print(Result);
                break;
            case 2:
                System.out.println("You have choosen: Geometric Progression");
                System.out.println("a * r^(n - 1)");
                System.out.println("Enter a");
                a = input.nextDouble();
                System.out.println(a + " * r^(n - 1)");
                System.out.println("Enter r");
                r = input.nextDouble();
                System.out.println(a + " * " + r + "^(n - 1)");
                System.out.println("Enter Range");
                Range = input.nextInt();
                for (int n = 1; n <= (Range - 1); n++){
                    Result = a * Math.pow(r, (n - 1));
                    System.out.print(Result + ", ");
                }
                Result = a * Math.pow(r, (Range - 1));
                System.out.print(Result);
                break;
        }
    }
}