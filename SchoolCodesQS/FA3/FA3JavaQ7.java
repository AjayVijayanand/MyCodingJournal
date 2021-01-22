import java.util.*;

public class FA3JavaQ7 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("Enter number pattern");
        int n = input.nextInt();
        for(int x = 1; x <= n; x++){
            for(int y = 1; y <= n; y++){
                if (x == 1 || x == n){
                    System.out.print("* ");
                } else {
                    if(y != x){
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
