<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <?php

    //Verificando se existe o índice 'enviar-formulario' na GLOBAL _POST.
    //Se o índice existir, é porque o usuário clicou no submit de name="enviar-formulario"
    if(isset($_POST['enviar-formulario'])){
        $formatosPermitidos = array("png", "jpeg", "jpg", "gif");

        //Pegando a extensão do arquivo
        $extensao = pathinfo($_FILES['arquivo']['name'], PATHINFO_EXTENSION);

        //Verificando se a extensão do arquivo existe no array $formatosPermitidos
        if(in_array($extensao, $formatosPermitidos)){
            $pasta = "arquivos/";
            $temporario = $_FILES['arquivo']['tmp_name'];

            //renomeando o arquivo
            $novoNome = uniqid().".$extensao";

            //Verificação para saber se houve o upload
            if(move_uploaded_file($temporario, $pasta.$novoNome)){
            //                    arquivo temp, novoCaminho (pasta + novoNome)
            $mensagem = "Upload feito com sucesso!<br>";
            }
            else{
                $mensagem = "Erro, não foi possível fazer o upload";
            }
        }
        else{
            $mensagem = "Formato inválido";
        }

        echo $mensagem;
    }

    ?>

    <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST" enctype="multipart/form-data">
    <!--                                                             enctype= Necessário para o Upload de arquivos -->
        <input type="file" name="arquivo"><br>
        <input type="submit" name="enviar-formulario">
    </form>
</body>
</html>