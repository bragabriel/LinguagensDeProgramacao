'''Entrar com 3 números e imprimi-los em ordem decrescente (suponha números
diferentes).'''

numeros = input().split()

num1 = int(numeros[0])
num2 = int(numeros[1])
num3 = int(numeros[2])

if (num1 < num2) and (num1 < num3):
    if(num2<num3):
        print(num3, num2, num1)
    else:
        print(num2, num3, num1)
     
if(num2 < num1) and (num2 < num3):
    if(num1<num3):
        print(num3, num1, num2)
    else:
        print(num1, num3, num2)
        
if(num3 < num1) and (num3 < num2):
    if(num1<num2):
        print(num2, num1, num3)
    else:
        print(num1, num2, num3)