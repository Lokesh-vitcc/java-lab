class StringBufferExample4{
    public static void main(String args[]){
        StringBuffer sb = new StringBuffer("Holaa");
        sb.append(" JAVA");
        sb.delete(1,3);
        System.out.println(sb);
    }
}