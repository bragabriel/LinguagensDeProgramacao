public class TiposDeDados {

    public static void main(String[] args){

        //valores int ou negativos, requer 8bits, maximo 127 e minimo -128
        byte meuByte = 127;
        System.out.println("Byte: " + meuByte);

        //dobro de bit do byte, min -32768 e max 32767
        short meuShort = 32767;

        //32bits, min -2147483648 e max 2147483647
        int meuInt = 10;

        //64bits
        long meuLong = 10L;

        //dupla precisao, 64bits;
        double meuDouble = 201.30;

        //precisao simples. 32bits
        float meuFloat = 201.30F;

        //char
        char meuChar = 'C';

        //String
        String minhaString = "CCCC";

        //1bit
        boolean meuBoolean = true;
    }
}
