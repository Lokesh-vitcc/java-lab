class StringBufferExample1{
    public static void main(String args[]){
        StringBuffer sb = new StringBuffer("Holaa");
        sb.append(" Dude");
        System.out.println(sb.substring(4));
        System.out.println(sb.substring(4,7));
    }
}