#Classe:
class Aluno():
    nome = ''
    ra = ''
    notaA1 = 0
    notaA2 = 0
    media = 0
    frequencia = 0
        
    #Métodos:
    def set_nome(self, nome):
        #Condicionando o NOME à ser uma String
        print('Método setter sendo utilizado')
        if(type(nome)==type(str())):
            self.__nome = nome
        else:
            print('Nome deve ser uma String!')
        
    def get_nome(self):
        print('Método getter sendo utilizado')
        return self.__nome
        
    def set_ra(self, ra):
        #Condicionando o R.A à ser um INT
        if(type(ra)==type(int())):
            self.__ra =ra
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
        print(f'A média do aluno {self.__nome} é: {self.media}')
        
    def situacao_Aluno(self):
        if(self.frequencia < 75):
            print('Aluno está Reprovado por faltas!')
            
        elif(self.media >= 5):
            print('Aluno está Aprovado! Parabéns!')
            
        elif(self.media >=3):
            print('Aluno está de RE!')
            
        else:
            print('Aluno está Reprovado por nota!')
            
    def getDadosAluno(self):
        print('Aluno:', self.__nome)
        print('R.A:', self.__ra)
        print('Frequência:', self.frequencia)
        print('Nota A1:', self.notaA2)
        print('Nota A2:', self.notaA2)
        print('Média:', self.media)
        
        
    #Atributo PRIVADO:
    # nome = property(set_nome)
    # ra = property(set_ra)