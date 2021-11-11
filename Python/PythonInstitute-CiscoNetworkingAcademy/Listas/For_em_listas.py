#  O loop for tem uma variante muito especial
#  que pode processar listas muito eficazmente

#  Vamos supor que deseja calcular a soma de todos
#  os valores armazenados na lista my_list

#  É necessária uma variável cuja soma será armazenada e
#  à qual será inicialmente atribuído um valor
#  de 0 - o seu nome será total

#FORMA "PADRÃO":
print("LISTA - FORMA \"NORMAL\"")
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

#EXPLICAÇÃO:
#  - à lista é atribuída uma sequência de cinco valores inteiros;
#  - a variável i toma os valores 0, 1, 2, 3, e 4, e depois indexa a lista,
#    selecionando os elementos seguintes: o primeiro, o segundo, o terceiro,
#    o quarto e o quinto;
#  - cada um destes elementos é adicionado em conjunto pelo operador += à variável
#    total , dando o resultado final no fim do loop;



#FORMA "OCULTA":
print("LISTA - FORMA \"OCULTA\"")
my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)

#EXPLICAÇÃO:
#  - a instrução FOR especifica a variável usada para navegar 
#    na lista ("i"neste caso) seguida pela keyword in e pelo nome
#    da lista que está a ser processada (my_list aqui)
#  - à variável i são atribuídos os valores de todos os elementos
#    da lista subsequente, e o processo ocorre tantas vezes quantos
#    os elementos da lista;
#  - isto significa que se utiliza a variável i como uma cópia dos
#    valores dos elementos, e não se precisa de utilizar índices;