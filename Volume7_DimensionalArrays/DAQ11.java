import java.util.*;
public class DAQ11{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int[] Num = {1, 2, 3, 4, 5, 6, 8, 9};
        int[] Rev = new int[Num.length + 1];
        int Index = 0;
        Boolean Added = false;
        System.out.print("Enter Number To add: ");
        int Element = input.nextInt();
        for(int x = 0; x <= Num.length - 1; x++){
            if (Num[Index] < Element){
              Index = x;
            }
        }
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