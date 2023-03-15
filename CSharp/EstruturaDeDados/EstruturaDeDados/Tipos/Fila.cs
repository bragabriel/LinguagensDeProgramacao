using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EstruturaDeDados.Tipos
{
    internal class Fila
    {
        public static void fila()
        {
            // cria e inicaliza a fila - queue
            Queue<string> chamada = new Queue<string>();

            // insere elementos na fila
            chamada.Enqueue("Mauricio");
            chamada.Enqueue("Marcelo");
            chamada.Dequeue();
            chamada.Enqueue("Guilherme");
            chamada.Enqueue("Paulo");
            chamada.Dequeue();
            chamada.Enqueue("João");

            // percorre a fila
            foreach (var contador in chamada)
            {
                Console.Write(contador + "\n"); // imprime os nomes na fila na ordem inserida
            }
        }          
    }
}
