import java.util.*;
public class DAQ7{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        char[] Characters = {'a', 'c', 'd', 'c', 'b', 'a', 'a'};
        boolean Found = false;
        System.out.print("What Character do you want to search: ");
        char Search = input.next().charAt(0);
        System.out.println("Your Array: " + Arrays.toString(Characters));
        System.out.println("Element Searched: " + Search);
        for(int x = 0; x <= (Characters.length - 1); x++){
            if (Characters[x] == Search){
                System.out.println("Element found at Index: " + x);
                Found = true;
            }
        }
        if(!Found){
            System.out.println("Element not found!");
        }
    }
}