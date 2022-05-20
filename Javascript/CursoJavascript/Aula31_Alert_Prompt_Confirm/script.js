/*

Alert = método do window que recebe apenas um parametro (string)

Prompt = método do window que recebe um parametro (string) e retorna o valor da caixa

Confirm = método do window que retorna true ou false

*/



//window.prompt("Digite seu nome")  ou  prompt("Digite seu nome")
let nome = window.prompt("Digite seu nome")


//window.confirm()  Ou   confirm()  -> Retorna True ou False
let resposta = window.confirm("Deseja prosseguir?")

console.log(resposta)

if(resposta == true){
    // window.alert("Alert")  Ou  alert("Alert")
    window.alert("Olá " + nome)
}else{
    window.alert("Até logo!")
}



