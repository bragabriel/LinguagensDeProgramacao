#include <stdio.h>

//ENTENDENDO FUNCAO

int main(void){
	
	float calcularAreaRetang(float x, float y); 
	//A função recebe 2 argumentos: float x e float y
	//A função retorna um valor do tipo float ('float' calcularArea...)
	
	float area = calcularAreaRetang(10.0, 20.0);
	
	printf("A area eh: %f", area);
	
	return 0;
}

float calcularAreaRetang(float base, float altura){
	
	float area = base * altura;
	
	return area;
}
