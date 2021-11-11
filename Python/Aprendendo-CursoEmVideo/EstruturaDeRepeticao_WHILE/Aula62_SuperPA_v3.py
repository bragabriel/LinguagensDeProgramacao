print("Gerador de PA")
print("-=-" * 10)

n = 0

n = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))

pa = n
cont = 1
total = 0


while n != 0:
    total = total + n
    while cont <= total:
        print("{} -> ".format(pa), end="")

        pa += razao
        cont += 1

    print("PAUSA")

    n = int(input("Quantos termos você quer mostrar a mais? "))
print("Progressão finalizada com {} termos mostrados.".format(total))
