from random import randint

class Pessoa:
    ano_atual = 2022 #variavel da classe

    def __init__(self, nome, idade): #metodo de instancia
        self.nome = nome
        self.idade = idade


    def get_ano_nascimento(self): #metodo de instancia
        print(self.ano_atual - self.idade)


    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento): #metodo de classe
        idade = cls.ano_atual - ano_nascimento #variavel disponivel apenas nesse metodo
        return cls(nome, idade)



    @staticmethod
    def gera_id():   #metodo estatico
        rand = randint(10000, 19999)     #variavel disponivel apenas nesse metodo
        return rand

     #nao precisa nem da instancia e nem da classe
    #É como se fosse uma "função normal"
    #Posso passar parametros, se eu quiser








p1 = Pessoa('Rafa', 32)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gera_id()) #Estou gerando um id para a classe Pessoa
print(p1.gera_id()) #Estou gerando um id para o objeto p1 #Estou chamando esse metodo pela instancia, porém eu não tenho acesso a instancia dentro do meu metodo
#mas vai funcionar normalmente