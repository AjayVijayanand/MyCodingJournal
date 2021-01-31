import java.util.*;
public class DAQ14{
    public static void main(String[] args){
        int[] Num = {3,1,2,6,4,1};
        int[] Rev = {3,1,2,6,4,1};
        int MaximumLength = Num.length;
        for (int x = 0; x < MaximumLength - 1; x++){
            for (int y = 0; y < (MaximumLength - x - 1); y++){
                if(Rev[y] > Rev[y+1]){
                    System.out.println(Arrays.toString(Rev));
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