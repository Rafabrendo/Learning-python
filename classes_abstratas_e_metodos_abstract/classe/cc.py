from classes_abstratas_e_metodos_abstract.classe.conta import Conta

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite
        #POr padrão o limite começa com 100. Mas posso passar outros valores.


    @property
    def limite(self):
        return self._limite


    
    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente')
            return

        self.saldo -= valor
        self.detalhes()




