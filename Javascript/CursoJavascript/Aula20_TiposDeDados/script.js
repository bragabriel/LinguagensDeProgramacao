/* Tipos de Dados */

//Tipagem dinâmica, não precisamos declarar int, ou string. 
//Basta atribuir o valor a variável

// string
var nome = "Gabriel"
console.log(typeof(nome))

//int
var idade = 20
console.log(typeof(idade))

//float
var float = 2.222
console.log(typeof(float))

//bolean
var solteiro = true
console.log(typeof(solteiro))

//array (tipo especial de objeto)
var frutas = ["goiaba", "maçã", "banana"]
console.log(typeof(frutas))

//object
var carro = new Object()
carro.fabricacao = "2025"
carro.cor = "azul"
console.log(typeof(carro))
console.log(typeof(carro.fabricacao))

//function
var soma = function(a, b){
    return a+b;
}
console.log(soma(10,5))
console.log(typeof(soma))