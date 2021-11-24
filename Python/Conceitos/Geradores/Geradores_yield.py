# Aula disponível por: 'códigofluente' -  'https://www.codigofluente.com.br/aula-17-python-geradores-yield/'

# Geradores:

# As funções geralmente seguem o seguinte fluxo:
# processar;
# retornar valores;
# encerrar;

# Geradores funcionam parecido, eles lembram o estado do processamento entre as chamadas,
#  ficando em memória e quando ativados retornam o próximo item.



# Vantagens dos geradores quando comparado às funções:

# Lazy Evaluation: geradores só são processados quando é realmente necessário, por isso, economizam recursos de processamento e memória;
# Reduzem a necessidade da criação de listas;
# Permitem trabalhar com sequências ilimitadas de elementos;



# --------------------------------------------------------------------


def numbers_fuc(max_n):     #definindo funcao
    lst = []    #declarando lista vazia
    for number in range(max_n + 1):     #for que percorre de 0 até max_n+1
        lst.append(number)      #anexa na lista o 0, 1, 2 ... max_n+1
    return lst

# EXPLICAÇÃO:

# A função numbers_fuc criada acima, cria uma lista chamada lst com [0, 1, 2, 3, 4, …, max_n] até chegar no max_n.

# Ela cria essa lista, aloca na memória e guarda toda a lista e seu conteúdo.

# Ocupa espaço e usa recursos de hardware para isso.

# Não há problema se max_n for um número pequeno, mas, se for algo absurdamente grande tipo: (3654 * 9872 ** 23), seu computador provavelmente irá travar.

# Então, nesses casos de um max_n gigantesco, o melhor é usar gerador ao invés de função.



#--------------------------------------------------

# Criando um gerador:
def numbers_yield(max_n):
    for n in range(max_n + 1):
        yield n

# Ao utilizar um numero gigante como: 623*10**21, com o gerador o computador não vai travar, pois não vai extrapolar os limites de memória

# Ele só vai calcular o primeiro elemento da sequência quando precisar dele e vai entregar o 0 e vai parar.

# Não processa mais nada, não aloca nada em memória até o código solicitar o próximo número.

# Aí então ele esquece do primeiro e te entrega o segundo e assim vai, ele vai entregando um por vez, o terceiro, depois o quarto, o quinto e assim por diante.



# O gerador só vai calcular alguma coisa a cada next(), que é a função chamada internamente se você, por exemplo, passar um gerador para um for.
my_generator = numbers_yield(5)
next(my_generator)
next(my_generator)
next(my_generator)