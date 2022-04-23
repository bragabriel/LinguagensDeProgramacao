<?php

//Arrays

//-----------------------------
// Array numérico
//-----------------------------

// Um array é numérico quando os índices ou chaves são INTEIROS
$carros3 = array(1=>"Camaro", 2=>"Mustang", 3=>"Porsche"); 


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


//------------------------------

//Count
echo "<br>Count:<br>";
echo count($carros), "<br>";
echo count($motos), "<br>";
echo count($clientes), "<br>";

$totalClientes = count($clientes);
echo "$totalClientes", "<br>";
echo "<hr>";

//Foreach
echo "<br>";
foreach($carros as $valor){ //para cada elemento do array $carros, será atribuído a variável $valor
                            //em cada repetição, o elemento de $carros será atribuído para a variável $valor e exibimos o valor. Depois volta para o segundo laço, terceiro...
    echo $valor."<br>";
}

echo "<br>";
foreach($motos as $valor){ 
    echo $valor."<br>";
}

echo "<br>";
foreach($clientes as $valor){ 
    echo $valor."<br>";
}
echo "<br><hr>";

?>