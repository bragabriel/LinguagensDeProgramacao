sal = float(input('Qual é o salário do funcionário? R$'))

if sal>1250:
    salario = sal + sal * (10/100)
else:
    salario = sal + sal * (15/100)

print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora.'.format(sal, salario))