public class StringConcatWithDifferentDTypes{
    public static void main(String args[]){
        int pnumber = 13400;
        char suffix = 'F';
        double boost = 4.6;
        String processor = "Intel Core i5 ";
        System.out.println(processor + pnumber + suffix + " @ "+boost+"GHz");
        
    }
}