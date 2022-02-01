<?php

/********************/
/*  SQL INJECTION   */
/********************/

//O que é?
//Tipo de ataque que se aproveita de sistemas que interajam com Banco de Dados e não possuem tratamentos nos inputs

//Como funciona?
// Sabendo que o sistema faz uma consulta no Banco de Dados, então ao invés de ele inserir a informação correta no input,
// ele insere códigos SQL para manipular as consultas

/*
Exemplo: 

//Consultando no banco os logins da tabela usuários onde login = $login (recebido do formulário através do método _POST)
$sql = "SELECT login FROM usuarios WHERE login = '$login'";

O hacker pode inserir um código sql no input

//Pegando o dado que veio do input Login
            //Filtrando os dados mysqli_escape...($"conexão com o banco", $"_POST['variável']")
        $login = mysqli_escape_string($connect, $_POST['login']);
        $senha = mysqli_escape_string($connect, $_POST['senha']);

        Com esse filtro, eliminaremos caracteres como \n, \r, \, ', ", escapando assim de códigos SQL
*/
?>