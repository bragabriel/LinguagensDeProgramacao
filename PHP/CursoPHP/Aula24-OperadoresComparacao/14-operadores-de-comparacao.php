<?php

/*  Operadores de Comparação  */

//Igual
echo "Igual: ";
if(10 == "10"): //true
    echo "True<br><hr>";
else:
    echo "False<br><hr>";
endif;


//Diferente
echo "Diferente: ";
if(10 != 10):
    echo "True<br><hr>";
else:
    echo "False<br><hr>";
endif;


//Identidade (verifica se é um valor é idêntico ao outro)
echo "Idêntico: ";
if(10 === "10"): //false
    echo "True<br><hr>";
else:
    echo "False<br><hr>";
endif;


//Não idêntico (verifica se é um valor é idêntico ao outro)
echo "Não Idêntico: ";
if(10 !== "10"): //false
    echo "True<br><hr>";
else:
    echo "False<br><hr>";
endif;


//Diferente - mesma coisa que o !=
echo "Diferente (2): ";
if(10 <> "10"): //false
    echo "True<br><hr>";
else:
    echo "False<br><hr>";
endif;


//Menor que
echo "Menor que: ";
if(10 < 30): 
    echo "True<br><hr>";
else:
    echo "False<br><hr>";
endif;


//Maior que
echo "Menor que: ";
if(10 > 30): 
    echo "True<br><hr>";
else:
    echo "False<br><hr>";
endif;


//Maior igual
echo "Menor que: ";
if(10 >= 30): 
    echo "True<br><hr>";
else:
    echo "False<br><hr>";
endif;


//Menor igual
echo "Menor que: ";
if(10 <= 30): 
    echo "True<br><hr>";
else:
    echo "False<br><hr>";
endif;

?>