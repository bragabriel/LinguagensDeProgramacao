var lista = document.getElementsByTagName("ul");
console.log(lista);


var listaSeparada = document.getElementsByTagName("ul")[0];
console.log(listaSeparada);

var itens = listaSeparada.children

var novoItem = document.createElement("li")

listaSeparada.insertBefore(novoItem, itens[0])
                //novo item, onde ele vai entrar

novoItem.textContent = "Suco de Laranja"