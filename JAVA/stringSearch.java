public class stringSearch{
    public static void main(String args[]){
        String sentence = "this is some random sentence\n";
        System.err.println(sentence+"postitons:");
        System.out.println("\"random\":"+sentence.indexOf("random"));
        System.out.println("\"sentence\":"+sentence.indexOf("sentence"));
    }
}