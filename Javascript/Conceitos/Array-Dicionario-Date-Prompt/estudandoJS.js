var nome = prompt("Qual seu nome?");
alert("Bem-vindo, " + nome);

var idade = prompt("Qual sua idade?");

if(idade < 18){
    alert("Menor de idade, acesso negado!");

    $(document).ready(function(){
        $("h1").text("Acesso negado!").css({"color": "red", "font-weight": "bold"});
    });
}

else{
    alert("Maior de idade, acesso permitido!");

    $(document).ready(function(){
        $("h1").text("Acesso permitido!").css({"color": "green", "font-weight": "bold"});
    });

    //----------------------
    //ARRAY:
    console.log("Array:\n")

    var lista = ["maça", "pera", "laranja"];
    console.log(lista);

    //adiciona na lista
    lista.push("uva");
    console.log(lista);

    //remove na lista
    lista.pop();
    console.log(lista);

    //transforma o array em uma string
    console.log(lista.toString());

    //pega o primeiro elemento da lista
    console.log(lista[0]);

    //pega o primeiro elemento da string
    console.log(lista.toString()[0]);

    //transforma e string e muda o parametro de separação
    console.log(lista.join(" |*| "));
    //----------------------

    //----------------------
    //DICIONARIO:
    console.log("\n\nDicionario:\n")

    //var frutas = {nome:"maça", cor:"vermelha"}
    var frutas = [{nome:"maça", cor:"vermelha"}, {nome:"uva", cor:"roxa"}]
    console.log(frutas)

    //elemento nome[1] do dicionario frutas:
    console.log(frutas[1].nome);

    //elemento cor[0] do dicionario frutas:
    console.log(frutas[0].cor);
    //----------------------

    //----------------------
    //CONDICIONAIS, LAÇOS DE REPETIÇÃO:
    console.log("\n\nWhile:")
    var count = 0;
    while(count <= 5){
        console.log(count);
        count++;
    };

   
    console.log("For:");
    var count=0;
    for(cont = 0; count <= 5; count++){
        console.log(count);
    };
    //----------------------

    //----------------------
    //DATE:
    console.log("\n\nDate:")
    var data = new Date();
    alert(data);

    //pegando o mês, horas, minutos e segundos
    console.log("Mês: " + data.getMonth()+1);
    console.log("Horas: " + data.getHours());
    console.log("Minutos: " + data.getMinutes());
    console.log("Segundos: " + data.getSeconds());

    console.log("Hoje é dia: " + data.getDate()+"/"+(data.getMonth()+1))
    //----------------------
};