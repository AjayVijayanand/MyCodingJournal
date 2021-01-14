//Java Code for five function calculator (continues till user wants)
import java.util.*;

public class FA2PSCJAVAQ2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int Result;
        int FN;
        int SN;
        boolean Exit = false;
        System.out.println("WELCOME TO THE CALCULATOR");
        while (Exit == false){
            System.out.println("Choices:\n1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Reminder\n6 - Exit ");
            System.out.println("Enter Choice: ");
            int Choice = input.nextInt();
            if (Choice != 6){
                System.out.println("Enter First Number: ");
                FN = input.nextInt();
                System.out.println("Enter Second Number: ");
                SN = input.nextInt();
            } else {
                FN = 0;
                SN = 0;
            }
            switch (Choice){
                case 1:
                    System.out.println("You have choosen: Addition");
                    Result = FN + SN;
                    System.out.println("Reuslt: " + Result);
                    break;
                case 2:
                    System.out.println("You have choosen: Subtraction");
                    Result = FN - SN;
                    System.out.println("Reuslt: " + Result);
                    break;
                case 3:
                    System.out.println("You have choosen: Multiplication");
                    Result = FN * SN;
                    System.out.println("Reuslt: " + Result);
                    break;
                case 4:
                    System.out.println("You have choosen: Division");
                    if (SN == 0){
                        System.out.println("Result: Undefined");
                    } else {
                        Result = FN / SN;
                        System.out.println("Reuslt: " + Result);
                    }
                    break;
                case 5:
                    System.out.println("You have choosen: Modulous");
                    if (SN == 0){
                        System.out.println("Result: Undefined");
                    } else {
                        Result = FN % SN;
                        System.out.println("Reuslt: " + Result);
                    }
                    break;
                case 6:
                    System.out.println("Good Bye");
                    Exit = true;
                    break;
                default:
                    System.out.println("Choose a Valid Choice");

            }
        }
    }
}