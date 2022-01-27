<?php

//----------------------
// Array associativos
//----------------------

// Um array é associativo quando os índices ou chaves são STRINGS
$pessoa = array("nome"=>"Gabriel", "idade"=>23, "altura"=>1.75);


$pessoa["cidade"] = "Pirassununga"; // adicionando +1 índice (cidade) com o valor "Pirassununga" no array

//echo $pessoa["altura"];

foreach($pessoa as $indice => $valor){
    echo $indice.":".$valor."<br>";
}
echo "<br><hr>";

?>