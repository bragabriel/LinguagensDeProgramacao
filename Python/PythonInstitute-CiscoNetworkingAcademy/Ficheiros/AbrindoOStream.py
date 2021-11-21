# Abrindo o Stream:

# Imagine que queremos desenvolver um programa que leia o conteúdo do ficheiro de texto nomeado: C:\Users\User\Desktop\file.txt.

try:
    stream = open("C:\Users\User\Desktop\file.txt", "rt")
    # Processing goes here.
    stream.close()
except Exception as exc:
    print("Cannot open the file:", exc)



# Diagnosticar problemas de stream

# O objeto IOError está equipado com uma propriedade chamada errno (o nome vem da frase error number) e pode acedê-lo da seguinte forma:
'''
    try:
        # Some stream operations.
    except IOError as exc:
        print(exc.errno)
'''

# Fechando o Stream
# Essa ação é executada por um método invocado de dentro do objeto de stream aberto: stream.close().
    #stream.close()
