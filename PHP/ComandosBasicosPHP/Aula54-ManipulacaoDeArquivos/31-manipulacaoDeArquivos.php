<?php

/*-------------------------------------------*/
/*          Manipulação de Arquivos          */
/*-------------------------------------------*/

//          caminho até o arquivo
$arquivo = '../Aula54-ManipulacaoDeArquivos/arquivo.txt';
$conteudo = "Conteúdo teste \r\n";

//                  nomeArquivo, modo (r, a, w..)
$arquivoAberto = fopen($arquivo, 'r');

//Tamanho arquivo
$tamanhoArquivo = filesize($arquivo);

/*
//Inserindo conteúdo no arquivo
//      arquivoAberto, conteudo a ser inserido
fwrite($arquivoAberto, $conteudo);
*/

//Lendo o conteúdo do arquivo
while(!feof($arquivoAberto)){ 
    //enquanto não for o final do arquivo
    
    //Pegando o conteúdo de cada linha e atribui à variável linha
    $linha = fgets($arquivoAberto, $tamanhoArquivo);

    echo $linha."<br>";

}


//Fechando arquivo aberto
fclose($arquivoAberto);
?>