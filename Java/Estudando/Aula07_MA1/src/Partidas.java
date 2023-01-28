import java.util.ArrayList;

public class Partidas {

	private int numeroDaPartida;
	private String placarFinal;
	private ArrayList<Itens> listaItens;
	
	public Partidas(int numeroDaPartida, String placarFinal, ArrayList<Itens> lista) {
		this.numeroDaPartida = numeroDaPartida;
		this.placarFinal = placarFinal;
		this.listaItens = lista;
	}
	
	public String getPlacarFinal() {
		return placarFinal;
	}
	
	public void setPlacarFinal(String placarFinal) {
		this.placarFinal = placarFinal;
	}
	
	public ArrayList<Itens> getItens() {
		return listaItens;
	}

	public int getNumeroDaPartida() {
		return numeroDaPartida;
	}

	public void setNumeroDaPartida(int numeroDaPartida) {
		this.numeroDaPartida = numeroDaPartida;
	}
	
	
	public void imprimirItens() {
		for(int i = 0; i < this.listaItens.size(); i++) {
			System.out.println("Nome do item: " + this.listaItens.get(i).getNome());
			System.out.println("Descrição do item: " + this.listaItens.get(i).getDescricao());
			System.out.println("Arma pode ser comprada pelo time: " + this.listaItens.get(i).getLado());
			System.out.println("Preço do item: $" + this.listaItens.get(i).getPreco());
			System.out.print("\n");
		}
	}
	
}