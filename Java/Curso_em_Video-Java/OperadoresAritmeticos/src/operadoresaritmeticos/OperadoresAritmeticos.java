/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package operadoresaritmeticos;

import java.util.Random;

/**
 *
 * @author birio
 */
public class OperadoresAritmeticos {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int n1 = 3;
        int n2 = 5;
        float m = (n1 + n2)/2;
        
        System.out.println("A média é igual a " + m);
        
        int numero = 5;
        int valor = 5 + numero++;
        System.out.println(valor); 
       
        
        //Math library
        System.out.println("\nMath.floor & Math.ceil");
        float v = 8.3f;
        int ar = (int) Math.floor(v);
        System.out.println(ar);
        ar = (int) Math.ceil(v);
        System.out.println(ar);
        
        
        System.out.println("\nMath.round");
        float r = 8.5f;
        int ro = (int) Math.round(r);
        System.out.println(ro);
         
        r = 8.4f;
        ro = (int) Math.round(r);
        System.out.println(ro);
        
        
        System.out.println("\nMath.random 0-1 (double)");
        double ale = Math.random();
        System.out.println(ale);
        
        
        System.out.println("\nMath.random 0-10 (int)");
        Random rand = new Random();
        int c = rand.nextInt(10);
        System.out.println(c);
        
    }
}
