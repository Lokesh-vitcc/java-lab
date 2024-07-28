public class EnhancedFor {
    public static void main(String[] args) {
        String lyrics[] = "Let me write this sentence across 8 lines."
        .split(" "); 
        for (String word : lyrics){
            System.out.println(word);
        }
    }
}