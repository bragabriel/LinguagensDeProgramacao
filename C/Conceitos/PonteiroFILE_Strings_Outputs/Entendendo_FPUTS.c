#include <stdio.h>

int main(){
	
	FILE *file;
	file = fopen("string.txt", "a");
	
	if(file == NULL){
		printf("Arquivo nao pode ser aberto \n");
		exit(1);
	}
	
	fprintf(file, "Primeira linha \n");
	
	char frase[] = ("AAAAAAAAAAAAAAAA \n");
	fputs(frase, file);
	
	char caractere = 3;
	
	fclose(file);
	
	return 0;
}
