"""
herança multiplas -> problema (Diamond Problem)
A primeira classe que eu herdei é a primeira que o interpretador busca

Classe mixin -> Não é uma classe abstrata. Ela não foi feita para ser instanciada diretamente. Ela possui uma funcionalidade
adicional, que se quer adicionar em outra classe. Porém, essa classe não está presente na hierarquia de classe.
"""

"""
class A:
    def falar(self):
        print('Falando... Estou em A.')



class B(A):
    #Sobreposição
    def falar(self):
        print('Falando... Estou em B.')


class C(A):
    def falar(self):
        print('Falando... Estou em C')


class D(B, C):
    pass
    
    
    #herança multipla(Ele vai começar a buscar da esquerda para a direita, da classe que estou herdando primeiro
    #No caso, ele vai buscar primeiro em B e dps em C

   def falar(self):
        print('Falando... Estoou em D.')#daí não vai buscar.."""

#d = D()
#d.falar() #Falando... Estou em B. #Ele chamou primeiro o metodo que está em B
#Se ele(Interpretador do python) não encontrar em B, ele vai procurar em C, e se ele não encontrar em C, ele vai procurar em A, porque
#C está herdando de A


#Para importar, eu só preciso da classe de smartphone, porque a de Eletronico já estou importando dentro de smartphone
from smartphone import Smartphone

smartphone = Smartphone('Pocophone F1')
smartphone.conectar()
smartphone.desligar()
smartphone.ligar()
smartphone.conectar()
smartphone.conectar()
smartphone.conectar()
smartphone.desligar()
smartphone.conectar()
smartphone.desconectar()











