/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package operadorternario;

/**
 *
 * @author birio
 */
public class OperadorTernario {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int n1, n2, result;
        
        n1 = 4;
        n2 = 8;
        
        result = (n1>n2)?n1+n2:n1-n2;
        //if true (n1+n2) else (n1-n2)
        
        System.out.println(result);
        
        
        String nome1 = "Gabriel";
        String nome2 = "Gabriel";
        String nome3 = new String("Gabriel");
        
        String res;
        
        res = (nome1==nome2)?"Eh igual":"Nao eh igual";
        System.out.println(res);
        
        res = (nome1==nome3)?"Eh igual":"Nao eh igual"; //Diferente pois compara tbm o tipo (Objeto x String)
        System.out.println(res);
        
        res = (nome1.equals(nome3))?"Eh igual":"Nao eh igual"; //Conteúdo do objeto é igual ao 'nome3'?
        System.out.println(res); 
        
        
        int x, y, z;
        x = 4;
        y = 7;
        z = 12;
        
        boolean r;
        
        r = (x<y && y<z)?true:false;
        
        System.out.println(r);
    }
    
}
