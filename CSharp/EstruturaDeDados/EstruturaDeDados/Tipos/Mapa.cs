using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EstruturaDeDados.Tipos
{
    public class Mapa
    {
        public static void mapa()
        {
            IDictionary<string, string> exemploDictionary = new Dictionary<string, string>()
            {
                {"QA","Mauricio"},
                {"DEV","Marcelo"},
                {"PO","Guilherme"},
                {"AM","Paulo"}
            };

            //exemploDictionary.Add("DEV", "Joao"); não pode chave duplicada
            exemploDictionary.Remove("QA");

            foreach (KeyValuePair<string, string> item in exemploDictionary)
            {
                Console.WriteLine("chave: {0}, valor: {1}", item.Key, item.Value);
            }
        }
    }
}
