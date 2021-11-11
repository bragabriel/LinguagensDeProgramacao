import math

num = int(input('Digite um número: '))

raiz = math.sqrt(num)

print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))

# import math : importa toda a biblioteca math
# math.ceil() : Arredonda para cima
# math.floor() : Arredonda para baixo


# from math import ceil: importa apenas ceil da biblioteca math
# ceil() : Arredonda para cima
# floor() : Arredonda para baixo