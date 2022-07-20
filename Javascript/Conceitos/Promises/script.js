/* 
    Promises

    - Promises são como promessas, elas esperam algum retorno
    - Para criar promessas precisamos instanciar a classe Promise;
    - Ela leva dois argumentos, o 'resolve'(solução) e o 'reject'(erro);
    - Para encadear mais processos utilizamos o método then
    - Alguns recursos de JS (Fetch API) e bibliotecas retornam Promises.
*/


                        /* Promise 01 */
//Criando uma promessa
const myPromise = new Promise((resolve, reject) => {
    
    const nome = "GaBRieL"
   
    if(nome === "GaBRieL"){
        resolve(`Usuário ${nome} encontrado!`)
    }else{
        reject(`O usuário ${nome} não foi encontrado!`)
    }
})

myPromise.then((data) => {
    console.log(data)
})


                        /* Promise 02 */
//Encadeamento de then's
const myPromise2 = new Promise((resolve, reject) => {
    
    const nome = "GaBRieL"
   
    if(nome === "GaBRieL"){
        resolve(`Usuário ${nome} encontrado!`)
    }else{
        reject(`O usuário ${nome} não foi encontrado!`)
    }
})

myPromise2.then((data) => {
    return data.toLowerCase()
}).then((stringModificada) => {
    console.log(stringModificada)
})


                        /* Promise 03 */
//Retorno do Catch = tratando erro ao invés de aparecer o Reject na tela
const myPromise3 = new Promise((resolve, reject) => {
    
    const nome = "GaBRieL"
   
    if(nome === "gaBRieL"){
        resolve(`Usuário ${nome} encontrado!`)
    }else{
        reject(`O usuário ${nome} não foi encontrado!`)
    }
})

myPromise3.then((data) => {
    console.log(data)
}).catch((err) => {
    console.log("Erro: " + err)
})


                        /* Promise 04 */
//Tratando varias promises
const p1 = new Promise((resolve, reject) => {
    resolve("p1 Ok")
})
const p2 = new Promise((resolve, reject) => {
    resolve("p2 Ok")
})
const p3 = new Promise((resolve, reject) => {
    resolve("p3 Ok")
})

const resolveAll = Promise.all([p1, p2, p3])
    .then((data) => {
        console.log(data)
})


                        /* Promise 05 */
//Fetch API request
const userName = 'bragabriel'
const URL = 'https://api.github.com/users'

/* fetch(https://api.github.com/users/bragabriel) */
/* fetch(https://api.github.com/users/${userName}) */
fetch(`${URL}/${userName}`, {
    method: 'GET',
    headers:{
        Accept: 'application/vnd.github.v3+json',
    },
})
.then((response) => {
    console.log(response)
    console.log(typeof(response))
    return response.json()
})
.then((dataEmJSON) => {
    console.log(dataEmJSON)
    console.log(`O nome do usuário desse perfil do GitHub é ${dataEmJSON.name}`)
}).catch((err) => {
    console.log("Erro: " + err)
})

