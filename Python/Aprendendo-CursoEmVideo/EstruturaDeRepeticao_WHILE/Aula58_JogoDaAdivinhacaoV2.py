import random

print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')


aleatorio = random.randint(0, 10)

n = 0
tentativas = 0

while (n != aleatorio):

    n = int(input('Qual é seu palpite? '))
    
    tentativas += 1

    if(n>aleatorio):
        print('Menos... Tente novamente.')
    elif(n<aleatorio):
        print('Mais... Tente novamente.')
    elif(n==aleatorio):
        print('Parabéns! Você acertou!')
        break


print('Você acertou com {} tentativas!'.format(tentativas))