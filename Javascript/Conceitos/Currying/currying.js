//Comum em linguagens funcionais

/* Técnica de transformar uma função com vários parâmetros
 em apenas uma função que
para cada parâmetro retorna uma função*/

//---------------------------------------
//Exemplo de função normal - sem currying:
function semCurrying(a, b){
    return a + b;
}

console.log("\nSem currying:")
console.log(semCurrying(2, 2));
console.log(semCurrying(2, 3));
console.log(semCurrying(2, 4));
console.log(semCurrying(2, 5));

//---------------------------------------
//Exemplo da função acima usando currying:
function comCurrying(a){
    return function(b){
        return a + b;
    }
}

const soma2 = comCurrying(2);

console.log("\nCom currying:")
console.log(soma2(2));
console.log(soma2(3));
console.log(soma2(4));
console.log(soma2(5));