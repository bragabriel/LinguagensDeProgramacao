# A diferença entre uma lista e um gerador está nos parenteses.


the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
#          ^                                         ^

the_generator = (1 if x % 2 == 0 else 0 for x in range(10))
#               ^                                         ^ 


for v in the_list:
    print(v, end=" ")
print()

for v in the_generator:
    print(v, end=" ")
print()


# Podemos verificar se é uma lista ou não da seguinte forma:

# Aplicar a função len() para ambas as entidades.

# len(the_list) avaliará a 10. Claro e previsível. 
# len(the_generator) irá levantar uma exceção, e verá a seguinte mensagem: TypeError: object of type 'generator' has no len()