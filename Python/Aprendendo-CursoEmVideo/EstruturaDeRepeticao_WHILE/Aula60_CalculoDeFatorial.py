from math import factorial

n = int(input("Digite um número para calcular seu Fatorial: "))

i = n

print("Calculando {}! = ".format(n), end="")

while i>0:
    print("{}".format(i), end="")
    print(" x " if i > 1 else " = ", end="")
    i -= 1

f = factorial(n)

print(f)


