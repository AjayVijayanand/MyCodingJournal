
import java.util.*;
public class DAQ15{
    public static void main(String[] args){
        int[] Num = {3,1,2,6,4,1};
        int[] Rev = {3,1,2,6,4,1};
        for (int x = 0; x < Num.length - 1; x++){
            int Index = x;
            for (int y = (x + 1); y < Num.length; y++){
                if (Rev[Index] > Rev[y]){
                    Index = y;
                }
            }
            int temp = Rev[Index];
            Rev[Index] = Rev[x];
            Rev[x] = temp;
        }
        System.out.println("Your Array: " + Arrays.toString(Num));
        System.out.println("Revised Array: " + Arrays.toString(Rev));
    }
}