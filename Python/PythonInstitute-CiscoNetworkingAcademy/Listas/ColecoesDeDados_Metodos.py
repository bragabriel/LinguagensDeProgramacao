#Em geral, uma invocação de função típica pode parecer-se com isto:

#result = function(arg)

#A função toma um argumento, faz algo, e devolve um resultado.


#--------------------


#Um método típico de invocação é geralmente semelhante a este:

#result = data.method(arg)

#Nota: o nome do método é precedido do nome dos dados que possuem o método. Em seguida, adiciona-se um ponto, seguido do nome do método,
#e um par de parêntesis que encerra os argumentos.


#-------------------------------------

#Utilizando métodos & listas:
print("\nLista DEFAULT: ")
numbers = [111, 7, 2, 1]
print("len: ", len(numbers))
print(numbers, "\n")


#método: append()
#Um novo elemento pode ser colado no fim da lista existente:
#   list.append(value)
numbers.append(4)
print("Método append(4): ", numbers)
print("len: ", len(numbers), "\n")


#método: insert()
#O método insert() é um pouco mais inteligente - pode acrescentar
#um novo elemento em qualquer lugar da lista,
#e não apenas no final.
#   list.insert(location, value)
numbers.insert(0, 222)
print("Método insert(0, 222): ", numbers)
print("len: ", len(numbers), "\n")


#método: reverse()
#O método reverse() pode ser utilizado para inverter a lista
numbers.reverse()
print("Método reverse(): ", numbers)
print("len: ", len(numbers), "\n")
