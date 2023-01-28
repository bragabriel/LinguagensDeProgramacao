public class Produto {

	//atributos
	String nome;
	String marca;
	float valor; 
	
	
	//Construtores:
	/*
	 * Podem ter nomes iguais, se forem diferenciados nos parametros;
	 * 
	 * Construtor padr�o: n�o recebe nada por parametro;
	 * 
	 * Se n�o definir o construtor padr�o, 
	 * n�o vai ter como usar ele na hora de testar a classe	
	 */
	Produto(){
		
	}
		
	
	Produto(String nome){
		this.nome = nome;
//esse 'nome' = atributo, vai receber a variavel de parametro
	}
	
	
	Produto(String nome, String marca){
		this.nome = nome;
		this.marca = marca;
	}
	
	
	Produto(String nome, String marca, float valor){
		this.nome = nome;
		this.marca = marca;
		this.valor = valor;
	}
	
}
