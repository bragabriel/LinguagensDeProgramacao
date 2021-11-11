#include <stdio.h>

//Entendendo STRING e FGETS 

int main(){
	
	char nome[11]; //11 - 1 = o ultimo caracter o sistema usa para encerrar, sobrando assim 10 caracteres para utilizar	
	// Essa declaração é de uma STRING = sequencia de caracteres
	// char nome; armazena apenas um caracter
	// char nome[11]; armazena 10 caracteres
	
	
	printf("Digite seu nome: \n");
	
// scanf("%s", &nome);  //Apenas uma palavra

//getchar = entrada de um caracter

//scanf= entrada de uma palavra

// Receber STRING: %s || Receber CHAR: %c

	fgets(nome, 11, stdin); // Recebe uma STRING COMPLETA, PODENDO USAR ESPAÇO
	//stdin = Entrada padrao do computador
	//stdin = standard input
	
	printf("O nome armazenado foi: %s", nome);
	
	return 0;
}
