# O protocolo iterador é uma forma de um objeto se comportar de acordo com as regras impostas pelo contexto das declarações for e in.
# Um objeto em conformidade com o protocolo iterador é chamado um iterador.

# Um iterador deve fornecer dois métodos:
# 1) __iter__() que deve devolver o objeto em si e que é invocado uma vez (é necessário para que Python inicie com sucesso a iteração)

# 2) __next__() que se destina a devolver o próximo valor (primeiro, segundo, etc.) da série desejada - será invocado pelas declarações
#  for/in a fim de passar pela próxima iteração; se não houver mais valores a fornecer, o método deve levantar a exceção StopIteration .


# Exemplo:
# Construímos uma classe capaz de iterar através dos primeiros valores n (onde n é um parâmetro construtor) dos números de Fibonacci.
class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")				
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fib(10):
    print(i)
