'''Entrar com um número e informar se ele é divisível por 10, por 5, por 2 ou se não é
divisível por nenhum destes.'''

num = int(input())

if(num % 10 == 0):
    print(f'O número {num} é divisível por 10!')
    
elif(num % 5 == 0):
    print(f'O número {num} é divisível por 5!')
    
elif(num % 2 == 0):
    print(f'O número {num} é divisível por 2!')
    
else:
    print(f'O valor {num} não é divisível por 10, nem por 5, nem por 2!')