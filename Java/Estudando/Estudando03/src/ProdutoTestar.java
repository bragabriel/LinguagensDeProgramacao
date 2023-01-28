
public class ProdutoTestar {

	public static void main(String[] args) {
		
		
		//Construtor padrão:
		
//chamando a classe Produto
//dando o nome de: p1
		Produto p1 = new Produto();  //new Produto(); ???? Faz o que?
		p1.nome = "Caneta Preta";
		p1.marca = "Bic";
		p1.valor = 1.50f;
		
		
		//Construtor de dois parâmetros:
		
//chamando a classe Produto
//dando o nome de: p2
		Produto p2 = new Produto("Caneta Vermelha", "Faber");
		p2.valor = 1.70f;

		
		//Construtor de três parâmetros:
		
//chamando a classe Produto
//dando o nome de: p3
		Produto p3 = new Produto("Borracha", "Mercur", 1.89f);
		
		
		//Objeto p1
		System.out.println("Nome: " + p1.nome + "\n Marca: " + p1.marca + "\n Valor: " + p1.valor + "\n\n");
		
		//Objeto p2
		System.out.println("Nome: " + p2.nome + "\n Marca: " + p2.marca + "\n Valor: " + p2.valor + "\n\n");
		
		//Objeto p3
		System.out.println("Nome: " + p3.nome + "\n Marca: " + p3.marca + "\n Valor: " + p3.valor + "\n\n");
		
		
		
		
		
	}

}
