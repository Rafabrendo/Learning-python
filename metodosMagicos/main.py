"""
https://rszalski.github.io/magicmethods/
metodos magicos-> são aqueles que tem dois underlines no começo e no fim. Eles modificam o comportamento da sua classe.
Tem-se varios metodos magicos
São chamados de dunders (dois underlines)
"""

class A:
    #__new__ é o "cara" que constroe a classe
    """
    def __new__(cls, *args, **kwargs):
          #Esses são apenas exemplos para mostrar o q se pode fazer já no construtor da classe
        #Pode se usar design patterns(padrões de objetos) e nesse padrão, só se terá uma instancia desse objetos no programa
        ##todo. Isso vai ser mto utel para banco de dados
        #print('Eu sou o new')
        #cls.nome = 'Rafael Brendo' #Esse é um atributo de classe, dentro do new
        def haha(*args, **kwargs):
            print('Fala OI')

        cls.haha = haha

        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = object.__new__(cls)


        #return super().__new__(cls)
        #return object().__new__(cls)
        return cls._jaexiste
        #Em pythontodas as classes derivam de object e por isso o super(). é a mesma coisa que falar
        #object."""

    def __init__(self):
        #print('Eu sou o INIT')
        #__init__ é um dos metodos magicos em python
        #a primeira coisa q é chamada é o __new__ e por isso ele é construtor
        pass

    #Esse metodo __call__ faz a nossa classe se comportar como uma função.
    """def __call__(self, *args, **kwargs):
        #print(args)
        #print(kwargs)

        resultado = 1

        for i in args:
            resultado *= i

        return resultado"""

    """def fala_oi(self):
        print('Oi')

    def __setattr__(self, key, value):
        #toda vez q configurar um atribute novo na classe, o __setattr__ vai ser chamado.
        #print(key, value)
        #self.__dict__[key] = value
        if key == 'nome':
            #isso é para se alguém tentar acessar o atributo nome
            self.__dict__[key] = 'Você não pode fazer isso'
        else:
            self.__dict__[key] = value"""

    #def __del__(self):
      #  print('Objeto coletado.')
        #Esse metodo vai ser chamado toda vez que o garbage collector estiver funcionando.

    #def __str__(self):
        #return 'Essa é a class A criada para tal coisa'
        #return "<class 'A'>"
    #Toda vez que eu tentar utilizar a classe como uma string. Daí esse metodo vai ser retornado


    def __len__(self):
        return 55
    #esse é o metodo que é executado quando eu chamo a função len()



a = A()
#print(type(a))
#print(a.nome)
#a.haha() #Quando eu faço isso, sem passar o "*args, **kwargs" lá nos metodos da função, ele vai mandar, automaticamento
#o parametro self, implicitamento. Para resolver isso e não dá erro, simplesmente é colocado *args, **kwargs lá na função haha
#b = A()
#c = A()
#Em nenhum momentos essas instancias estão sendo diferentes. b é uma copia de a e c é uma copia das outras.

#print(a == b) #a não era pra ser igual a b. Mas como todas as instancias são as mesmas, vai ser
#até porque são objetos e tem que ser diferentes. Mas nesse caso, NÃO!
#print(id(a), id(b), id(c))

#a(1,2,3,4,5, nome='Rafael')#Isso não seria possivel se não tivesse esse metodo __call__, mas como se tem, pode-se chamar
#esses metodos como se fosse uma função normal
"""
(1, 2, 3, 4, 5)
{'nome': 'Rafael'}"""
#variavel = a(1,2,4,5,3,7,8,9,10)
#print(variavel)
#a.nome = 'Rafael Brendo' #Esse atributo não vai ser configurado na classe
#print(a.nome)#Se eu tentar acessar ele, vai dar erro porque eu não configurei ele no init ou setattr
#print(a.nome) #agr vai aparecer porque eu configurei com self.__dect__[key] e passei o value(valor)
"""print(a.nome)
a.qualquer = 225
print(a.nome, a.qualquer)"""

print(a)
print(len(a))

