import java.util.Scanner;

public class Figure{
    Scanner input = new Scanner(System.in);
    int sides = 0;
    String Shapes;
    public void getFigure(){
        System.out.print("Enter Number of Sides: ");
        sides = input.nextInt();
    }

    public void setFigure(){
        if (sides == 0){
            Shapes = "Nothing";
        } else if (sides == 1){
            Shapes = "Point";
        } else if (sides == 2){
            Shapes = "Line";
        } else if (sides == 3){
            Shapes = "Triangle";
        } else if (sides == 4){
            Shapes = "Quadrilateral";
        } else if (sides == 5){
            Shapes = "Pentagon";
        } else if (sides == 6){
            Shapes = "Hexagon";
        } else if (sides == 7){
            Shapes = "Septagon";
        } else if (sides == 8){
            Shapes = "Octogon";
        } else if (sides == 9){
            Shapes = "Nonagon";
        } else if (sides == 10){
            Shapes = "Decagon";
        } else {
            Shapes = "Polygon";
        }
    }
    public void displayFigure(){
        System.out.println("Shape Result: " + Shapes);
    }

    public static void main(String[] args){
        Figure F1 = new Figure();
        Figure F2 = new Figure();
        F1.getFigure();
        F2.getFigure();
        F1.setFigure();
        F2.setFigure();
        F1.displayFigure();
        F2.displayFigure();
    }
}
