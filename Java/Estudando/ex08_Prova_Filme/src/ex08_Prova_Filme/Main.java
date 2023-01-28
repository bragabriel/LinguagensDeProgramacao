package ex08_Prova_Filme;

import java.util.ArrayList;

public class Main {

	public static void main(String[] args) {
		
		//Criando uma lista de atores
		ArrayList<Ator> listaAtores = new ArrayList<Ator>();
		
		Ator ator1 = new Ator("Daniel Craig", listaAtores);
		
		Ator ator2 = new Ator("Javier Bardem", listaAtores);
		
		Ator ator3 = new Ator("Bénénice Marlohe", listaAtores);
		
		Ator ator4 = new Ator("Judi Dench", listaAtores);
		
		
		listaAtores.add(ator1);
		listaAtores.add(ator2);
		listaAtores.add(ator3);
		listaAtores.add(ator4);
		
		Filme filme1 = new Filme("007 - Operação Skyfall", listaAtores, "29/09/2015", "Opnião no site 'ADOROCINEMA'", "O Melhor de todos, cheio de ação, suspense, emoção e muito mais, 007 - Operação Skyfall é um daqueles filme que entra na mente e nunca mais sai, um filme espetacular no ponto de ser eterno. 'Jefferson, Thomas.'");
		
		filme1.imprimirInformacoes();
		filme1.imprimirAtores();
		
		System.out.println("~~~~~~~~~~~~~~");
		System.out.println("Removendo o ator/atriz: " + ator4.getNome() + "\n");
		listaAtores.remove(ator4);
		
		filme1.imprimirAtores();
	}

}
