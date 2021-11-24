# Tutorial disponível no YouTube, pelo canal 'Otávio Miranda'
# Vídeo aula do tutorial: https://www.youtube.com/watch?v=gHrc6FLBh20&ab_channel=Ot%C3%A1vioMiranda


# "um objeto “iterável”, ele é qualquer tipo de coisa que você consegue realizar um laço sobre, por exemplo, um array, um objeto, uma sequencia de números, uma stream, ou qualquer coisa"
# por: Santos, Lucas. | https://medium.com/trainingcenter/iterators-em-javascript-880adef14495#:~:text=Se%20voc%C3%AA%20ainda%20n%C3%A3o%20entendeu,uma%20stream%2C%20ou%20qualquer%20coisa.

import time
import sys

lista = [0, 1, 2, 3, 4, 5]
String = 'String'
Numeros = 1, 2, 3, 4

print(hasattr(lista,'__iter__')) # Confirmando que a lista é um objeto iteravel
print(hasattr(String,'__iter__')) # String é um objeto iteravel
print(hasattr(Numeros,'__iter__')) # Números não são iteraveis

print(hasattr(lista, '__next__')) # Se tivesse o método __next__ a lista seria um iterador

# Se é objeto iteravel, podemos utilizar o 'for'
# O método for utiliza o método iterador
for v in lista:
    print(v, end=' ')

#-------------------- 
print('\n\n Iterando nossa lista: \n')
lista = iter(lista) # Iterando nossa lista

print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

print(hasattr(lista, '__next__')) # Tem o método __next__, a lista está iterada

# obs: Um iteravel é um objeto que podemos iterar sobre ele, mas ele não necessáriamente é um Iterador
# Um iterador vai te dar um valor de cada vez


#---------------------------------------

# Entendendo os Geradores: 

# Uma 'lista(range(100000))' vai consumir muitos bytes do computador, servidor... 

# Podemos utilizar os Geradores para evitar esse problema, pois não precisamos de todos os valores da lista ao mesmo tempo
# Cada vez que precisarmos de um valor, ele nos retornará.

'''
# Função normal: 
def gera(): # funcao gera()
    r = [] # r = array
    for n in range(100): 
        r.append(n) # a cada iteração do laço for, tremos um append de 'n' no array 'r'
        time.sleep(0.1) # interpretador python vai dormir por 0.1 segundos (Simulando um processamento pesado)
    return r

g = gera() # atribuindo o resultado da função na variavel 'g'

for v in g:
    print(v)
'''

# Função Geradora:  Ao invés de esperar por todos os valores, ele faz o 'lazy evaluation' ele da um valor por vez
def gerador(): 
    for n2 in range(100): 
        yield n2 # gerador
        time.sleep(0.1)

g2 = gerador() # atribuindo o resultado do gerador na variavel 'g2'

for testeGerador in g2:
    print(testeGerador)

print(hasattr(g2, '__next__')) # Tem o método next, então é um iterador
print(hasattr(g2, '__iter__')) # Tem o método iter, então é um iteravel


#---------------------------------------

# Outro exemplo do uso de gerador:

def gerador2():
    variavel = 'Valor 1'
    yield variavel
    variavel = 'Valor 2'
    yield variavel
    variavel = 'Valor 3'
    yield variavel

g = gerador2()

print(next(g))
print(next(g))
print(next(g))
#print(next(g)) = vai levantar uma exceção StopIteraction - pois acabaram os valores

print('')
for a in gerador2():
    print(a)


#------------------------------------------

# Outra forma de criar um gerador:

listaTeste1 = [x for x in range(10000)]
print('\nlista lista teste 1: ', type(listaTeste1))
print('tamanho (bytes) lista teste 1: ', sys.getsizeof(listaTeste1))

listaTeste2 = (x for x in range(10000))
print('\nlista teste 2: ',type(listaTeste2))
print('tamanho (bytes) lista teste 2: ', sys.getsizeof(listaTeste2), '\n\n')
