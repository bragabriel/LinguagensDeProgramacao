from datetime import date

ano = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = ano - nascimento

print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, ano))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')

elif idade < 18:
    saldo = 18 - idade
    print('Ainda falta(m) {} anos para o alistamento'.format(saldo))
    anoAlistamento = ano + saldo
    print('Seu alistamento será em {}'.format(anoAlistamento))

elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} ano(s).'.format(saldo))
    anoAlistamento = ano - saldo
    print('Seu alistamento foi em {}'.format(anoAlistamento))