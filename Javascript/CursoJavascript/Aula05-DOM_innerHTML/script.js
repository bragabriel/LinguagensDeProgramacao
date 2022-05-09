console.log(
    document.getElementById("p1").innerHTML
)

document.getElementById("p1").innerHTML = "Novo conteúdo"


var paragrafo = document.getElementById("p1");

paragrafo.innerHTML = "novo conteúdoooooooo";

paragrafo.style.color = "red";
paragrafo.style.backgroundColor = "#333";
paragrafo.style.height = "400px";


var imagem = document.getElementById("imagem")
imagem.src = "img.png"
imagem.alt = "logo do html"
imagem.width = "50"