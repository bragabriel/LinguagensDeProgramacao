print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
p1 = float(input('Primeiro segmento: '))
p2 = float(input('Segundo segmento: '))
p3 = float(input('Terceiro segmento: '))

if (p1 < p2 + p3 and p2 < p1 + p3 and p3 < p1 + p2):
    print('Os seguimentos acima PODEM formar um triângulo!')
else:
    print('Os seguimentos acima NÃO podem formar um triângulo!')