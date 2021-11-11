my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")


#Explicação
#o valor alvo é armazenado na variável to_find ;
#o estado atual da pesquisa é armazenado na variável found (True/False)
#quando found se torna True, o loop for é encerrado
