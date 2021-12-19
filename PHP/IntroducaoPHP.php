<!--
Vídeo aula disponível pelo canal: "Danki Code"
Link da vídeo aula: https://www.youtube.com/watch?v=NhUFUfzZowM&ab_channel=DankiCode
-->

<?php

// PHP = Personal Home Page

$nome = 'Gabriel';

$Gabriel = 'Bla Bla!';

echo 'O meu nome é '.$nome;  //variavel nome
echo '<br> O meu nome é '.$$nome; //interpreta a string Gabriel como a variavel Gabriel


//-----------------------

echo '<br><br>Teste idade 1:';

$idade = 20;

if($idade == '20'){ // == 'compara apenas o VALOR
    echo '<br> Idade confere!';
}else{
    echo '<br> Idade não confere!';
}

echo '<br><br>Teste idade 2:';
if($idade === '20'){ // === 'compara levando em conta o VALOR e o TIPO
    echo '<br> Idade confere!';
}else{
    echo '<br> Idade não confere!';
}


// Loops:
echo '<br><br>Loops:';

echo '<br>For:<br> ';
for($i=0; $i<10; $i++){
    echo $i;
    echo '<hr>';
}

$i=0;

echo '<br>While:<br> ';
while($i < 10){
    echo $i;
    echo '<br><hr>';
    $i++;
}


//Função:
echo '<br><br>Função: ';

function printNumero($n){
    echo '<br>'.$n;
}

printNumero(30);
printNumero(50);
printNumero(100-50);


//Classes:
echo '<br><br>Classes: ';

?>