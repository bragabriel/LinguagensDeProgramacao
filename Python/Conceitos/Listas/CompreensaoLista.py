lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('\nlista 1: ', lista1)

exemplo1 = [variavel for variavel in lista1] # Iterando cada item da lista1
print('exemplo 1: ', exemplo1)

exemplo2 = [v * 2 for v in lista1]
print('exemplo 2: ', exemplo2)

exemplo3 = [(v, v2) for v in lista1 for v2 in range(3)]
# v está no primeiro for e vai iterar sob a lista1
# para cada valor da lista, utilizamos o segundo for jogando o valor no v2 em range de 3
print('exemplo 3: ', exemplo3)

#------------------------

lista2 = ['Luiz', 'Gabriel', 'Douglas', 'Joana', 'Luiza']
print('\nlista 2: ', lista2)

exemplo4 = [v.replace('a', '@').upper() for v in lista2] # para cada valor da lista 2, vamos substituir o 'a' por '@', e deixar tudo maiusculo
print('exemplo 4: ', exemplo4)

#------------------------

tupla1 = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)
print('\ntupla 1: ', tupla1)

exemplo5 = [(y, x) for x, y in tupla1]
print('exemplo 5: ', exemplo5)

exemplo5 = dict(exemplo5)
print(exemplo5['valor2'])

#----------------------------

lista3 = list(range(100)) # criando uma lista com 100 valores (0-99)
print('\nlista 3: ', lista3)

# Filtrando todos os números que são divisiveis por 2
exemplo6 = [v for v in lista3 if v % 2 == 0]
print('\nexemplo 6: ', exemplo6)

# Filtrando todos os números que são divisiveis por 3 e divisiveis por 8
exemplo7 = [v for v in lista3 if v % 3 == 0 if v % 8 == 0]
print(exemplo7)
print('\nexemplo 7: ', exemplo7)

# Se valor não for divisivel por 3 vai printar a msg 'Não'
exemplo8 = [v if v % 3 == 0 else 'Não' for v in lista3]
print('\nexemplo 8: ', exemplo8)