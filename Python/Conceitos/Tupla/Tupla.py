# Tutorial disponível no YouTube, pelo canal 'Curso em Vídeo - Gustavo Guanabara'
# Vídeo aula do tutorial: https://www.youtube.com/watch?v=0LB3FSfjvao&ab_channel=CursoemV%C3%ADdeo


#                   Tuplas

# Tuplas são IMUTÁVEIS (depois de criada, não podemos adicionar nem criar elementos nela)
# Tuplas podem conter dados de diferentes tipos

# Variaveis e seus respectivos inicios: (tupla), [lista], {dicionário}


lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

# printando 'lanche'

for cont in range(0,len(lanche)):
    print(lanche[cont])


# for comida in lanche:
#     print(f'Eu vou comer {comida}')
# print('Eu vou ficar gordo')


print('\n tupla ordenada: ', sorted(lanche))

tuplaNumeros = (2, 5, 5, 7, 8, 1, 9, 0)

print('\n o número 5 apareceu', tuplaNumeros.count(5), 'vezes na tupla')
print('\n o número 7 aparece na pos:',tuplaNumeros.index(7))