# Tutorial disponível no YouTube, pelo canal 'Otávio Miranda'
# Vídeo aula do tutorial: https://www.youtube.com/watch?v=gHrc6FLBh20&ab_channel=Ot%C3%A1vioMiranda


# um objeto “iterável”, ele é qualquer tipo de coisa que você consegue realizar um laço sobre, por exemplo, um array, um objeto, uma sequencia de números, uma stream, ou qualquer coisa
# por: Santos, Lucas. | https://medium.com/trainingcenter/iterators-em-javascript-880adef14495#:~:text=Se%20voc%C3%AA%20ainda%20n%C3%A3o%20entendeu,uma%20stream%2C%20ou%20qualquer%20coisa.



lista = [0, 1, 2, 3, 4, 5]
String = 'String'
Numeros = 1, 2, 3, 4

print(hasattr(lista,'__iter__')) # Confirmando que a lista é um objeto iteravel
print(hasattr(String,'__iter__')) # String é um objeto iteravel
print(hasattr(Numeros,'__iter__')) # Números não são iteraveis

# Se é objeto iteravel, podemos utilizar o 'for'
