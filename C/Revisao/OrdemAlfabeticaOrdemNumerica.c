#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TAM 6
#define true 1

/* Struct principal */
	typedef struct _cadastro{
		char nome[15];
		int idade;
}Cadastro;

void inicializaVetor(Cadastro *ponteiro); //Inicializa o vetor de struct e recebe os valores do txt
void imprime(Cadastro *ponteiro); //imprime o vetor de struct
//void ordena(Cadastro *ponteiro, int tam); //ordena o vetor de struct



/*------------------------------------------------*/
/*			Funcao - Inicializa o Vetor 		  */
					
void inicializaVetor(Cadastro *p){
			// *p = ponteiro para dadosPib
    
    int i;
			
	//Abrindo arquivo txt para a leitura dos dados (Cadastro de Clientes)
	FILE *arqEnt; //arquivo entrada
	arqEnt = fopen("dadosCadastro.txt", "r");
	
	//Nao existe o arquivo dadosCadastro.txt, ou nao foi encontrado:
	if(arqEnt == NULL){
		printf("Nao foi possivel abrir o arquivo dadosCadastro.txt \n");
		getchar();
		exit(0);
	}
			
	for(i=0; i<TAM; i++){
		
		//Lendo arquivos do txt
		//fgets(nome, 40, stdin, "%d"); // Recebe uma STRING COMPLETA, PODENDO USAR ESPAÇO
		fscanf(arqEnt, "%s %d", &p[i].nome, &p[i].idade); //Atribuindo os dados do txt para variaveis aqui no programa
	
				
	}//fim for
} 
/*		Fim da Funcao - Inicializa o Vetor 	   */
/*---------------------------------------------*/



/*-------------------------------------------*/
/*		Funcao - imprime o Vetor de Struct 	*/		
void imprime(Cadastro *p){
	
	int i;

	//Exibindo os dados
	printf("-----------------------------------------------------\n");
	printf("\t\t Cadastro de pessoas sendo exibidos...\n");
	printf("------------------------------------------------------\n\n");
	printf("Nome:\t Idade:\n\n");	
	
	for(i=0; i<TAM; i++){
		printf(" %s \t\t %d \n\n\n", p[i].nome, p[i].idade);
	}
}


void categoriaIdade(Cadastro *p){
	
	int i;

	//Exibindo os dados
	printf("-----------------------------------------------------\n");
	printf("\t\t10 MAIORES PIB'S E SEUS ANOS:\n");
	printf("------------------------------------------------------\n\n");
	printf("INDICE:\t ANO:\n\n");	
	
	for(i=49; i>37; i--){
		printf(" %s \t %d\n\n\n", p[i].nome, p[i].idade);
	}
	printf("-----------------------------------------------------\n");
	printf("\t\t10 MENORES PIB'S E SEUS ANOS:\n");
	printf("------------------------------------------------------\n\n");
	printf("INDICE:\t ANO:\n\n");	
	
	for(i=1; i<11; i++){
		printf(" %s \t %d\n\n\n", p[i].nome, p[i].idade);
	}
}

/*		Fim da Funcao - imprime o Vetor de Struct		 */
/* ------------------------------------------------------*/



/*---------------------------------------------*/
/*		Funcao - ordenaIdade com ShellSort	   */				

void ordenaIdade(Cadastro *vetor, int N){ 

 int k, i, j;
 Cadastro aux;
 
 for(k=0; k<N; k++){
 	
 	for(i=k; i<N; i++){
 		
 		aux = vetor[i];
 		
 		for(j=i-k; j>=0 && vetor[j].idade > aux.idade; j-=k){
 			
 			vetor[j+k] = vetor[j];
		 }
		 
	vetor[j+k] = aux;
	}
 }

}
/*		Fim da Funcao - ordenaIdade com ShellSort		 */
/*-------------------------------------------------------*/



/*---------------------------------------------*/
/*		Funcao - ordenaNome com ShellSort	   */				

void ordenaNome(Cadastro *vetor, int N){ 

 int i=0, j=0;
 Cadastro aux;
 
 for(i=0; i<=TAM; i++){
 	for(j=0; j<TAM-1; j++){
 		if (strcmp(vetor[j].nome, vetor[j+1].nome) > 0) {
 			//printf("TRUE");
 			aux = vetor[j];
 			vetor[j] = vetor[j+1];
 			vetor[j+1] = aux;
 		}
	}
 } 
}
/*		Fim da Funcao - ordenaNome com ShellSort		 */
/*-------------------------------------------------------*/



/*-----------------------------------------------*/
/* * main - arquivo de utilizacao do usuario  * */

int main (){

  int anoPesq, anoPesquisado;
	
	Cadastro listaCadastro[TAM]; //'listaCadastro' eh um vetor do tipo 'Cadastro'

    inicializaVetor(listaCadastro); //inicializando o vetor de Struct, e recebendo os valores do txt
    
    printf("---- Case Tecnico ----\n\n");
    
    int op = 0;
    while(true){
    	
    	do{
    	printf("\nPor favor, selecione uma opcao: \n");
    	printf("1 - Cadastrar usuario \n");
    	printf("2 - Listar usuarios por Idade \n");
    	printf("3 - Listar usuarios por Ordem Alfabetica \n");
    	printf("4 - Listar por Categoria \n");
    	printf("9 - Sair \n");	
    	printf("Opcao: ");
    	
    	scanf("%d", &op);
    	
		}while(op != 1 && op != 2 && op != 3 && op != 4 && op != 9);
    	
    	if(op == 9){
    		break;
		}else{
			switch(op)
			{
				case 1:;
				
					int idade;
					char nome[40];
					
					printf("\n--- Cadastro de Usuario ---\n");
					printf("Por favor, insira o nome do usuario: ");
					scanf("%s", &nome);
					printf("Por favor, insira a idade do usuario: ");
					scanf("%d", &idade);
					
					
				break;
				
				case 2:
					printf("oi");
				break;
					
			}
		}
    	
	}
    /*
    imprime(listaCadastro); //imprimindo o vetor de Struct
    
    
    printf("------------------------------------------------------\n");
	printf("\t Dados ordenados pela IDADE utilizando ShellSort:\n");
    ordenaIdade(listaCadastro, TAM);//ordenando as idades utilizando o ShellSort, de acordo com o ANO

	imprime(listaCadastro); //imprimindo o vetor de Struct apos a ordenacao
	
	
	printf("------------------------------------------------------\n");
	printf("\t Dados ordenados pelo NOME\n");
    ordenaNome(listaCadastro, TAM);//ordenando as idades utilizando o ShellSort, de acordo com o ANO

	imprime(listaCadastro); //imprimindo o vetor de Struct apos a ordenacao
	*/
	
	
	//ordenapib(dadosPib, 0, TAM-1);
	//imprimeordpib(dadosPib);

    return 0;
}
/*	    	Fim da Funcao - Main  		 */
/*---------------------------------------*/
