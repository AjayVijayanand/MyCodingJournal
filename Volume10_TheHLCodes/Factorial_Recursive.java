import java.util.*;

public class Factorial_Recursive {
    static int Result = 1;
    public static int Factorial(int Num){
        if (Num == 0){
            return Result;
        } else {
            Result = Num * Factorial(Num - 1);
            return Result;
        }
    }
    public static void main(String[] args) {
        try (Scanner input = new Scanner(System.in)) {
            System.out.print("Enter Number: ");
            int x = input.nextInt();
            System.out.println(Factorial(x));
        }
    }
}
