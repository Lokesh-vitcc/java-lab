import java.util.Scanner;
public class ScannerMethods{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Welcome to back of buruda");
        System.out.print("Enter Your name:");
        String name = sc.nextLine();
        System.out.print("Enter your age:");
        int age = sc.nextInt();
        System.out.print("Enter your bank balance:"); 
        double balance = sc.nextDouble();
        System.out.println("YOUR INFO");
        System.out.println("NAME:".concat(name));
        System.out.println("AGE:"+age);
        System.out.println("BALANCE:"+balance);

    }
}
    