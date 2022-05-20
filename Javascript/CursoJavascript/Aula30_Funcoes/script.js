/* Functions */

function exibirAlert(){
    alert("Alerta!")
}

function soma(){
    return (5 + 5)
}

function somaComParametros(x, y){
    let result = x + y
    return result
}

function testando(x, y){
    let paragrafo = document.createElement("h1")

    let resultado = x + y
    
    paragrafo.innerHTML = resultado

    //Inserindo nosso paragrafo no elemento pai
    document.getElementById("teste").appendChild(paragrafo);
}

//exibirAlert()

console.log(soma())

console.log(somaComParametros(10, 5))

document.getElementById("resultado").innerHTML = somaComParametros(50, 70)

testando(7, 7)
