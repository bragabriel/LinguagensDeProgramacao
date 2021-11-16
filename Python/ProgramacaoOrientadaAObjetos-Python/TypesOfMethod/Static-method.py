from random import randint

class Pessoa:
    ano_atual = 2019

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # método de instância - Precisa receber o (self)
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    # método statico
    @staticmethod
    def gera_id():
    # método statico não recebe nem a classe, nem a instância (self)
    
        rand = randint(1, 100)
        return rand

p1 = Pessoa('Gabriel', 19)

print(Pessoa.gera_id())
print(Pessoa.gera_id())



print('\n')
# Tutorial disponível no YouTube, pelo canal 'Otávio Miranda'
# Vídeo aula do tutorial: https://www.youtube.com/watch?v=fChIn5Agl90&list=PLbIBj8vQhvm34qAAEEH_PdL2tMG9rz-P7&index=4&ab_channel=Ot%C3%A1vioMiranda
