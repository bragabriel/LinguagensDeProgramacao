print("-" * 10)
print("Sequência de Fibonacci")
print("-" * 10)

termos = int(input("Quantos termos você quer mostrar? "))

print("~" * 10)
print("\n")

n1 = 0
n2 = 1

i = 3

print("{} -> {}".format(n1, n2), end='')

while (i <= termos):
    n3 = n1 + n2
    print(' -> {}'.format(n3), end='')
    n1 = n2
    n2 = n3
    i += 1
print("\n")
print("~" * 10)