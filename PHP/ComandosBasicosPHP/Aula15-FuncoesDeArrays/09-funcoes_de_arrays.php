<?php

/*
Documentação do PHP - Funções: https://www.php.net/manual/en/book.array.php
*/

$nomes = array("Gabriel", "Felipe", "Maria", "José");

if(is_array($nomes)){ //Verifica se é um array
    echo "É um array!";
}
else{
    echo "Não é um array!";
}

echo "<br><br><hr>";
//---------------------------------
// in_array("valor", ($array)); //Verifica se um determinado valor existe em alguma posição do array

echo in_array("Gabriel", $nomes); //Verifica se um determinado valor existe em alguma posição do array

echo in_array("Carlos", $nomes); //Não retorna nada se o valor for Falso (se não tiver o valor no array)

echo "<br><br><hr>";

if(in_array("Elza", $nomes)){
    echo "Existe no array!";
}
else{
    echo "Não existe no array!";
}


echo "<br><br><hr>";
//---------------------------------
// array_keys($array) = Retorna um novo array com as chaves (ÍNDICES) do array passado como parâmetro
echo("Array \$nomes: ");
print_r($nomes);
echo "<br>";

echo("Array \$keys: ");
$keys = array_keys($nomes);
print_r($keys);
echo "<br><br>";


$nomes2 = array("Primo"=>"Rodrigo", "Vizinha"=>"Joana", "Vizinho"=>"João", "Prima"=>"Rebeca", "Irmão"=>"Barnabé", "Tia"=>"Maria");

echo("Array \$nomes2: ");
print_r($nomes2);
echo "<br>";
$keys2 = array_keys($nomes2);
echo("Array \$keys2: ");
print_r($keys2);


echo "<br><br><hr>";
//---------------------------------
// array_values($array) = Retorna um novo array com os valores do array passado como parâmetro
echo("Array \$nomes: ");
print_r($nomes2);
echo "<br>";
$values = array_values($nomes2);
echo("Array \$<ins>VALUES</ins>: ");
print_r($values);


echo "<br><br><hr>";
//---------------------------------
// array_merge($array1, $array2) = Agrega o conteúdo de dois arrays
$carros = array("Camaro", "Uno", "Gol");
$motos = array("50cc", "cb1000", "kawasaki 750");

echo("Array \$carros: ");
print_r($carros);
echo "<br>";

echo("Array \$motos: ");
print_r($motos);
echo "<br>";

$veiculos = array_merge($carros, $motos);
echo("Array <ins>MERGE</ins> \$veiculos: ");
print_r($veiculos);


echo "<br><br><hr>";
//---------------------------------
// array_pop($array) = Exclui a ÚLTIMA posição do array
echo("Array \$carros: ");
print_r($carros);
echo "<br>";

echo("Array <ins>POP</ins> \$carros: ");
array_pop($carros);
print_r($carros);


echo "<br><br><hr>";
//---------------------------------
// array_shift($array) = Exclui a PRIMEIRA posição do array
echo("Array \$carros: ");
print_r($carros);
echo "<br>";

echo("Array <ins>SHIFT</ins> \$carros: ");
array_shift($carros);
print_r($carros);


echo "<br><br><hr>";
//---------------------------------
// array_unshift($array, "valor1", "valor2") = Adiciona um ou mais elementos no INÍCIO do array
$frutas = array("Uva", "Laranja", "Maçã");
echo("Array \$frutas: ");
print_r($frutas);
echo "<br>";

echo("Array <ins>UNSHIFT</ins> \$frutas: ");
array_unshift($frutas, "Manga", "Acerola", "Morango");
print_r($frutas);


echo "<br><br><hr>";
//---------------------------------
// array_push($array, "valor1", "valor2") = Adiciona um ou mais elementos no FINAL do array
$frutas = array("Uva", "Laranja", "Maçã");
echo("Array \$frutas: ");
print_r($frutas);
echo "<br>";

echo("Array <ins>PUSH</ins> \$frutas: ");
array_push($frutas, "Manga", "Acerola", "Morango");
print_r($frutas);


echo "<br><br><hr>";
//---------------------------------
// array_combine($array, "valor1", "valor2") = Mescla dois arrays
$keys = array("Campeão", "Vice", "Terceiro");
$values = array("Vasco", "Flamengo", "Botafogo");

echo("Array \$keys: ");
print_r($keys);
echo "<br>";

echo("Array \$values: ");
print_r($values);
echo "<br>";

$times = array_combine($keys, $values);
echo("Array <ins>COMBINE</ins> \$times: ");
print_r($times);


echo "<br><br><hr>";
//---------------------------------
// array_sum() = Calcula a soma dos elementos de um array
$soma = array(5.5, 6, 10.1, 8);
echo("Array \$soma: ");
print_r($soma);
echo "<br>";

$total = array_sum($soma);
echo("Array <ins>SUM</ins> \$soma: $total");


echo "<br><br><hr>";
//---------------------------------
// array_sum() = Calcula a soma dos elementos de um array

?>