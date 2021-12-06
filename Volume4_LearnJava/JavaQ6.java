import java.util.*;

public class JavaQ6 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("Enter number pattern");
        int n = input.nextInt();
        int c = 0;
        for(int x = 1; x <= n; x++){
            for(int y = 1; y <= x; y++){
                c++;
                System.out.print(c + " ");
            }
            System.out.println();
        }
    }
}
