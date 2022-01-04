#Classe:
class Classe1:
    
    #Função
    def incrementa(self, v, i):
        self.valor = v
        self.incremento = i
        self.resultado = self.valor + self.incremento
        return self.resultado
    
B = Classe1()

B.incrementa(2,5)

print('B.valor: ',B.valor)

#Herança: 
class Calculos(Classe1):
    def decrementa(self):
        self.valor = self.valor - self.incremento

C = Calculos()

C.incrementa(5, 2)

print('C.valor: ',C.valor)

C.decrementa()

C.valor

print('C.valor: ',C.valor)