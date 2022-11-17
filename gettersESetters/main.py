
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


    def desconto(self, percentual):
        self.preco = self.preco - (self.preco*(percentual / 100))


    @property
    def nome(self):
        return self._nome



    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()



    #Getter
    @property
    def preco(self):
        return self._preco
        #Posso retornar qualquer nome, mas por convesão, eu pego o nome do atributo e adiciono uma underline no começo
        #_preco


    #Setter
    #Vai configurar o preço. Sempre que eu tentar atribuir um valor no preço. Primeiro ele vai passar no setter e dps ele vai pro preço
    #tem que usar o @ + nome da propriede que eu quero + .setter
    #o valor de parametro vai ser o q vai ser atribuido na variavel lá
    #como eu passei um valor de string e preciso de um inteiro ou float eu vou precisar fazer algumas condições
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str): #Eu vou checar se o valor que estou recebendo é uma instancia de string. Se for, daí eu validar o meu valor
            valor = valor.replace('R$', '')
            valor = float(valor)

        self._preco = valor





p1 = Produto('CAMISETA', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produto('CANECA', 'R$15') #Assim daria erro. Então eu faço eu getter e um setter
p2.desconto(10)
print(p2.nome, p2.preco)

