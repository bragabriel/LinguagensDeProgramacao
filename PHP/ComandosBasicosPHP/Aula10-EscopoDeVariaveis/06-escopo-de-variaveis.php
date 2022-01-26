<?php

//ESCOPO GLOBAL
$nome = "Gabriel Braga";
$a = 1;
$b = 3;
$c = 7;

//Exemplo 01:
function exibeNome(){
    //ESCOPO LOCAL
    global $nome; //acessando uma variável do escopo GLOBAL
    echo $nome; 
}
exibeNome();
echo "<hr>";


//Exemplo 02:
function exibeCidade(){
    //ESCOPO LOCAL
    global $cidade; //definindo $cidade como uma variável global
    $cidade = "Pirassununga";
}
exibeCidade();
echo "$cidade";
echo "<hr>";


//Exemplo 03:
function soma(){
    $GLOBALS['a'] + $GLOBALS['b'] + $GLOBALS['c']; 
    //Acessando o valor das variáveis globais através do ARRAY ESPECIAL
}
soma();

?>