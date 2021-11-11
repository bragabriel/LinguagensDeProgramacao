# Substituindo/Alterando um valor no dicionário: 
# vamos substituir o valor "chat" com "minou", o que não é muito preciso, mas funcionará bem com o nosso exemplo.

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['cat'] = 'minou'
print(dictionary)


# Adicionando uma nova chave: 
# basta atribuir um valor a uma nova chave, previamente inexistente.

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary['swan'] = 'cygne'
print(dictionary)



# Inserindo um item de outra forma: Método .update()

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary.update({"duck": "canard"})
print(dictionary)


# Removendo um item da chave:
# Nota: remover uma chave causará sempre a remoção do valor associado. Valores não podem existir sem as suas chaves.
# Isto é feito com a del instrução.

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

del dictionary['dog']
print(dictionary)



#Para remover o último item num dicionário, pode-se utilizar o método popitem() :

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary.popitem()
print(dictionary)    # outputs: {'cat': 'chat', 'dog': 'chien'}

#Nas versões mais antigas do Python, ou seja, antes do 3.6.7, o método popitem() remove um item aleatório de um dicionário.