<?php
    //Conexão com o db_connect.php
    require_once 'db_connect.php';

    //Sessão
    session_start();

    //Botão enviar
    //Se existir esse índice, é pq alguém clicou no botão de name="btn-entrar"
    if(isset($_POST['btn-entrar'])){
        $erros = array();

        //Pegando o dado que veio do input Login
            //Filtrando os dados mysqli_escape...($"conexão com o banco", $"_POST['variável']")
        $login = mysqli_escape_string($connect, $_POST['login']);
        $senha = mysqli_escape_string($connect, $_POST['senha']);

        //Verificando se os campos vieram vazios:
        if(empty($login) or empty($senha)){
            $erros[] = "<li>O campo login/senha precisa ser preenchido</li>";
        }
        else{
            //Consultando no banco os logins da tabela usuários onde login = $login (recebido do formulário através do método _POST)
            $sql = "SELECT login FROM usuarios WHERE login = '$login'";

            //Criando variável para armazenar o resultado da consulta
                //mysqli_query($conexao, "comando sql")
            $resultado = mysqli_query($connect, $sql);


            //Verificando se o login que o usuário digitou existe no Banco de Dados
                //Verificando se o número de linhas que existe na variável $resultado é maior do que 0
                //Se for > 0, é porque existe algum registro lá no banco
            if(mysqli_num_rows($resultado) > 0){
                
                //Criptografando a senha para bater com a senha do banco
                $senha = md5($senha);

                //Verificando se a senha que ele digitou confere com a que está armazenada no banco de dados
                $sql = "SELECT * FROM usuarios WHERE login = '$login' and senha = '$senha'";

                //Criando variável para armazenar o resultado da consulta
                    //mysqli_query($conexao, "comando sql")
                $resultado = mysqli_query($connect, $sql);

                //Verificando se no banco existe um login e uma senha igual ao login e senha digitado pelo usuário
                if(mysqli_num_rows($resultado) == 1){

                    //Converte o $resultado em um array e atribui na variável $dados
                    $dados = mysqli_fetch_array($resultado);

                    //Encerrando a conexão depois de realizar todas as consultas (Boa prática de programação)
                    mysqli_close($connect);

                    $_SESSION['logado'] = true;
                    $_SESSION['id_usuario'] = $dados['id'];

                    //Redirecionando o usuário
                    header('Location: home.php');
                }
                else{
                    $erros[] = "<li>Usuário e senha não conferem</li>";
                }
            }
            else{
                $erros[] = "<li>Esse usuário não existe</li>";
            }
        }
    }

?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema de Login</title>
</head>
<body>
    <h1>Login</h1>
    <?php
    //Se houver erros (se não estiver vazio o array $erros):
    if(!empty($erros)){
        //pegamos todos os $erro dentro do array $erros
        foreach($erros as $erro){
            echo "$erro <hr><br>";
        }
    }
    ?>

    <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST">
        Login: <input type="text" name="login"><br>
        Senha: <input type="password" name="senha"><br>
        <button type="submit" name="btn-entrar">Entrar</button>
    </form>
</body>
</html>