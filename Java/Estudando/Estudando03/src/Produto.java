public class Produto {

	//atributos
	String nome;
	String marca;
	float valor; 
	
	
	//Construtores:
	/*
	 * Podem ter nomes iguais, se forem diferenciados nos parametros;
	 * 
	 * Construtor padrão: não recebe nada por parametro;
	 * 
	 * Se não definir o construtor padrão, 
	 * não vai ter como usar ele na hora de testar a classe	
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
