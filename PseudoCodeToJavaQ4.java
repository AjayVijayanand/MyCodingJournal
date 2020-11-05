public class PseudoCodeToJavaQ4 {
    public static void main(String[] args){
        int num = 6;
        boolean Prime = true;
        for (int x = 2; x < num; x++){
            if (num % x == 0){
                System.out.println("Number is Not Prime");
                Prime = false;
                break;
            }
        }
        if(Prime == true){
            System.out.println("Number is a Prime");
        }
    }
}
