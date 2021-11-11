#APPEND:
#list.append(value)
#Insere no fim da lista

my_list = []  # Creating an empty list.

i=0

for i in range(5):
    print(i)
    my_list.append(i + 1)

print(my_list)



#INSERT:
#list.insert(location, value)
#Pode acrescentar um novo elemento em qualquer lugar da lista

my_list = []  # Creating an empty list.

i=0

for i in range(5):
    print(i)
    my_list.insert(0, i + 1)
    #Neste caso, está sendo inserido sempre na posição 0,
    #gerando uma lista na ordem inversa da primeira

print(my_list)