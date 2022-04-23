<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <h1>Recebendo dados através do método <ins>POST</ins>: </h1><br>
    <form action="dados.php" method="POST">
        Nome: <input type="text" name="nome"><br>
        Email: <input type="email" name="email"><br><br>
        <!-- Botão INPUT, também passa os dados <input type="submit" name="enviar"> -->
        <button type="submit">Enviar</button>
        <p>(Remover o comentário do código no dados.php para funcionar, e comentar o código do método GET)</p>
    </form><br>



    <h1>Recebendo dados através do método <ins>GET</ins></h1><br>
    <form action="dados.php" method="GET">
        Nome: <input type="text" name="nome"><br>
        Email: <input type="email" name="email"><br><br>
        <!-- Botão INPUT, também passa os dados <input type="submit" name="enviar"> -->
        <button type="submit">Enviar</button><br>

        <!-- 
            É possível passar parâmetros através de LINK com o método GET
            href="dados.php?PARAMETROS"
        -->
        <a href="dados.php?idade=25&sobrenome=Braga">Enviar dados através de LINK</a>
    </form><br>

</body>
</html>