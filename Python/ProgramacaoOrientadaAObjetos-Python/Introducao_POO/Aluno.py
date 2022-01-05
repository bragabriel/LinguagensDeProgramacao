#Classe:
class Alunoo:
    
    notaA1 = 0
    notaA2 = 0
    media = 0
    frequencia = 0
        
#Métodos:
def set_nome(self, nome):
    
    #Condicionando o NOME à ser uma String
    if(type(nome)==type(str())):
        self._nome = nome
    else:
        print('Nome deve ser uma String!')
    
def set_ra(self, ra):
    #Condicionando o R.A à ser um INT
    if(type(ra)==type(int())):
        self._ra =ra
    else:
        print('R.A deve ser um Número Inteiro!')
        
def set_notaA1(self, notaA1):
    self.notaA1 = notaA1
    
def set_notaA2(self, notaA2):
    self.notaA2 = notaA2
    
def calcular_Media(self):
    self.media = (self.notaA1 + (2*self.notaA2)) / 3

def set_frequencia(self, freq):
    self.frequencia = freq
    
def get_media(self):
    print('A média do aluno ', self._aluno, 'é: ', self.media)
    
def situacao_Aluno(self):
    if(self.frequencia < 75):
        print('Aluno está reprovado por faltas!')
        
    elif(self.media >= 5):
        print('Aluno está reprovado!')
        
    elif(self.media >=3):
        print('Aluno está de RE!')
        
    else:
        print('Aluno está reprovado por nota!')
        
def getDadosAluno(self):
    print('\nAluno: ', self._nome)
    print('R.A: ', self._ra)
    print('Frequência: ', self.frequencia)
    print('Nota A1: ', self.notaA2)
    print('Nota A2: ', self.notaA2)
    print('Média: ', self.media)
    
    
    #Atributo PRIVADO:
    _nome = property(set_nome)
    _ra = property(set_ra)