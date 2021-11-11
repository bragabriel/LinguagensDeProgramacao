i = 0
cont = 0
par = 0

for i in range(1, 7):
    numero = int(input('Digite o {} valor: '.format(i)))

    if(numero%2==0):
        cont += 1
        par += numero
    
print('Você informou {} números, sendo {} números pares. A a soma dos números pares foi {}'.format(i, cont, par))