<?php

//Constantes
define("NOME", "Gabriel Braga");
define("IDADE", 20);
define("ALTURA", 1.74);
define("SOLTEIRO", true);

const TIMES = array('Psg', 'Real Madrid', 'Barcelona', 'Bayern de Munique');

echo 'Constante NOME: '.NOME. '<br>';
var_dump(NOME);
echo "<br><br>";

echo 'Constante IDADE: '.IDADE. '<br>';
var_dump(IDADE);
echo "<br><br>";

echo 'Constante ALTURA: '.ALTURA. '<br>';
var_dump(ALTURA);
echo "<br><br>";

echo 'Constante SOLTEIRO: '.SOLTEIRO. '<br>';
var_dump(SOLTEIRO);
echo "<br><br>";

echo 'Constante TIMES:';
echo TIMES[1];
var_dump(TIMES);
echo "<br><br>";

function exibeNome(){
    echo NOME;
}
ExibeNome();


?>