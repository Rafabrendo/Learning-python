"""
Associação -> Usa  | Agregação -> Tem  | Composição -> É dono  | Herança ->  Um objeto é outro objeto(herda)
"""

from classes import *



c1 = Cliente('Rafa', 24)
print(c1.nome)
c1.falar()
c1.comprar()
print()

a1 = Aluno('Brendo', 24)
print(a1.nome)
a1.falar()
a1.estudar()
print()

p1 = Pessoa('Rafa', 54)






