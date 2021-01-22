import java.util.*;

public class FA3JavaQ5 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("Enter number pattern");
        int n = input.nextInt();
        int x = 1;
        do{
            int y = 1;
            do{
                System.out.print("* ");
                y++;
            }while(y <= x);
            System.out.println();
            x++;
        }while(x <= n);
        x = n - 1;
        do{
            int y = 1;
            do{
                System.out.print("* ");
                y++;
            }while(y <= x);
            System.out.println();
            x--;
        }while(x >= 1);
    }   
}
