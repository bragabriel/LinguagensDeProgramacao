using EstruturaDeDados.Tipos;

public class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Main Program");

        Console.WriteLine("\nLista: ");
        Lista.lista();
        Console.WriteLine("\nFila: ");
        Fila.fila();
        Console.WriteLine("\nPilha: ");
        Pilha.pilha();
        Console.WriteLine("\nMapa: ");
        Mapa.mapa();
    }
}