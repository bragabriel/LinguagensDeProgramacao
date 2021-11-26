# Tutorial disponível no YouTube, pelo canal 'Curso em Vídeo - Gustavo Guanabara'
# Vídeo aula do tutorial: https://www.youtube.com/watch?v=8BgSqrOpKvU&list=PLHz_AreHm4dksnH2jVTIVNviIMBVYyFnH&index=7&ab_channel=CursoemV%C3%ADdeo

palavras = ('maça', 'janela', 'pessego', 'porta', 'ingles', 'python', 'aprender', 'aprendendo', 'tupla')

for i in palavras:
    print(f'\nNa palavra {i.upper()} temos as vogais: ', end='')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')