/**PseudoCodetoJavaQ1 (Swtich...Case Calculator)**/
import java.util.*;

public class PseudoCodeToJavaQ1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int Result;
        boolean Exit = false;
        System.out.println("WELCOME TO THE CALCULATOR");
        while (Exit == false){
            System.out.println("Choices:\n1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Reminder\n6 - Exit ");
            System.out.println("Enter Choice: ");
            int Choice = input.nextInt();
            System.out.println("Enter First Number: ");
            int FN = input.nextInt();
            System.out.println("Enter Second Number: ");
            int SN = input.nextInt();
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