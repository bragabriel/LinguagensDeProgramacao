/* Objeto */

let pessoa = {
    nome: "Gabriel",
    idade: 20,
    feliz: true,
    setup: ["computador", "mouse", "teclado", "monitor"],
    carros: {
        camaro:{
            placa: 12345,
            cor: "amarelo"
        },
        lamborghini:{
            placa: 54321,
            cor: "laranja"
        }
    },

    //método:
    viajar: function(km){
        alert(pessoa.nome + " viajou por: " + km + "km")
    }

} //criando obj



console.log(pessoa)
console.log(pessoa.nome)
console.log(pessoa.setup[0])

pessoa.nome = "Gabriel B."
console.log(pessoa.nome)

console.log(pessoa.carros)
console.log(pessoa.carros.camaro.cor)
console.log(pessoa.carros.lamborghini.placa)

pessoa.viajar(100)