package retorno;

public class Main {

	public static void main(String[] args) {
		
		//Utilizando sobrecarga de m�todos + Retorno:
		double retornoQuadrado = quadrilatero_retorno.area(4);
		double retornoRetangulo = quadrilatero_retorno.area(5, 5);
		double retornoTrapezio = quadrilatero_retorno.area(7, 6, 9);

		System.out.println("�rea do quadrado: " + retornoQuadrado);

		System.out.println("�rea do ret�ngulo: " + retornoRetangulo);	
	
		System.out.println("�rea do trap�zio: " + retornoTrapezio);
	}
}