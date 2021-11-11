//----------------------
//Alterar elementos na página
function clicou(){
    document.getElementById("agradecimento").innerHTML = " <b> Obrigado por clicar</b>"
    document.getElementById("clique1").innerHTML = "<u><i>Clique aqui</i></u>"
    document.getElementById("clique2").innerHTML = "<u><i>Clique aqui</i></u>"
    alert("Obrigado por clicar!");
}

//------------
//Redirecionar
function redirecionar1(){
    window.open("https://github.com/bragabriel")
}
function redirecionar2(){

    window.location.href = "https://github.com/bragabriel"
}

//-------------
//Mouse Move
function trocar(){
    //alert("trocar texto")
    console.log("Passou o mouse!")
    document.getElementById("mouseMove1").innerHTML = " <b>Passou o mouse aqui</b>"
}

function voltar(){
    document.getElementById("mouseMove1").innerHTML = " <b>Passe o mouse aqui <---</b>"
}

//Elemento e "THIS"
function trocar2(elemento){
    elemento.innerHTML = "Obrigado por passar o mouse aqui"
}

function voltar2(elemento){
    elemento.innerHTML = "Passe o mouse aqui"
}


//------------
//LOAD
function load(){
    alert("Página carregada!")
}

//------------
//CHANGE
function change(elemento){
    console.log(elemento.value)
}