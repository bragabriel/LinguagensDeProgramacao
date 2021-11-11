import datetime

nascimento = int(input('Ano de nascimento: '))

anoAtual = datetime.date.today().year 

idade = anoAtual - nascimento

print('O atleta tem {} anos.'.format(idade))

if(idade<=9):
    print('categoria: MIRIM')
elif(9 < idade >=14):
    print('categoria: INFANTIL')
elif(14 < idade <=19):
    print('categoria: JUNIOR')
elif(19 < idade >= 25):
    print('categoria: SÊNIOR')
else: 
    print('categoria: MASTER')