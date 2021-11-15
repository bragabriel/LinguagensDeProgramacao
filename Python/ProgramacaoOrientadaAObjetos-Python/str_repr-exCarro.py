class Carro:
  def __init__(self, marca, modelo, ano):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano


#O __str__ serve para exibir o objeto para usuário final, usada pelo comando print e pela função str

#O __repr__ serve para exibir o objeto para o programador, usada pelo console do Python e pela função repr


# O método __str__() deve retornar uma representação em forma de string do valor do objeto.
# __str__ é um método especial, como __init__, usado para retornar uma representação de string de um objeto.
  def __str__(self):
    return f"{self.marca}/{self.modelo} - Ano {self.ano}"


  def __repr__(self):
    return (
      f"Marca: {self.marca}\n"
      f"Modelo: {self.modelo}\n"
      f"Ano: {self.ano}"
    )

possante = Carro('Ferrari', 'F8 Tributo', '21')

print(f'{possante}')


# Resumo:

# __repr__
# quando precisa do código que reproduz o objeto
# gera output para o desenvolvedor

# __str__
# torna o objeto legível
# gera output para o usuário final