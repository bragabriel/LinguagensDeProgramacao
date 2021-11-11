#include<stdio.h>

int main(){
	
	char x[150];
	
/*	
	//Standard input: teclado
	fgets(x, 150, stdin);
	printf("%s", x);
*/

/*
	//Standard input: arquivo
	freopen("file.txt", "r", stdin);
	fgets(x, 150, stdin);
	printf("%s", x);
*/	



	FILE *teste;
	
	//Criando arquivo teste.txt
	teste = fopen("teste.txt", "w");
	
	//Escrevendo no arquivo teste.txt
	fprintf(teste, " Pao com mortadela. \n Teste \n Coxinha com Coca - Cola");
	
	//Salvar e fechar arquivo - por segurança
	fclose(teste);


	FILE *lendo;
	
	//Lendo arquivo teste.txt
	lendo = fopen("teste.txt", "r");
	
	//testando se o arquivo existe ou não
	if(lendo == NULL){
		printf("Arquivo nao pode ser aberto \n");
		exit(1);
	}
	
//	fscanf(lendo, "%s", &x); Usado para entrada de dados formatadas
// Ex: %d %d %d, &a, &b, &c
	
	while(fgets(x, 150, lendo) != NULL){
		printf("%s", x);
	}
	
	fclose(lendo);


	return 0;
}
