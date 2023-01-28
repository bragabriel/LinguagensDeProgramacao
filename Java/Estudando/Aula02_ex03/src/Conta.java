
public class Conta {

	private String nome;
	private float saldo;
	private int numero;
	
	public void setNome(String n) {
		nome = n;
	}
	
	public void setNumero(int numero) {
		this.numero = numero;
		this.saldo = 0;
	}
	
	public void Sacar(int valor) {
		if(this.saldo >= valor) {
			this.saldo = this.saldo-valor;
			System.out.println("Valor sacado com sucesso!");
		}
		else {
			System.out.println("Saldo insuficiente");
		}
		
	} 
	
	public void Depositar(int valor) {
		this.saldo = this.saldo + valor;
		System.out.println("Valor depositado com sucesso!");
	}
	
	public void ImprimirSaldo() {
		System.out.println("Saldo = " + this.saldo);
	}
		
	public void ImprimirDadosDaConta() {
		System.out.println("\n");
		System.out.println("Dados da conta:");
		System.out.println("Nome do titular: " + this.nome);
		System.out.println("Numero da conta: " + this.numero);
		System.out.println("Saldo bancário: " + this.saldo);
	}
	
}
