class StringBufferExample6{
    public static void main(String args[]){
        StringBuffer sb = new StringBuffer();
        System.out.println("size of empty buffer:"+sb.capacity());
        System.out.println(sb);
        System.out.println("Size after appending \"Hello\":"+sb.capacity());
        sb.append("java is my favourite language");
        System.out.println("Size after appending a long string:"+sb.capacity());

    }
}