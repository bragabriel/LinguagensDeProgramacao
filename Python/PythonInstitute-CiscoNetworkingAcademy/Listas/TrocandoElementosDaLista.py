#Trocando facilmente os elementos da lista para inverter a sua ordem:
my_list = [10, 1, 8, 3, 5]
print("Default list: ", my_list)

my_list[0], my_list[4] = my_list[4], my_list[0]
print("Troca 1: ", my_list)

my_list[1], my_list[3] = my_list[3], my_list[1]
print("Troca 2: ", my_list)



#  Será ainda aceitável com uma lista contendo 100 elementos? 
#  Não, não será.

#  Pode utilizar o loop for para fazer a mesma coisa automaticamente,
#  independentemente do comprimento da lista? Sim, pode.
print("\nForma automática de troca: ")
my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range(length // 2): #em uma lista de 5elementos, teremos 2 trocas (5/2=(int)2.5)
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)