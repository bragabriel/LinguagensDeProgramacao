import java.util.ArrayList;

public class Main {

	public static void main(String[] args) {
		
		ArrayList<Pokemon> listaPokemons = new ArrayList<Pokemon>();
		
		Pikachu p1 = new Pikachu("Pikachu", "Elétrico", "Choque do Trovão", 100, "Cauda de Ferro");
		
		Bulbassauro p2 = new Bulbassauro("Bulbassauro", "Planta", "Chicotes de Vinha", 98, "Folhas de Navalha");
		
		Charmander p3 = new Charmander("Charmander", "Fogo", "Presas de Fogo", 99, "Lança-Chamas");
	
		Squirtle p4 = new Squirtle("Squirtle", "Água", "Rajada de Bolhas", 97, "Jato d'água");
		
		listaPokemons.add(p1);
		
		listaPokemons.add(p2);
		
		listaPokemons.add(p3);
		
		listaPokemons.add(p4);
		
		
		for(int i = 0; i < listaPokemons.size(); i++) {
			System.out.println((i+1) + "° Pokemon: ");
			listaPokemons.get(i).imprimirPokemon();
			System.out.println("------------------");
		}
		
		
		for(int i = 0; i < listaPokemons.size(); i++) {
			System.out.println(listaPokemons.get(i).getNome() + " use sua habilidade! ");
			System.out.println("vvvvvvvvvvvvvvvv");
			System.out.println(listaPokemons.get(i).getHabilidade());
			System.out.println("^^^^^^^^^^^^^^^^\n");
		}
		
		
		
	}

}
