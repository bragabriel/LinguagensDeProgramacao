#----------------------
# lower()
# A classe lower() faz uma cópia de uma source string, substitui todas as letras maiúsculas por minúsculas

# Demonstrating the lower() method:
print('\nlower')
print("SiGmA=60".lower())


#---------------------
# lstrip()

# O parâmetro sem lstrip() método devolve uma cadeia recém-criada 
#  formada a partir da original, removendo todos os principais espaços em branco.

# Demonstrating the lstrip() method:
print('\nlstrip: ')
print("[" + " tau ".lstrip() + "]")

#ex02
print('\nlstrip ex02: ')
print("www.cisco.com".lstrip("w."))


#----------------------
# replace()

# O método de dois parâmetros replace() devolve uma cópia da string original na qual todas
#  as ocorrências do primeiro argumento foram substituídas pelo segundo argumento.

# Demonstrating the replace() method:
print('\nreplace:')
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

print('\nreplace ex02:')
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))



#--------------------------
# rfind()

# Os métodos de um, dois e três parâmetros chamados rfind() fazem quase as mesmas coisas
#  que os seus homólogos (os desprovidos do prefixo r), mas começam as suas buscas a partir do fim da string, não do início (daí o prefixo r, para right).

# Demonstrating the rfind() method:
print('\n rfind:')
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))



#------------------------
# rstrip()

# Duas variantes do método rstrip() fazem quase o mesmo que lstrip,
#  mas afetam o lado oposto da string.

# Demonstrating the rstrip() method:
print('\nrstrip: ')
print("[" + " upsilon ".rstrip() + "]")

print("cisco.com".rstrip(".com"))



#------------------------
# split()

# A classe split() faz o que diz - divide a string e constrói uma lista de todas as substrings detetadas.
# O método assume que as substrings são delimitadas por espaços em branco - os espaços não participam na
#  operação, e não são copiados para a lista resultante.

# Demonstrating the split() method:
print('\nstrip: ')
print("phi       chi\npsi".split())

#OBS: a operação inversa pode ser realizada pelo método join() .


#-----------------------
# startswith()

# A classe startswith() é um reflexo espelhado de endswith() - verifica se uma determinada string começa com a substring especificada.

# Demonstrating the startswith() method:
print("omega".startswith("meg"))
print("omega".startswith("om"))

print()


#------------------------
# strip()

# A classe trip() combina os efeitos causados por rstrip() e lstrip() - faz uma nova string com falta de todos os espaços em branco à esquerda e à direita.

# Demonstrating the strip() method:
print("[" + "   aleph   ".strip() + "]")


#-------------------------
# swapcase()

# A classe swapcase() faz uma nova string, trocando a maiúscula/minúscula de todas as letras dentro da source string: carateres minúsculos tornam-se maiúsculas e vice-versa.
# Todos os outros carateres permanecem intocados.

# Demonstrating the swapcase() method:
print("I know that I know nothing.".swapcase())



#------------------------
# title()

# A classe title() muda a primeira letra de cada palavra para maiúscula, transformando todas as outras em minúsculas.

# Demonstrating the title() method:
print("I know that I know nothing. Part 1.".title())



#------------------------
# upper()

# O método upper() faz uma cópia da source string, substitui todas as letras minúsculas pelas suas contrapartes maiúsculas, e devolve a string como resultado.

# Demonstrating the upper() method:
print("I know that I know nothing. Part 2.".upper())