#include <stdio.h>
		
	int main(){


//STRUCT		

	struct carro{
		char nome [20];
		char cor [20];
		int potencia;
		int velocidadeMAX;	
	};
	
	struct carro carro1, carro2; //Meu struct carro atende pela variavel car

//carro1	
	printf("Insira o nome do carro: \n");
	fgets(carro1.nome, 20, stdin);
	
	carro1.potencia = 200;
	
	printf("O nome do carro 1 eh: %s ", carro1.nome );
	
	printf("A potencia do carro 1 eh: %d \n \n", carro1.potencia );
	
//carro2
	
	//carro2.nome = "";
	carro2.potencia = 400;
	printf("A potencia do carro 2 eh: %d \n", carro2.potencia );
	
//TYPEDEF

	//typedef int inteiro; //int passa a ser inteiro
/*	
	typedef struct carro{
		char nome [20];
		char cor [20];
		int potencia;
		int velocidadeMAX;	
	}car;
	
	car carro1, carro2;
	
	*/
	
	
	
return 0;
}
