'''Criar um algoritmo que imprima a tabuada de um número.'''

num = int(input("Insira um número inteiro: "))

for i in range(1, 11):  # Começando em 1, até 11
    print(f'{num} x {i} = {num*i}')
