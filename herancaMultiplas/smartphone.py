"""
python file -> modulo
vai herdar a classe Eletronico
"""

from eletronico import Eletronico
from log import LogMixin

class Smartphone(Eletronico, LogMixin):
#A partir de agora, que eu passei LogMixin como herança, eu tenho as suas funcionalidades
# tudo que está na classe Eletronico, está aqui tbm

# Preciso dos mesmos parametros da superclasse
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False


    def conectar(self):
        if not self._ligado:
            error = f'{self._nome} não está ligado.'
            print(error)
            self.log_error(error)
            return

        if self._conectado:
            error = f'{self._nome} JÁ ESTÁ CONECTADO'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} ESTÁ CONECTADO'
        print(info)
        self.log_info(info)
        self._conectado = True




    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} não está conectado.'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} foi desligado com sucesso.'
        print(info)
        self.log_info(info)
        self._conectado = False



