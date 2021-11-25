# Tutorial disponível no YouTube, pelo canal 'Curso em Vídeo - Gustavo Guanabara'
# Vídeo aula do tutorial: https://www.youtube.com/watch?v=1u7oA8ckjAc&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=77&ab_channel=CursoemV%C3%ADdeo

n = (int(input('Digite um número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite outro um número: ')),
     int(input('Digite o último número: '))
    )

print('Você digitou os números: ', n)
print('O valor 9 apareceu {} vez(es)'.format(n.count(9)))

if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3)}ª posição')
else:
    print('O número 3 não foi inserido na tupla')

print('Os valores pares digitados foram: ', end='')
for i in n:
    if i % 2 == 0:
        print(i, end=' ')