<?php

//Arrays

//Exemplo 01:
$carros = array("BMW", "Veloster", "Hilux");

//Inserindo nos determinados índices
$carros2 = array(1=>"BMW", 2=>"Veloster", 3=>"Hilux");

echo "<br>";
print_r($carros);
echo "<br>";
print_r($carros2);
echo "<br>";

echo $carros[0];
echo "<br>";

$carros[] = "Amarok";
$carros[10] = "Camaro";

print_r($carros);
echo "<br>";


//Exemplo 02:
$motos = array();
$motos[] = "Yamaha";
$motos[] = "Honda";
$motos[5] = "Suzuki";

print_r($motos);


//Exemplo 03:
$clientes = ["Rodrigo", "Felipe", "Bia"];
print_r($clientes);
echo "<hr>";
