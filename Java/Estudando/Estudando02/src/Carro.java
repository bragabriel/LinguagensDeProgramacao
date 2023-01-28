
public class Carro {

	//atributos
	String modelo;
	String marca;
	int ano;
	float velocidade;


	//métodos
	void acelerar(int aceleracao) {
		//definindo o que o método vai fazer
		velocidade += aceleracao;
	}
	
	void frear(int reduzir) {
		velocidade -= reduzir;
	}
	
	void buzinar() {
		System.out.println("bih");
	}
}
