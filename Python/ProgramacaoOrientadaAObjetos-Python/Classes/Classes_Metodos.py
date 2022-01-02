#Classe ex01
class Exemplo01:
    
    #Função
    def incrementa(self, v, i):
        valor = v
        incremento = i
        resultado = valor + incremento
        return resultado

#instanciando um objeto chamado 'a', da classe Exemplo01
a = Exemplo01()

#Método
b = a.incrementa(10, 5)
print('\nExemplo 01: ', b)

# Fazendo a mesma coisa de forma direta: 
# a = Exemplo01().incrementa(10, 5)

# Não é possível acessar os atributos de dentro da classe Exemplo01

#-----------------------------------
#Classe ex02
class Exemplo02:
    
    #Função
    def incrementa(self, v, i):
        self.valor = v
        self.incremento = i
        self.resultado = self.valor + self.incremento
        return self.resultado

#instanciando um objeto chamado 'a', da classe Exemplo02
a = Exemplo02()

#Método
b = a.incrementa(10, 5)
print('\nExemplo 02: ', b)

# Fazendo a mesma coisa de forma direta: 
# a = Exemplo01().incrementa(10, 5)

# É possível acessar os atributos da classe Exemplo02
print('Acessando os atributos da Classe \'Exemplo02\':')
print('Valor: ', a.valor)
print('Incremento: ', a.incremento)