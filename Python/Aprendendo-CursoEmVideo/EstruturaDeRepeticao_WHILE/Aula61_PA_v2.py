print("Gerador de PA")
print("-=-" * 10)

n = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))

pa = n

cont = 1

while cont <= 10:
    print("{} -> ".format(pa), end="")

    pa += razao

    cont += 1

print("FIM")

