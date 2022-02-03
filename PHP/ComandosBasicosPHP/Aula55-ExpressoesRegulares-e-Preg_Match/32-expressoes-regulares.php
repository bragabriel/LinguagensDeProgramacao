<?php

/*---------------------------------------*/
/*          EXPRESSÕES REGULARES         */
/*---------------------------------------*/

//Serve para definir um padrão a ser usado para procurar ou substituir palavras/grupo de palavras




//          ^ = Início da expressão
//          $ = Fim da expressão
//          i = Vai pegar tanto minúscula como maiúscula
//          {} = Ocorrências - ?{0,1}  *{0,}  +{1,}
//          {X, Y} = Validando de X caractere até Y caractere
//          {X} = Validando X caracteres, se tiver + ou - vai dar erro
//          ? = Podemos aceitar nenhuma ou uma ocorrência (Se só tiver 1 = aceita, se não tiver nenhum = aceita)
//          * = Podemos não ter nenhuma ocorrência ou várias ocorrências
//          + = Só não aceita se não tiver nenhuma ocorrência

//$padrao = "/^[a-z0-9]{6}?$/i"; //expressões regulares

$string = "Abcabc";
$padrao = "/^[a-z0-9]?$/i"; //expressões regulares

echo "1° validação: <br>";
if(preg_match($padrao, $string)){
    //se quando a gente fizer a comparação o result for true:
    
        echo "Válido<br>";
        echo $string;
        echo "<hr><br>";
        
}
else{
    echo "Inválido";
    echo "<hr><br>";
}


//------------------------------------
$stringEmail = "contato@gmail.com";
$padraoEmail = "/^[a-z0-9.\-\_]+@[a-z0-9.\-\_]+\.(com|br|com.br)$/i"; //aceitando a-z, 0-9, . , - , _ , @

echo "2° validação - String Email: <br>";
if(preg_match($padraoEmail, $stringEmail)){
    //se quando a gente fizer a comparação o result for true:
    
        echo "Válido<br>";
        echo $stringEmail;
        echo "<hr><br>";
        
}
else{
    echo "Inválido";
    echo "<hr><br>";
}


//------------------------------------
$stringData = "02/03/2022";
$padraoData = "/^[0-9]{2}\/[0-9]{2}\/[0-9]{4}$/i"; // 0-9 {2 ocorrências} / 0-9 {2} / 0-9 {4}

echo "3° validação - Data:<br>";
if(preg_match($padraoData, $stringData)){
    //se quando a gente fizer a comparação o result for true:
    
        echo "Válido<br>";
        echo $stringData;
        echo "<hr>";
}
else{
    echo "Inválido";
    echo "<hr>";
}