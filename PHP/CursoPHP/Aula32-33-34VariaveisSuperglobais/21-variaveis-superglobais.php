<?php

/*-------------------------------------*/
/*       Variáveis Super Globais       */

/*    
    $GLOBALS = Armazena todas as variáveis globais em um array chamado GLOBALS
    $_SERVER = Contém informações de cabeçalhos, caminhos e informações de script (array que contém vários índices)
    $_POST
    $_GET
    $_FILES
    $_ENV
    $_COOKIE
    $_SESSION

    Todos as variáveis super globais e exemplos de uso:
    https://www.php.net/manual/pt_BR/reserved.variables.server.php
*/

/*-------------------------------------*/


//---------------------------------
// $GLOBALS
$x = 10;
$y = 15;

function soma(){
    // echo $x + $y; Não dá para acessar as variáveis globais assim
    echo $GLOBALS['x'] + $GLOBALS['y']; //Acessando o array GLOBALS com todas as variáveis globais. Pegando o índice[variável]
}
soma();


echo "<br><br><hr>";
//---------------------------------
// $_SERVER
echo $_SERVER['PHP_SELF'].'<br><br>'; //Retorna o nome do arquivo script que está sendo executado
echo $_SERVER['SERVER_NAME'].'<br><br>'; //Retorna o nome do host do servidor onde o script está sendo executado
echo $_SERVER['SCRIPT_FILENAME'].'<br><br>'; //Retorna o caminho absoluto do script em execução
echo $_SERVER['DOCUMENT_ROOT'].'<br><br>'; //Retorna o diretório raiz do script em execução
echo $_SERVER['SERVER_PORT'].'<br><br>'; //Retorna a porta do servidor web
echo $_SERVER['REMOTE_ADDR'].'<br><br>'; //Retorna o endereço IP de onde o usuário está acessando a página 



?>