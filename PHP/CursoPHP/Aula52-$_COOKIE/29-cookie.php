<?php

/*----------------------------*/
/*          COOKIE            */
/*----------------------------*/


//Fica armazenado no computador do usuário e não no servidor
//O servidor apenas cria o arquivo e armazena no computador do usuário


//Setando Cookie:
//      'nome do cookie', 'valor do cookie', 'validade do cookie - time()+3600segundos = 1 hora'
setcookie('user', 'Gabriel Braga', time()+3600);
setcookie('email', 'gabriel.bragasilva@hotmail.com', time()+3600);
setcookie('ultima_pesquisa', 'tênis adidas', time()+3600);

var_dump($_COOKIE);


//Removendo Cookie:
//                                                  Colocamos valor negativo no time
setcookie('email', 'gabriel.bragasilva@hotmail.com', time()-3600);


//Exibindo dados do Cookie:
echo $_COOKIE['ultima_pesquisa'];
?>