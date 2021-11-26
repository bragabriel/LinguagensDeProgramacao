# Tutorial disponível no YouTube, pelo canal 'Curso em Vídeo - Gustavo Guanabara'
# Vídeo aula do tutorial: https://www.youtube.com/watch?v=Qp2cXfCHk2I&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=6&ab_channel=CursoemV%C3%ADdeo

listagem = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Transferidor', 4.20,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.30,
         'Libro', 34,90,)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for posicao in range(0, len(listagem)):
    if posicao % 2 == 0:
        print(f'{listagem[posicao]:.<30}', end='')
        #                          ^^ ^
        #             caracter | alinhado a esq | n caracteres
    else:
        print(f'R${listagem[posicao]:>7.2f}')