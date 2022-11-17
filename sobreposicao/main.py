"""
Associação -> Usa  | Agregação -> Tem  | Composição -> É dono  | Herança ->  Um objeto é outro objeto(herda)


Sobreposição -> Reescrever dentro de outra classe.
Só pode acontecer com Herança
"""

from classes import *

c1 = Cliente('Rafa', 24)
print(c1.nome)
c1.comprar()
print()

c2 = ClienteVIP('Rafildes', 25, 'Brendo')
c2.falar()


