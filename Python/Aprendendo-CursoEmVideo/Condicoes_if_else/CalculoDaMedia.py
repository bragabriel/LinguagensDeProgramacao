n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1+n2) / 2

print('A média do aluno é {:.1f}'.format(media))

if media>7.0:
    print('aluno está Aprovado!')
elif 7 > media >= 5:
    print('aluno está de Recuperação')
else:
    print('aluno está Reprovado!')