package Volume7_DimensionalArrays;
import java.util.*;
public class DAQ14{
    public static void main(String[] args){
        int[] Num = {3,1,2,6,4,1,6,1,3,4};
        int[] Rev = {3,1,2,6,4,1,6,1,9,4};
        int MaximumLength = Num.length - 1;
        for (int x = 0; x < MaximumLength; x++){
            for (int y = 0; y < (MaximumLength - x); y++){
                if(Rev[y] > Rev[y+1]){
                    int temp = Rev[y];
                    Rev[y] = Rev[y+1];
                    Rev[y+1] = temp;
                }
            }
        }
        System.out.println("Your Array: " + Arrays.toString(Num));
        System.out.println("Revised Array: " + Arrays.toString(Rev));
    }
}