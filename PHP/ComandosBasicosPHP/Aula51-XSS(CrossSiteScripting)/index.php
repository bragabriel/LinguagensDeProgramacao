<?php

/******************************/
/*  XSS Cross Site Scripting  */
/******************************/

// Semelhante ao SQL Injection, ao invés de inserir comandos SQL, o invasor insere Scripts no sistema.

//Exemplo de prevenção para esse ataque disponível no arquivo "create.php" da pasta: 'aula46-47-48-48-50-CRUD'

/*
----------------------------------------------------------------------
Exemplo de código vulnerável a XSS Attack e HTML CODE Attack:

    $nome = mysqli_escape_string($connect, $_POST['nome']);
    $sobrenome = mysqli_escape_string($connect, $_POST['sobrenome']);
    $email = mysqli_escape_string($connect, $_POST['email']);
    $idade = mysqli_escape_string($connect, $_POST['idade']);


----------------------------------------------------------------------
Exemplo de prevenção para os ataques:

//Clear - Prevenção à ataques:
function AttackPrevent($input){
    
    global $connect;

    //SQL Injection Prevent:
    $var = mysqli_escape_string($connect, $input);

    //XSS Attack Prevent:
    $var = htmlspecialchars($var);

    return $var;
}


    //FILTER_SANITIZE = HTML CODE ATTACK PREVENT
    $nome = filter_input(INPUT_POST, 'nome', FILTER_SANITIZE_SPECIAL_CHARS);
    $nome = AttackPrevent($nome);

    $sobrenome = filter_input(INPUT_POST, 'sobrenome', FILTER_SANITIZE_SPECIAL_CHARS);
    $sobrenome = AttackPrevent($sobrenome);

    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $email = AttackPrevent($email);

    $idade = filter_input(INPUT_POST, 'idade', FILTER_SANITIZE_NUMBER_INT);
    $idade = AttackPrevent($idade);
*/

?>