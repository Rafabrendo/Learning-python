from heranca.tiraDuvidas.bibliotecas import Biblioteca


#vai herdar de Biblioteca
class Interface(Biblioteca):
    def metodo_da_interface(self):
        print('Sou o metodo da interface.')
