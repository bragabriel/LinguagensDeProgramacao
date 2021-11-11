n = i = soma =0

while True:

    n = int(input("Digite um número [999] para parar: "))
    
    if(n==999):
        break

    soma = soma + n
    i += 1

print('Você digitou {} números e a soma entre eles foi {}'.format(i, soma))