# a função len() aceita tuples, e devolve o número de elementos contidos no seu interior;
# o operador + pode juntar tuples (já lhe mostrámos isto)
# o operador * pode multiplicar tuples, assim como listas;
# os operadores in e not in trabalham da mesma maneira que nas listas

print("\nExemplo 01: \n")
my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)


# EX02: 
# os elementos de um tuple podem ser variáveis, 
# e não apenas literais. Além disso, 
# podem ser expressões se estiverem no lado 
# direito do operador de atribuição.
print("\nExemplo 02: \n")

var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)



