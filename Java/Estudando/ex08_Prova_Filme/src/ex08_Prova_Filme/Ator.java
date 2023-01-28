package ex08_Prova_Filme;

import java.util.ArrayList;

public class Ator {

	private String nome;
	private ArrayList<Ator> listaAtores;
	
	public void setNome(String nome) {
		this.nome = nome;
	}
	
	public String getNome() {
		return nome;
	}	
	
	public Ator(String nome, ArrayList<Ator> listaAtores) {
		this.nome = nome;
		this.listaAtores = listaAtores;
	}

}