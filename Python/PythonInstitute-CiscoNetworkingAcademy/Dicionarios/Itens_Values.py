#  .items():

#  Outra forma é baseada na utilização de um método de dicionário chamado items().
#  O método devolve tuples (este é o primeiro exemplo onde os tuples são algo mais do que apenas um exemplo de si mesmos)
#  onde cada tuple é um par key-value.

# É assim que funciona:
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for english, french in dictionary.items():
    print(english, "->", french)


# .values():

# Há também um método chamado values(), que funciona de forma semelhante a keys(), mas devolve valores.
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval", "cachorro":"teste"}

for french in dictionary.values():
    print(french)
