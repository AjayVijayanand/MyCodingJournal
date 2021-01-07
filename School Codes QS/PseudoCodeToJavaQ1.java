//PseudoCodetoJavaQ1 (Swtich...Case Calculator)
public class PseudoCodeToJavaQ1 {
    public static void main(String[] args) {
        int Choice = 1;
        int Result;
        int FN = 5;
        int SN = 10;
        boolean Exit = false;
        while (Exit == false){
            switch (Choice){
                case 1:
                    System.out.println("Addition");
                    Result = FN + SN;
                    System.out.println("Reuslt: " + Result);
                    break;
                case 2:
                    System.out.println("Subtraction");
                    Result = FN - SN;
                    System.out.println("Reuslt: " + Result);
                    break;
                case 3:
                    System.out.println("Multiplication");
                    Result = FN * SN;
                    System.out.println("Reuslt: " + Result);
                    break;
                case 4:
                    System.out.println("Division");
                    if (SN == 0){
                        System.out.println("Result: Undefined");
                    } else {
                        Result = FN / SN;
                        System.out.println("Reuslt: " + Result);
                    }
                    break;
                case 5:
                    System.out.println("Modulous");
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