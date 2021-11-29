# Tutorial disponível no YouTube, pelo canal 'Curso em Vídeo - Otávio Miranda'
# Vídeo aula do tutorial: https://www.youtube.com/watch?v=EQRsJ2bKvUU&ab_channel=Ot%C3%A1vioMiranda


# Lambda: Função Anônima


# Função padrão: 
def funcao(arg, arg2):
    return arg * arg2

var = funcao(2, 2)

print('\nFunção default: ', var)


# Função anônima OU Expressão lambda:
a = lambda x, y: x * y

print('\nFunção Lambda: ', a(2,2))

# Função anônima, sem nome.
# não utilizamos parenteses, chaves nem return

# Utilizamos expressões lambdas por exemplo, quando queremos passar uma função de parâmetro para outra função, ou para algum método.



# Exemplo de uso: "Listas com outras Listas dentro"

print('\nExemplo de uso:')
lista = [
    ['Produto1', 15],
    ['Produto2', 20],
    ['Produto3', 9],
    ['Produto4', 35],
    ['Produto5', 4],
]

# lista.sort() = não funciona, pois temos outras listas dentro a serem ordenadas

def ordena(item):
    return item[1] # item 0 'array', item 1 'int' - preço

lista.sort(key=ordena, reverse=True)
print('\nUtilizando uma função default para ordenar: ', lista)


lista.sort(key=lambda item: item[1], reverse=True)
print('\nUtilizando uma função anônima para ordenar: ', lista)



# Podemos usar a função sorted() sem afetar a lista original

print('\n\nExemplo de uso \'sorted()\':')
lista2 = [
    ['Produto1', 15],
    ['Produto2', 20],
    ['Produto3', 9],
    ['Produto4', 35],
    ['Produto5', 4],
]
print('\nUtilizando uma função anônima + sorted() para ordenar: ', sorted(lista2, key=lambda item: item[1], reverse=True))
print('\nLista original está intacta: ', lista2)