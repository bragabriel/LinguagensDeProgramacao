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

    /*
    SANITIZAÇÃO
    https://www.php.net/manual/pt_BR/filter.filters.sanitize.php
    */

    //Verificando se existe o índice "enviar-formulário" na super global POST.
    //Se existir o índice, é porque alguém clicou no botão
    if(isset($_POST['enviar-formulario'])){

        $erros = array();

        //Sanitize: LIMPA AS VARIÁVEIS (espaços em branco, caracteres: ³£¢¹², etc)
        //Validate: VALIDA E VERIFICA SE O FORMATO ESTÁ CORRETO

        //filter_input(Pegando os dados através do método POST)
        $nome = filter_input(INPUT_POST, 'nome', FILTER_SANITIZE_SPECIAL_CHARS);
        //                  INPUT POST, nome variável, filtro_special_chars (Serve para escapar todos os códigos HTML)
        echo "$nome<br>";


        //filter_input(Pegando os dados através do método POST)
        $idade = filter_input(INPUT_POST, 'idade', FILTER_SANITIZE_NUMBER_INT);
        //                  INPUT POST, nome variável, filtro_number_int (Serve para pegar apenas números INT de tudo o que foi inserido)
        
        //Aplicando Filtro de Validação: (Valida a variável, não a entrada de dados)
        if(!filter_var($idade, FILTER_VALIDATE_INT)){
            $erros[] = "Idade precisa ser um inteiro!";
        }
        echo "$idade<br>";


        //filter_input(Pegando os dados através do método POST)
        $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
        //                  INPUT POST, nome variável, filtro_number_int (Serve para pegar apenas o email (Limpa caracteres como: ()-//))

        //Aplicando Filtro de Validação: (Valida a variável, não a entrada de dados)
        if(!filter_var($email, FILTER_VALIDATE_EMAIL)){
            $erros[] = "E-mail inválido!";
        }
        echo "$email<br>";


        //filter_input(Pegando os dados através do método POST)
        $url = filter_input(INPUT_POST, 'url', FILTER_SANITIZE_URL);
        //                  INPUT POST, nome variável, filtro_number_int (Serve para pegar apenas a URL (Limpa caracteres como: ²³£¢¹¬ ))

        //Aplicando Filtro de Validação: (Valida a variável, não a entrada de dados)
        if(!filter_var($url, FILTER_VALIDATE_URL)){
            $erros[] = "URL inválido!";
        }
        echo "$url<br>";


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

    <form action="<?php echo $_SERVER['PHP_SELF']?>" method="POST">
    <!--  action= ?php echo $_SERVER 'PHP_SELF' ?      =  Utilizando essa mesma página para processar os dados -->

        Nome: <input type="text" name="nome"><br>
        Idade: <input type="text" name="idade"><br>
        Email: <input type="text" name="email"><br>
        URL: <input type="text" name="url"><br><br>
        <button type="submit" name="enviar-formulario">Enviar</button>

    </form><br>

</body>
</html>