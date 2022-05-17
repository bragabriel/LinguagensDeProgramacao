/* Variáveis */

//JS é 'case sensitive'  -> Oi != oi

// var = (escopo global. Obs -> 'Var' vaza da função, por ex.)

// let = melhor prática, pois não vaza do escopo

// const = constante, não reescreve

if(true){
    nome = "Braga"; //Escopo Global
}
console.log(nome);

if(true){
    let nome2 = "Gabriel"; //Apenas escopo Local
    console.log(nome2)
}

const nome3 = "Gabriel"
// nome3 = "Braga"  <- não é possível (constante)

