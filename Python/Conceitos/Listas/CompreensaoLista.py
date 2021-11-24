lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('lista 1: ', lista1)

exemplo1 = [variavel for variavel in lista1] # Iterando cada item da lista1
print('exemplo 1: ', exemplo1)

exemplo2 = [v * 2 for v in lista1]
print('exemplo 2: ', exemplo2)

exemplo3 = [(v, v2) for v in lista1 for v2 in range(3)]
# v está no primeiro for e vai iterar sob a lista1
# para cada valor da lista, utilizamos o segundo for jogando o valor no v2 em range de 3
print('exemplo 3: ', exemplo3)