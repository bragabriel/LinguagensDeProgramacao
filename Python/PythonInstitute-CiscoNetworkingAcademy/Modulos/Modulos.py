#   O que é um módulo?
# O Tutorial Python define-o como um ficheiro contendo definições e declarações Python,
# que pode ser posteriormente importado e utilizado quando necessário.

# o primeiro (provavelmente o mais comum) acontece quando se pretende utilizar um módulo já existente,
#  escrito por outra pessoa, ou criado por si próprio durante o seu trabalho nalgum projeto complexo - neste caso você é o utilizador do módulo;

# o segundo ocorre quando se pretende criar um novo módulo, quer para uso próprio, quer para facilitar
#  a vida a outros programadores - você é o fornecedor do módulo.


# Todos estes módulos, juntamente com as funções integradas, formam a Python standard library

# Para tornar um módulo utilizável, deve importá-lo
#Ex: 
import math
print(math.sin(math.pi/2))
print(math.pi)


#Outra forma é: a sintaxe de import indica precisamente qual a entidade (ou entidades) do módulo que é aceitável no código:
#Ex: 
from math import pi
print(pi)


# É possível importar tudo do módulo:
# from <module> import *
from math import *


# Usando ALIAS na importação do módulo:
import math as matematica
print(matematica.sin(matematica.pi/2))


#Forma correta de invocação das funções de módulos:
#  import mint
#  mint.make_money()

# ou

#  from mint import make_money
#  make_money()

# ou

#  from mint import *
#  make_money()


# Usando o DIR()
# O dir lista as informações do módulo, exemplo:
import math
dir(math)
