#include <stdio.h>
#include <time.h> //necessário para usar localtime() e struct tm
int main(void)
{
	//ponteiro para struct que armazena data e hora	
	struct tm *data_hora_atual;		 
	
	//variável do tipo time_t para armazenar o tempo em segundos	
	time_t segundos;
	
	//obtendo o tempo em segundos	
	time(&segundos);	 
	
	//para converter de segundos para o tempo local	
	//utilizamos a função localtime	
	data_hora_atual = localtime(&segundos);	
	
		
	printf("\nHora ........: %d:",data_hora_atual->tm_hour);//hora	 
	printf("%d:",data_hora_atual->tm_min);//minuto
	printf("%d\n",data_hora_atual->tm_sec);//segundo	
	
	/* Obtendo os valores da struct data_hora_atual	e formatando a saída de dados no formato dia/mes/ano */	

	printf("\nData ........: %d/", data_hora_atual->tm_mday); //dia do mês
	printf("%d/",data_hora_atual->tm_mon+1); //mês
	printf("%d\n\n",data_hora_atual->tm_year+1900); //ano
	
	return 0;
}
