<?php

/*----------------------*/
/*       Funções        */
/*----------------------*/

//ex 01:
function exibirNome(){
    echo "Meu nome é Gabriel<br>";
}
exibirNome();


//ex 02:
function exibirNome2($nome){
    echo "Meu nome é $nome <br>";
}
exibirNome2("Gabriel");


echo "<br><hr>";

//Função Calcular Média:
function calcularMedia($nome, $n1, $n2, $n3, $n4){
    $media = ($n1 + $n2 + $n3 + $n4) / 4;
    if($media >= 7){
        echo "$nome foi aprovado com a média: $media <br>";
    }
    else{
        echo "$nome foi reprovado com a média: $media <br>";
    }
}
calcularMedia("Bob", 5, 6, 4, 10);
calcularMedia("Douglas", 8, 7, 8, 6);

?>