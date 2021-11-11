// callback -> promise

//callback = vai chamar depois
//promise = faz uma "promessa" que no futuro vou trazer um valor para ele

//------------------------
const fs = require('fs')

console.log(1)

//ler arquivo é uma operação custosa ao computador
/*o js empilha essa requisição e quando terminar de ler,
vai chamar de volta um trecho do código
chamar de volta uma função = callback*/
function callback(err, contents){
    console.log(err, String(contents));
}

//lê o arquivo, e quando tiver pronto chama de volta
fs.readFile('./arq1.txt', callback);



//---------------------------
//PROMISE
const readFile = file => new Promise((resolve, reject) => {
    fs.readFile(file, (err2, contents2) => {
        if(err2){
            reject(err2)
        }
        else{
            resolve(contents2)
        }
    })
})
readFile('./arq2.txt').then(contents2 =>{
    console.log(String(contents2))
})


console.log(2)

console.log(3)