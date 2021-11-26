# Tutorial disponível no YouTube, pelo canal 'Curso em Vídeo - Gustavo Guanabara'
# Vídeo aula do tutorial: https://www.youtube.com/watch?v=N1hTsbW50eM&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=8&ab_channel=CursoemV%C3%ADdeo

#Exemplo 01
print('\nExemplo 01: ')
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
print(num)

num.insert(2, 2)

if 4 in num:
    num.remove(4)
else:
    print('O número 4 não foi encontrado')

print(num)
print(f'Essa lista tem {len(num)} elementos')


#Exemplo 02
print('\nExemplo 02: ')
lista2 = []
lista2.append(5)
lista2.append(15)
lista2.append(8)
lista2.append(4)

for c, v in enumerate(lista2):
    print(f'\nNa posição {c} encontrei o valor {v}...', end='')
print('Cheguei ao final da lista')


# Exemplo 03
print('\nExemplo 03: ')
lista3 = []

for cont in range(0, 5):
    lista3.append(int(input('Digite um valor: ')))

for c, v in enumerate(lista3):
    print(f'\nNa posição {c} encontrei o valor {v}...', end='')
print('Cheguei ao final da lista')


# Cópia de String:
print('\nExemplo 04: ')
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8

print('A: ', a)
print('B: ', b)