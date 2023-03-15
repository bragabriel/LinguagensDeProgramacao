using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EstruturaDeDados.Tipos
{
    public class Pilha
    {
        public static void pilha()
        {
            // cria e inicializa uma pilha
            Stack exemploPilha = new Stack();

            // adicionando elementos na pilha utilizando o método push
            exemploPilha.Push("Mauricio");
            exemploPilha.Push("Marcelo");
            exemploPilha.Pop();
            exemploPilha.Push("Guilherme");
            exemploPilha.Push("Paulo");
            exemploPilha.Pop();
            exemploPilha.Push("Joao");

            // acessa os elementos da pilha e imprime
            foreach (var elemento in exemploPilha)
            {
                Console.WriteLine(elemento);
            }
        }
    }
}
