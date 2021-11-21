# toma dois argumentos:
# uma função;
# uma lista.


# map(function, list)

# o segundo argumento map() pode ser qualquer entidade que possa ser iterada (por exemplo, um tuple, ou apenas um gerador)

# map() pode aceitar mais de dois argumentos.


# O que o map() faz:
# A função map() aplica a função passada pelo seu primeiro argumento a todos os elementos do seu segundo argumento,
#  e devolve um iterador entregando todos os resultados subsequentes da função.

list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()
