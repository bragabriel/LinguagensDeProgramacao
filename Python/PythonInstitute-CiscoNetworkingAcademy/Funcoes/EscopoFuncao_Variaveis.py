#Entendendo o ESCOPO das váriaveis dentro das funções

def hello(meu_nome,idade):
   print('Olá',meu_nome,'\nSua idade é:',idade)
   
hello('Teste', 20)


#  Uma variável existente fora de uma função tem um scope dentro dos corpos das funções.

def my_function():
    print("Do I know that variable?", var)

var = 1
my_function()


#  Uma variável existente fora de uma função tem um scope dentro dos corpos das funções, 
#  excluindo aqueles que definem uma variável com o mesmo nome.

def my_function2():
    var = 2
    print("Do I know that variable?", var)

var = 1
my_function2()


#  OBS: existem também variaveis globais em python, através da sintaxe:
#  global <var>


# Exemplificando novamente a questão do escopo:

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)