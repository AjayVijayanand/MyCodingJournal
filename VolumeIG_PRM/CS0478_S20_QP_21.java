import java.util.*;
public class CS0478_S20_QP_21{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        String Phone[][] = {
            {"BPCM", "Compact", "29.99"},
            {"BPSH", "Clam Shell", "49.99"},
            {"RPSS", "RoboPhone – 5-inch screen and 64GB memory", "199.99"},
            {"RPLL", "RoboPhone – 6-inch screen and 256GB memory", "499.99"},
            {"YPLS", "Y-Phone Standard – 6-inch screen and 64GB memory", "549.99"},
            {"YPLL", "Y-Phone Deluxe – 6-inch screen and 256GB memory", "649.99"}
        };
        String Tablet[][] = {
            {"RTMS", "RoboTab – 8-inch screen and 64GB memory", "149.99"},
            {"RTLM", "RoboTab – 10-inch screen and 128GB memory", "299.99"},
            {"YTLM", "Y-Tab Standard – 10-inch screen and 128GB memory", "499.99"},
            {"YTLL", "Y-Tab Deluxe – 10-inch screen and 256GB memory", "599.99"}
        };
        String SIM[][] = {
            {"SMNO", "SIM Free (no SIM card purchased)", "0.00"},
            {"SMPG", "Pay As You Go (SIM card purchased)", "9.99"}
        };
        String Case[][] = {
            {"CSST", "Standard", "0.00"},
            {"CSLX", "Luxury", "50.00"}
        };
        String Charger[][] = {
            {"CGCR", "Car", "19.99"},
            {"CGHM", "Home", "15.99"}
        };
        boolean Validation1 = false;
        boolean Validation2 = false;
        boolean Validation3 = false;
        boolean Validation4 = false;
        boolean Validation5 = false;
        boolean Validation6 = false;
        String Choice1 = "P";
        String Choice2 = "BPCM";
        System.out.println();
        System.out.println("PHONES");
        System.out.println("CODE | DESCRIPTION | PRICE");
        for(int x = 0; x < Phone.length; x++){
            for(int y = 0; y <= 2; y++){
                System.out.print(Phone[x][y] + " | ");
            }
            System.out.println();
        }
        System.out.println();
        System.out.println("TABLETS");
        System.out.println("CODE | DESCRIPTION | PRICE");
        for(int x = 0; x < Tablet.length; x++){
            for(int y = 0; y <= 2; y++){
                System.out.print(Tablet[x][y] + " | ");
            }
            System.out.println();
        }
        System.out.println();
        System.out.println("SIM CARDS");
        System.out.println("CODE | DESCRIPTION | PRICE");
        for(int x = 0; x < SIM.length; x++){
            for(int y = 0; y <= 2; y++){
                System.out.print(SIM[x][y] + " | ");
            }
            System.out.println();
        }
        System.out.println();
        System.out.println("CASE");
        System.out.println("CODE | DESCRIPTION | PRICE");
        for(int x = 0; x < Case.length; x++){
            for(int y = 0; y <= 2; y++){
                System.out.print(Case[x][y] + " | ");
            }
            System.out.println();
        }
        System.out.println();
        System.out.println("CHARGERS");
        System.out.println("CODE | DESCRIPTION | PRICE");
        for(int x = 0; x < Charger.length; x++){
            for(int y = 0; y <= 2; y++){
                System.out.print(Charger[x][y] + " | ");
            }
            System.out.println();
        }
        System.out.println();
        while (!Validation1){
            System.out.print("What Do you want to buy, Phone(P) or Tablet(T): ");
            Choice1 = input.nextLine();
            System.out.println(Choice1 == "T");
            System.out.println(Choice1 == "P");
            System.out.println(Choice1);
            if ((Choice1 == "T") || (Choice1 == "P")){
                Validation1 = true;
            } else {
                System.out.println("Enter P or T");
            }
        }
        while (!Validation2){
            if(Choice1 == "P"){
                System.out.print("Enter code of the Phone you want to buy: ");
                Choice2 = input.next();
                for(int x = 0; x < Phone.length; x++){
                    if(Phone[x][0] == Choice2){
                        Validation2 = true;
                        break;
                    }
                }
                if (!Validation2){
                    System.out.println("Enter Valid Phone ID");
                }
            }
        }
    }    
}