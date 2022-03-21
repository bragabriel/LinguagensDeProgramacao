'''Ler um número inteiro entre 1 e 12 e escrever o mês correspondente.
Caso o número seja fora desse intervalo,
informar que não existe mês com este número.'''

validos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 0

while i not in validos:
    i = int(input("Insira um inteiro entre 1 e 12: "))

if i == 1:
    print("Janeiro")
elif i == 2:
    print("Fevereiro")
elif i == 3:
    print("Março")
elif i == 4:
    print("Abril")
elif i == 5:
    print("Maio")
elif i == 6:
    print("Junho")
elif i == 7:
    print("Julho")
elif i == 8:
    print("Agosto")
elif i == 9:
    print("Setembro")
elif i == 10:
    print("Outubro")
elif i == 1:
    print("Novembro")
elif i == 12:
    print("Dezembro")
