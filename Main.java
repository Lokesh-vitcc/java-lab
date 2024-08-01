import java.util.Scanner;
class Main{
    public static void main(String args[]){
        // int arr[] = {1,2,3,4,5,6,7,8,9,0};
        // Array arr = new Array();
        Scanner sb = new Scanner(System.in);
        System.err.println("Enter Numbers of array:");
        for (;;){
            System.out.println(">>>");
            sb.nextLine()
        }
        int max[]= {0,0,0};
        for (int i=0;i<arr.length;i++){
            int val=arr[i];
            for (int j=0; j<max.length;j++){
                if (max[j] < val){
                    int tmp = max[j];
                    max[j]=val;
                    val = tmp;
                }
            }
        }
        System.out.println("3rd largest number is:"+max[max.length-1]);
    }
}