
import java.util.*;
public class DAQ16{
    public static void main(String[] args){
        String[] Rev = {"HELLO", "WORLD","MY", "NAME", "IS", "SOMEBODY"};
        System.out.println("Your Array: " + Arrays.toString(Rev));
        int MaximumLength = Rev.length - 1;
        for (int x = 0; x < MaximumLength; x++){
            for (int y = 0; y < (MaximumLength - x); y++){
                if(Rev[y].compareTo(Rev[y+1]) > 0){
                    String temp = Rev[y];
                    Rev[y] = Rev[y+1];
                    Rev[y+1] = temp;
                }
            }
        }
        System.out.println("Revised Array: " + Arrays.toString(Rev));
    }
}