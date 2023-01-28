package ex08_Prova_Filme;

public class Comentario {

	private String data;
	private String tipo_publicacao;
	private String texto;
		
	public String getData() {
		return data;
	}
	
	public void setData(String data) {
		this.data = data;
	}
	
	public String getTipo_publicacao() {
		return tipo_publicacao;
	}
	
	public void setTipo_publicacao(String tipo_publicacao) {
		this.tipo_publicacao = tipo_publicacao;
	}
	
	public String getTexto() {
		return texto;
	}
	
	public void setTexto(String texto) {
		this.texto = texto;
	}	
	
	public Comentario(String data, String tipo_publicacao, String texto) {
		this.data = data;
		this.tipo_publicacao = tipo_publicacao;
		this.texto = texto;
	}	
}