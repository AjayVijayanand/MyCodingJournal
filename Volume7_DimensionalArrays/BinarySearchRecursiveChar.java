
import java.util.*;
public class BinarySearchRecursiveChar{
    static void BinarySearch(int Search, int[] Array, int S, int E){
        int Mid = (S + E)/2;
        if ((S <= Mid && Mid <= E)){
            if (Array[Mid] == Search){
                System.out.println("Character is First Found at: " + Mid);
            }
            if (Search < Array[Mid]){
                BinarySearch(Search, Array, 0, Mid - 1);
            }
            if (Search > Array[Mid]){
                BinarySearch(Search, Array, Mid + 1, E);
            }
        } else {
            System.out.println("Character is not Found!");
        }   
    }
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int[] Character = {'a', 'b', 'd', 'e', 'v', 'x', 'y', 'z', 'z'};
        System.out.print("What Character do you want to search: ");
        int SearchChar = input.next().charAt(0);
        BinarySearch(SearchChar, Character, 0, Character.length - 1);
    }
}