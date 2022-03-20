n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

print('A soma vale {}'.format(n1+n2))
print('A multiplicação vale {}'.format(n1*n2))
print('A divisão vale {}'.format(n1/n2))
print('A divisão Inteira vale {}'.format(n1//n2))
print('A potência vale {}'.format(n1**n2))

soma = n1+n2
sub = n1-n2
mult = n1*n2
expo = n1**n2
div = n1/n2
divI = n1//n2

print('\n')
print('Esse é um print geral com tudo\nTem a soma: {}\n Tem a subtração: {}\n Tem a multiplicação: {}'.format(soma, sub, mult))
print('Tem a divisão{}\nTem a divisão inteira{}\nTem a potência{}\n'.format(div, divI, expo))