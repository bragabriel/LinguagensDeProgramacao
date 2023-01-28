
public abstract class Heroi {

	private String nome;
	private String codinome;
	private String universo;
	
	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getCodinome() {
		return codinome;
	}

	public void setCodinome(String codinome) {
		this.codinome = codinome;
	}

	public String getUniverso() {
		return universo;
	}

	public void setUniverso(String universo) {
		this.universo = universo;
	}

	public void imprimir() {
		System.out.println("Dados do Heroi: ");
		System.out.println("Nome: " + this.nome);
		System.out.println("Codinome: " + this.codinome);
		System.out.println("Universo: " + this.universo + "\n");
	}
	
	public abstract void executarPoder();
}
