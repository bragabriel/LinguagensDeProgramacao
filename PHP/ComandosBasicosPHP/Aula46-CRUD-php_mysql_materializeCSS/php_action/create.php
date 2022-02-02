<?php

//Conexão
require_once 'db_connect.php';

//Verificando se o usuário clicou no botão de índice/name = btn-cadastrar
if(isset($_POST['btn-cadastrar'])){

    //Atribuindo os dados que vieram do form para variáveis:
            //filtrando para evitar ataques SQL Injection
    $nome = mysqli_escape_string($connect, $_POST['nome']);
    $sobrenome = mysqli_escape_string($connect, $_POST['sobrenome']);
    $email = mysqli_escape_string($connect, $_POST['email']);
    $idade = mysqli_escape_string($connect, $_POST['idade']);

    //Inserindo os dados das variáveis no Banco de Dados na tabela 'clientes':
    $sql = "INSERT INTO clientes (nome, sobrenome, email, idade) VALUES ('$nome', '$sobrenome', '$email', '$idade')";

    //Verificando se a query(comando sql) foi executada com sucesso:
    if(mysqli_query($connect, $sql)){
        //Se deu certo, retornaremos para a index.php, passando como parâmetro através do link a string: "sucesso"
        header('Location: ../index.php?sucesso');
    }
    else{
        //Se NÃO deu certo, retornaremos para a index.php, passando como parâmetro através do link a string: "erro"
        header('Location: ../index.php?erro');
    }
}

?>