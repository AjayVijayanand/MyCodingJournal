package Volume10_TheHLCodes;
public class R2AQ3 {
    public static void main(String[] args) {
        int[][] Num = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };
        int LD = 0;
        int RD = 0;
        for (int R = 0; R < 3; R++){
                LD = LD + Num[R][R];
        }
        int C = 2;
        for (int R = 0; R < 3; R++){
                RD = RD + Num[R][C];
                C--;
        }
        System.out.println("LD: " + LD);
        System.out.println("RD: " + RD);
    } 
}
