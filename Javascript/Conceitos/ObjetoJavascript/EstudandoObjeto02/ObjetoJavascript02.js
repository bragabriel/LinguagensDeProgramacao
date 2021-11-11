function load(){
    var produtos = new Array('caneta', 'lapis', 'tesoura', 'borracha', 'caderno', 'livro');

    //criando referencia em javascript para o elemento de id: output
    //var output = document.querySelector('#output')

    var msg = '';

    produtos.push('compasso', 'cola', 'cartolina');

    console.log(produtos.length);

    produtos.pop();

    //propriedade length sempre retorna quantos indices tem
    for(var i=0; i<produtos.length; i++){
        msg += 'produto ' + (i + 1) + ': ' + produtos[i] + '<br>';
    }

    output.innerHTML = msg;
}