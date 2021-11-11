import math

angulo = float(input('Digite o ângulo que você deseja: '))

# Pegar o angulo, converter para radianos, e calcular o seno dele(usando radianos).
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))

cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))

tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem o tangente de {:.2f}'.format(angulo, tangente))