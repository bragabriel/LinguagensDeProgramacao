
public class Principal {

	public static void main(String[] args) {

		//Composi��o
		// Na composi��o o objeto todo nao pode existir sem o
		// objeto parte, e o objeto parte n�o pode existir sem o 
		// objeto todo.

		//objeto todo
		Fogao fogao = new Fogao("Kitchenaid", true, "Vidro Temperado", true, 6);
		
		fogao.imprimir();
	}

}
