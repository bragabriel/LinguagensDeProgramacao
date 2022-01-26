<?php

/* -------------------------- */
/* Tipos de dados "Escalares" */
/* -------------------------- */

//string:
$nome = "Hello World 123 321 !@#$%¨&";
var_dump($nome); // função var_dump mostra informações sobre a variável()
echo "<br>Valor da variável \$nome: $nome <br>";

if(is_string($nome)): //Verificando se a variável ($nome) é uma String
    echo "É uma String!";
else:
    echo "Não é uma String!";
endif;

echo "<hr>";

//int:
$idade = 20;
var_dump($idade);
echo "<br>Valor da variável \$idade: $idade <br>";

if(is_int($idade)):
    echo "É um inteiro!";
else:
    echo "Não é um inteiro!";
endif;

echo "<hr>";

//float:
$altura = 1.74;
var_dump($altura);
echo "<br>Valor da variável \$altura: $altura <br>";

if(is_float($altura)):
    echo "É um float!";
else:
    echo "Não é um float!";
endif;

echo "<hr>";

//boolean:
$admin = True;
var_dump($admin);
echo "<br>Valor da variável \$admin: $admin <br>";

if(is_bool($admin)):
    echo "É um boolean!";
else:
    echo "Não é um boolean!";
endif;

echo "<hr>";


/* -------------------------- */
/* Tipos de dados "Compostos" */
/* -------------------------- */

//array:
$carros = array("Mustang", "Camaro", "Ferrari", "Lamborghini", 20, 12.4, true);
var_dump($carros);
echo "<br>";
$teste = print_r($carros, true);
echo "<br>Valor do array \$carros: $teste <br>";
print_r ($carros, "<br>");




if(is_array($carros)):
    echo "É um array!";
else:
    echo "Não é um array!";
endif;

echo "<hr>";

/*
gettype() - Retorna o tipo da variável.
var_dump() – Retorna o tipo e o valor.

is_int() – Verifica se a variável em questão é do tipo integer.
is_bool() – Verifica se a variável em questão é do tipo boolean.
is_numeric() – Verifica se a variável em questão é uma string numérica, ex "100".
is_string() – Verifica se a variável em questão é do tipo string.
is_float() – Verifica se a variável em questão é do tipo flutuante.
is_array() – Verifica se a variável em questão é do tipo Array.
is_object() – Verifica se a variável em questão é do tipo objeto.
*/

?>