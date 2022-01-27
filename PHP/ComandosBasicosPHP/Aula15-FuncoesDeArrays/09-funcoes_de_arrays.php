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

echo "<br><hr>";
//---------------------------------
// in_array("valor", ($array)); //Verifica se um determinado valor existe em alguma posição do array

echo in_array("Gabriel", $nomes); //Verifica se um determinado valor existe em alguma posição do array

echo in_array("Carlos", $nomes); //Não retorna nada se o valor for Falso (se não tiver o valor no array)

echo "<br><hr>";

if(in_array("Elza", $nomes)){
    echo "Existe no array!";
}
else{
    echo "Não existe no array!";
}


echo "<br><hr>";
//---------------------------------
// array_keys($array) = Retorna um novo array com as chaves do array passado
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


echo "<br><hr>";
//---------------------------------
// array_values($array) = Retorna um novo array com os valores do array passado como parâmetro
echo("Array \$nomes: ");
print_r($nomes2);
echo "<br>";
$values = array_values($nomes2);
echo("Array \$values: ");
print_r($values);


echo "<br><hr>";
//---------------------------------
// array_merge($array1, $array2) = Agrega o conteúdo de dois arrays
?>