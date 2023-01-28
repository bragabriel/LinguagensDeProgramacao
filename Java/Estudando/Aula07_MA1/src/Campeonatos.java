import java.util.ArrayList;

public class Campeonatos {

	private String nome;
	private String cidade;
	private int premiacao;
	private ArrayList<Times> listaTimes;
	private ArrayList<Partidas> listaPartidas;
	
	public Campeonatos(String nome, String cidade, int premiacao, ArrayList<Times> listaTimes, ArrayList<Partidas> listaPartidas) {
		this.nome = nome;
		this.cidade = cidade;
		this.premiacao = premiacao;
		this.listaTimes = listaTimes;
		this.listaPartidas = listaPartidas;
	}
	
	public String getNome() {
		return nome;
	}
	
	public void setNome(String nome) {
		this.nome = nome;
	}
	
	public String getCidade() {
		return cidade;
	}
	
	public void setCidade(String cidade) {
		this.cidade = cidade;
	}
	
	public int getPremiacao() {
		return premiacao;
	}
	
	public void setPremiacao(int premiacao) {
		this.premiacao = premiacao;
	}

	public void imprimirTimesCampeonato() {
		for(int i = 0; i < this.listaTimes.size(); i++) {
			System.out.println("-" + this.listaTimes.get(i).getNome());
		}
	}
	
	public void imprimirPartidasCampeonato() {
		for(int i = 0; i < this.listaPartidas.size(); i++) {
			System.out.println(this.listaPartidas.get(i).getPlacarFinal());
		}
	}
}