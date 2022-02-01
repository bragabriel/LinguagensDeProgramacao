<?php

$senha = "123456";

$novaSenha = base64_encode($senha);
//base64 = Criptografia de mão dupla (Tem uma função para codificar e uma função para descodificar)

echo "base64: $novaSenha<br>";
echo "Sua senha é: " . base64_decode($novaSenha);


echo "<br><hr>";
echo "Md5: ".md5($senha);
//md5 gera um hash de 32 caracteres. Não é possível descriptografar
//Como fazemos a autenticação da senha? Quando o usuário for se cadastrar no sistema, temos que criptografar a senha antes de inserir no Banco de Dados
//Quando formos fazer a comparação, temos que criptografar a senha inserida e comparar com a senha criptografada no banco de dados


echo "<br><hr>";
echo "Sha1: ", sha1($senha);
//Sha1, não é possível descriptografar.
//Segue o mesmo esquema da Md5


//MD5 e SHA1 são vulneráveis. Os hackers criam bancos de dados / dicionários com os hashs, pois a senha "123" vai sempre gerar o mesmo hash "hasdZZASD" por exemplo.


?>