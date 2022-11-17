"""
composição -> "Tem-um, Tem-vários"
uma classe vai ser dona da outra
"""

from classes import Cliente

"""
não preciso importar o Endereco porque a classe Cliente está responsável por instanciar o endereço"""

cliente1 = Cliente('Rafael Brendo', 24)
cliente1.insere_endereco('Brasília', 'DF')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1  #Apaguei o meu objeto cliente1 e tudo que tinha nele
print()


cliente2 = Cliente('Maria', 55)
cliente2.insere_endereco('Salavador', 'BA')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()

cliente3 = Cliente('João', 19)
cliente3.insere_endereco('São Paulo', 'SP')
print(cliente3.nome)
cliente3.lista_enderecos()
del cliente3
print()


print('###' *30)
"""
aqui vai mostrar o Garbage Collector. Porém, se eu apagar os objetos antes, não vai mostrar, porque vai ser retirado da memória.
Isso por causa da Composição.
Todos os objetos morrem se a classe principal(que contém) morrer.
"""
