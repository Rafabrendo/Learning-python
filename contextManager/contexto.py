#como o gerenciador de contexto não é preciso usar o .close()
#mtas das vezes, as pessoas esquecem de fechar o arquivo. Para corrigir esse problema, a galaera do python criou o gerenciador de
#arquivos que corrige esse problema
#Isso serve para uma serie de coisas que se precisa abrir e fechar, pode ser arquivos ou outras coisas. Para capturar e liberar tbm
"""
#Esse é um modo de criar gerenciador de contexto
class Arquivo:
    #Esse é um protocolo de gerenciador de contexto
    def __init__(self, arquivo, modo):
        print('Abrindo arquivo')
        self.arquivo = open(arquivo, modo)



    def __enter__(self):
        #metodo de entrada(vai retornar o arquivo)
        print('retornando arquivo')
        return self.arquivo


    def __exit__(self, exc_type, exc_val, exc_tb):
        #metodo de saida(onde o arquivo é fechado)
        print('Fechando arquivo')
        self.arquivo.close()
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        return True
    #Só de colocar o return True,a exceção não vai ser levantada, isso assumindo que se tenha tratado as exceções, de alguma maneira.
"""


#arquivo = open('abc.txt', 'w')
#arquivo.write('Alguma coisa')
#arquivo.close() #as vezes, as pessoas esquecem de fechar .close(). Daí é melhor usar o gerenciador de contexto


#Isso aqui é um gerenciador de contexto(padrão)
"""with open('abc.txt', 'w') as arquivo:
    arquivo.write('Alguma coisa')
    #como o gerenciador de contexto não é preciso usar o .close()"""

#Ao inves de passar open, normalmente, eu faço uma classe, como está ali em cima, e nessa classe eu abro, escrevo e fecho o arquivo
#"automaticamente"
#obs.: o open fecha "automaticamente". Isso de criar é para o caso do operador estiver fazendo algo que não tenha suporte.
#daí no with, eu passo o nome da Classe, que nesse caso é o Arquivo
#with Arquivo('abc.txt', 'w') as arquivo:
    #arquivo.write('Alguma coisa')
    #arquivo.sfasfa('Alguma coisa')
    #chamei um metodo que não existe nessa classe e por isso vai dar erro


#outro jeito de criar gerenciador de contexto:
from contextlib import contextmanager
#daí não é necessario utilizar a classe
#a função precisa ser decorada com o @contextmanager
@contextmanager
def abrir(arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(arquivo, modo)
        #se eu usar o return, a função vai parar aqui. Por isso eu utiligo o yield
        yield arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()


#vou passar, dps do with, o nome da função
with abrir('abc.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')



