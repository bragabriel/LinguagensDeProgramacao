<?php 
    //Diferença entre o INCLUDE e o REQUIRE:

    include 'header.php'; //Se não encontrar a pág header.php, ele exibe um erro e CONTINUA EXIBINDO o resto do script
    require 'header.php'; //Se não encontrar a pág header.php, ele exibe um erro e NÃO EXIBE o resto do script


    //Diferença entre o INCLUDE_ONCE e INCLUDE:

    //Aqui incluímos 2x o header na página
    include 'header.php';
    include 'header.php';

    //Aqui incluímos apenas 1x o header na página, pois mesmo estando duplicado o código, ele só faz a inclusão uma vez
    //Verifica se já está incluído, se não estiver, ele incluí,
    include_once 'header.php';
    include_once 'header.php';



    echo "Olá pessoal <br><br>"; 
    echo "Para visualizar os exemplos na prática, acesse o código fonte da página.<br>";
    echo "<ins>Botão direito</ins> -> <ins>Exibir código fonte da página</ins><br><br>";



    //Diferença entre o REQUIRE_ONCE e REQUIRE:

    //Aqui incluímos 2x o header na página
    require 'footer.php';
    require 'footer.php';

    //Aqui incluímos apenas 1x o header na página, pois mesmo estando duplicado o código, ele só faz a inclusão uma vez
    //Verifica se já está incluído, se não estiver, ele incluí,
    require_once 'footer.php';
    require_once 'footer.php';
?>