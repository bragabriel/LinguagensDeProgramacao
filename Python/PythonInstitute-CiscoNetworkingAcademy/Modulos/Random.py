# A função RANDOM

# A função mais geral chamada random() (não confundir com o nome do módulo) 
# produz um número float x vindo do intervalo (0.0, 1.0) - por outras palavras: (0,0 <= x < 1,0).

from random import randint, random

for i in range(5):
    print(random())



# Gerando um número aleatorio entre 1 e 10:

random_number = randint(1,10)
print("N° aleatorio entre 1 e 10: ", random_number)
# Se tivesse usado: import random
# usariamos: random_number = random.randint(1, 10)

