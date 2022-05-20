/* Loops */

let paises = document.getElementsByClassName('pais')


console.log("Usando For:")
for(let i = 0; i < paises.length; i++){
    console.log(paises[i])
    console.log(paises[i].innerHTML)
}


console.log("\n Usando While: ")
let i = 0;
while(i < paises.length){
    console.log(paises[i])
    console.log(paises[i].innerHTML)

    i++;
}


console.log("\n Usando Do While: ")
let j = 0;
do{
    console.log(paises[j])
    console.log(paises[j].innerHTML)

    j++;
}while(j < paises.length)


