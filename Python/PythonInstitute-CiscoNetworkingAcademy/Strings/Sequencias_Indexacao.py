# As strings de Python são sequências.

# As strings não são listas,
#  mas pode tratá-las como listas em muitos
#  casos particulares.


# Por exemplo, se quiser aceder a qualquer um dos carateres
#  de uma string, pode fazê-lo utilizando a indexação:

# Indexing strings.
print('\nString indexada: ')
the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()



# Strings como sequências: iteração

# Iterar através das strings também funciona.
# EX:
# Iterating through a string.
print('\nIteração: ')
the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

print()


# Slices:
# EX:

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])
