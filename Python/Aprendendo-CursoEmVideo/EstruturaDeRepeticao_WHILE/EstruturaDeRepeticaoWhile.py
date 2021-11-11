'''
for c in range (1,10):
    print(c)
print('Fim')

nomes = ['Pedro', 'João', 'Leticia']
for n in nomes:
     print(n)
'''


c = 1
while c<10:
    print(c)
    c += 1
print('Fim')


#--------------------------

'''
for c in range('1, 5'):
    n = int(input('Digite um valor: '))
print('Fim')

# ---------------

n=1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')
'''

resposta = 'SIM'
while resposta == 'SIM':
    n = int(input('Digite um valor: '))
    resposta = str(input('Quer continuar?')).upper()
print('Fim')