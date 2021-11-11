print('=-='*10)
# ^40 = centralizado em 40 espaços
print('{:^30}'.format('LOJA'))
print('=-='*10)

valor = float(input('Insira o valor do produto: '))

print('Escolha a opção de pagamento abaixo: ')
print('''
[ 1 ] à vista dinheiro/cheque (10 pcento de desconto)
[ 2 ] à vista no cartão (5 pcento de desconto)
[ 3 ] em até 2x no cartão (preço normal)
[ 4 ] 3x ou mais no cartão (20 pcento de juros)\n''')

op = int(input('Qual é a opção de compra?'))

if (op == 1):
    total =  valor - (valor* 10 / 100)

elif (op == 2):
    total =  valor - (valor* 5 / 100)
    
elif (op == 3):
    parcela = valor / 2
    print('O valor das parcelas ficou em: R${:.2f}'.format(parcela))

elif (op == 4):
    total =  valor - (valor* 20 / 100)
    parcela = total / 2
    print('O valor das parcelas ficou em: R${:.2f}'.format(parcela))

else:
    print('Opção inválida!')

print('Sua compra de R${:.2f} vai custar R${:.2f} com essa opção de compra'.format(valor, total))