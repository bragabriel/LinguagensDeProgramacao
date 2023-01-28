
public class Cliente {
	
	private String nome;
	private String rg;
	private boolean status;
	
	public String getNome() {
		return nome;
	}
	
	public void setNome(String nome) {
		this.nome = nome;
	}
	
	public String getRg() {
		return rg;
	}
	
	public void setRg(String rg) {
		this.rg = rg;
	}
	
	public boolean isStatus() {
		return status;
	}
	
	public void setStatus(boolean status) {
		this.status = status;
	}

	public Cliente(String nome, String rg, boolean status) {
		super();
		this.nome = nome;
		this.rg = rg;
		this.status = status;
	}
	
}
