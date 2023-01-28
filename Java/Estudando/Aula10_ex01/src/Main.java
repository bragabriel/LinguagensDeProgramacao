
public class Main {

	public static void main(String[] args) {

		Batman batman = new Batman();
		Homemaranha spiderman = new Homemaranha();

		batman.setNome("Bruce Wayne");
		batman.setCodinome("Batman");
		batman.setUniverso("DC");
		batman.setEnderecoDaBatCaverna("Mansão Wayne, 333, Gotham City, Universo Paralelo");
		batman.imprimir();
		
		spiderman.setNome("Peter Parker");
		spiderman.setCodinome("Homem-Aranha");
		spiderman.setUniverso("Marvel");
		spiderman.setNumeroDeMortesTioBen(5);
		spiderman.imprimir();
		
		System.out.println("Executando poder: \n");
		System.out.print("Batman: ");
		batman.executarPoder();
		
		System.out.println("^^^^^^^^^^^^^^^^");
		System.out.print("Homem-Aranha: ");
		spiderman.executarPoder();
		
		System.out.println("^^^^^^^^^^^^^^^^");
		System.out.print("Robin: ");
		batman.ExecutarPoderParceiro();
	}

}
