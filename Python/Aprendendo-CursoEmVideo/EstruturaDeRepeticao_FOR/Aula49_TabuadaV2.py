n = int(input('Digite um número para ver sua tabuada: '))

for i in range(1, 11, 1):
    result = n * i
    print('{} x {} = {}'.format(n, i, result))