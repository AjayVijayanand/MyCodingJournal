import java.util.*;

public class J3Q8 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("Enter number pattern");
        int n = input.nextInt();
        int z = n;
        int c = 0;
        int RD = 0;
        int LD = 0;
        for(int x = 1; x <= n; x++){
            for(int y = 1; y <= n; y++){
                c++;
                System.out.print(c + " "); 
                if (x == y){
                    LD = LD + c;
                } else if (x == z){
                    RD = RD + c;
                }
            }
            System.out.println();
            z--;
        }
        System.out.println("Right Diagonal: " + LD);
        System.out.println("Left Diagonal: " + LD);
    }   
}
