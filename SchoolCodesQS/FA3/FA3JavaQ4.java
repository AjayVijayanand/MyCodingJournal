import java.util.*;

public class FA3JavaQ4 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("Enter number pattern");
        int n = input.nextInt();
        int x = 1;
        while(x <= n){
            int y = 1;
            while(y <= x){
                System.out.print("* ");
                y++;
            }
            System.out.println();
            x++;
        }
    }   
}
