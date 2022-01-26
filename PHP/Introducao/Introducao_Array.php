<?php

$notas = [
    'joao' => [
        'nota-provas' => [4, 5, 6],
        'nota-final' => 5
    ],
    'maria' => [
        'nota-provas' => [7, 5, 6],
        'nota-final' => 6
    ],
    'omar' => [
        'nota-provas' => [4, 5, 3],
        'nota-final' => 4
    ],
    'gabriela' => [
        'nota-provas' => [8, 7, 9],
        'nota-final' => 8
    ],
    'daniel' => [
        'nota-provas' => [2, 1, 3],
        'nota-final' => 2
    ],
    'lucia' => [
        'nota-provas' => [10, 8, 9],
        'nota-final' => 9
    ]
];

// nota final do aluno joão
echo $notas['joao']['nota-final']; // exibe 5

// Nota da primeira prova do aluno joão
echo $notas['joao']['nota-prova'][0] // exibe 4

?>