<?php

//Encerrando a sessão:

//Iniciando a sessão
session_start();

//Limpando a sessão
session_unset();

//Destruindo a sessão
session_destroy();

//Redirecionado o usuário depois de finalizar a sessão
header('Location: index.php')

?>