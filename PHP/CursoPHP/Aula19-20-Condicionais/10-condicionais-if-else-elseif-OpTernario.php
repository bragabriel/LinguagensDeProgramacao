<?php

$numero = 10;

//exemplo 01 A:
if ($numero == 10){
    echo "É igual a 10<br>";
}
else{
    echo "É diferente de 10<br>";
}


//exemplo 01 B:
if($numero == 10):
    echo "É igual a 10<br>";
else:
    echo "É diferente de 10<br>";
endif;

echo "<hr>";

//exemplo 02:
$numero = 50;
if ($numero == 10){
    echo "É igual a 10<br>";
}
elseif($numero <=9){
    echo "É menor ou igual a 9<br>";
}
else{
    echo "É diferente de 10<br>";
}

echo "<hr>";

//Operador ternário
$media = 7;

echo ($media >= 7) ? "Aprovado!" : "Reprovado";

?>