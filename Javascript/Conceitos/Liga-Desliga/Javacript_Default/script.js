/*function ligar(){
  var imagem;
  //document.getElementsByTagName("img")[0].setAttribute("src", "lamp_on.gif");
  // OU
  imagem = document.getElementsByTagName("img")[0];
  imagem.setAttribute("src", "lamp_on.gif");
}*/

/*function desligar(){
    var imagem;
    document.getElementsByTagName("img")[0].setAttribute("src", "lamp_off.gif");
}*/

function Mudar() {

  if (document.getElementById("img").value == "Ligar"){
    document.getElementById("img").value = "Desligar";
    document.getElementsByTagName("img")[0].setAttribute("src", "lamp_on.gif");
  }else{
    document.getElementById("img").value = "Ligar";
    document.getElementsByTagName("img")[0].setAttribute("src", "lamp_off.gif");
  }
}
