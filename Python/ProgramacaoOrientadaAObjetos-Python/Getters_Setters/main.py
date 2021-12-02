# Tutorial disponível no YouTube, pelo canal 'Otávio Miranda'
# Vídeo aula do tutorial: https://www.youtube.com/watch?v=PGXwNophTOQ&list=PLbIBj8vQhvm34qAAEEH_PdL2tMG9rz-P7&index=5&ab_channel=Ot%C3%A1vioMiranda


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual /100))

    # Getter preco
    @property
    def preco(self):
        return(self._preco)

    # Setter preco
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor

    # Getter nome
    @property
    def nome(self):
        return self._nome

    # Setter nome
    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

print()
produto1 = Produto('CAMISETA', 50)
produto1.desconto(50)
print('Produto 1:', produto1.nome, '\tPreço:', produto1.preco, '\n')

produto2 = Produto('CaNecA', 'R$15')
produto2.desconto(10)
print('Produto 2:', produto2.nome, '\tPreço:', produto2.preco, '\n')