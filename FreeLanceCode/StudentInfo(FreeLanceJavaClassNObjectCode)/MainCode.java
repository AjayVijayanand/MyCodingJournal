public class MainCode{
    public static void main(String[] args){
        int x = 3;
        StudentBio[] Students = new StudentBio[x];
        Students[0] = new StudentBio("AJ", 17, 9, 1, 2004);
        Students[1] = new StudentBio("VJ", 11, 9, 11, 2004);
        Students[2] = new StudentBio("DJ", 9, 10, 12, 2004);
        for(StudentBio e : Students){
            System.out.println(e.getName());
            System.out.println(e.getAge());
            System.out.println(e.getDOB());
        }
    }
}
