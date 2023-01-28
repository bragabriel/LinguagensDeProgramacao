import java.util.ArrayList;

public class Times {

	private String nome;
	private int rank;
	private String coach;
	private ArrayList<Jogadores> listaJogadores;
	
	public Times(String nome, int rank, String coach,  ArrayList<Jogadores> lista) {
		this.nome = nome;
		this.rank = rank;
		this.coach = coach;
		this.listaJogadores = lista;
	}
	
	public int getRank() {
		return rank;
	}

	public void setRank(int rank) {
		this.rank = rank;
	}

	public String getNome() {
		return nome;
	}
	
	public void setNome(String nome) {
		this.nome = nome;
	}

	public void imprimir_jogadores() {		
		
		/*for(int i = 0; i < this.listaJogadores.size(); i++) {
			System.out.println(this.listaJogadores.get(i).getNome());
		}*/
		
		int tamanho_lista = this.listaJogadores.size();
		Jogadores j;
		for(int i = 0; i < tamanho_lista; i++) {
			j = this.listaJogadores.get(i);
			System.out.println("-" + j.getNick());
		}		
	}

	public String getCoach() {
		return coach;
	}

	public void setCoach(String coach) {
		this.coach = coach;
	}
}