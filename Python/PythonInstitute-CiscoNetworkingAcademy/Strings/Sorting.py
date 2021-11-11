# Sorting

# Ordenando listas contendo strings

# Ex 01:
# sorted()

# A função toma um argumento (uma lista) e devolve uma nova lista, preenchida com os elementos do argumento ordenados.
#  (Nota: esta descrição é um pouco simplificada em comparação com a implementação real - discuti-la-emos mais tarde).
# A lista original permanece intacta.

# Demonstrating the sorted() function:
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)

print()


# Ex 02:
# sort()

# O segundo método afeta a própria lista - nenhuma nova lista é criada. A ordenação é
#  realizada in situ pelo método chamado sort().

# Demonstrating the sort() method:
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)