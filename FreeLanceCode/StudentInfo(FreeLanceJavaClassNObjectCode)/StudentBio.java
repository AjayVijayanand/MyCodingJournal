import java.time.LocalDate;
public class StudentBio{
    private String Name;
    private int Age;
    private LocalDate DOB;
    public StudentBio(String n, int a, int d, int m, int y){
        Name = n;
        Age = a;
        DOB = LocalDate.of(y, m, d);
    }

    public String getName(){
        return Name;
    }

    public int getAge(){
        return Age;
    }

    public LocalDate getDOB(){
        return DOB;
    }
}