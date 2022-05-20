let fruta = {nome: "banana", preco: "9.99", unidade: 1}

//For In: Percorre as propriedades de um objeto
for(let valor in fruta){
    console.log("id: ", valor)
    console.log("conteúdo: ", fruta[valor])
}



console.log("-=-=-=-=-=-=-=-=-=-=-=-=-")

let aparelhos = ["Celular", "Fone de ouvido", "Microfone"]

//For Of: Percorre as propriedades de um array
for (let i of aparelhos){
    console.log("conteúdo: ", i)
}


