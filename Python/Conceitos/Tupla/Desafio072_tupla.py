# Desafio proposto pelo canal 'Curso em Vídeo | Gustavo Guanabara'
# link: https://www.youtube.com/watch?v=0LB3FSfjvao&ab_channel=CursoemV%C3%ADdeo

tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

n = 21

while(n<0 or n>20):
    n = int(input('Digite um número entre 0 e 20: '))

result = tupla[n]

print('O número digitado foi: ', n)
print('Esse número, escrito por extenso é:', result)