package Volume9_ObjectsAndClasses;
import java.util.*;

public class Travel {
    Scanner input = new Scanner(System.in);
    String T_Code = "Null";
    int No_of_Adults = 0;
    int No_of_Children = 0;
    int Distance = 0;
    float TotalFare = 0;

    public void AssignFare(){
        if(Distance >= 1000) {
            TotalFare = No_of_Adults * 500 + No_of_Children * 250;
        } else if (Distance < 1000 && Distance >= 500){
            TotalFare = No_of_Adults * 300 + No_of_Children * 150;
        } else {
            TotalFare = No_of_Adults * 200 + No_of_Children * 100;
        }
    }

    public void EnterTravel(){
        System.out.print("Enter Travel Code: ");
        T_Code = input.nextLine();
        System.out.print("Enter Number of Adults: ");  
        No_of_Adults = input.nextInt();
        System.out.print("Enter Number of Children: ");  
        No_of_Children = input.nextInt();
        System.out.print("Enter Distance Travelling: ");
        Distance = input.nextInt();
    }   

    public void ShowTravel(){
        System.out.println("Train Code: " + T_Code);
        System.out.println("Number of Adults: " + No_of_Adults);
        System.out.println("Number of Children: " + No_of_Children);
        System.out.println("Distance: " + Distance);
        System.out.println("Total Fare: $" + TotalFare);
    }

    public static void main(String[] args) {
        Travel T1 = new Travel();
        T1.EnterTravel();
        T1.AssignFare();
        T1.ShowTravel(); 
    }
}
