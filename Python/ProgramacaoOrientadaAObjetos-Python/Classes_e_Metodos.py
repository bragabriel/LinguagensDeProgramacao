# Class:
# Sintaxe:
class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        # __init__ = construtor
        # self = dizendo que estamos trabalhando na class Computador (.this)
        
        #Atributos:
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    
    # Métodos
    def Ligar(self):
        print('Ligando...')

    def Desligar(self):
        print('Desligando...')

    def ExibirInformacoesComputador(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)


# Instanciando a classe:
computador1 = Computador('Asus', '8gb', 'Nvidia')
computador2 = Computador('Dell', '16gb', 'AMD')


print('Computador 1:', '\nMarca:', computador1.marca, '\nMemória-Ram:', computador1.memoria_ram, '\nPlaca-de-Vídeo: ', computador1.placa_de_video, end='\n\n')
print('Computador 2:', '\nMarca:', computador2.marca, '\nMemória-Ram:', computador2.memoria_ram, '\nPlaca-de-Vídeo: ', computador2.placa_de_video, end='\n\n')


# Utilizando os métodos:
print('=-=-=' * 5)
computador1.Ligar()
computador1.ExibirInformacoesComputador()
computador1.Desligar()
print('=-=-=' * 5)

