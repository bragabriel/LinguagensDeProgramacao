var p = document.createElement("p");
p.innerHTML = "Olá pessoal!"; 
//Inserindo nosso paragrafo no elemento pai
document.getElementById("conteudo").appendChild(p);


var img = document.createElement("img");
img.src = "img.png";
//Inserindo no elemento pai ('conteudo')
document.getElementById("conteudo").appendChild(img)


//Removendo item do elemento pai
document.getElementById("conteudo").removeChild(p)