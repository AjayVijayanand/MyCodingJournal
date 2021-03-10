package Volume8_CT2Practice;
import java.util.*;
public class CT2PQ1 {
    public static void main(String[] args){
        int[] Num = {1, 2, 3, 1, 2, 6, 7, 8, 9};
        boolean Duplicate = false;
        for (int x = 0; x < Num.length; x++){
            for (int y = x+1; y < Num.length; y++){
                if (Num[x] == Num[y]){
                    Duplicate = true;
                    System.out.println("Duplicate Found! It is at positions " + x + " And " + y + ". The Number in both of these positions is: " + Num[x]);
                }
            }
        }
        if (!Duplicate){
            System.out.println("Duplicate Not Found!");
        }
    }
}
