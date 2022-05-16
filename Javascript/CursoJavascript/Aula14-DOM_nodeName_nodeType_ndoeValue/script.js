console.log(
    document.body.childNodes
)

var lista = document.body.childNodes
alert(lista.length)


console.log(lista[5].nodeName)
// Retorna 1 - nó de elemento
// 2 - nó de atributo
// 3 - nó de texto
// 8 - nó de comentário

console.log(lista[5].nodeType)

console.log(lista[5].nodeValue)

console.log(lista[5].innerHTML)

console.log(lista[5].childNodes[3].childNodes[0].nodeValue)