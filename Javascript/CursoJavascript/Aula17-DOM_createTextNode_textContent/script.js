var titulo = document.querySelector("h1")
var texto = document.createTextNode("Um texto qualquer")

titulo.appendChild(texto);

titulo.textContent = "Um novo texto";