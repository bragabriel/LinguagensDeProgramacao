# Pode parecer um pouco surpreendente à primeira vista, mas é preciso ter em mente que não se trata de uma instrução condicional.
#  Além disso, não é uma instrução de todo. É um operador.


# ex: 
# O código preenche uma lista com 1e 0- se o index de um determinado elemento for estranho,
#  o elemento é definido para 0, e para 1 caso contrário.
 
the_list = []

for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)

print('\nexemplo 1: ', the_list)


# Outro exemplo: 
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]

print('\nexemplo 2: ',the_list)
