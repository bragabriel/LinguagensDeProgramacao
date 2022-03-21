'''Chico tem 1,50 m e cresce 2 centímetros por ano, enquanto Juca tem 1,10m e
cresce 3 centímetros por ano. Construir um algoritmo que calcule e imprima
quantos anos serão necessários para que Juca seja maior que Chico.'''

C = 1.50
J = 1.10
ano = 0

while(J < C):
    ano += 1
    J += 0.03
    C += 0.02

print("Anos:", ano)
