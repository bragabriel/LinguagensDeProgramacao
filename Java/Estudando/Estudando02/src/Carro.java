
public class Carro {

	//atributos
	String modelo;
	String marca;
	int ano;
	float velocidade;


	//m�todos
	void acelerar(int aceleracao) {
		//definindo o que o m�todo vai fazer
		velocidade += aceleracao;
	}
	
	void frear(int reduzir) {
		velocidade -= reduzir;
	}
	
	void buzinar() {
		System.out.println("bih");
	}
}
