
public class CaixaEletronico {

	private float quantiaDisponivel;
	private boolean statusLogin;
	private int contaLogin;
	
	public float getQuantiaDisponivel() {
		return quantiaDisponivel;
	}
	
	public void setQuantiaDisponivel(float quantiaDisponivel) {
		this.quantiaDisponivel = quantiaDisponivel;
	}
	
	public boolean isStatusLogin() {
		return statusLogin;
	}
	
	public void setStatusLogin(boolean statusLogin) {
		this.statusLogin = statusLogin;
	}
	
	public int getContaLogin() {
		return contaLogin;
	}
	
	public void setContaLogin(int contaLogin) {
		this.contaLogin = contaLogin;
	}

	public CaixaEletronico(float quantiaDisponivel, boolean statusLogin, int contaLogin) {
		super();
		this.quantiaDisponivel = quantiaDisponivel;
		this.statusLogin = statusLogin;
		this.contaLogin = contaLogin;
	}
	
	public void atualizarStatusLoginCaixa() {}
	public void obterNumConta() {}
	public void obterQuantDisponivel() {}
	}
