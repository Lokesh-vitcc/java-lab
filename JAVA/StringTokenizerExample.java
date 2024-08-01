import java.util.StringTokenizer;
public class StringTokenizerExample{
    public static void main(String[] arg){
        StringTokenizer st = new StringTokenizer("My name is LOKESH, currently at the JAVA lab."," ");
        while (st.hasMoreTokens()){
            System.out.println(st.nextToken());
        }
    }
}