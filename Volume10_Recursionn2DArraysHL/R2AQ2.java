package Volume10_Recursionn2DArraysHL;
import java.util.Scanner;

public class R2AQ2 {
    static int Num1 = 0;
    static int Num2 = 1;
    static int Num3;
    public static void Fibonnachi(int Num){
        if(Num > 1){
            Num3 = Num1 + Num2;
            Num1 = Num2;
            Num2 = Num3;
            System.out.print(", " + Num3);
            Fibonnachi(Num-1);
        }
    }
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter Number: ");
        int x = input.nextInt();
        System.out.print("0, 1");
        Fibonnachi(x-1);
        System.out.println();
    }
}
