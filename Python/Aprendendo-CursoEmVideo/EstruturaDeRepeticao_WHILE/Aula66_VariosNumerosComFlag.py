v = 0
soma = 0
i = 0

while True:
    v = int(input('Digite um valor (999 para parar):'))
    if(v==999):
        break
    soma += v
    i += 1
    
print('A soma dos {} valores foi: {}'.format(i, (soma)))