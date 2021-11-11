//-------------------------
//Variável VAR
//problema: Ela Vaza dentro do escopo da função
function imprimeIdadeVAR(){
    var idade = 19
    console.log('Idade do Gabriel - Dentro da Function', idade)

    for(var idade = 19; idade<=100; idade++){
        console.log('Idade do Gabriel - Dentro do For', idade)
    }

    console.log('Idade do Gabriel - Fora do for, dentro da function', idade)

    if(true){
        var nome = 'Canadá'
    }
    console.log('Fora do if', nome)
}

imprimeIdadeVAR()



//-------------------------
//Variável LET
//obs: Não vaza dentro do escopo de for, while, if...
function imprimeIdadeLET(){

    for(let idade = 19; idade<=100; idade++){
        console.log('Dentro do For', idade)
    }

    console.log('Idade do Gabriel - Fora do for, dentro da function', idade)
}

imprimeIdadeLET()



//-------------------------
//Variável CONST
//obs: É imutável, não é possível alterar depois de definido,
//ao tentar incrementar um "i" em um for, apresentará erro.
const pais = 'Estados Unidos'
pais = 'Irlanda'


//-------------------------
//Variável CONST no JSON
//obs: podemos alterar um elemento do objeto JSON, mesmo sendo const
const nome = {
    nome: 'Marco',
    idade: 30
}

nome.idade = 31

console.log('Idade do Marco', nome.idade)