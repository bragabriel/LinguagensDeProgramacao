
public class Batman extends Heroi implements IParceiro{

	private String EnderecoDaBatCaverna;
	
	public String getEnderecoDaBatCaverna() {
		return EnderecoDaBatCaverna;
	}

	public void setEnderecoDaBatCaverna(String enderecoDaBatCaverna) {
		EnderecoDaBatCaverna = enderecoDaBatCaverna;
	}

	public void executarPoder() {
		System.out.println("Batarang!");
	}
	
	public void ExibirNomeParceiro() {
		System.out.println("Robin");
	}
	
	public void ExecutarPoderParceiro() {
		System.out.println("Voadora!");
	}
}
