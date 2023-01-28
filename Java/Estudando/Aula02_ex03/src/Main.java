
public class Main {

	public static void main(String[] args) {
		
		Conta c1 = new Conta();
		c1.setNome("Gabriel");
		c1.setNumero(123);
		c1.Depositar(500);
		c1.ImprimirDadosDaConta();
		c1.Sacar(100);
		c1.ImprimirSaldo();
		
		Conta c2 = new Conta();
		c2.setNome("Diego");
		c2.setNumero(321);
		c2.Depositar(200000);
		c2.ImprimirDadosDaConta();
		c2.Sacar(100);
		c2.ImprimirSaldo();
		
		Conta c3 = new Conta();
		c3.setNome("Ivan");
		c3.setNumero(213);
		c3.Depositar(1000000);
		c3.ImprimirDadosDaConta();
		c3.Sacar(111);
		c3.ImprimirSaldo();
		
		c1.Depositar(100);
		
		c2.Depositar(200);
		
		c3.Depositar(1000000);
	}

}
