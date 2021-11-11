# Funções: Choice & Sample

# choice(sequence)
# sample(sequence, elements_to_choose),


# A primeira variante escolhe um elemento "aleatório" a partir da sequência de input e devolve-o.

# O segundo constrói uma lista (uma amostra; em inglês, uma sample) que consiste no elemento
#  elements_to_choose “sorteado” a partir da sequência de input. 


# EX:
from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))