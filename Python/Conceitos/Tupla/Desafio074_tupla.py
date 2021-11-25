# Desafio proposto pelo canal 'Curso em Vídeo | Gustavo Guanabara'
# link: https://www.youtube.com/watch?v=mlwt2CRQkTQ&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=75&ab_channel=CursoemV%C3%ADdeo

from random import randint, random

tupla = (randint(1, 50), randint(1, 50), randint(1, 50), randint(1,50), randint(1, 50))

print('Foram sorteados os números: ', end = '')

for i in tupla:
    print(f'{i}', end=' ')

print('\nO maior valor é: ', max(tupla))

print('O menor valor é: ', min(tupla))
    

