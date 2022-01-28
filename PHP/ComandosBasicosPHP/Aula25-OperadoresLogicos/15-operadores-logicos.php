<?php

/*------------------------*/
/*   Operadores Lógicos   */
/*------------------------*/

/*

e (&& - and)
ou (|| - or)
ou exclusivo (xor)
negação (!)

*/

$idade = 20;
$nome = "Gabriel";

// E (&& - and) = Se as duas expressões são verdadeiras = Verdadeiro
if(($idade == 20) && ($nome == "Gabriel")){ 
    echo "É verdadeiro <br><hr>";
}
else{
    echo "É falso <br><hr>";
}


// OU (|| - or) = Se pelo menos uma é expressão é verdadeira, ou as duas forem verdadeiras = Verdadeiro
if(($idade == 10) || ($nome == "Gabriel")){
    echo "É verdadeiro <br><hr>";
}
else{
    echo "É falso <br><hr>";
}

// OU EXCLUSIVO (xor) = Se APENAS UMA expressão for verdadeira. OU um OU outra.
if(($idade == 20) xor ($nome == "Gabriel")){
    echo "É verdadeiro <br><hr>";
}
else{
    echo "É falso <br><hr>";
}

// NEGAÇÃO (!)
if(!($idade == 20) and !($nome == "Gabriel")){
    echo "É verdadeiro <br><hr>";
}
else{
    echo "É falso <br><hr>";
}

?>