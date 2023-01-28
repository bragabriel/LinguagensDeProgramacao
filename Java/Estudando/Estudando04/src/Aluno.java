
public class Aluno {

	private String nome;
	private int idade;
	
	
	//Dentro do m�todo, � possivel definir restri��es.
	//ex: o usuario n�o pode definir a idade dele = 500
	//se n�o fosse private, ele poderia.
	
	//Definindo modificador de acesso do m�todo:
	public void setNome(String nome) {
		this.nome = nome;
	} 
	
	
	//m�todo que retorna o nome (nome � do tipo String)
	public String getNome() {
		return nome;
	} 

	
	//m�todo set idade
	public void setIdade(int idade) {
		
		this.idade = idade;
		
		if(idade>0 && idade<110) {
			this.idade = idade;
			System.out.println("Idade cadastrada");
		}
		else {
			System.out.println("Erro! Idade � invalida");
		}
		
		
	}
	
}
