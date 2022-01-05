from aluno import Aluno

Aluno1 = Aluno()
Aluno2 = Aluno()
Aluno3 = Aluno()

print()
print('=-='*10)
print('Aluno 1:')

Aluno1.set_nome('Gabriel Braga')
Aluno1.set_ra(110080)
Aluno1.set_notaA1(10)
Aluno1.set_notaA2(10)
Aluno1.set_frequencia(100)
Aluno1.calcular_Media()
print('get_nome: ', Aluno1.get_nome())
Aluno1.get_media()
print('\nDados do aluno:')
Aluno1.getDadosAluno()
print('\nSituação do aluno:', end=' ')
Aluno1.situacao_Aluno()

print('=-='*10, '\n')


print('=-='*10)
print('Aluno 2:')

Aluno2.set_nome('Douglas')
Aluno2.set_ra(564232)
Aluno2.set_notaA1(4)
Aluno2.set_notaA2(4)
Aluno2.set_frequencia(80)
Aluno2.calcular_Media()
print('get_nome: ', Aluno1.get_nome())
Aluno2.get_media()
print('\nDados do aluno:')
Aluno2.getDadosAluno()
print('\nSituação do aluno:', end=' ')
Aluno2.situacao_Aluno()

print('=-='*10, '\n')


print('=-='*10)
print('Aluno 3:')

Aluno3.set_nome('Geraldo')
Aluno3.set_ra(458789)
Aluno3.set_notaA1(7)
Aluno3.set_notaA2(6)
Aluno3.set_frequencia(20)
Aluno3.calcular_Media()
print('get_nome: ', Aluno3.get_nome())
Aluno3.get_media()
print('\nDados do aluno:')
Aluno3.getDadosAluno()
print('\nSituação do aluno:', end=' ')
Aluno3.situacao_Aluno()

print('=-='*10, '\n')
