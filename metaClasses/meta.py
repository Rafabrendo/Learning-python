"""
EM PYTHON TUDO É UM OBJETO: incluindo classes
Metaclasses são as  "classes" que criam classes.
type é uma metaclasse (!!!???)

"""

""" Classe como molde em linguagens
class A:
    attr = 'Valor'
    
a = A()
b = A()
c = A()"""


"""class A:
    def fala(self):
        self.b_fala()

class B(A):
    #def b_fala(self):
    #    print('Oi')
    pass


b = B()"""
#b.fala() #Estou chamando um metodo da classe pai, que vai chamar o metodo da classe filha
#Se o metodo não existir, vai dar erro.








#criando uma meta classe #Posso usar type para criar classes
"""class Meta(type):
    def __new__(mcs, name, bases, namespace):
        #msc -> metaclasse; name-> nome da classe que está sendo criada; bases ->as classes pai(s) das classes que estão sendo criadas
        #namespace -> todo atributo de classe e todo metodo que é ctriado naquela classe
        #type para criar classes
        #print(name)
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace) #criei uma meta classe aqui

        #não vou ver nada de 'A' porque eu estou retornado(matando) ela ali. Só vou ver coisas das filhas de 'A'
        #print(namespace) #{'__module__': '__main__', '__qualname__': 'B', 'teste': 'Valor', 'sei_la': <function B.sei_la at 0x0000011B132C56C0>}

        if 'b_fala' not in namespace:
            print(f'Oi, você precisa criar o metodo b_fala em {name}')
        else:
            if not callable(namespace['b_fala']):
                print(f'b_fala precisa ser um método, não um atributo em {name}')


        #De todo jeito eu tenho que retornar isso para criar a nova classe
        return type.__new__(mcs, name, bases, namespace) #criei uma meta classe aqui



#Toda classe que herdar de A, incluindo a A, vai se comportar da maneira que eu configurar na meta classe. #Posso fazer coisas especificas
#como exemplo: forçar que o metodo b_fala(self) tenha sido criado na class B
class A(metaclass=Meta):
    def fala(self):
        self.b_fala()

class B(A):
    teste = 'Valor'
    #b_fala = 'Wow' #criei um atributo ao invés de um metodo #Só pra passar na primeira(if), mas vai ser chamado no else
    #pass
    def b_fala(self):
        print('Oi')
    def sei_la(self):
        pass




b = B()
"""

"""
class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'attr_classe' in namespace:
            #pass
            print(f'{name} tentou sobrescrever o atributo.')
            del namespace['attr_classe'] #toda vez que alguem criar o attr_classe, eu vou excluir ele do namespace da classe
            #mesmo o pycharm falando que sobreescreveu, nesse caso, não sobreescreveu porque eu apaguei ele no meio do caminho


        #De todo jeito eu tenho que retornar isso para criar a nova classe
        return type.__new__(mcs, name, bases, namespace) #criei uma meta classe aqui




class A(metaclass=Meta):
    attr_classe = 'Valor A'
    #Se eu não quiser q attr_classe seja sobreescrevido, eu posso configurar isso na meeta classe


class B(A):
    attr_classe = 'Valor B'

class C(B):
    attr_classe = 'Valor C'


b = B()
print(b.attr_classe) #dps que eu apaguei a sobreescrita, vai aparecer o "Valor A"
c = C()
print(c.attr_classe) #Valor A"""


class Pai:
    nome = 'Teste'



#Utilizando type para criar classes

"""A = type(
    'A',
    (),
    {
        'attr': 'Olá mundo'
    }
)"""
#name -> nome da classe; base -> não herda de lugar nenhum (); namespace -> attr : olá mundo


#vou passar a classe Pai como classe pai. Daí a metaclasse vai herdar da classe pai
A = type(
    'A',
    (Pai,),
    {
        'attr': 'Olá mundo'
    }
)


a = A()
"""print(a.attr) #Olá mundo
print(type(a)) #<class '__main__.A'>"""
print(a.nome) #Teste
