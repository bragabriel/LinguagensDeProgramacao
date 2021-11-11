#include <stdio.h>

int main(){
	
	int x = 10;
	
	int *ponteiro;
	
	ponteiro = &x;
	//ponteiro aponta para &x
	
	int y = 20;
	*ponteiro = y; //&x recebe vlr de y
	
	printf("%d %d\n", x, y);
	
	return 0;
}
