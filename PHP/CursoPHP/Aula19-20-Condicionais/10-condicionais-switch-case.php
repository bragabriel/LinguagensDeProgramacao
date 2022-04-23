<?php

$cor = "roxo";

switch($cor):

    case 'vermelho';
    echo "Sua cor preferida é o vermelho!";
    break;

    case 'verde';
    echo "Sua cor preferida é o verde!";
    break;

    case 'azul';
    echo "Sua cor preferida é o azul!";
    break;

    case 'amarelo';
    echo "Sua cor preferida é o amarelo!";
    break;

    default:
    echo "Sua cor preferida não é vermelho, verde, azul ou amarelo";

endswitch;

?>