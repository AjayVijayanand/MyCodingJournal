//Fibonacci Sequence
import java.util.*;
public class JavaQ3{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("Enter Range:");
        int Range = input.nextInt();
        int Total = 0;
        int NumBuf1 = 1;
        int NumBuf2 = 1;
        int Buffer;
        System.out.print(Total + ", " + NumBuf1 + ", " + NumBuf2 + ", ");
        for (int x = 2; x < (Range - 2); x++) {
            Total = NumBuf1 + NumBuf2;
            NumBuf2 = NumBuf1;
            NumBuf1 = Total;
            System.out.print(Total + ", ");
        }
        Total = NumBuf1 + NumBuf2;
        System.out.print(Total);
    }
}