somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeMaisVelho = ''
totMulher20 = 0

for i in range(1, 5):
    print('---- {}ª Pessoa ----'.format(i))
    nome = str(input('Nome ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    somaIdade += idade

    if(i==1 and sexo in 'Mm'):
        #usando in'Mm' para pegar maiusculo ou minusculo, 
        #poderia tbm ser usado .upper na hora de receber a informação

        maiorIdadeHomem = idade
        nomeMaisVelho = nome

    if(sexo in 'Mm' and idade>maiorIdadeHomem):
        maiorIdadeHomem = idade
        nomeMaisVelho = nome
    
    if(sexo in 'Ff' and idade < 20):
        totMulher20 += 1

mediaIdade = somaIdade / 4

print("A média de idade do grupo é de {} anos".format(mediaIdade))
print("O homem mais velhor tem {} anos e se chama {}".format(maiorIdadeHomem, nomeMaisVelho))
print("Ao todo existe(m) {} mulher(es) com menos de 20 anos".format(totMulher20))
