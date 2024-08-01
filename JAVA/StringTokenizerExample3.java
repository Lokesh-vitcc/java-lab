import java.util.*;
public class StringTokenizerExample3{
    public static void main(String[] arg){

        String Text ="My name is LOKESH, currently at the JAVA lab.\n"+
        "Our Sir asked us to add few more lines.\n"+
        "So that i am adding these 2 lines to make this string long engouh."+
        "\nI guess this will do!.";

        StringTokenizer st = new StringTokenizer("My name is LOKESH, currently at the JAVA lab.\nOur Sir asked us to add few more lines.\nSo that i am adding these 2 lines to make this string long engouh.\nI guess this will do!."," ");
        System.out.printf("Total number of tokens: %d\n", st.countTokens());
        // while (st.hasMoreElements()){
        //     System.out.println(st.nextToken());
        // }
    }
}