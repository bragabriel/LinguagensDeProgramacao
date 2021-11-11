#Pergunta: como se pode trocar os valores de duas variáveis?

# Sabemos que é necessário uma variável auxiliar para não perdemos
# o valor de uma variável no meio da traca

#É assim que se pode fazer:
print("forma 1:")
variable_1 = 1
variable_2 = 2
print("antes da troca: ", variable_1, variable_2)

auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary

print("depois da troca: ", variable_1, variable_2)


# Contudo, o Python oferece uma forma mais 
# conveniente de fazer a troca:
print("forma 2:")
variable_1 = 1
variable_2 = 2
print("antes da troca: ", variable_1, variable_2)

variable_1, variable_2 = variable_2, variable_1

print("depois da troca: ", variable_1, variable_2)