#include <stdio.h>

int main(void){
	
	struct horario{
		int hora;
		int minuto;
		int segundo;
	};
	
	struct horario agora, *depois;
	
	depois = &agora;
	
	
	//*depois.hora = 20;  
	 
	/* nao funciona, pois o compilador entende:	*(depois.hora) = 20;
	   por causa da precedencia de sinais em C */
	
	//O correto é
	/*
	(*depois).hora = 20;
	(*depois).minuto = 20;
	(*depois).segundo = 20;
	*/
	
	//Ou usar um atalho para isso, que é:
	depois->hora = 22;
	depois->minuto = 20;
	depois->segundo = 22;
	
	printf("%d:%d:%d", agora.hora, agora.minuto, agora.segundo);
	
}
