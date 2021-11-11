import random
n1 = str(input('Digite o nome da primeira pessoa: '))
n2 = str(input('Digite o nome da primeira pessoa: '))
n3 = str(input('Digite o nome da primeira pessoa: '))
n4 = str(input('Digite o nome da primeira pessoa: '))

#Criando uma lista, e atribuindo n1... para essa lista
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))