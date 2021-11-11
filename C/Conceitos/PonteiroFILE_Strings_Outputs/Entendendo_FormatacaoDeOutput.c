#include <stdio.h>

int main(void){
	
	int intVar = 9999999;
	int intVar2 = 10;
	double doubleVar = 100.123456789;
	
	//Formatacao variaveis inteiras
	//Mesmo numero: 9999999
	printf("Variavel inteira(%%d) = %d\n", intVar); //variavel normal
	printf("Variavel inteira(%%i) = %i\n", intVar); //variavel normal
	printf("Variavel inteira(%%x) = %x\n", intVar); //converte o numero da base 10 para a base 16
	//base 16 usado em cores para html
	printf("Variavel inteira(%%o) = %o\n", intVar); //converte o numero da base 10 para a base 8
	printf("\n");
	
	//Formatacao variaveis float e double
	printf("Variavel double(%%f) = %f\n", doubleVar); //maxima precisão do float no printf
	printf("Variavel double(%%e) = %e\n", doubleVar); //escreve o número em notação cientifica
	printf("Variavel double(%%g) = %g\n", doubleVar); //perde a precição mais rapido, e não arredonda
	printf("Variavel double(%%a) = %a\n", doubleVar); //notação cientifica, mas utilizando virgula
	printf("\n");
	
	//Formatando para esquerda
	printf("Variavel inteira(%%d) = %7d\n", intVar2); //Alinhada a esquerda
	
	return 0;
}
