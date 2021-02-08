import java.util.*;
public class DAQB {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int[] Num = {3,1,2,6,4,1,6,1,3,4};
        int[] Rev = {3,1,2,6,4,1,6,1,9,4};
        for (int x = 0; x < 9; x++){
            for (int y = 0; y < 10; y++){
                if(Rev[y] > Rev[y+1]){
                    System.out.println(Arrays.toString(Rev));
                    int temp = Rev[y];
                    Rev[y] = Rev[y+1];
                    Rev[y+1] = temp;
                }
            }
        }
    }
}
