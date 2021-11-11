# A parte da classe Python responsável pela criação de novos objetos é chamada de construtor, e é implementada como um método do nome __init__.

# Cada declaração de método de classe deve conter pelo menos um parâmetro (sempre o primeiro) geralmente referido como self, e é usado pelos objetos para se identificarem.

class Stack:  # Defining the Stack class.
    def __init__(self):  # Defining the constructor function.
        print("Hi!")


stack_object = Stack()  # Instantiating the object.


# obs: Se quisermos esconder qualquer um dos componentes de uma classe do mundo exterior, devemos começar o seu nome com __. Tais componentes são chamados privados.