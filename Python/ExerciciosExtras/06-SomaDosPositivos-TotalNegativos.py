'''Entrar com 20 números e imprimir a soma dos positivos e o total de números
negativos.'''

from random import randint

lista = []
i = 0
totNeg = 0
soma = 0

for i in range(0, 20):
    lista.append(randint(-20, 20))

for i in lista:
    if(lista[i] < 0):
        totNeg += 1
    elif(lista[i] > 0):
        soma = soma + lista[i]

print(lista)
print("A soma dos números positivos é: ", soma)
print("A quantidade de números negativos é de: ", totNeg)
