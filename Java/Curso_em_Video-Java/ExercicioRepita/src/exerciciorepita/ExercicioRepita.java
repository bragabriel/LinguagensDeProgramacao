/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package exerciciorepita;

import javax.swing.JOptionPane;

/**
 *
 * @author birio
 */
public class ExercicioRepita {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        JOptionPane.showMessageDialog(null, "Olá, Mundo!", "Boas Vindas", JOptionPane.INFORMATION_MESSAGE);
    
        int n, sum = 0, even=0, odd=0, above100=0, average=0, cont=0;
        
        do{
            n = Integer.parseInt(JOptionPane.showInputDialog(null,
                    "<html>Informe um número: <br> <em>(valor 0 interrompe)</em></html>"));
            sum += n;
            
            if(n % 2 == 0){
                even++;
            }else{
                odd++;
            }
            
            if(n>100){
                above100++;
            }
            
            cont++;
            
        }while(n!=0);
        
        average = sum/cont;
        
        JOptionPane.showMessageDialog(null,
                "<html> Resultado final<hr>" + 
                        "<br>Total de valores: " + (cont-1) +
                        "<br>Total de pares: " + (even-1) +
                        "<br>Total de ímpares: " + odd +
                        "<br>Acima de 100: " + above100 +
                        "<br>Média dos valores: " + average +
                "</html>");
    }
    
}
