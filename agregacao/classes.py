"""
Agregação -> Ocorre quando uma classe usa outras classe em suas operações. As classe participam da classe principal,
mas, a classe principal não contém estas classe utilizadas como suas.
Onde as classe podem existir sozinhas, mas precisam umas das outras.
"""


class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []
        #como eu já ia passar uma lista, eu a passei vazia


    def inserir_produto(self, produto):
        self.produtos.append(produto)


    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)


    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total





class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
