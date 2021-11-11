n = int(input('Digite um número: '))

print('O dobro de {} vale {}'.format(n, n*2))
print('O triplo de {} vale {}'.format(n, n*3))

#Raiz quadrada matematicamente é o número elevado à 1/2

print('A raiz quadrada de {} é igual a {:.2f}'.format(n, n ** (1/2)))

#Formas de calcular a raiz quadrada: 

#  n ** (1/2)
#  pow(n, (1/2))