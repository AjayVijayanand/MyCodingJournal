
import java.util.*;

public class J3Q1 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("Enter number pattern");
        int n = input.nextInt();
        for(int x = 1; x <= n; x++){
            for(int y = 1; y <= x; y++){
                System.out.print(x + " ");
            }
            System.out.println();
        }
    }   
}
