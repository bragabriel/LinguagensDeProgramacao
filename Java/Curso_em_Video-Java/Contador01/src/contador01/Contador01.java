/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package contador01;

/**
 *
 * @author birio
 */
public class Contador01 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int cc = 1;
        
        while(cc<=5){
            System.out.println("Cambalhota " + cc);
            cc++;
        }
        
        
        System.out.println("\n\n");
        
        
        cc = 0;
        while(cc<15){
            cc++;
            if(cc == 5 || cc == 7 || cc == 9){
                continue;
            }
            if(cc == 10){
                break;
            }
                System.out.println("Estrelinha" + cc);
        }
        
         
        System.out.println("\n\n");
        
         
        cc = 0;
        
        do{
            System.out.println(cc);
            cc++;
        }while(cc < 4);
        }
    }
   