//--------------------------
//representação de variáveis:
const title = "Harry Potter";
const url = "https://caminho.com/imagem";

//mostrando o conteúdo da variável:
console.log('\n Variável title: ',title)


//---------------------------
//Objeto:
//variável que guarda um objeto
//as variáveis dentro do objeto estão atreladas
const movie = {
    //atributo ou propriedade do objeto: title
    title: "Harry Potter",
    url: "https://caminho.com/imagem",
};


//mostrando o conteúdo do objeto:
console.log('\n Objeto title: ',movie.title, '\n url:', movie.url, '\n');



//---------------------------
//Treinando o uso do JSON
//Transformando um array em JSON em um objeto Javascript
let MeuJSON='{"colaboradores":['+
    '{"nome":"Bruno", "salario":10000, "idade":40},'+
    '{"nome":"Gabriel", "salario":1000000, "idade":19},'+
    '{"nome":"Douglas", "salario":230000, "idade":50}'+
']}'

console.log('\n JSON: ', MeuJSON);

//Parse é quando tem o JSON e converte em objeto literal JS
let colaboradoresObjeto = JSON.parse(MeuJSON);
console.log('\n Meu objeto literal: ', colaboradoresObjeto);
//Stringify é quando tem o elemento JS e converte para JSON


//Acessando o elemento do array objeto:
console.log(colaboradoresObjeto.colaboradores);

console.log(colaboradoresObjeto.colaboradores[0]);

console.log(colaboradoresObjeto.colaboradores[0].nome);



//---------------------------------
//Array com objetos em JS:
let MeuOBJ=[
    {"nome":"Bruno", "salario":10000, "idade":40},
    {"nome":"Gabriel", "salario":1000000, "idade":19},
    {"nome":"Douglas", "salario":230000, "idade":50}
]

//Convertendo o array em JS para JSON
//Stringify é quando tem o elemento JS e converte para JSON
let colaboradoresJSON = JSON.stringify(MeuOBJ)

//Acessando JSON:
console.log(colaboradoresJSON);



