<!--
Vídeo aula disponível pelo canal: "DFILITTO"
Link da vídeo aula: https://www.youtube.com/watch?v=SQCE24KZNHw&ab_channel=DFILITTO
-->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form>
        <p>Qual o seu nome?: </p>
        <input type="text" name="usuario">
        <input type="submit" value="Enviar">
    </form>
</body>
</html>



<?php

if(isset($_GET["usuario"])){
    //Se existir valor dentro do vetor GET pos[usuario]:
    $nome = $_GET["usuario"];
    $msg = "Olá ". $nome. ", Welcome! =)";
    echo "<h1>$msg</h1>";
}


$n1 = 3;
$n2 = 2;

echo "<h2> Valores: $n1 e $n2 </h2>";

echo "A soma vale ", ($n1 + $n2);
echo "<br/> A subtração vale ", ($n1 - $n2); 
echo "<br/> A multiplicação vale ", ($n1 * $n2);
echo "<br/> A divisão vale ", ($n1 / $n2);
echo "<br/> O módulo vale ", ($n1 % $n2);

?>