class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        #protected
        self._ligado = False


    def ligar(self):
        if self._ligado:
            return
        self._ligado = True
        #Mudei o status da variavel do atributo de instancia ligado


    def desligar(self):
        if not self._ligado:
            #Lembre-se que o not troca o valor
            return
        self._ligado = False


