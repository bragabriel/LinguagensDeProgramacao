frase = str(input('Digite uma frase: ')).strip().upper()
# .strip() = tirar os espaços em branco de antes e depois do final da frase

print("Você digitou a frase {}".format(frase))

#separando a frase em palavras
palavras = frase.split()

#juntando a frase, separando as palavras por: ''
junto = ''.join(palavras)



#pegar o numero de letras(junto) - 1, vai até a letra -1 (antes da primeira), e volta uma letra
'''
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
'''

#inverso = junto começando do inicio, terminar no fim, e pegar de trás para frente
inverso = junto[::-1]

#comparação para verificar se é palíndromo
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print("A frase digitada não é um palíndromo!")

print('O inverso de {} é {}'.format(junto, inverso))

