import java.util.*;
public class DAQC {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        char[] Character = {'a', 'b', 'd', 'c', 'x', 'y', 'z', 'r', 'q'};
        boolean Validation = false;
        int Index = 0;
        while (!Validation){
            System.out.print("Enter where you want to remove an element (0 - " + Character.length  + "): ");
            Index = input.nextInt();
            if (Index < Character.length && Index >= 0){
                Validation = true;
            } else {
                System.out.println("Enter Valid Index");
            }
        }
        char[] Rev = new char[Character.length - 1];
        for(int x = 0, y = 0; x <= Rev.length; x++){
            if (x == Index) {
                continue;
            } else {
                Rev[y++] = Character[x];
            }
        }
        System.out.println("Your Array: " + Arrays.toString(Character));
        System.out.println("Revised Array: " + Arrays.toString(Rev));
        String[] R = new String[5];
        System.out.println("Revised Array: " + Arrays.toString(R));
    }
}
