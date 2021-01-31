import java.util.*;
public class DAQ11{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int[] Num = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        boolean Validation = false;
        int Index = 0;
        System.out.print("Enter Number: ");
        int Element = input.nextInt();
        while (!Validation){
            System.out.print("Enter where you want to add a element: ");
            Index = input.nextInt();
            if (Index < Num.length && Index > 0){
                Validation = true;
            } else {
                System.out.println("Enter Valid Index");
            }
        }
        int[] Rev = new int[Num.length + 1];
        Boolean Added = false;
        for(int x = 0; x <= Num.length; x++){
            if (!Added){
                if(x == Index){
                    Rev[x] = Element;
                    Added = true;
                } else {
                    Rev[x] = Num[x];
                }
            } else {
                Rev[x] = Num[x-1];
            }
        }
        System.out.println("Your Array: " + Arrays.toString(Num));
        System.out.println("Revised Array: " + Arrays.toString(Rev));
    }
}