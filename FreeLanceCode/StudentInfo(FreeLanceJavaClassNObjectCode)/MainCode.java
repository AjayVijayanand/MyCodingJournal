import java.util.*;
public class MainCode{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("Enter Number of Students:");
        int Range = input.nextInt();
        Person[] Students = new Person[Range];
        for(int x = 0; x < Range; x++){
            System.out.println("Enter Name of Student:");
            String Name = input.nextLine();
            System.out.println("Enter Age of Student:");
            int Age = input.nextInt();
            System.out.println("Enter Month of Student's Birth:");
            int DOB = input.nextInt();
            System.out.println("Enter Day of Student's Birth:");
            int MOB = input.nextInt();
            System.out.println("Enter Year of Student's Birth:");
            int YOB = input.nextInt(x);
            Students[x] = Person(Name, Age, DOB, MOB, YOB);
        }
        for(Person f : Students){
            System.out.println("Name: " + f.getName());
            System.out.println("Age: " + f.getAge());
            System.out.println("Date of Birth: " + f.getDOB());
        }

    }
}
