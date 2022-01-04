#Classe:
class Alunoo:
    _nome
    _ra
    _notaA1
    _notaA2
    _media
    _frequencia
    
#Métodos:
def setNome(nome):
    self._nome = nome
    
def setRa(ra):
    self._ra =_ra
    
def setNotaA1(notaA1):
    self._notaA1 = notaA1
    
def setNotaA2(notaA2):
    self._notaA2 = notaA2
    
def calcularMedia():
    self._media = (self._notaA1 + (2*self._notaA2)) / 3
    
def setFrequencia(freq):
    self._frequencia = freq
    
def getMedia():
    print('A média do aluno ', self._aluno, 'é: ', self._media)
    
def situacaoAluno():
    if(self._frequencia < 75):
        print('Aluno está reprovado por faltas!')
        
    elif(self._media >= 5):
        print('Aluno está reprovado!')
        
    elif(self._media >=3):
        print('Aluno está de RE!')
        
    else:
        print('Aluno está reprovado por nota!')
        
def getDadosAluno():
    print('\nAluno: ', self._nome)
    print('R.A: ', self._ra)
    print('Frequencia: ', self._frequencia)
    print('Nota A1: ', self._notaA2)
    print('Nota A2: ', self._notaA2)
    print('Média: ', self._media)