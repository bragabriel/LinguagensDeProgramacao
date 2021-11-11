largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(largura, altura, (largura*altura)))
#A cada 2m² precisa de 1l de tinta
print('Para pintar essa parede, você precisará de {}l de tinta.'.format((largura*altura)/2))