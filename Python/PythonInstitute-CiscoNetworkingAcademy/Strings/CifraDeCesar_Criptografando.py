# Caesar cipher.
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)


# Explicação do código:

# linha 02: pedir ao utilizador para inserir a mensagem aberta (não encriptada), de uma linha;
# linha 03: preparar uma string para uma mensagem encriptada (vazia por agora)
# linha 04: iniciar a iteração através da mensagem;
# linha 05: se o caratere atual não for alfabético...
# linha 06: ...ignorá-lo;
# linha 07: converter a letra em maiúsculas (é preferível fazê-lo cegamente, em vez de verificar se é necessário ou não)
# linha 08: obter o código da letra e incrementá-lo em um;
# linha 09: se o código resultante tiver “deixado” o alfabeto latino (se for maior do que o código Z)...
# linha 10: ...alterá-lo para o código A;
# linha 11: anexar o caratere recebido ao fim da mensagem encriptada;
# linha 13: imprimir a cifra.