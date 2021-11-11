n1 = (int(input('Primeiro termo: ')))
razao = (int(input('Razão: ')))
i = 0

decimoTermo = n1 + (10 - 1) * razao

for i in range(n1, decimoTermo + razao, razao):
    print('{} '.format(i), end=' -> ')
print('fim')