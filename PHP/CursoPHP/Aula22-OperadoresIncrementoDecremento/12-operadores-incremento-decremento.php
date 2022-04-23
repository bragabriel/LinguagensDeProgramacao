<?php

/* ----------- */
/* Incremento: */
/* ----------- */

$valor = 20;
echo "Valor original: $valor <br><br>";

//Pré-incremento
echo 'Pré-incremento:'. ++$valor. '<br>';
//retorna 21, pois incrementou e retornou o valor

$valor = 20;

//Pós-incremento
echo 'Pós-incremento: '.$valor++.', '.$valor.'<br>';
//retorna o valor 20 e depois incrementa


echo "<br><hr><br>";
/* ----------- */
/* Decremento: */
/* ----------- */

$valor = 20;
echo "Valor original: $valor <br><br>";

//Pré-decremento
echo 'Pré-decremento:'. --$valor. '<br>';
//retorna 21, pois dez o decremento e retornou o valor

$valor = 20;

//Pós-incremento
echo 'Pós-decremento: '.$valor--.', '.$valor.'<br>';
//retorna o valor 20 e depois fez o decremento
?>