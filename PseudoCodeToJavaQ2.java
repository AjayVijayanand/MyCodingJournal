//PseudoCodeToJavaQ2 (Even Numbers without Multiples of 4)
public class PseudoCodeToJavaQ2 {
    public static void main(String[] args) {
        int x = 2;
        int c = 1;
        while (c <= 50){
            if (x % 4 == 0){
                x = x + 2;
                continue;
            }
            System.out.println(x);
            x = x + 2;
            c = c + 1;
        }
        System.out.println(c);
    }
}