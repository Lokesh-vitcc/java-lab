import java.util.Scanner;
public class ConditionalStatements{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your age:");
        int age = sc.nextInt();
        if (age >=21){
            System.out.println("Don\'t do that");
        }
        else if (age >=18){
            System.out.println("you can go to deadpool and wolverine, enjoy liphe ;)");
        }else{
            System.out.println("You got a long fight my boi");
        }
        sc.close();
    }
}
    