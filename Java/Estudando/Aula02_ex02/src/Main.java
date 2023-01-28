
public class Main {

	public static void main(String[] args) {

		Aluno aluno1 = new Aluno();
		aluno1.setNome("Gabriel");
		aluno1.setRa(110080);
		aluno1.setNotaA1(9);
		aluno1.setNotaA2(10);
		aluno1.setFrequencia(100);
		aluno1.CalcularMedia();
		aluno1.getDadosAluno();
		aluno1.situacaoAluno();

		
		Aluno aluno2 = new Aluno();
		aluno2.setNome("José");
		aluno2.setRa(104490);
		aluno2.setNotaA1(5);
		aluno2.setNotaA2(4);
		aluno2.setFrequencia(75);
		aluno2.CalcularMedia();
		aluno2.getDadosAluno();
		aluno2.situacaoAluno();
		
		
		Aluno aluno3 = new Aluno();
		aluno3.setNome("Maria");
		aluno3.setRa(102780);
		aluno3.setNotaA1(10);
		aluno3.setNotaA2(8);
		aluno3.setFrequencia(74);
		aluno3.CalcularMedia();
		aluno3.getDadosAluno();
		aluno3.situacaoAluno();
		
		
		Aluno aluno4 = new Aluno();
		aluno4.setNome("Fulano");
		aluno4.setRa(809900);
		aluno4.setNotaA1(7.5f);
		aluno4.setNotaA2(6.4f);
		aluno4.setFrequencia(74.9f);
		aluno4.CalcularMedia();
		aluno4.getDadosAluno();
		aluno4.situacaoAluno();
		
		
		Aluno aluno5 = new Aluno();
		aluno5.setNome("Ciclano");
		aluno5.setRa(112356);
		aluno5.setNotaA1(9);
		aluno5.setNotaA2(10);
		aluno5.setFrequencia(99.9f);
		aluno5.CalcularMedia();
		aluno5.getDadosAluno();
		aluno5.situacaoAluno();
		
	}

}
