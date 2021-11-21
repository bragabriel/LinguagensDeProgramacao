# Espera o mesmo tipo de argumentos que map(), mas faz algo diferente - filtra o seu segundo argumento ao mesmo tempo que é guiado
#  por instruções que fluem da função especificada como o primeiro argumento (a função é invocada para cada elemento da lista, tal como em map()).


# A lista é então filtrada, e apenas os números que são iguais e superiores a zero são aceites.

from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)
