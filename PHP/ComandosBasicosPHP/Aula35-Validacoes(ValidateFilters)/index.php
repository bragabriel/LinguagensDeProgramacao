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

    /* VALIDAÇÕES
    Funções (filter_input - Filter_var)
    FILTER_VALIDATE_INT
    FILTER_VALIDATE_EMAIL
    FILTER_VALIDATE_FLOAT
    FILTER_VALIDATE_IP
    FILTER_VALIDATE_URL

    https://www.php.net/manual/pt_BR/filter.filters.validate.php
    */

    //Verificando se existe o índice "enviar-formulário" na super global POST.
    //Se existir o índice, é porque alguém clicou no botão
    if(isset($_POST['enviar-formulario'])){

        $erros = array();

        //Validando $idade e vendo se é do tipo INT
        if(!$idade = filter_input(INPUT_POST, 'idade', FILTER_VALIDATE_INT)){
            $erros[] = "Idade precisa ser um inteiro!";
        }

         //Validando $email e vendo se é do tipo EMAIL
         if(!$email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL)){
            $erros[] = "E-mail inválido!";
        }

        //Validando $peso e vendo se é do tipo FLOAT
        if(!$peso = filter_input(INPUT_POST, 'peso', FILTER_VALIDATE_FLOAT)){
            $erros[] = "Peso precisa ser um FLOAT!";
        }

        //Validando $ip e vendo se é do tipo IP
        if(!$ip = filter_input(INPUT_POST, 'ip', FILTER_VALIDATE_IP)){
            $erros[] = "IP inválido!";
        }

        //Validando $url e vendo se é do tipo URL
        if(!$url = filter_input(INPUT_POST, 'url', FILTER_VALIDATE_URL)){
            $erros[] = "URL inválida!";
        }


        //Se não estiver vazia:
        if(!empty($erros)){

            //Exibindo todos os erros ($erro) do array $erros
            foreach($erros as $erro){
                echo "<li> $erro </li>";
            }
        }
        else{
            echo "Parabéns, seus dados estão corretos!";
        }
    }
        
    ?>


    <h1>Recebendo dados através do método <ins>POST</ins>: </h1><br>
    <form action="<?php echo $_SERVER['PHP_SELF']?>" method="POST">
    <!--  action= ?php echo $_SERVER 'PHP_SELF' ?      =  Utilizando essa mesma página para processar os dados -->

        Idade: <input type="text" name="idade"><br>
        Email: <input type="email" name="email"><br>
        Peso: <input type="text" name="peso"><br>
        IP: <input type="text" name="ip"><br>
        URL: <input type="text" name="url"><br><br>
        <button type="submit" name="enviar-formulario">Enviar</button>

    </form><br>

</body>
</html>