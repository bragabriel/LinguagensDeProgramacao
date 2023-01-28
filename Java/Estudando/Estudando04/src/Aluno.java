
public class Aluno {

	private String nome;
	private int idade;
	
	
	//Dentro do método, é possivel definir restrições.
	//ex: o usuario não pode definir a idade dele = 500
	//se não fosse private, ele poderia.
	
	//Definindo modificador de acesso do método:
	public void setNome(String nome) {
		this.nome = nome;
	} 
	
	
	//método que retorna o nome (nome é do tipo String)
	public String getNome() {
		return nome;
	} 

	
	//método set idade
	public void setIdade(int idade) {
		
		this.idade = idade;
		
		if(idade>0 && idade<110) {
			this.idade = idade;
			System.out.println("Idade cadastrada");
		}
		else {
			System.out.println("Erro! Idade é invalida");
		}
		
		
	}
	
}
