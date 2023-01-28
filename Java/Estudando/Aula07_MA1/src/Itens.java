public class Itens {

	private String nome;
	private String municao;
	private int preco;
	private String descricao;
	private String lado;
	
	public Itens(String nome, String municao, int preco, String descricao, String lado) {
		
		this.nome = nome;
		this.municao = municao;
		this.preco = preco;
		this.descricao = descricao;
		this.lado = lado;
	}
	
	public String getNome() {
		return nome;
	}
	
	public void setNome(String nome) {
		this.nome = nome;
	}
	
	public String getMunicao() {
		return municao;
	}
	
	public void setMunicao(String municao) {
		this.municao = municao;
	}
	
	public int getPreco() {
		return preco;
	}
	
	public void setPreco(int preco) {
		this.preco = preco;
	}
	
	public String getDescricao() {
		return descricao;
	}
	
	public void setDescricao(String descricao) {
		this.descricao = descricao;
	}
	
	public String getLado() {
		return lado;
	}
	
	public void setLado(String lado) {
		this.lado = lado;
	}	
	
}