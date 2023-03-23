using System.Security.Cryptography.X509Certificates;

internal class Program
{
    private static void Main(string[] args)
    {
       
     var lista = new List<int>() { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

        //var listaFiltrada = lista.Where(Filtro); //Passando função como referencia, e não executando ela: Filtro()
        var listaFiltrada = lista.Where(x => x > 4);

        foreach (var x in listaFiltrada)
        {
            Console.WriteLine(x);
        }
    }

    public bool Filtro(int x)
    { 
        return x > 4;
    }

}