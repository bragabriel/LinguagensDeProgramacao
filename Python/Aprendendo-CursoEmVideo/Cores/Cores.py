print('\033[4;1;43mHello World!\033[m')

nome = str(input('Digite seu nome: '))

print('Prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

cores = {'limpa':'\033[m',
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'pretoEbranco':'\033[4;1;40m'}

print('Testando {} as cores {}na variavel {}cores :) {}:D :P'.format(cores['azul'], cores['amarelo'], cores['pretoEbranco'], cores['limpa']))