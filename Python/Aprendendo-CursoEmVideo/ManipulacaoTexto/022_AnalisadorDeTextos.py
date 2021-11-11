nome = str(input('Digite seu nome completo: ')).strip()

#.strip = elimina espaços antes e depois da frase, mas não no meio

print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
#nome.count(' ') = conta quantos espaços em branco tem
#len(nome) - nome.count(' ') = tira a quantidade de espaços da quantidade de letras
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#nome.find (' ') = encontrando o primeiro espaço para descobrir o primeiro nome
print('Seu primeiro nome tem {} letras'.format(nome.find (' ')))
#jogando o nome em uma lista, e pegando o primeiro nome ( 0 )
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))