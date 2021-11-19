'''
def fun(n):
    for i in range(n):
        yield i
'''

# Adicionámos yield em vez de return.
# Esta pequena emenda transforma a função num gerador, e executar a declaração yield tem alguns efeitos muito interessantes.

# Todos os valores das variáveis são congelados e aguardam a próxima invocação, quando a execução é retomada (não tirada do zero, como depois return).

# Há uma limitação importante: tal função não deve ser invocada explicitamente porque - na realidade - já não é uma função; é um objeto gerador.
# A invocação devolverá o identificador do objeto, não a série que esperamos do gerador.

def fun(n):
    for i in range(n):
        yield i


for v in fun(5):
    print(v)
