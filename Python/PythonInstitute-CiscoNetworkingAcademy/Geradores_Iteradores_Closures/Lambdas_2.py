# Como usar lambdas e para quê?

# A parte mais interessante da utilização de lambdas surge quando se pode 
# utilizá-los na sua forma pura - como partes anônimas de código destinadas a avaliar um resultado.


# Vamos analisá-la. A função print_function() toma dois parâmetros:

# o primeiro, uma lista de argumentos para os quais queremos imprimir os resultados;
# o segundo, uma função que deve ser invocada tantas vezes quanto o número de valores que são recolhidos dentro do primeiro parâmetro.

# Nota: também definimos uma função chamada poly() - esta é a função cujos valores vamos imprimir.

def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')


def poly(x):
    return 2 * x**2 - 4 * x + 2


print_function([x for x in range(-2, 3)], poly)

