<?php

/*------------------------------*/
/*     Funções para Strings     */
/*------------------------------*/

$nome = "gaBriel Braga";

//---------------------------------
// strtoupper() = Converte para maiúsculo
echo("String \$nome: ");
print_r($nome);
echo "<br>";
$novoNome = strtoupper($nome);
echo("String <ins>STRTOUPPER</ins> \$nome: $novoNome");


echo "<br><br><hr>";
//---------------------------------
// strtolower() = Converte para minusculo
echo("String \$nome: ");
print_r($nome);
echo "<br>";
$novoNome = strtolower($nome);
echo("String <ins>STRTOUPPER</ins> \$nome: $novoNome");


echo "<br><br><hr>";
//---------------------------------
// substr() = Retorna parte de uma String a partir do caractere, com o comprimento ($string, CARACTERE, COMPRIMENTO)
$mensagem = "Olá mundo!";
echo("String \$mensagem: ");
print_r($mensagem);
echo "<br>";
$novaMensagem = substr($mensagem, 4, 5);
echo("String <ins>SUBSTR</ins> \$mensagem: $novaMensagem");


echo "<br><br><hr>";
//---------------------------------
// str_pad($String, pad_length, caractere) = Complementa uma outra String com a quantidade especificada de caracteres
$objeto = "Mouse";
echo("String \$objeto: ");
print_r($objeto);
echo "<br>";
$novoObjeto = str_pad($objeto, 11, "*");
echo("String <ins>STR_PAD</ins> \$objeto: $novoObjeto <br>");
$novoObjeto = str_pad($objeto, 11, "*", STR_PAD_LEFT);
echo("String <ins>STR_PAD_LEFT</ins> \$objeto: $novoObjeto <br>");
$novoObjeto = str_pad($objeto, 11, "*", STR_PAD_BOTH);
echo("String <ins>STR_PAD_BOTH</ins> \$objeto: $novoObjeto");


echo "<br><br><hr>";
//---------------------------------
// str_repeat("String", qtd de vezes) = Serve para repetir uma String
$string = "Teste de Frase!";
echo("String \$string: $string");
echo("String <ins>STR_REPEAT</ins> \$string: ". str_repeat($string, 5). "<br>");

$string2 = str_repeat("Sucesso!", 5);
echo("String <ins>STR_REPEAT</ins>: $string2 <br>");


echo "<br><hr>";
//---------------------------------
// strlen($string) = Exibe o número de caracteres da String
$frase = "alalalaalla";
echo("String \$frase: $frase <br>");
echo("String <ins>STRLEN</ins> \$frase: ". strlen($frase). "<br>");


echo "<br><hr>";
//---------------------------------
// str_replace("Palavra a ser substituída", "Palavra que vai substituir", $string) = Serve para substituir uma palavra em um texto/frase
$texto = "A seleção Espanhola será campeã da copa do mundo de 2022";
echo("String \$texto: $texto <br>");
$novoTexto = str_replace("Espanhola", "Brasileira", $texto);
echo("String <ins>STR_REPLACE</ins> \$texto: $novoTexto");



echo "<br><br><hr>";
//---------------------------------
// strpos() = Retorna a posição de uma palavra em um texto/frase
echo("String \$texto: $novoTexto <br>");
echo("String <ins>STRPOS</ins> \$texto: (Posição da palavra \"Copa\" dentro da frase): ".strpos($texto, "copa")."<br>");

?>