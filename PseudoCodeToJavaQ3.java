//PseudoCodeToJavaQ3 (C to F and F to C Convertor)
public class PseudoCodeToJavaQ3 {
    public static void main(String[] args) {
        float C = 18;
        float F = 19;
        int x = 1;
        int Choice = 1;
        do{
            if (Choice == 1){
                F = (C * (9/5)) + 32;
                System.out.println("Temperature in Farenheit: " + F);
            } else if (Choice == 2){
                C = (F - 32) * (5/9);
                System.out.println("Temperature in Celcius: " + C);
            }  
            x = x + 1;
        } while (x <= 10);
    }
}