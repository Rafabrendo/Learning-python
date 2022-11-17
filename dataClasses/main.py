"""
O módulo Dataclasses fornece um decorador e funções para criar automaticamente métodos, como __init__(),
__repr__(), __eq__(etc) em classes definidas pelo usuário.
Basicamente, dataclasses são syntax sugar para criar classes normais.
Foi originalmente descrito na PEP 557.
Adicionado na versão 3.7 do python.
Leia na documentação: docs.python.org/pt-br/3/library/dataclasses.html

Padrão do dataclass:
dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False, match_args=True,
kw_only=False, slots=False, weakref_slot=False)

"""
"""
from dataclasses import dataclass

#Ao invés de eu escrever init, au apenas importo o dataclass(que gera codigo automaticamente) e decoro a minha classe

#Aqui tem uma classe pronta
@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


p1 = Pessoa('Rafa', 'Brendo')
print(p1) #Pessoa(nome='Rafa', sobrenome='Brendo')
print(p1.nome)
print(p1.sobrenome)
print(p1.nome_completo)
"""


"""
#Se eu precisar utilizar o metodo init, eu posso desativar ele na dataclass e dps monta-lo normalmente
#ou eu posso chamar o metodo __post_init__()

from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    #vai ser executado logo dps do init
    def __post_init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'


    #@property
    #def nome_completo(self):
    #    return f'{self.nome} {self.sobrenome}'



p1 = Pessoa('Rafa', 'Brendo')
p2 = Pessoa('Rafa', 'Brendo')

print(p1 == p2) #Deu True porque eles são iguais, porque tem valores iguais
print(p1)
print(p1.nome)
print(p1.sobrenome)
print(p1.nome_completo)

"""



#desativando o repr(que vai mostrar o objeto como uma string, ao invés da referencia na memoria), eq e
#Se eu passar init como False, eu teria que criar o init na classe, normalmente
#frozen = False -> o frozen por padrão é False. Quando passado True, não vai permitir editar a classe. Nem criar e nem apagar.
#cria uma classe imutavel(em True)
#order -> Se true, eu posso ordenar os objetos. Posso fazer uma lista de, nesse caso Pessoa, ordenadas. Para isso o eq tem que ser
#true tbm e init tem q ser true ou deve-se fazer um init

from dataclasses import dataclass
from dataclasses import field
from dataclasses import asdict, astuple
#para converter a classe para tuplas ou dicionarios


@dataclass(eq=True, repr=True, order=True, frozen=False, init=True) #olhar na documentação
class Pessoa:
    nome: str
    sobrenome: str = field(repr=False)  #default='Wow' para se eu não mandar o argumento
    #field(repr=False) -> não vai mostrar o sobrenome

    #vai ser executado logo dps do init  #se o frozen=True -> esse metodo daria erro. Levantaria uma exceção
    def __post_init__(self):
        #self.nome_completo = f'{self.nome} {self.sobrenome}'
        #Seu eu quiser forçar criar uma pessoa com um determinado tipo, eu faço aqui, no post_init
        if not isinstance(self.nome, str):
            #se eu mandar o tipo errado pra nome, entraria na exceção que eu criei
            raise TypeError(
                f'Tipo inválido {type(self.nome).__name__} != str em {self}'
            )


    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'




"""p1 = Pessoa('A', 'Brendo')
p2 = Pessoa('C', 'Brendo')
p3 = Pessoa('D', 'Brendo')
p4 = Pessoa('B', 'Brendo')"""

p1 = Pessoa('A', '5')
p2 = Pessoa('C', '3')
p3 = Pessoa('D', '4')
p4 = Pessoa('E', '6')


pessoas = [p1, p2, p3, p4]
print(sorted(pessoas, key=lambda pessoa: pessoa.sobrenome))
#[Pessoa(nome='C', sobrenome='3'), Pessoa(nome='D', sobrenome='4'), Pessoa(nome='A', sobrenome='5'),
#Pessoa(nome='B', sobrenome='6')]
#lambda recebendo pessoa:(retornando) pessoa.sobrenome

print(sorted(pessoas, key=lambda pessoa: pessoa.sobrenome, reverse=True))
#[Pessoa(nome='B', sobrenome='6'), Pessoa(nome='A', sobrenome='5'), Pessoa(nome='D', sobrenome='4'),
#Pessoa(nome='C', sobrenome='3')]




#print(p1 == p2) #False
#print(p1) #dps q eu desativei o repr #<__main__.Pessoa object at 0x000001FAD6A27FD0>
#print(p1.nome)
#print(p1.sobrenome)
#print(p1.nome_completo)


print(asdict(p1)) #{'nome': 'A', 'sobrenome': '5'}
print(astuple(p1)) #('A', '5')