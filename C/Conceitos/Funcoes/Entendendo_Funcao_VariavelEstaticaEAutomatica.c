#include <stdio.h>

int main(void){
	
	void teste(void);
	
	void imprimaMensagem();
	
	teste();
	teste();
	teste();
	
	return 0;
}

void teste(void){
	
	//AUTOMATICA
	int variavelLocalAutomatica = 2;
	variavelLocalAutomatica*= 2;
	printf("Local Automatica: %d \n", variavelLocalAutomatica);
	
	//ESTATICA
	static int variavelLocalEstatica = 2;
	variavelLocalEstatica *= 2;
	printf("Local Estatica: %d \n", variavelLocalEstatica);

//Variavel LOCAL e não GLOBAL
} 
