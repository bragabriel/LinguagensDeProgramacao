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
    $msg = "Clique em voltar para informar um nome na página de entrada.";
    # var_dump($_POST); # var_dump para ver o que veio com o submit

    if(isset($_POST["usuario"])){
        $nome = $_POST["usuario"];

        #genero
        if($_POST["gender"] == "Masculino"){
            $msg = "Olá cavalheiro ".$nome.", tudo certo?";
        }
        if($_POST["gender"] == "Feminino"){
            $msg = "Olá senhorita ".$nome.", tudo certo?";
        }
    }
    ?>
    <script>
        alert("<?php echo $msg; ?>");
    </script>
    <a href="ColetandoDados_RadioButton.php">Voltar</a>
    
</body>
</html>