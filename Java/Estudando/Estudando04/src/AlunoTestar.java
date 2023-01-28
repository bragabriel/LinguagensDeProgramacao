
public class AlunoTestar {

	public static void main(String[] args) {

		Aluno aluno1 = new Aluno();
		

		//nao vai funcionar pois está PRIVATE: 
		//aluno1.setNome = "Gabriel";
		
		aluno1.setNome("Gabriel");

		System.out.println(aluno1.getNome());
		
		//aluno1.idade = 500;
		aluno1.setIdade(500);
	}

}
