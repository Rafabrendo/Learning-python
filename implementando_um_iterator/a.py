"""
Uma introdução a estrutura de dados 

Recriando parte do protocolo do iteraitor

"""


from os import remove


class MinhaLista:
    def __init__(self) -> None:
        self.__items = []
        self.__index = 0

    
    def add(self, valor):
        self.__items.append(valor)
    
    def __setitem__(self, index, valor):
        if index >= len(self.__items):
            self.__items.append(valor)
            #vou adicionar um valor novo, dependendo do indice que foi enviado
            #tem que ser enviado o indice da 'proxima casa'
        self.__items[index] = valor
    
    #obs.: Aqui eu não chequei se existe. Eu apenas implementei
    def __delitem__(self, index):
        del self.__items[index]


    def __getitem__(self, index):
        try:
            return self.__items[index]
            #vai pegar um elemento da minha lista
        except IndexError:
            raise StopIteration
    
    def __iter__(self):
        return self
        #o iterador da classe é a propria classe, nesse caso.
        #o iter vai dizer qual é o iterador da classe
    
    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item 
        except IndexError:
            raise StopIteration
            #Na hora que eu levantar essa exceção, eu estou 'falando' pro for pra parar a interação


    
    def __str__(self):
        return f'{self.__class__.__name__}({self.__items})'
        #quando eu der um print na classe. Vai retornar o nome da classe
        #{self.__class__.__name__} -> vai mostrar o nome da lista, nesse caso 'MinhaLista'
        #({self.__items}) -> vai mostrar os items da minha lista

    def __repr__(self):
        #seria representação para desenvolvedores
        return self.__str__()





#Essa aula vai funcionar com lista. Mas posso mudar algumas coisas e utlizá-la em tuplas e dicionarios 
if __name__ == "__main__":
    lista = MinhaLista()
    lista.add('Rafael')
    lista.add('Brendo')
    
    #lista = list(lista)
    #Agora a minha lista passar a ser uma lista normal 
    #agora posso fazer dois ou mais for's numa lista


    #print(lista)
        
   
    #for valor in lista:
       # print(valor)


    #print(next(lista)) #Rafael
    #print(next(lista)) #Brendo


    print(lista[0])
    #um metodo para obter o valor é o __getitem__
    print(lista[1])

    lista[0] = 'Rafa' 
    #Eu usei o __setitem__ para mudar o valor
    print(lista[0])

    lista[2] = 'Rafildes'
    print(lista)

    del lista[2]
    print(lista)

    #print(next(lista))

    for valor in lista:
        print(valor)