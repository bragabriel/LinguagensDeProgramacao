list_1 = [1]
list_2 = list_1
list_1[0] = 2
print("Sem o uso de slice: ", list_2)

#  Uma slice é um elemento da sintaxe Python que lhe permite fazer uma cópia completamente
#  nova de uma lista ou partes de uma lista.

list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print("\nUsando slice: ", list_2)



# SLICE START e END

#  my_list[start:end]

#  start é o index do primeiro elemento incluído no slice;
#  end é o index do primeiro elemento não incluído no slice.

#  Uma slice desta forma faz uma nova lista (alvo),
#  retirando elementos da source list - os elementos dos
#  índices desde o início até end - 1.

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print("\nExemplo 01: Slice lista(alvo): ", new_list)
# Output: [8, 6]


#  É assim que os índices negativos funcionam com o slice:

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print("\nExemplo 02: Slice lista(alvo) com índices negativos: ", new_list)
#O output do snippet é: [8, 6, 4]


#  Se o start especifica um elemento que se encontra mais longe do
#  que o descrito pelo end (do ponto de vista inicial da lista), o slice estará vazio:
my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print("\nExemplo 03: Slice lista(alvo) vazio: ", new_list)
#  O output do snippet é: []



# OMITINDO O START
# Se omitir o start no seu slice, assume-se que pretende 
# obter um slice começando pelo elemento com index 0.
# my_list[:end]
# é um equivalente mais compacto de:
# my_list[0:end]

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print("\nExemplo 04: Omitindo o START: ", new_list)
# O output é: [10, 8, 6].



# OMITINDO O END
# Da mesma forma, se omitir o end no seu slice, presume-se 
# que deseja que o slice termine no elemento com o index len(my_list).
# my_list[start:]
#é um equivalente mais compacto de:
#my_list[start:len(my_list)]

my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print("\nExemplo 05: Omitindo o END: ",new_list)
# O output é: [4, 2].



#DELETANDO ELEMENTOS DA LISTA COM SLICE
#  A instrução anteriormente descrita del é capaz de apagar mais
#  do que apenas um elemento de uma lista ao mesmo tempo,
#  também pode apagar slices:

my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print("\nExemplo 06: Deletando parte da lista com slice: ",my_list)
#O output do snippet é: [10, 4, 2].

#Nota: neste caso, o slice não produz nenhuma lista nova!



#DELETANDO O SLICE INTEIRO
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print("\nExemplo 07: Deletando o slice inteiro: ", my_list)
#A lista fica vazia e o output é: [].

# -> OBS: A instrução del eliminará a lista em si, não o seu conteúdo.
# A print() invocação da função a partir da última linha do código
# causará então um erro de runtime.