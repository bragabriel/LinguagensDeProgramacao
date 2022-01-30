<?php

/*------------------------*/
/*  Funções para Números  */
/*------------------------*/


// number_format($variavel, "qtd casas decimais", "separador decimal", "separador de milhares"); = Formatar casas decimais
$db = 1234.56;

echo("Variável \$db: $db <br>");
$preco = number_format($db, 2, ",", ".");
echo("Teste 01: Variável <ins>NUMBER_FORMAT</ins> \$db: $preco <br>");
$preco = number_format($db, 2);
echo("Teste 02: Variável <ins>NUMBER_FORMAT</ins> \$db: $preco");


echo "<br><br><hr>";
//---------------------------------
// round() = Serve para arredondar o número (p/ baixo ou p/ cima)
$valor = 5.4;
echo("Variável \$valor: $valor <br>");
echo("Variável <ins>ROUND</ins> \$valor: ". round($valor). "<br>");


echo "<br><br><hr>";
//---------------------------------
// ceil() = Serve para arredondar o número (sempre p/ cima)
$valor = 5.4;
echo("Variável \$valor: $valor <br>");
echo("Variável <ins>CEIL</ins> \$valor: ". ceil($valor). "<br>");


echo "<br><br><hr>";
//---------------------------------
// floor("valor inicial", "valor final") = Serve para arredondar o número (sempre p/ baixo)
$valor = 5.4;
echo("Variável \$valor: $valor <br>");
echo("Teste 01: Variável <ins>FLOOR</ins> \$valor: ". floor($valor). "<br><br>");
$valor = 5.9;
echo("Variável \$valor: $valor <br>");
echo("Teste 02: Variável <ins>FLOOR</ins> \$valor: ". floor($valor). "<br>");


echo "<br><br><hr>";
//---------------------------------
// rand() = Serve para fazer sorteios (gerar números aleatórios)
echo("Variável <ins>RAND</ins>: ". rand(1, 20). "<br>");
?>