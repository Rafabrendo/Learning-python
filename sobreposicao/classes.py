"""
A sobreposição acontece muito em construtores. Se eu tivesse feito construtores em Cliente ou ClienteVIP, eu estaria
sobreescrevendo o construtor de Pessoa
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


    def falar(self):
        print('Estou em CLIENTE.')



class ClienteVIP(Cliente):
    #ClienteVIP que herda de Cliente, que herda de Pessoa
    #Tudo que tem em Pessoa e em Cliente, tem em ClienteVIP. ClienteVIP tbm é uma pessoa

    #Sobreposição. Podemos sobrepor metodos/membros da classe(atributos de classe/ de instancia e metodos)


    # Sobreposição do metodo(falar) que está na classe Pessoa
    """def falar(self):
        print('Outra coisa qualquer.')"""

    #Um jeito de chamar o metodo da classe pai é usar o super(), que se refere a super classe, que no caso é a classe Pessoa
    #e sobreescrever
    """def falar(self):
        super().falar()
        #vai executar primeiro o metodo falar() de Pessoa e dps vai executar essa classe(falar de ClienteVIP)
        print('Outra coisa qualquer.')"""

    """def falar(self):
        super().falar()
        #vai executar primeiro o metodo falar() de Cliente e dps vai executar essa classe(falar de ClienteVIP)
        #POrque esse metodo existe lá. Vai executar em cadeia e na primeira que ele achar, ele vai parar
        print('Outra coisa qualquer.')"""


    """def falar(self):
        Pessoa.falar(self)
        #vai executar primeiro o metodo falar() de Pessoa e dps vai executar essa classe(falar de ClienteVIP)
        #Isso porque eu expecifiquei em qual super classe procurar o metodo e sobreescrever, e tenho que mandar os mesmos argumentos. No
        #caso só tem self lá no metodo Pessoa.falar(), então eu vou mandar esse aqui tbm
        print('Outra coisa qualquer.')"""

    """def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self) #Ou posso usar o super() #vai ter os metodos(falar) das outras classe (Pessoa, Cliente)
        #super().falar()
        print('Outra coisa qualquer.')"""

    #Definindo outros construtores
    #Posso copiar e colar tudo que tinha lá, ou apenas chamar. Assim:
    #Isso vai sobrepor -> vai ter duas opçoes para isso: reescrever o construtor de Pessoa ou chamar o construtor de Pessoa
    #vou chamar o metodo que já está pronto. Daí eu escrevo menos código. Daí eu tenho que receber os mesmo parametros do construtor de Pessoa
    #Obs.: Posso passar mais paramentros
    #Isso é para o caso de haver varios construtores
    def __init__(self, nome, idade, sobrenome):
        #super().__init__(nome, idade)
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome #Estou pegando o valor do argumento sobrenome
        #Estou chamando o construtor da superclasse
        """
        Se eu tivesse uma cadeia de construtores e quisesse chamar um construtor em especifico
        eu tenho que passar o nome da classe.__init__(self(como primeiro argumento),argumentos que estão lá), ao invés de super().
         Ex.:
         Pessoa.__init__(self, nome, idade)"""


    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        #Olha pro self.nome -> eu estou chamando ele, do construtor da classe Pessoa
        print(f'{self.nome} {self.sobrenome}')
