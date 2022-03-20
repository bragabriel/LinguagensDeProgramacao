#include <stdio.h>

int main(){

	int pista, voltas, qtdAbastecimentos, consumo;
	float reabastecimento1, voltasParada1;
	
	printf("Qual o comprimento da pista? (em metros): ");
	scanf("%d", &pista);
	
	printf("Qual o numero de voltas? ");
	scanf("%d", &voltas);
	
	printf("Qual o numero de paradas para reabastecimento? ");
	scanf("%d", &qtdAbastecimentos);
	
	printf("Qual o consumo de combustivel? (em km/l): ");
	scanf("%d", &consumo);
	
	voltasParada1 = voltas / qtdAbastecimentos;
	
	reabastecimento1 = voltasParada1 * pista;
	
	printf("\n");
	printf("O numero minimo de litros necessarios para percorrer ate o primeiro reabastecimento e de: %.2f litros", reabastecimento1);

	return 0;	
}
