class StringBufferExample3{
    public static void main(String args[]){
        StringBuffer sb = new StringBuffer("Holaa");
        sb.append(" JAVA");
        sb.replace(1,3,"Java");
        System.out.println(sb);
    }
}