/*
Programa que compara se depois da letra 'A' existe 3 caracteres e o 4° é a letra 'B'.

Se isso acontecer, imprime 'true', se não, imprime 'false'
*/

#include <stdio.h> 
#include <string.h>
#include <ctype.h>

int StringChallenge(char * str) {
  
  // code goes here  
  int i=0, tam;
  
  tam = strlen(str);

  char aux[tam];

  strcpy(aux, str);
  
  //Colocando as strings em Maiusculo
  for(i=0; i<tam; i++){
    str[i] = toupper(str[i]);
    aux[i] = toupper(aux[i]);
  }
  
  for(i=0; i<tam; i++){
      if(str[i]=='A'){
        if(aux[i+3]=='B'){
          //printf("true");
          return(1);

        }
      }
    }
  return(0);
  //str = "false";
  //printf("false");
}

int main(void) { 
  int res;
  char str[50] = "Laura sobs";
  // keep this function call here
  res = StringChallenge(str);

 if(res==1){
    printf("true");
  }
  else{
    printf("false");
  }
  return 0;
    
}
