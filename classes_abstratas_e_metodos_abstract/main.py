"""
Uma classe abstrata são classe que não podem ser instanciadas.
É uma forma de garantir herança total: Somente subclasses não abstratas podem ser instanciadas, mas nunca a superclasse abstrata.
Podem ter metodos abstratos e metodos concretos.
Um metodo abstrato é um metodo que não tem corpo. As classe filhas, que herdam esse(s) metodos, são obrigadas a criar esses metodos

"""
#Para criar uma classe abstrata em python: Tem que ir na biblioteca abc(abstract basic class) e importar o decorador
#abstractmethod
#obs.: Tem outros jeitos tbm

"""from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def falar(self):
        pass
#Criei a classe A e herdei de ABC
#todas as classe filhas de A, vai ter determinado metodo, por exemplo falar()
#Ele é um metodo abstrato


class B(A):
    #Estou sobrepondo o metodo abstrato de A
    def falar(self):
        print('Falando... B...')



a = B()
#Estou instanciando a classe
a.falar()"""


from classe.cp import ContaPoupanca
from classe.conta import Conta

cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(10)
cp.sacar(5)
cp.sacar(5)
cp.sacar(5)

#Não se pode instanciar a conta. vai dar erro:
#conta = Conta(1111, 2222, 0)
print('###'*30)

from classe.cc import ContaCorrente
cc = ContaCorrente(agencia=1111, conta=3333, saldo=0, limite=500)
cc.depositar(100)
cc.sacar(250)
cc.depositar(1000)

