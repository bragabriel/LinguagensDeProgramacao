<?php

    //Conexão com o db_connect.php
    require_once 'db_connect.php';

    //Sessão
    session_start();

    //Verificação - Verificando se a sessão está encerrada
        //Importante para o usuário não conseguir acessar a página restrita sem estar logado (sessão ativa)
    //Se a sessão não for 'logado':
    if(!isset($_SESSION['logado'])){
        header('Location: index.php');
    }

    //Dados
    //Atribuindo o id do usuario para a variável $id
    $id = $_SESSION['id_usuario'];

    //Pegando os dados do usuário cujo id = $id
    $sql = "SELECT * FROM usuarios WHERE id = '$id'";

    //Realizando a consulta no banco e atribuindo o resultado para a variável $resultado
    $resultado = mysqli_query($connect, $sql);

    //Variável $dados recebe todos os dados do usuário 
    $dados = mysqli_fetch_array($resultado);

    //Encerrando a conexão depois de realizar todas as consultas (Boa prática de programação)
    mysqli_close($connect);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Página Restrita</title>
</head>
<body>
    <h1>Restricted page</h1>

    <h1>Olá <?php echo $_SESSION['id_usuario']; ?> </h1>

    <a href="logout.php">Logout</a>

</body>
</html>