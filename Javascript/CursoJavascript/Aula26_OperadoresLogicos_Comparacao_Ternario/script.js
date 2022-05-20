/* Operadores: Lógicos, Comparação, Ternário */

let x = 5

//Op de comparação:
console.log(x == 5) //compara o número
console.log(x == "5") //compara o número
console.log(x === "5") //compara o número && o tipo de dado

console.log(x != 4)
console.log(x <= 2)


//Op lógicos:
let media = 8
let frequencia = 80

console.log(media >=  7 && frequencia >= 80)
console.log(media >= 9 || frequencia >= 50)


//Op ternário:
let idade = 16
let eleitor = (idade >= 16) ? "Pode votar" : "Não pode votar"
//              condição    ?  verdadeiro  ?   falso
console.log(eleitor) 