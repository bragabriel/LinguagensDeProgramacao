using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EstruturaDeDados.Tipos
{
    public class Lista
    {
        public static void lista()
        {
            //Lista de Objeto:
            //List<Produto> listaProdutos = new List<Produto>();

            List<string> listaNomes = new List<string>();
            listaNomes.Add("Mauricio");
            listaNomes.Add("Marcelo");
            listaNomes.Add("Guilherme");
            listaNomes.Add("Paulo");
            listaNomes.Add("João");
            listaNomes.Remove("Guilherme");
            listaNomes.Remove("João");

            foreach (String item in listaNomes)
            {
                Console.WriteLine(item);
            }

        }
         
    }
}
