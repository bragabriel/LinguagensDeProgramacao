#--------------------------------------
frase = 'Gabriel Braga da Silva'

print(frase)

#contar quantos 'a' tem na frase
print(frase.count('a'))
print(frase.count('A'))

#jogar frase para maiúsculo, e contar a quantidade de A
print(frase.count('a'))

#----------------------------------
qtd = '            a sd           '

#contar a qtd de caracteres na frase
print(len(qtd))

#Remove os espaços indesejados (antes e depois do começo e fim da frase)
print(len(qtd.strip()))

#---------------------------------
troca = 'Gabriel Python'

#Trocando palavra da Frase, nesta instancia
print(troca.replace('Python', 'Braga da Silva\n'))
print(troca, '\n')

#Trocando palavra da Frase, e armazenando a nova frase no local da antiga
troca = troca.replace('Python', 'gosta de lasanhaaaaaa!!!')
print(troca)

#Verificando se a palavra gosta está na frase 'troca'
print('gosta' in troca)

#Procurando 'gosta' na frase 'troca'
print(troca.find('gosta'))

#----------------------------------------
lista = 'Gabriel Braga da Silva'

#Criou uma lista, separando por espaço
print(lista.split())

dividido = lista.split()

#Exibindo primeiro item da lista 'dividido' que armazena a frase
print(dividido[0])

#Pegue a palavra[2] e mostre a letra [3] dentro de dividido
print(dividido[0][3])
