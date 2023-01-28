
public class ContaComum extends Conta{

	private double limite;
	
	public ContaComum(int senha, int numero, float saldo, boolean status) {
		super(senha, numero, saldo, status);
		// TODO Auto-generated constructor stub
	}

	public double getLimite() {
		return limite;
	}

	public void setLimite(double limite) {
		this.limite = limite;
	}
	
}
