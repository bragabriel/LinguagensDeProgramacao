package ex08_Prova_Filme;

import java.util.ArrayList;

public class Filme {

	private String titulo;
	private Ator atores;
	private Comentario comentario;
	private ArrayList<Ator> listaAtores;
	
	public String getTitulo() {
		return titulo;
	}

	public void setTitulo(String titulo) {
		this.titulo = titulo;
	}

	public Ator getAtores() {
		return atores;
	}

	public void setAtores(Ator atores) {
		this.atores = atores;
	}

	public Comentario getComentario() {
		return comentario;
	}

	public void setComentario(Comentario comentario) {
		this.comentario = comentario;
	}
	
	public Filme(String titulo, ArrayList<Ator> listaAtores, String data, String tipo_publicacao, String texto) {
		this.titulo = titulo;
		this.listaAtores = listaAtores;
		this.comentario = new Comentario(data, tipo_publicacao, texto);
	}

	public void imprimirInformacoes() {
		System.out.println("Nome do filme: " + this.titulo);
		System.out.println("\n--------------------\nComent�rio do filme:\n");
		System.out.println("Data do coment�rio: " + this.comentario.getData());
		System.out.println("Tipo da publica��o: " + this.comentario.getTipo_publicacao());
		System.out.println("Coment�rio: " + this.comentario.getTexto() + "\n");
	}
	
	public void imprimirAtores() {
		System.out.println("O elenco do filme " + this.getTitulo() + " �: \n");
		for(int i = 0; i < this.listaAtores.size(); i++) {
			System.out.println("Nome do ator/atriz: " + this.listaAtores.get(i).getNome());
			System.out.print("\n");
		}
	}
}