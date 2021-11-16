class Pessoa:
    ano_atual = 2019

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
    # cls (ou classe) = pois é um método da classe, ou seja, não está disponível em outras instâncias (objetos), apenas nessa classe.
 
        # esse método tem como parâmetro o cls, portanto estamos nos referindo a classe
        # por isso temos acesso a variavel 'ano_atual'
        idade = cls.ano_atual - ano_nascimento

        # retornando a própria classe, passando parâmetros
        return cls(nome, idade)

p1 = Pessoa('Luiz', 10)

p2 = Pessoa.por_ano_nascimento('Gabriel', 2001)

print(p1.idade)

p1.get_ano_nascimento()

print(p2.idade)