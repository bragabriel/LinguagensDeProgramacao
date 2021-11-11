vlrCasa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salário do comprador? '))
anos = int(input('Em quantos anos ele vai pagar? '))

prestacao = vlrCasa / (anos*12)

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(vlrCasa, anos, prestacao))

if (prestacao > (30/100 * salario)):
    print('Emprestimo negado')
else:
    print('Emprestimo aprovado!')