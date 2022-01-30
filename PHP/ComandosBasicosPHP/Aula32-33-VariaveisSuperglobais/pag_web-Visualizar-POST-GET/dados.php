<?php

//---------------------------------
// $_POST = Usada para coletar dados de formulário (de forma invisível)

//Recebendo o valor do index.php através do método POST

/*
echo "Dados recebidos através do método POST: <br><br>";
$nome = $_POST['nome'];  //$_POST['name do input (name="THIS NAME")']
$email = $_POST['email'];

echo "Seu nome é $nome e seu e-mail é $email <br>";

var_dump($_POST);
*/

//---------------------------------
// $_GET = Usada para coletar dados de formulário (através de parâmetros URL, ou seja, de forma visível na URL)

//Recebendo o valor do index.php através do método GET
echo "Dados recebidos através do método GET: <br><br>";
$nome = $_GET['nome'];  //$_POST['name do input (name="THIS NAME")']
$email = $_GET['email'];

echo "Seu nome é $nome e seu e-mail é $email <br>";

//Recebendo dados através do LINK:
//echo $_GET['idade']."<br>".$_GET['sobrenome']."<br>";

var_dump($_GET);
?>