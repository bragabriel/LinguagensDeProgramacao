<?php

/*-------------------------------------*/
/*          DATAS - HORÁRIOS           */
/*-------------------------------------*/


//Setando o timezone
date_default_timezone_set('America/Sao_Paulo');

//data:
echo date('d/m/Y')."<br>";

//dia da semana:
echo date('l')."<br>";

//horário no formato 12horas
echo date('d/m/Y h')."<br>";

//horário no formato 24horas
echo date('d/m/Y H')."<br>";

//horário no formato 24horas, com minutos e segundos
echo date('d/m/Y H:i:s')."<br>";

//exibindo o PM/AM como 'A'
echo date('d/m/Y h:i:s A')."<br>";


//------------------------
//Datas no Banco de Dados:

//se a coluna for do tipo date:
$date = date('Y-m-d');
echo $date.'<br>';

//se o campo do bd for datetime:
$datetime = date('Y-m-d H:i:s');
echo $datetime.'<br>';


//-----------------------
//TIME - Retorna a hora atual medida no número de segundos desde a Era Unix (January 1 1970 00:00:00 GMT).
echo time().'<br>';
//echo date('d/m/Y', $time).'<br>';

//-----------------------
//MKTIME - Função para trabalhar com datas passadas ou futuras
//                    horas, minutos, segundos, dia, mês ( 2 dígitos), ano (4 dígitos)
$data_pagamento = mktime(15, 30, 00, 02, 03, 2022);
echo date('d/m - h:i', $data_pagamento).'<br>';

//------------------------
// STRTOTIME - Resgatando data do banco de dados - A data vai vir nesse formatado
$Date = '2019-04-10'; //se for tipo date
$DateTime = '2019-04-10 13:30:00'; //se for tipo datetime

//vem como string, temos que converter para time

$Date = strtotime($Date);
echo date('d/m/Y', $Date).'<br>';

//$DateTime = strtotime($DateTime).'<br>';
//echo date('d/m/Y', $DateTime).'<br>';
?>