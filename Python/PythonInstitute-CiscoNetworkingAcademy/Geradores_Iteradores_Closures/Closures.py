#  O closure é uma técnica que permite o armazenamento de valores apesar do facto de o contexto em que foram criados já não existir.

def outer(par):
    loc = par

    def inner():
        return loc
    return inner


var = 1
fun = outer(var)
print(fun())

# a função inner() devolve o valor da variável acessível dentro do seu scope, uma vez que inner() pode utilizar
#  qualquer uma das entidades à disposição de outer()

# a função outer() devolve a função inner() em si; mais precisamente, devolve uma cópia da função inner(),
#  a que estava congelada no momento de invocação outer(); a função congelada contém o seu ambiente completo,
#  incluindo o estado de todas as variáveis locais, o que também significa que o valor de loc é retido com sucesso,
#  embora outer() tenha deixado de existir há muito tempo.


# A função devolvida durante a invocação outer() é um closure.