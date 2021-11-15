class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    # métodos

    def falar(self, assunto):
        #Se já estiver comendo, ou seja, se comendo = TRUE
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return
        #Se já estiver falando    
        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando: {assunto}')
        self.falando = True


    def parar_falar(self):
        #Se ele não está falando
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False



    def comer(self, alimento):
        # Se já estiver comendo: 
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True
    

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False



# Tutorial disponível no YouTube, pelo canal 'Otávio Miranda'
# Vídeo aula do tutorial: https://www.youtube.com/watch?v=RLVbB91A5-8&list=PLbIBj8vQhvm34qAAEEH_PdL2tMG9rz-P7&ab_channel=Ot%C3%A1vioMiranda
