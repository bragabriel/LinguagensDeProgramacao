var lista = document.getElementsByTagName("ul");
console.log(lista);


var listaSeparada = document.getElementsByTagName("ul")[0];

var itens = listaSeparada.children;

var novoItem = document.createElement("li");

listaSeparada.insertBefore(novoItem, itens[0]);
                //novo item, onde ele vai entrar

novoItem.textContent = "Água";

console.log(listaSeparada);


var listaSeparada2 = document.getElementsByTagName("ul")[1]
var itens2 = listaSeparada2.children;
var novoItem2 = document.createElement("li");
novoItem2.textContent = "Margarina";

listaSeparada2.replaceChild(novoItem2, itens2[2]);
console.log(listaSeparada2);