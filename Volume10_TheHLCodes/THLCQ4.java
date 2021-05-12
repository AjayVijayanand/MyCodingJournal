import java.util.*;

public class THLCQ4{
    static Scanner input = new Scanner(System.in);
    public static float[][] AddingMatrix(float[][] M1, float[][] M2){
        float[][] MR = new float[2][2];
        for (int i = 0; i < MR.length; i++){
            for (int j = 0; j < MR[i].length; j++){
                MR[i][j] = M1[i][j] + M2[i][j];
            }
        }
        return MR;
    }

    public static float[][] SubtractingMatrix(float[][] M1, float[][] M2){
        float[][] MR = new float[2][2];
        for (int i = 0; i < MR.length; i++){
            for (int j = 0; j < MR[i].length; j++){
                MR[i][j] = M1[i][j] - M2[i][j];
            }
        }
        return MR;
    }

    public static float[][] MultiplyingMatrix(float[][] M1, float[][] M2){
        float[][] MR = new float[2][2];
        MR[0][0] = (M1[0][0] * M2[0][0]) + (M1[0][1] * M2[1][0]);
        MR[0][1] = (M1[0][0] * M2[0][1]) + (M1[0][1] * M2[1][1]);
        MR[1][0] = (M1[1][0] * M2[0][0]) + (M1[1][1] * M2[1][0]);
        MR[1][1] = (M1[1][0] * M2[0][1]) + (M1[1][1] * M2[1][1]);
        return MR;
    }

    public static float[][] InverseMatrix(float[][] M){
        float[][] MR = new float[2][2];
        float d = (M[0][0] * M[1][1]) - (M[0][1] * M[1][0]);
        float D = 1/d;
        MR[0][0] = M[1][1];
        MR[0][1] = -M[1][0];
        MR[1][0] = -M[0][1];
        MR[1][1] = M[0][0];
        for (int i = 0; i < MR.length; i++){
            for (int j = 0; j < MR[i].length; j++){
                MR[i][j] =  D * MR[i][j];
            }
        }
        return MR;
    }
    public static void main(String[] args) {
        float[][] Ma1 = new float[2][2];
        float[][] Ma2 = new float[2][2];
        float[][] MaR1 = new float[2][2];
        float[][] MaR2 = new float[2][2];
        float[][] MaR3 = new float[2][2];
        float[][] MI1 = new float[2][2];
        float[][] MI2 = new float[2][2];
        
        for (int i = 0; i < Ma1.length; i++){
            for (int j = 0; j < Ma1[i].length; j++){
                System.out.print("Enter Number for first Matrix: ");
                Ma1[i][j] = input.nextInt();
            }
        }
    
        for (int i = 0; i < Ma2.length; i++){
            for (int j = 0; j < Ma2[i].length; j++){
                System.out.print("Enter Number for second Matrix: ");
                Ma2[i][j] = input.nextInt();
            }
        }     
        
        MaR1 = AddingMatrix(Ma1, Ma2);
        MaR2 = SubtractingMatrix(Ma1, Ma2);
        MaR3 = MultiplyingMatrix(Ma1, Ma2);
        MI1 = InverseMatrix(Ma1);
        MI2 = InverseMatrix(Ma2);
        System.out.println("Matrix 1: " + Arrays.deepToString(Ma1));
        System.out.println("Matrix 2: " + Arrays.deepToString(Ma2));
        System.out.println("Added Result Matrix: " + Arrays.deepToString(MaR1));
        System.out.println("Subtracted Result Matrix: " + Arrays.deepToString(MaR2));
        System.out.println("Mulitplied Result Matrix: " + Arrays.deepToString(MaR3));
        System.out.println("Inverse Matrix 1: " + Arrays.deepToString(MI1));
        System.out.println("Inverse Matrix 2: " + Arrays.deepToString(MI2));
    }
}