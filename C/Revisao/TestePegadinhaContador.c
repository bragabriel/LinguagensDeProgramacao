#include <stdio.h>

int main(){
	
	
    //teste1();
    
    testeHello();
    
    
    return 0;
}

void teste1(){
	
	int numero = 5;
    int valor = 0;
	
	valor = 5 + numero++;
    
    printf("%d\n\n", valor);
    
}

void testeHello(){
	
	int i = 0;
	
	for(i=0; i<10; i=i++) {
		i+=1;
		printf("Hello World!\n");
	}
	
	
	int j = 0;
	//j = j++;
	printf("\n%d", j++); 
}











