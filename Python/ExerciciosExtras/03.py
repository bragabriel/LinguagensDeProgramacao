'''Entrar com nome, sexo e idade de uma pessoa. Se a pessoa for do sexo masculino
e tiver menos que 25 anos, imprimir nome e a a mensagem: ACEITO. Caso contrário,
imprimir nome e a mensagem: NÃO ACEITO.'''

nome = str(input("Insira seu nome: "))
idade = int(input("Insira sua idade: "))
# Tirando os Espaços, Deixando em Maiúsculo, Pegando a Primeira Letra
sexo = str(input("Insira seu sexo: ")).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input("Dados inválidos. Por favor, informe seu sexo: ")).strip().upper()[0]

if((sexo in 'Mm') and (idade < 25)):
    print("ACEITO!")
else:
    print("NÃO ACEITO!")
