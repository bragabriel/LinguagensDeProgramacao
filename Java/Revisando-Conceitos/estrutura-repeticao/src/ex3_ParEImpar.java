import java.util.Scanner;

/*
 * Fa�a um programa que pe�a N n�meros inteiros, calcule e mostre a quantidade
 * de n�meros pares e a quantidade de n�meros �mpares*/

public class ex3_ParEImpar {

	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		
		int qtdNumeros;
		int numero;
		int qtdPares = 0;
		int qtdImpares = 0;
		
		System.out.println("Quantida de n�meros: ");
		qtdNumeros = scan.nextInt();
		
		int count = 0;
		
		do {
			System.out.println("N�mero: ");
			numero = scan.nextInt();
			
			if(numero % 2 == 0) {
				qtdPares++;
			}
			else {
				qtdImpares++;
			}
			
			count++;
			
		}while(count < qtdNumeros);
		
		System.out.println("Quantida de n�meros pares: " + qtdPares);
		System.out.println("Quantida de n�meros �mpares: " + qtdImpares);
	}

}
