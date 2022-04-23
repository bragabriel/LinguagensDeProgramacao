<?php

$senha = "12345";
$senha_db = '$2y$10$pqe6xFGFOlxQrjqnsJkZUe6hTCjEr2TwVbR.IrGoLW.NCZa90tc2S';

$options = [
    'cost' => 10 //Quanto maior o custo, mais seguro o HASH. Contudo mais recursos do hardware serão consumidos para gerar o Hash.
    // O valor 10 para o custo é padrão, então não precisa colocar o $options se for utilizar o valor padrão
];


//                          $senha, ALGORITMO, [array de opções]
$senhaSegura = password_hash($senha, PASSWORD_DEFAULT, $options);

//password_hash sempre vai gerar um hash diferente, impossibilitando os banco de dados / dicionários de Hash's

echo $senhaSegura . "<br>";

//$senha(digitada pelo usuário) $senha_db(senha cadastrada no banco)
if(password_verify($senha, $senha_db)){
    echo "Senha válida";
}
else{
    echo "Senha inválida";
}

?>