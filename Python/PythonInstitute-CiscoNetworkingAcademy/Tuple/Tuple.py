# Mutabilidade e Imutabilidade:
# Os dados mutáveis podem ser atualizados livremente a qualquer momento; ex: list.append(1) -> estamos inserindo 1 no final da lista
# Se a lista fosse imutável, teriamos que criar outra lista com o 1 no final, e não apenas adicionar o valor com a lista já criada.



# TUPLE: 
# Um tuple é um tipo de sequência imutável.

# A primeira e mais clara distinção entre listas e tuples é a sintaxe 
# utilizada para as criar - os tuples preferem usar parêntesis curvos, 
# enquanto as listas gostam de ver parêntesis retos, embora também seja 
# possível criar um tuple a partir de um conjunto de valores separados por vírgulas.

tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

print(tuple_1)
print(tuple_2)


#  Nota: cada elemento tuple pode ser de um tipo diferente (floating-point, inteiro, ou qualquer outro tipo de dados ainda não introduzidos).


# É possível criar um tuple vazio - são necessários então parêntesis:
empty_tuple = ()


# Exemplo:
my_tuple = (1, 10, 100, 1000)

print("\nmy_tuple[0]: ", my_tuple[0], "\n")
print("my_tuple[-1]: ", my_tuple[-1], "\n")
print("my_tuple[1:]: ", my_tuple[1:], "\n")
print("my_tuple[:-2]: ", my_tuple[:-2], "\n")

print("conteúdo em seq do tuple: ")
for elem in my_tuple:
    print(elem)


# OBS!!:
# não tente modificar o conteúdo de um tuple! Não é uma lista!

#Todas estas instruções (exceto a mais acima) causarão um erro de runtime:

# my_tuple = (1, 10, 100, 1000)

# my_tuple.append(10000)
# del my_tuple[0]
# my_tuple[1] = -10