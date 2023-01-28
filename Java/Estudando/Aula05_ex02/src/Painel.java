
public class Painel {
	
	private int qtdBocas;
	private Botao botao;

	public Painel() {
		this.setBotao(null);
	}
	
	public int getQtdBocas() {
		return qtdBocas;
	}

	public void setQtdBocas(int qtdBocas) {
		this.qtdBocas = qtdBocas;
	}

	public void setBotao(Botao botao) {
		this.botao = new Botao(true);
	}
	
	public Botao getBotao() {
		return this.botao;
	}

}
