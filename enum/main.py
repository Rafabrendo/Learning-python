"""
https://docs.python.org/pt-br/3/library/enum.html?highlight=enum#module-enum
"""

from enum import Enum, auto
#Posso importar o auto e ao invés de colocar os valores, eu coloco auto e ele gera automaticamente os valores pra mim

class Directions(Enum):
    right = auto()
    left = auto()
    up = auto()
    down = auto()

    """right = 0
    left = 1
    up = 2
    down = 3"""



#Tem varios jeitos de passar a direction. Ex.:typeint, posso checar a instancia é da classe...
def move(direction):
    """if direction != 'right' and direction != 'left':
        raise ValueError('Cannot move in this direction')"""
    if not isinstance(direction, Directions):
        raise ValueError('Cannot move in this direction')

    return f'Moving {direction.name}'
    #.name é o nome do mebro da classe enum
    #se eu passar .value, os valores vão começar com 1
    #com o name, vai mostrar o valor da variavel como o nome dela


if __name__ == "__main__":
    print(move(Directions.right))
    print(move(Directions.left))
    print(move(Directions.up))
    print(move(Directions.down))

    #print(move('qualquer lugar'))
    #print(move('up'))
    #print(move('Down'))


    print()

    for direction in Directions:
        print(direction)
        print(direction.value, direction.name)