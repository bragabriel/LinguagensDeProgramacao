print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)

p1 = float(input('Primeiro segmento: '))
p2 = float(input('Segundo segmento: '))
p3 = float(input('Terceiro segmento: '))

if (p1 < p2 + p3 and p2 < p1 + p3 and p3 < p1 + p2):
    print('Os seguimentos acima PODEM formar um triângulo!')
    print('Triângulo do tipo: ', end='')

    if(p1 == p2 and p2 == p3):
        print('Equilátero')

    elif(p1 == p2 or p1 == p3 or p2 == p3):
        print('Isósceles')

    #elif(p1 != p2 and p2 != p3 and p1 != p3):   OU
    elif(p1 != p2 != p3):
        print('Escaleno')
    
else:
    print('Os seguimentos acima NÃO podem formar um triângulo!')