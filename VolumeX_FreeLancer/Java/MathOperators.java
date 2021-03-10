package VolumeX_FreeLancer.Java;
public class MathOperators {
    public double Addition(double Num1, double Num2){
        double Result = Num1 + Num2;
        return Result;
    }
    public double Subtraction(double Num1, double Num2){
        double Result = Num1 - Num2;
        return Result;
    }
    public double Multiplication(double Num1, double Num2){
        double Result = Num1 * Num2;
        return Result;
    }
    public double Division(double Num1, double Num2){
        if (Num2 != 0){
            double Result = Num1/Num2;
            return Result;
        } else {
            System.out.println("Error: Division by Zero");
            return 0.0;
        }
    }
    public int Mod(int Num1, int Num2){
        if (Num2 != 0){
            int Result = Num1 % Num2;
            return Result;
        } else {
            System.out.println("Error: Division by Zero");
            return 0;
        }
    }
}
