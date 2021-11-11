# Função para calcular o imc

# 01:
def imc(weight, height):
    result = weight / height \
        ** 2

    return result

a = imc(68, 1.74)

print(a)

# A barra invertida é usada quando queremos quebrar a linha de código
# em outra linha, e ela continuará funcionando 
# ex:
#  result = weight / height \
#        ** 2


#02: 
def imc(weight, height):
    return weight / height ** 2


print(imc(52.5, 1.65))



