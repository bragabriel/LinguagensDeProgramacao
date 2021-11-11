# exemplo 01:
squares = [x ** 2 for x in range(10)]
print("exemplo 01 - squares: ", squares)
# O snippet produz uma lista de dez elementos preenchida com quadrados 
# de dez números inteiros começando do zero (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)


# exemplo 02:
twos = [2 ** i for i in range(8)]
print("exemplo 01 - twos: ", twos)
# O snippet cria um array de oito elementos contendo as primeiras
# oito potências de dois (1, 2, 4, 8, 16, 32, 64, 128)


# exemplo 03:
odds = [x for x in squares if x % 2 != 0 ]
print("exemplo 03 - odds: ", odds)
# O snippet faz uma lista apenas com os elementos
# ímpares da lista squares .