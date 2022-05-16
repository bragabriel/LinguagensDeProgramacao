console.log(
    document.documentElement.lastChild
)

console.log(
    document.documentElement.firstChild
)

console.log(
    document.body.childNodes
)

var lista = document.body.childNodes

console.log(
    "Child Nodes:",
    lista[5].innerHTML,
    "",
    lista[5].nodeName
)