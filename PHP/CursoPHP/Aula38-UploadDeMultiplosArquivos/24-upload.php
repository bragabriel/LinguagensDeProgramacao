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

        $quantidadeArquivos = count($_FILES['arquivo']['name']);

        $contador = 0;
    
        while($contador < $quantidadeArquivos){

            //Pegando a extensão do arquivo
            $extensao = pathinfo($_FILES['arquivo']['name'][$contador], PATHINFO_EXTENSION);

            //Verificando se a extensão do arquivo existe no array $formatosPermitidos
            if(in_array($extensao, $formatosPermitidos)){
                $pasta = "arquivos/";
                $temporario = $_FILES['arquivo']['tmp_name'][$contador];

                //renomeando o arquivo
                $novoNome = uniqid().".$extensao";

                //Verificação para saber se houve o upload
                if(move_uploaded_file($temporario, $pasta.$novoNome)){
                //                    arquivo temp, novoCaminho (pasta + novoNome)
                echo "Upload feito com sucesso para $pasta$novoNome<br>";
                }
                else{
                    echo "Erro ao enviar o arquivo $temporario <br>";
                }
            }
            else{
                echo "Extensão: '$extensao' não é permitida <br>";
            }

            $contador++;
        }

    }

    ?>

    <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST" enctype="multipart/form-data">
    <!--                                          
                           enctype= Necessário para o Upload de arquivos -->
        <input type="file" name="arquivo[]" multiple><br>
        <!-- multiple = Permite selecionar + de 1 arquivo. Para isso tbm precisamos colocar o array no name -->
        
        <input type="submit" name="enviar-formulario">
    
    </form>
</body>
</html>