"""
class Pessoa:
    def falar(self):
        print('Pessoa está falando...')"""


from datetime import datetime


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y')) #curiosidade: o y(minusculo) vai pegar apenas os dois ultimos digitos da data
    #variavel da classe, ou seja, todos os objetos dessa classe terão essa variavel, inclusive a classe em sí.
    #atributo da classe e não da instancia em sí.

    def __init__(self, nome, idade, comendo=False, falando=False): #metodo especial do proprio python. O self referencia a propria instancia do objeto (ao proprio objeto) que está sendo recebida
        #O parametro self deve ser enviado obrigatoriamente.Esse parametro poderia ter outro nome, mas por conveção, utiliza-se o self.
        #Os outros, eu que escolho passar. O self não precisa ser enviado porque ele já enviado automaticamente pelo python
        #variaveis de instancia(atributos)
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

        #o self nesse caso é parecido com o this no java

        #variavel = 'valor'
        #print(variavel)
        #Essa variavel é valida, porém ela só é valida no metodo __init__ (esse)
        #Se tiver outro metódo, ele não vai ter acesso a essa variavel ali

    """def outro_metodo(self):
        #print(variavel) #vai dar erro porque essa variavel não foi definida
        #Obs.: Eu posso usar qualquer uma das variaveis que tem a palavra self dentro desse metodo(outro_metodo)
        print(self.nome)"""

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True


    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False



    def comer(self, alimento):
        if self.comendo: #Vai cair aqui se for True. No caso de eu passar outro alimento e meu objeto já tenha "comido"
            print(f'{self.nome} já está comendo.')
            return
            #vai parar aqui e não vai executar nada mais

        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

        #Como o self é automaticamente passado, só começamos a "contabilizar" valores a partir do proximo parametro. Nesse caso: alimento
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True


    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False


    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
        #para utilizar a variavel da classe, precisa usar o self tbm
    #esse metodo utiliza um atributo da classe e um atributo da instancia.
