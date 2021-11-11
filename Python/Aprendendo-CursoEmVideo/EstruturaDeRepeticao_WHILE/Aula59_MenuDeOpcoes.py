n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))

opcao = 0

while opcao != 5:

    print("\n")
    print("->Menu de opções<-")
    print(''' 
    [ 1 ] - somar
    [ 2 ] - subtrair
    [ 3 ] - maior
    [ 4 ] - inserir novos números
    [ 5 ] - exit
    ''')

    opcao = int(input("Qual é sua opção? "))

    print("\n")

    if(opcao == 1):
        print("O resultado da soma eh:", n1+n2)

    elif(opcao == 2):
        print("O resultado da subtração eh:", n1-n2)

    elif(opcao == 3):
        if(n1>n2):
           maior = n1
        else:
            maior = n2
        print("O maior número eh:", n2)

    elif(opcao == 4):
        print("Insira os novos números: ")
        n1 = float(input("Primeiro valor: "))
        n2 = float(input("Segundo valor: "))
       
    elif(opcao == 5):
        print("Saindo do programa...")

    else:
        print("Opção inválida!")

    print("=-=" * 10)
print('Programa finalizado com sucesso!\n')