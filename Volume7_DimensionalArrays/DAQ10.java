package Volume7_DimensionalArrays;
import java.util.*;
public class DAQ10{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        char[] Character = {'a', 'b', 'd', 'c', 'x', 'y', 'z', 'r', 'q'};
        boolean Validation = false;
        int Index = 0;
        System.out.print("Enter Character: ");
        char Element = input.next().charAt(0);
        while (!Validation){
            System.out.print("Enter where you want to add a element (0 - " + Character.length  + "): ");
            Index = input.nextInt();
            if (Index < Character.length && Index >= 0){
                Validation = true;
            } else {
                System.out.println("Enter Valid Index");
            }
        }
        char[] Rev = new char[Character.length + 1];
        Boolean Added = false;
        for(int x = 0; x <= Character.length; x++){
            if (!Added){
                if(x == Index){
                    Rev[x] = Element;
                    Added = true;
                } else {
                    Rev[x] = Character[x];
                }
            } else {
                Rev[x] = Character[x-1];
            }
        }
        System.out.println("Your Array: " + Arrays.toString(Character));
        System.out.println("Revised Array: " + Arrays.toString(Rev));
    }
}