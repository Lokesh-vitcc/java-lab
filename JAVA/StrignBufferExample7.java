class StrignBufferExample7{
    public static void main(String args[]){
        StringBuffer sb = new StringBuffer();
        System.out.println("size of empty buffer:"+sb.capacity());
        System.out.println(sb);
        System.out.println("Size after appending \"Hello\": " + sb.capacity());
        sb.append("java is my favourite language");
        System.out.println("Size after appending a long string: " + sb.capacity());
        sb.ensureCapacity(50);
        System.out.println("content of size 50: "+sb.capacity());
    }
}