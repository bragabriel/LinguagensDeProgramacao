resp = "S"

soma = cont = media = maior = menor = 0

while resp in "Ss":

    n = int(input("Digite um número: "))

    soma += n

    cont += 1

    if(cont == 1):
        maior = menor = n

    elif(n>maior):
        maior = n
    
    elif(n<menor):
        menor = n

    resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]

media = soma / cont

print("Você digitou {} números e a média foi {}".format(cont, media))
print("O maior valor foi {} e o menor foi {}".format(maior, menor))