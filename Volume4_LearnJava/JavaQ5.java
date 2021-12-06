public class JavaQ5 {
    public static void main(String[] args){
        int PrimeNo = 1;
        int PrimeNo2 = 1;
        for (int x = 1; x <= 100; x++){
            int Factor = 0;
            for (int y = 1; y <= x; y++){
                if (x % y == 0){
                    Factor++;
                }
            }
            if (Factor == 2){
                PrimeNo2 = PrimeNo;
                PrimeNo = x;
                if((PrimeNo - PrimeNo2) == 2){
                    System.out.println(PrimeNo2 + ", " + PrimeNo + ": Is a Twin Prime");
                }
            }
        }
    }
}
