# Strings em python são imutáveis 

alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)



# Operações em String:



#--------------
# min()

# A função encontra o elemento mínimo da sequência passada como um argumento.
#  Há uma condição - a sequência (string, lista, não importa)
#  não pode estar vazia, ou então terá uma exceção ValueError .

# Demonstrating min() - Example 1:
print('\nmin: ')
print(min("aAbByYzZ")) # segundo a tabela ASCII

# Demonstrating min() - Examples 2 &amp; 3:
print('\nmin ex02: ')
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')

print('\nmin ex03: ')
t = [0, 1, 2]
print(min(t))



#--------------
# max()

# Da mesma forma, uma função chamada max() encontra o elemento máximo da sequência.

# Demonstrating max() - Example 1:
print('\nmax: ')
print(max("aAbByYzZ"))

# Demonstrating max() - Examples 2 &amp; 3:
print('\nmax 02: ')
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')

print('\nmax03: ')
t = [0, 1, 2]
print(max(t))



#--------------
# index()

# A classe index() (é um método, não uma função) pesquisa a sequência desde o início,
#  a fim de encontrar o primeiro elemento do valor especificado no seu argumento.
# O método devolve o index da primeira ocorrência do argumento

# Demonstrating the index() method:
print('\nindex: ')
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))



#---------------
# list()  &  count()

# A função list() toma o seu argumento (uma string) e cria uma nova lista contend0o
#  todos os carateres da string, um por elemento de lista.

# Demonstrating the list() function:
print('\nlist: ')
print(list("abcabc"))

# A classe count() conta todas as ocorrências do elemento dentro da sequência.
#  A ausência de tais elementos não causa problemas.

# Demonstrating the count() method:
print('\ncount: ')
print("abcabc".count("b"))
print('abcabc'.count("d"))



#----------------
# capitalize()

# O método capitalize() faz exatamente o que diz - cria uma nova string cheia de carateres retirados da source string,
#  mas tenta modificá-los da seguinte forma:

# - se o primeiro caratere dentro da string for uma letra (nota: o primeiro caratere
#  é um elemento com um index igual a 0, não apenas o primeiro caratere visível), será convertido para maiúsculas;

# - todas as letras restantes da string serão convertidas em minúsculas.

# Demonstrating the capitalize() method:
print('\ncapitalize: ')
print('aBcD'.capitalize())
print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())


