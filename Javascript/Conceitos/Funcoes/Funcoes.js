//----------
//Função soma:
function soma(n1, n2){
    return n1 + n2;
}
//alert(soma(5, 10));
console.log(soma(5,10));

//----------
//Função de replace:
function setReplace(frase, nome, novo_nome){
    return frase.replace(nome, novo_nome)
}
console.log(setReplace("Essa frase é a que estou passando para a função", "que estou passando para a função", "modificada"));

//----------
//Função com variável:
function validarIdade(idade){
    var validar;
    if(idade >= 18){
        validar = true
    }else{
        validar = false
    }
    return validar;
}

var idade = prompt("Qual sua idade?");
console.log(validarIdade(idade));

