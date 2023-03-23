class Program
{
    static async Task<int> PassarCafe()
    {
        int qtdCafe = 0;

        await Task.Run(() => //Criando outra Thread para 'passar o café'
        {
            for (int i = 0; i < 10; i++)
            {
                Console.WriteLine($"Passando Café {i}");
                Thread.Sleep(1000);
                qtdCafe++;
            }
            Console.WriteLine("Café pronto");
        });
        return qtdCafe;        
    }

    static void TostarPao()
    {
        for (int i = 0; i < 5; i++)
        {
            Console.WriteLine($"Tostando Pão {i}");
            Thread.Sleep(1000);
        }
        Console.WriteLine("Pão pronto");
    }

    static void Main(string[] args) //Quando o Main é executado, é executada uma única thread
    {
        Task<int> taskPassarCafe = PassarCafe();
        TostarPao();

        taskPassarCafe.Wait();

        int qtdCafe = taskPassarCafe.Result; //Obtendo o valor da variável de retorno
        Console.WriteLine($"Café da manhã na mesa! - Quantidade de Café: {qtdCafe}");
        Console.ReadKey();
    }
}