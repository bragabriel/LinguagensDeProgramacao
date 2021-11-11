#-------------------
# center()

# A variante de um parâmetro do método center() faz uma cópia da
#  string original, tentando centralizá-la dentro de um campo de uma largura especificada.

# O exemplo no editor usa parêntesis retos para mostrar claramente onde começa e termina a string centrada.

# Demonstrating the center() method:
print('\ncenter: ')
print('[' + 'alpha'.center(10) + ']')
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')


#--------------------
# endswith()

# A classe endswith() verifica se a string dada termina com o argumento especificado e devolve True ou False,
#  dependendo do resultado da verificação.

# Demonstrating the endswith() method:
print('\nendswith: ')
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")

#ex 2
print('\nendswith ex2: ')
t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))


#---------------------
# find()

# A classe find() é semelhante a index(), que já conhece - procura uma substring e devolve o index 
# de primeira ocorrência desta substring, mas:

# - é mais seguro - não gera um erro para um argumento que contém uma 
# substring inexistente (devolve -1 então)

# - funciona apenas com strings - não tente aplicá-lo a qualquer outra sequência.

# OBS: Nota: não use find() se quiser apenas verificar se um único caratere ocorre dentro de 
# uma string - o operador in será significativamente mais rápido.

# Demonstrating the find() method:
print('\nfind: ')
print("Eta".find("ta"))
print("Eta".find("mma"))


#---------------
# find()
# Se quiser realizar a procura, não desde o início da string, mas a partir de qualquer 
# posição, pode usar uma variante de dois parâmetros do find() método. Veja o exemplo:
print('\nfind ex2: ')
print('kappa'.find('a', 2))

# ex 2:
# Pode utilizar o método find() para procurar todas as ocorrências da substring, como aqui:
print('\nfind - variação em texto: ')

the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)


#---------------------------
# isalnum()

# O método sem parâmetros chamado isalnum() verifica se a string contém apenas
#  dígitos ou carateres alfabéticos (letras) e devolve True ou False
#  de acordo com o resultado.

# Demonstrating the isalnum() method:
print('\nisalnum: ')
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())


# t = 'Six lambdas'
# print(t.isalnum())

# resultado: False
# A causa do resultado é um espaço - não é nem um dígito nem uma letra.


#-------------------------------------
# isalpha()

# A classe isalpha() é mais especializado - está interessado apenas em letras.
# Example 1: Demonstrating the isapha() method:
print('\nisalpha: ')
print("Moooo".isalpha())
print('Mu40'.isalpha())


#--------------------------------------
# isdigit()

# Por sua vez, o método isdigit() olha apenas para os dígitos - qualquer outra coisa produz False como o resultado.
# Example 2: Demonstrating the isdigit() method:
print('\nisdigit: ')
print('2018'.isdigit())
print("Year2019".isdigit())


#-------------------------------------
# islower()
# A classe islower() é uma variante picuinhas do isalpha() - aceita apenas letras minúsculas.

# Example 1: Demonstrating the islower() method:
print('\nislower: ')
print("Moooo".islower())
print('moooo'.islower())


#-------------------------------------
# isspace()
# A classe isspace() identifica apenas os espaços em branco - ignora qualquer outro caratere (o resultado é False então).

# Example 2: Demonstrating the isspace() method:
print('\nisspace: ')
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())



#-------------------------------------
# isupper()
# A classe isupper() é a versão maiúscula do islower() - concentra-se apenas em letras maiúsculas.

# Example 3: Demonstrating the isupper() method:
print('\nisupper: ')
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())



#------------------------------------
# join()
# - como o seu nome sugere, o método realiza uma junção (em inglês, join) - espera um argumento como 
# uma lista; deve ter a certeza de que todos os elementos da lista são strings - o método irá levantar uma exceção TypeError de outra forma;
# - todos os elementos da lista serão unidos numa string, mas...
# - ... a string a partir da qual o método foi invocado é usada como um separador, colocado entre as strings;
# a string recém-criada é devolvida como um resultado.

# Demonstrating the join() method:
print('\njoin: ')
print(",".join(["omicron", "pi", "rho"]))

# explicação:
# o método join() é invocado de dentro de uma string contendo uma vírgula (a string pode ser arbitrariamente longa, ou pode estar vazia)
# o argumento join é uma lista contendo três strings;
# o método devolve uma nova string.