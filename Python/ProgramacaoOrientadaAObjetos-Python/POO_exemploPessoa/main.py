from pessoa import Pessoa

p1 = Pessoa('Luiz', 31)
p2 = Pessoa('João', 9)

p1.comer('maçã')
p1.falar('Que fruta boa!')
p1.parar_comer()
p1.parar_comer()
p1.falar('Que fruta boa!')
p1.comer('mamão')

print('\n')
p2.comer('sorvete')
p2.falar('lalalalaa')

print('\n')
print(p1.ano_atual)
print(Pessoa.ano_atual)

print('\n')
print('O ano de nascimento do', p1.get_name(), 'é:', p1.get_ano_nascimento())



print('\n')
# Tutorial disponível no YouTube, pelo canal 'Otávio Miranda'
# Vídeo aula do tutorial: https://www.youtube.com/watch?v=RLVbB91A5-8&list=PLbIBj8vQhvm34qAAEEH_PdL2tMG9rz-P7&ab_channel=Ot%C3%A1vioMiranda
