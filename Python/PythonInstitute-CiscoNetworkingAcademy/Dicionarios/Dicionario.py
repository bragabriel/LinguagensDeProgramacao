# O dicionário é outra estrutura de dados Python. 
# Não é um tipo de sequência (mas pode ser facilmente adaptado ao processamento de sequências)
# e é mutável.


#  dicionário Python funciona da mesma forma que um dicionário bilingue.
#  Por exemplo, tem uma palavra inglesa e precisa do seu equivalente francês.

# No mundo de Python, a palavra que se procura chama-se key. 
# A palavra que obtém do dicionário chama-se um value.



# cada chave deve ser única - não é possível ter mais do que uma chave com o mesmo valor;
# uma chave pode ser qualquer tipo de objeto imutável: pode ser um número (inteiro ou float), ou mesmo uma string, mas não uma lista;
# um dicionário não é uma lista - uma lista contém um conjunto de valores numerados, enquanto que um dicionário contém pares de valores;
# a função len() funciona também para dicionários - devolve o número de elementos de key-value no dicionário;
# um dicionário é uma ferramenta de sentido único - se tiver um dicionário inglês-francês, pode procurar por equivalentes franceses de termos ingleses, mas não vice-versa.


#A lista de pares é rodeada por chaves, enquanto os pares em si são separados por vírgulas, e as chaves e valores por dois pontos.
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

# No primeiro exemplo, o dicionário usa chaves e valores que são ambas strings. No segundo, as chaves são strings, mas os valores são inteiros. 
# A disposição inversa (teclas → números, valores → strings) também é possível, bem como a combinação número-número.