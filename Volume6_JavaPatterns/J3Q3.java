package Volume6_JavaPatterns;
import java.util.*;

public class J3Q3 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("Enter number pattern");
        int n = input.nextInt();
        int x = 1;
        while(x <= n){
            int y = 1;
            while(y <= n){
                System.out.print("* ");
                y++;
            }
            System.out.println();
            x++;
        }
    }   
}
