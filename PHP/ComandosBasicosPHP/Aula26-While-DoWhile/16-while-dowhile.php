<?php

/*---------------*/
/*     WHILE     */
/*---------------*/

$contador = 1;

//exemplo 01
while($contador <= 4):
    echo "Contador é $contador <br>";
    $contador++;
endwhile;

$contador = 5;
//exemplo 02
while($contador <= 10){
    echo "Contador é $contador <br>";
    $contador++;
}

echo "<hr>";
/*------------------*/
/*     DO WHILE     */
/*------------------*/

$contador = 1;

do{
    echo "Contador é $contador <br>";
    $contador++;
}while($contador <= 10);

?>