# #variavel 
# nome = 'John Connor'

# #separa o string em uma lista
# nome_completo = nome.split(' ')
# #nao escolho o separadador, tem que indicar o que esta separando o nome na lista, no exemplo é o espaço ' ' que separa os dois nomes

# nome_completo = nome.capitalize()


# for parte_nome in nome_completo:
#     print(parte_nome, end=' ')
#     #end=' ' elimina quebra de linha, ficam na mesma linha os itens da lista


##################################################
#usuario informa o nome 
nome = input('Informe seu nome completo: ')

#separa as palavras do nome
nome_lista = nome.split(' ')

#capitular as palavras do nome
for i in range(len(nome_lista)):
    nome_lista[i] = nome_lista[i].capitalize()
    print(nome_lista, end=' ')

    
#junte o nome em uma variavel
nome_completo = ' '.join(nome_lista)

#exibe na tela
print(nome_completo)
