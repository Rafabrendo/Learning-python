"""
Polimorfismo é o principio que permite que classes derivadas de uma mesma superclasse tenham métodos iguais
(de mesma assinatura) mas comportamentos diferentes.
Mesma assinatura = mesma quantidade e tipo de parâmetros

obs.: Utuilizei na aula anterior(classes abstratas)
"""

from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def fala(self, msg): pass


class B(A):
    def fala(self, msg):
        print(f'B está falando {msg}')

class C(A):
    def fala(self, msg):
        print(f'C está falando {msg}')


b = B()
c = C()

b.fala('UM ASSUNTO')
c.fala('Outro assunto')




