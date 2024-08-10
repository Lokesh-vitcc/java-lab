// import java.util.*;
public class classExample1{
    public static void main(String[] arg){
        Student[] arr;
        arr = new Student[3];
        arr[0] = new Student(1,"LOKESH");
        arr[1] = new Student(2,"AMAN");
        arr[2] = new Student();
        for (Student stu:arr){
            stu.display();
        }
    }
    
}
class Student{
    public int rollNo;
    public String name;
    Student(){
        this.rollNo =0;
        this.name = "UNKNOWN";
    }
    Student(int rollNo, String name){
        this.rollNo = rollNo;
        this.name = name;
    }
    void display(){
        System.out.printf("STUDENT %d\nNAME: %s\n",this.rollNo,this.name);
    }
}