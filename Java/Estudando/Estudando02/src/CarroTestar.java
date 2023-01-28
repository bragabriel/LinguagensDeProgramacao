
public class CarroTestar {

	public static void main(String[] args) {

//Chamar a classe carro | Dar o nome para o objeto de: c1
		Carro c1 = new Carro();
		
		//new Carro(); = construtor ??
	
		c1.modelo = "Ferrari 458 Turbo";
		c1.marca = "Ferrari";
		c1.ano = 2021;
		c1.velocidade = 250;
		
		//método acelerar, passando 50 para = int aceleracao
		c1.acelerar(50);
		System.out.println("A velocidade do carro (" + c1.modelo + ") depois da aceleração é de: " + c1.velocidade + " km/h");
	
	
		c1.frear(70);
		System.out.println("A velocidade do(a) " + c1.modelo + " após a freada é de: " + c1.velocidade + " km/h");
	}
}
