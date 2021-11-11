//Treinando OBJETO em JavaScript

let mariana = {
    nome: "Julia Jorge",
    cursos: ["Análise de Sistemas", "Estrutura de Dados", "Introdução a computação"],
    isActive: true,
    points: 2000
};

let gabriel = {
    nome: "Gabriel Braga",
    cursos: ["Javascript", "Estrutura de Dados", "Programação para Web", "Introdução aos Frameworks"],
    isActive: true,
    points: 3200
};

let marcos = {
    nome: "Mariana de Matos",
    cursos: ["Análise de Sistemas", "Estrutura de Dados", "Introdução a computação"],
    isActive: false,
    points: 2400
};

let estudantes = [mariana, gabriel, marcos];

console.log(estudantes);

for(estudantes of estudantes){
    console.log('Estudantes Ativos(as): \n')
    if(estudantes.isActive){
        console.log(estudantes.points);
    };

        console.log("\n O(a) " + estudantes.nome + " está cursando:");
        for(curso of estudantes.cursos){
            console.log(curso);
        };
}