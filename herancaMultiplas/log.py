"""

"""

class LogMixin:
    #classe que vai adicionar funcionalidades a outras classe
    @staticmethod
    def write(msg):
        with open('log.log', 'a+') as f:
            f.write(msg)
            f.write('\n')
    """   #Para quebrar a linha no final do arquivo
    #Obs.: dentro desse metodo, em nenhum momento eu utilizo a palavra self. Isso demonstra que esse metodo pode se tornar um metodo estatico
    #já que eu não preciso saber da instancia, no momento
    
    #O python tem um modulo de log só para isso. Esse caso é um exemplo"""

    def log_info(self, msg):
        self.write(f'INFO: {msg}')


    def log_error(self, msg):
        self.write(f'ERROR: {msg}')
