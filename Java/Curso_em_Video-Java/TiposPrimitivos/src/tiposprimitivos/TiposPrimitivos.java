/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package tiposprimitivos;

import java.util.Scanner;

/**
 *
 * @author birio
 */
public class TiposPrimitivos {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        float nota = 8.5f;
        float nota2 = (float) 9.5;
        
       
        
        System.out.println("A nota eh " + nota);
        System.out.printf("A nota eh %.2f \n", nota2);
        
        Scanner teclado = new Scanner(System.in);
        
        System.out.println("Insira um nome: ");
        
        String nome = teclado.nextLine();
        
        System.out.println("A nota de " + nome + " eh: " + nota2);
        
        
        //Int para String
        int idade = 20;
        String valor = Integer.toString(idade);
        System.out.println("Int para String: " + valor);

        //String para Int
        String valor2 = "20";
        int idade2 = Integer.parseInt(valor2);
        System.out.println("String para Int: " + idade2);
        
        //String para Float
        String valor3 = "21";
        float idade3 = Float.parseFloat(valor3);
        System.out.println("String para Float: " + idade3);
    }
    
}
