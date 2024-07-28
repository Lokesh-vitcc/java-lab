public class TernaryOperator{
    public static void main(String args[]){
        int pnumber = 13400;
        char suffix = 'F';
        double boost = 4.6;
        String processor = "Intel Core i5 ";
        System.out.println(processor + pnumber + suffix + " @ "+boost+"GHz");
        String emotion;
        boolean isIntel = processor.toLowerCase().contains("intel");

        emotion = ( isIntel && 14999> pnumber && pnumber >12999) ? "PANIQUE":"VIBIN";
        System.out.println("Current state: "+emotion +" MODE");
    }
}