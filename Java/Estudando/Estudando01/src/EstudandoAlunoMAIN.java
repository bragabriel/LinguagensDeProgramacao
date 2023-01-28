public class EstudandoAlunoMAIN {

	public static void main(String[] args) {
		
		//instanciando o objeto:
		Aluno aluno1 = new Aluno();
		
		//declarando valores aos atributos:
		aluno1.nome = "Gabriel";
		aluno1.idade = 19;
		aluno1.curso = "Sistemas de informação";
		
		//chamando os métodos:
		aluno1.assistirAula();
		aluno1.fazerProva();
		aluno1.calcularNota();

	}

}
