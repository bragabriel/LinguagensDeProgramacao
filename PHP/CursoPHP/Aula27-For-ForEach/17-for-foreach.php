<?php

//-------------------
// FOR:
//-------------------

for($i = 0; $i <= 4; $i++):
    echo "O valor do contador é: $i . <br>";
endfor;

for($i = 5; $i <= 10; $i++){
    echo "O valor do contador é: $i ,<br>";
}

echo "<br><hr>"; 

// Tabuada com FOR:
for($i = 0; $i <= 10; $i++){
    echo "8 x $i = ".($i*8)."<br>";
}

echo "<br><hr>";

//-------------------
// FOR EACH: (geralmente usado para percorrer Arrays)
//-------------------

$cores = array("Verde", "Azul", "Amarelo", "Vermelho", "Rosa");

foreach($cores as $valor):  //em cada repetição, vai atribuir um item do $cores para a variavel que acabou de ser criada "$valor"
    echo("$valor <br>");
endforeach;

echo "<br><hr>";


foreach($cores as $indice => $valor){  //Atribuindo para cada item de $cores = um indice e um valor
    echo("$indice - $valor <br>");
}

echo "<br><hr>";

// Tabuada com FOR EACH:
$numeros = array(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
foreach($numeros as $i){ //para cada $i em $numeros faça:
    echo '8 x '.$i.' = '.($i*8).'<br>';
}

echo "<br><hr>";

?>