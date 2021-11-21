#  É totalmente possível declarar um closure equipado com um número arbitrário de parâmetros, por exemplo, um, tal como a power() função.

# Isto significa que o closure não só faz uso do ambiente congelado, como também pode modificar o seu comportamento, utilizando valores retirados do exterior.


# Este exemplo mostra mais uma circunstância interessante - pode criar tantos closures quantos quiser usando um e o mesmo código.
#  Isso é feito com uma função chamada make_closure(). 

#Obs:
# o primeiro closure obtido a partir de make_closure() define uma ferramenta que enquadra o seu argumento;
# o segundo foi concebido para cubrir o argumento.

def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power


fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))
