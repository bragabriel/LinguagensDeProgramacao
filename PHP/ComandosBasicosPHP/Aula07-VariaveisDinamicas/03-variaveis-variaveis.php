<?php


//Variáveis variáveis
echo "Exemplo 01: <br>";
//exemplo 01:
$bebida = "refrigerante"; 

//Estou dizendo que o nome dessa variável será o valor da variável $bebida
$$bebida = "Guanará";

echo $refrigerante;
echo "<br><br>";


echo "Exemplo 02: <br>";
//exemplo 02:
$destino = "cidade"; //Variável $destino recebe o valor "cidade"

$$destino = "Ilhéus"; //Criei a variável com o nome "cidade" e atribuí à ela o valor "Ilhéus"

echo "Variável \$destino | Conteúdo: $destino <br>";
echo "Variável \$\$destino | Conteúdo: $cidade <br>";


?>