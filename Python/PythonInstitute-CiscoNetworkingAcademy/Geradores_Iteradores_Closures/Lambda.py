two = lambda: 2
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))


# Explicação: 

# a primeira lambda é uma função anónima sem parâmetros que devolve sempre 2.
#  Como a atribuímos a uma variável chamada two, podemos dizer que a função já não é anónima, e podemos usar o nome para a invocar.

# a segunda é uma função anónima de um parâmetro que devolve o valor do seu argumento ao quadrado.
#  Também a nomeámos como tal.

# a terceira lambda toma dois parâmetros e devolve o valor do primeiro elevado à potência do segundo.
#  O nome da variável que transporta a lambda fala por si. Não utilizamos pow para evitar confusão com a função integrada do mesmo nome e do mesmo objetivo.