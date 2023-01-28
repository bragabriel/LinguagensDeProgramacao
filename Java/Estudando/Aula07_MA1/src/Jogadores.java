import java.util.ArrayList;

public class Jogadores {

	private String nome;
	private String nick;
	private int idade;
	private int salario;
	private float economia;
	private int killstreak;
	private ArrayList<Itens> listaItens;
	
	public Jogadores(ArrayList<Itens> lista) {
		this.listaItens = lista;
	}
	
	public float getEconomia() {
		return economia;
	}

	public void setEconomia(float economia) {
		this.economia = economia;
	}

	public String getNome() {
		return nome;
	}
	
	public void setNome(String nome) {
		this.nome = nome;
	}
	
	public String getNick() {
		return nick;
	}
	
	public void setNick(String nick) {
		this.nick = nick;
	}
	
	public int getSalario() {
		return salario;
	}
	
	public void setSalario(int salario) {
		this.salario = salario;
	}

	public int getIdade() {
		return idade;
	}

	public void setIdade(int idade) {
		this.idade = idade;
	}
	
	public void kill() {
		this.economia += 1000;
		System.out.println("O player " + this.nick + " fez uma eliminação");
		System.out.println("A economia atual de " + this.nick + " é $" + this.economia + "\n");
		this.killstreak += 1;
		
		if(killstreak == 5) {
			System.out.println("O jogador " + this.nick + " fez um ACE!");
			System.out.print("\n");
			this.killstreak = 0;
		}
	}
	
	public void comprarAWP() {
		System.out.println("O jogador " + this.nick + " comprou uma " + this.listaItens.get(4).getNome());
		
		this.economia = this.economia - this.listaItens.get(4).getPreco();
		
		System.out.println("A economia atual de " + this.nick + " é $" + this.economia + "\n");
	}
	
	public void comprarDeagle() {
		System.out.println("O jogador " + this.nick + " comprou uma " + this.listaItens.get(5).getNome());
		
		this.economia = this.economia - this.listaItens.get(5).getPreco();
		
		System.out.println("A economia atual de " + this.nick + " é $" + this.economia + "\n");
	}
	
}