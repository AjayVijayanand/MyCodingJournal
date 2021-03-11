//I got Question 12: WAP to calculate area of a circle, rectangle or triangle depending upon the user's choice (read required values accordingly)
package VolumeFA2_JudgementDay;
import java.util.*;

public class Question{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Area Calculator");
        boolean Validate = false;
        boolean Validate1 = false;
        boolean Validate2 = false;
        double Answer = 0;
        int Choice = 0;
        double A = 0;
        double B = 0;
        while (!Validate){
            System.out.println("Enter the Option, where you want to find the area of the shape, below: ");
            System.out.println("1 - Circle");
            System.out.println("2 - Rectangle");
            System.out.println("3 - Triangle");
            System.out.print("Enter Your Option: ");
            Choice = input.nextInt();
            if (1 <= Choice  && Choice <= 3){
                Validate = true;
            } else {
                System.out.println("Enter Valid Value!");
            }
        }
        switch(Choice){
            case 1:
                System.out.println("You have choosen: Area of a Circle");
                System.out.println("The Area of the circle is Pi * r^2");
                while(!Validate1){
                    System.out.print("Enter the radius of the circle(r): ");
                    A = input.nextInt();
                    if (0 < A){
                        Validate1 = true;
                    } else {
                        System.out.println("Enter Valid Value!");
                    }
                }
                System.out.println("The Area of the circle is Pi * " + A + "^2");
                Answer = 3.14 * A;
                System.out.println("Answer: " + Answer);
                break;
            case 2:
                System.out.println("You have choosen: Area of a Rectangle");
                System.out.println("The Area of the Rectangle is l * b");
                while(!Validate1){
                    System.out.println("Enter the Length of the Rectangle(l): ");
                    A = input.nextInt();
                    if (0 < A){
                        Validate1 = true;
                    } else {
                        System.out.println("Enter Valid Value!");
                    }
                }
                while(!Validate2){
                    System.out.println("Enter the Breadth of the Rectangle(b): ");
                    B = input.nextInt();
                    if (0 < B){
                        Validate2 = true;
                    } else {
                        System.out.println("Enter Valid Value!");
                    }
                }
                System.out.println("The Area of the Rectangle is " + A + " * " + B);
                Answer = A * B;
                System.out.println("Answer: " + Answer);
                break;
            case 3:
                System.out.println("You have choosen: Area of a Triangle");
                System.out.println("The Area of the Triangle is 1/2 * b * h");
                while(!Validate1){
                    System.out.println("Enter the length of the Base of the Triangle(b): ");
                    A = input.nextInt();
                    if (0 < A){
                        Validate1 = true;
                    } else {
                        System.out.println("Enter Valid Value!");
                    }
                }
                while(!Validate2){
                    System.out.println("Enter the length of the height of the Triangle(h): ");
                    B = input.nextInt();
                    if (0 < B){
                        Validate2 = true;
                    } else {
                        System.out.println("Enter Valid Value!");
                    }
                }
                System.out.println("The Area of the Triangle is 1/2 * " + A + " * " + B);
                Answer = (double) 1/2 * A * B;
                System.out.println("Answer: " + Answer);
                break;
        }
    }
}