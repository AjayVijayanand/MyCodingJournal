//Java Code to read  a number 1 to 7 from user and print respective day of week e.g if user enters 1 code prints Monday 
import java.util.*;

public class FA2PSCJAVAQ6 {
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("1 - Sunday\n2 - Monday\n3 - Tuesday\n4 - Wednesday\n5 - Thursday\n6 - Friday\n7 - Saturday\nEnter Day:");
        int Day = input.nextInt();
        switch(Day){
            case 1:
                System.out.println("It's Sunday");
                break;
            case 2:
                System.out.println("It's Monday");
                break;
            case 3:
                System.out.println("It's Tuesday");
                break;
            case 4:
                System.out.println("It's Wednesday");
                break;
            case 5:
                System.out.println("It's Thursday");
                break;
            case 6:
                System.out.println("It's Friday");
                break;
            case 7:
                System.out.println("It's Saturday");
                break;
            default:
                System.out.println("ITS SOME DAY!");
        }
    }
}