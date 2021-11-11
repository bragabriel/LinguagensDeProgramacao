n = float(input('Qual é a velocidade atual do carro? '))

if(n>80):
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (n-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
else:
    print('Bom dia! Dirija com segurança!')