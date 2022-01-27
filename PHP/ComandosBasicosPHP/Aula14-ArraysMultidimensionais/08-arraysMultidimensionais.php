<?php

//--------------------------
// Arrays multidimensionais
//--------------------------

// Um array multidimensional é um array que contem um ou mais arrays
$times = array(
    "cariocas"=> array("campeao"=>"Vasco", "vice"=>"Flamengo", "terceiro"=>"Botafogo"),
    "paulistas"=> array("3 lugar"=>"Santos", "1 lugar"=>"São Paulo", "2 lugar"=>"Palmeiras"),
    "baianos"=> array("teste"=>"Bahia", ""=>"Vitoria", "teste3"=>"Itabuna")
);

//echo $times["cariocas"][0]."<br>";
echo $times["cariocas"]["terceiro"]."<br>";
echo $times["paulistas"]["1 lugar"]."<br>";

echo "<br>";
foreach($times["paulistas"] as $indice => $valor){
echo $indice.": ".$valor."<br>";
}

echo "<br>";
foreach($times["cariocas"] as $indice => $valor){
echo $indice.": ".$valor."<br>";
}

echo "<br>";

foreach($times["baianos"] as $i => $valor): //Para cada item do Array times - baianos, atribuir o indice para $i e o valor para $valor
echo $i.": ".$valor."<br>";
endforeach

?>