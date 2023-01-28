/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author birio
 */
public class ContadorPegadinhaRevisao {
    
    public static void main(String[] args) {
		
    substring("strawberrie");
    qtdHello();
    }
	
    public static void substring(String st) {
		
        st = "strawberries";
		
	System.out.println(st.substring(2,5));
    }
	
    public static void qtdHello() {
        for(int i=0; i<10; i=i++) {
            i+=1;
            System.out.println("Hello World!");
	}
		
        //Debuggando meu cérebro:
        int j = 0;
        j = j++;
        System.out.println(j); 
        
        /*
        int j = 0;
        //j = j++;
        System.out.println(j++); 
        */
        
         //Exemplo Guanabará
        int numero = 5;
        System.out.println("debug:");
        System.out.println("antes = " + numero);
        int valor = 5 + numero++;
        System.out.println("depois = " + numero);
        System.out.println(valor);
        System.out.println("depois do resultado= " + numero);
        
    }
}
