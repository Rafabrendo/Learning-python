"""
No python, o comportamento dos operadores é definido por métodos especiais.
Vamos alterar o comportamento de operadores com classes definidas pelo usuário.

Operador    Método          Operação
------------------------------------------------------
+           __add__         adição
-           __sub__         subtração
*           __mul__         multiplicação
/           __div__         divisão
//          __floordiv__    divisão inteira
%           __mod__         Módulo
**          __pow__         Potência
+           __pos__         Positivo
-           __neg__         Negativo
<           __lt__          Menor que
>           __gt__          Maior que
<=          __le__          Menor ou igual a
>=          __ge__          Maior ou igual a
==          __eq__          Igual a
!=          __ne__          Diferente de
<<          __lshift__      Deslocamento para a esquerda
>>          __rshift__      Deslocamento para a direita
&           __and__         E bit-a-bit
|           __or__          OU bit-a-bit
^           __xor__         OU exclusivo bit-a-bit
~           __inv__         inversão
"""

class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        return self.x * self.y


    #<__main__.Retangulo object at 0x00000220D78E7E50> -> agr eyu vou mudar esse comportamento com outro metodo magico
    #vou mudar a saida
    def __repr__(self):
        return f"<class 'Retangulo({self.x}, {self.y})'>"
    #Agr, quando eu der um print no objeto, é esse metodo que vai ser executado
    #<class 'Retangulo(20, 40 )'> #vai ter um triangulo novo com a soma

    def __add__(self, other):
        novo_x = self.x + other.x  #vai somar os dois x(s) dos retangulo e pegar o resultado e inserir na variavel novo_x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)
        #Nesse caso, tá criando um novo objeto na classe (factore metody)

    #lt less than(menor que)
    def __lt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 < a2:
            return True
        else:
            return False

    def __gt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()

        if a1 > a2:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False




r1 = Retangulo(10, 20)
r2 = Retangulo(10, 20)
r3 = r1 + r2 #x+x, y+y
#print(r1 + r2)
#esse operador de + vai chamar a função __add__ que eu criei.
print(r3)
print(r3 > r1)
print(r3 < r1)
#print(r1 == r2) #False #Eles são iguais, mas deu falso porque não passei o operador como metodo
#Agr eu passei o operador como função(metodo na classe)
print(r1 == r2) #True


