'''Construir um algoritmo que leia 2 números e efetue a adição. Caso o valor somado
seja maior que 20, este deverá ser apresentando somando-se a ele mais 8; caso o
valor somado seja menor ou igual a 20, este deverá ser apresentado subtraindo-se 5.'''

num1 = int(input())
num2 = int(input())

soma = num1 + num2

if(soma>20):
    print(soma+8)

else:
    print(soma-5)
