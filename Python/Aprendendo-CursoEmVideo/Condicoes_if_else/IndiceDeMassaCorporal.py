peso = float(input('Qual é seu peso? (kg)'))
alt = float(input('Qual é sua altura? (m)'))

imc = peso / (alt ** 2)

print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if (imc<18.5):
    print('Você está ABAIXO do peso')
elif(18.5 <= imc < 25):
    print('PARABÉNS, você está na faixa de peso NORMAL')
elif(25 <= imc < 30):
    print('Você está em SOBREPESO')
elif(30 <= imc < 40):
    print('Você está em OBESIDADE, cuidado!')
elif(imc >= 40):
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
