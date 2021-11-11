def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True

n1 = n2 = n3 = 0

int(input("n1: "))
int(input("n2: "))
int(input("n3: "))

print(is_a_triangle(n1, n2, n3))

