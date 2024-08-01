class StringBuilderTheExample{
    public static void main(String args[]){
        StringBuilder sb = new StringBuilder("Holaa");
        System.out.println("Initial String:"+ sb);
        System.out.println("Initial mutable String Object Size: "+ sb.capacity());
        sb.append(" Java. IAMNEO");
        System.out.println("Appended: "+ sb);
        sb.replace(0, 5, "Hello");
        System.out.println("replace: "+ sb);
        sb.substring(5,9);
        System.out.println("substring: "+ sb);
        sb.delete(10, 14);
        System.out.println("delete: "+ sb);
        sb.reverse();
        System.out.println("reverse: "+ sb);
        sb.ensureCapacity(30);
        System.out.println("mutable String Object size when 50Chars are stored: "+ sb.capacity());
        sb.capacity();
    }
}