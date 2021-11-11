//Default Function expression: 
function soma(number1, number2){
    return number1 + number2
}

console.log("Função padrão: " + soma(8,2));



//Anonymous Function (Sem nome)
const Anony = function(number1, number2){
    return number1 + number2
}
console.log("Função anonima: " + Anony(30, 30));



//Arrow Function:
const arrowSoma = (number1, number2) => {
    return number1 + number2
}

console.log("Função Arrow: " + arrowSoma(18,2));