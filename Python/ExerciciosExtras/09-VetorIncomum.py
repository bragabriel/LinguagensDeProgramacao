'''Criar 2 vetores com 10 números inteiros cada. Gerar e imprimir um vetor dos
números não comuns aos e vetores.'''

from random import randint

vet1 = [randint(0, 12) for i in range(0, 10)]
vet2 = [randint(0, 12) for i in range(0, 10)]

print("Vetor 01: ", vet1)
print("Vetor 02: ", vet2)

# set: conjuntos
print("Números incomuns: ", set(vet1) ^ set(vet2))
# print("Números incomuns", set(vet1) - set(vet2) and set(vet2) - set(vet1))

'''
sets (conjuntos): {}
    p1 | p2  OU  p1.union(p2) -> união (Elementos do primeiro mais o segundo eliminando as repetições)
    p1 & p2  OU  p1.intersection(p2) -> Intersecção (Elementos que estão em um conjunto & no outro conjunto)
    p1 - p2  OU  p1.difference(p2) -> Diferença (Elementos que tem em um mas não tem no outro)
    p1 ^ p2  OU  p1.symmetric_difference(p2) -> Diferença Simétrica (Elementos que tem em no p1 mas não tem no p2, e os que tem no p2 mas não tem no p1)
                 p1.isdisjoint(p2) -> Disjuntos (Não tem nenhum elemento em comum = TRUE)
                 
    cópia de conjuntos:
    p1 = {'Terra', 'Marte}
    p2 = p1.copy()
    
    add:
    p1.add('Jupiter')
    
    remove:
    p1.remove('Jupiter') //Dá erro se não tiver esse elemento no conjunto
    
    discard:
    p1.discard('asdasd') //Só vai remover se tiver, se não tiver, não da erro
    
    clear:
    p1.clear //Limpando o conjunto
    
    OBS: Conjuntos não tem elementos repetidos.
'''
