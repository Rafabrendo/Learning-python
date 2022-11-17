
class A:
    vc = 123 #É uma variavel da classe que está disponivel para todas as instancias dessa classe
    #variavel de classe

    def __init__(self):
        pass
        #self.vc = 321 #variavel de instancia



#Se tem duas instancias que estão sendo inicializadas, as duas instancias terão o valor vc(321) do construtor
#E só a classe tera o valor da variavel de classe vc(123)

a1 = A()
a2 = A()

A.vc = 'Alterado'

#A.vc = 321 #mudei minha variavel de classe. #Mudei para todas as instancias
#Estou usando a classe para alterar o valor dessa classe

#a1.vc = 321 #Nesse caso, ele não vai alterar o valor da variavel da classe, mas sim, estou criando um atributo direto na minha instancia
#

print(a1.__dict__) #{'vc': 321}
print(a2.__dict__) #{}
print(A.__dict__)

#__dict__ -> quando executa direto da instancia, primeiro o interpretador do python vai procurar na instancia se a classe existe
#se ela existir, ele já vai exibir o valor dela. Se ela não existir na instancia, ele já vai procurar na classe em sí.



print(a1.vc)
print(a2.vc)
print(A.vc)