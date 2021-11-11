import random
from random import randint

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

n = int(input('Em que número eu pensei? '))

r = randint(0, 5)

print('PROCESSANDO...')

if (n==r):
    print('PARABÉNS! Você acertou!')
else:
    print('el el el, você perdeu :(')
    print('Eu pensei no número {} e não no {}'.format(r, n))