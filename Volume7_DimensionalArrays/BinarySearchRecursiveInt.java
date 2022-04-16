
import java.util.*;
public class BinarySearchRecursiveInt{
    static void BinarySearch(int Search, int[] Array, int S, int E){
        int Mid = (S + E)/2;
        if (S <= Mid && Mid <= E){
            if (Array[Mid] == Search){
                System.out.println("Number is First Found at: " + Mid);
            }
            if (Search > Array[Mid]){
                BinarySearch(Search, Array, 0, Mid - 1);
            }
            if (Search < Array[Mid]){
                BinarySearch(Search, Array, Mid + 1, E);
            }
        } else {
            System.out.println("Number is not Found!");
        }
    }
    public static void main(String[] args){
        try (Scanner input = new Scanner(System.in)) {
            int[] Num = {9, 8, 7, 6, 5, 5, 3, 2, 1};
            System.out.print("What Number do you want to search: ");
            int SearchNum = input.nextInt();
            BinarySearch(SearchNum, Num, 0, Num.length - 1);
        }
    }
}