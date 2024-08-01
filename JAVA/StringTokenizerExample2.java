import java.util.*;
public class StringTokenizerExample2{
    public static void main(String[] arg){
        StringTokenizer st = new StringTokenizer("My,name,is,LOKESH,,currently,at,the,JAVA,lab.");
        while (st.hasMoreTokens()){
            System.out.printf("NEXT TOKEN IS %s\n",st.nextToken(","));
        }
    }
}