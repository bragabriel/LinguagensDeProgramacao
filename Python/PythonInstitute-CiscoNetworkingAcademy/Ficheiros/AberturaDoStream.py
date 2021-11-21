# A abertura do stream é realizada por uma função que pode ser invocada da seguinte forma:

'''
stream = open(file, mode = 'r', encoding = None)
'''  

# O nome da função (open) fala por si; se a abertura for bem sucedida, a função devolve um objeto de stream; caso contrário, é levantada uma exceção (por exemplo, FileNotFoundError se o ficheiro que vai ler não existir);

# O primeiro parâmetro da função (file) especifica o nome do ficheiro a ser associado ao stream;

# O segundo parâmetro (mode) especifica o modo aberto utilizado para o stream; é uma string cheia de carateres, e cada um deles tem o seu significado especial (mais detalhes em breve);

# O terceiro parâmetro (encoding) especifica o tipo de codificação (por exemplo, UTF-8 quando se trabalha com ficheiros de texto)


# Abrir os streams: modos

# r modo aberto: read
# w modo aberto: write
# a modo aberto: append
# r+ modo aberto: read and update
# w+ modo aberto: write and update
