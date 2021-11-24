# Tutorial disponível no YouTube, pelo canal 'Otávio Miranda'
# Vídeo aula do tutorial: https://www.youtube.com/watch?v=qAaBTrq5mw8&ab_channel=Ot%C3%A1vioMiranda

# Exemplo 01:

lista = [
    ('chave', 5),
    ('chave2', 'valor2'),
]

dicionario1 = {x: y*2 for x, y in lista}   
# dicionario1 = dict(lista)

print('\nexemplo 01: \n', dicionario1)

#--------------------------
#Exemplo 02:

lista2 = [
    ('cachorro', 'dog'),
    ('gato', 'cat'),
]

dicionario2 = {x.upper(): y.upper() for x, y in lista2}   
# Não daria para usar o .upper ou o *2 utilizando a funcao dict()
# dicionario2 = dict(lista)

print('\nexemplo 02: \n', dicionario2)

#--------------------------
#Exemplo 03:

dicionario3 = {x: y for x, y in enumerate(lista2)}   

print('\nexemplo 03: \n Tipo: ', type(dicionario3), '\n', dicionario3)