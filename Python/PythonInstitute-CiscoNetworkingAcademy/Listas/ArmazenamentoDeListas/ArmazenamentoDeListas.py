list_1 = [1]
list_2 = list_1
list_1[0] = 2
print("Sem o uso de slice: ", list_2)

#  O programa acima:
#  cria uma lista de um elemento chamada list_1;
#  atribui-o a uma nova lista chamada list_2;
#  altera o único elemento de list_1;
#  imprime list_2.

# Resultado:
# O programa fará o output: [2], não [1], que parece ser a solução óbvia.


#  Lista x Variável ordinária
#  - o nome de uma variável ordinária é o nome do seu conteúdo;
#  - o nome de uma lista é o nome de um local de memória onde
#  a lista é armazenada.


#  A atribuição: list_2 = list_1 copia o nome do array, não o seu conteúdo.
#  Com efeito, os dois nomes (list_1 e list_2) identificam 
#  o mesmo local na memória do computador. 
#  Modificar um deles afeta o outro, e vice-versa.


#---------------------------------
#SOLUÇÃO: slice

#  Uma slice é um elemento da sintaxe Python que lhe permite fazer uma cópia completamente
#  nova de uma lista ou partes de uma lista.

list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print("\nUsando slice: ", list_2)

#  Esta parte inconspícua do código descrito como [:] é capaz de produzir
#  uma lista completamente nova.


#  Uma das formas mais gerais da slice tem o seguinte aspeto:
#  my_list[start:end]

#  Uma slice desta forma faz uma nova lista (alvo),
#  retirando elementos da source list - os elementos dos
#  índices desde o início até end - 1.

#  É possível utilizar valores negativos tanto para o início
#  como para o fim (tal como na indexação).

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print("\nSlice lista(alvo): ", new_list)

#  A new_list lista terá end - start (3 - 1 = 2) elementos - aqueles com
#  índices iguais a 1 e 2 (mas não 3).

#  O output do snippet é: [8, 6]
