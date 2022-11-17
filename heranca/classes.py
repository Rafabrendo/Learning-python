"""
Ao invés de usar o extends como no java, é só passar a superclasse como parametro nas outras classe
A herança é de cima pra baixo na hierarqui. Para alterar isso tem que fazer o casting(downcasting/upercasting)
"""


class Pessoa:
    #Essa é a superclasse(classe principal)
    #Essa classe que definiu os metodos principais
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__
        #vou pegar o nome da classe que está sendo usada no momento


    def falar(self):
        print(f'{self.nomeclasse} Falando...')




class Cliente(Pessoa):
    #subclasse
    #é a mesma coisa que extends. Herdando tudo que tem dentro de Pessoa
    #Essa classe herda, mas tbm tem suas especificidades

    def comprar(self):
        print(f'{self.nomeclasse} comprando...')




class Aluno(Pessoa):
    #subclasse
    def estudar(self):
        print(f'{self.nomeclasse} estudando...')