sexo = str(input("Informe seu sexo: [M/F] ")).strip().upper()[0]
# .strip() = Eliminar os espaços em branco depois da inserção do caractere
# [0] = pegar só o primeiro elemento, ex: Masculino = M

while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print("Sexo {} registrado com sucesso".format(sexo))