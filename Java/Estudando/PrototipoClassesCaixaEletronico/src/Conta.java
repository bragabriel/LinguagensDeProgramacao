
public class Conta {

	private int senha;
	private int numero;
	private float saldo;
	private boolean status;
	
	public int getSenha() {
		return senha;
	}

	public void setSenha(int senha) {
		this.senha = senha;
	}

	public int getNumero() {
		return numero;
	}

	public void setNumero(int numero) {
		this.numero = numero;
	}

	public float getSaldo() {
		return saldo;
	}

	public void setSaldo(float saldo) {
		this.saldo = saldo;
	}

	public boolean isStatus() {
		return status;
	}

	public void setStatus(boolean status) {
		this.status = status;
	}

	public Conta(int senha, int numero, float saldo, boolean status) {
		super();
		this.senha = senha;
		this.numero = numero;
		this.saldo = saldo;
		this.status = status;
	}
	
	public void verificarSenha() {}
	
	public void obterStatus() {}
	
	public void obterSaldo() {}
	
	public void debitar() {}
	
	public void desativar() {}
	
	public void depositar() {}
	
	public void ativar() {}

	public void obterConta() {}
	
	
}

