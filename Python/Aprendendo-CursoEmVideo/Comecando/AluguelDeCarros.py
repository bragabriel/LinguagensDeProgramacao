print('Aluguel de carros\n')
dias = int(input('Por quantos dias o carro foi alugado? '))
kmRodados = int(input('Quantos Km foram rodados? '))
vlrPagar = (dias*60) + (0.15*kmRodados)
print('O valor a pagar é de R${:.2f}'.format(vlrPagar))

