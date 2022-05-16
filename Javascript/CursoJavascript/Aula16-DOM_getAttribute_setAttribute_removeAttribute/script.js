document.getElementById("btn-set").addEventListener("click", function(){
                                 //evento que vamos escutar,  função

    document.getElementById("tittle").setAttribute("class", "red");
    //attributo que vamos setar, valor que queremos passar
    //ex: .red: #ff0000;    vamos passar o attr 'class' pois é uma class, e o valor 'red' (nome da nossa class)
})


document.getElementById("btn-remove").addEventListener("click", function(){                       
    document.getElementById("tittle").removeAttribute("class");
    //removendo o attr 'class' do elemento cujo id é 'tittle'
})

document.getElementById("btn-get").addEventListener("click", function(){                       
    var valorDoAttr = document.getElementById("tittle").getAttribute("class");
    //Recebendo o valor do Atributo e guardando na variável

    document.getElementById("class").innerHTML = valorDoAttr;
    //Atribuindo o valor da variável no nosso elemento de id 'class'
})