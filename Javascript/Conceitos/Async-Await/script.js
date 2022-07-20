/* 
    Async e Await

    - As funções assíncronas funcionam como Promises, porém com uma sintaxe mais simples;
    - Precisamos declarar a função com a palavra async;
    - E quando precisamos aguardar por algo a instrução precisa ser de await;
    - Podemos aplicar o recurso em funções anônimas e métodos de classe;
    - Tentar usar o await sem o async gera um erro!
*/


                        /* exemplo 01 */
/* function primeiraFuncao(){

    return new Promise((resolve) => {
        
        setTimeout(() => {
            console.log("Esperou 1 segundo")
            resolve()
        }, 1000)
    
    })
}

async function segundaFuncao(){
    
    console.log("Iniciou")

    await primeiraFuncao()
    
    console.log("Terminou")
}

segundaFuncao() */


                        /* exemplo 02 */
//exemplo prático - API
function getUser(id){
    return fetch(`https://reqres.in/api/users?id=${id}`).then((data) => {
        return data.json()
    }).catch((err) => {
        console.log("Erro: " + err)
    })
}

async function showUserName(id){

    try{
        const user = await getUser(id)

        console.log(`O nome do usuário é: ${user.data.first_name}`)
    }catch(err){
        console.log("Erro: " + err)
    }
}

showUserName(2)