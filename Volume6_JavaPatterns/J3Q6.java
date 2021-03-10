package Volume6_JavaPatterns;
import java.util.*;

public class J3Q6 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("Enter number pattern");
        int n = input.nextInt();
        for(int x = 1; x <= n; x++){
            for(int y = 1; y <= n; y++){
                if (x == 1 || x == n){
                    System.out.print("* ");
                } else {
                    if(y != (n-x+1)){
                        System.out.print("  ");
                    } else {
                        System.out.print("*  ");
                    }
                }
            }
            System.out.println();
        }
    }   
}
