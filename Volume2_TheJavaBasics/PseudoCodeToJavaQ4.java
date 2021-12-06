
public class PseudoCodeToJavaQ4 {
    public static void main(String[] args){
        int num = 40;
        int Factors = 0;
        for (int x = 2; x < num; x++){
            if (num % x == 0){
                Factors = Factors + 1;
            }
        }
        if(Factors == 0){
            System.out.println("Number is a Prime");
        } else{
            System.out.println("Number is Not A Prime. It has this many factors: " + (Factors + 2));
    }
}
}
