"""
Protege certas partes do código(esconde-o)

modificadores de acessos:
public, protected, private  -> não tem essas palavras no python

no python: (convenções)
_     -> private/protected obs.: Só que é de maneira mais fraca #Pode ser chamado de protected (que é mais fraquinho)
__    -> priviate(mais forte) obs.: Recomenda-se fortemente que esse não seja acessado
Estou indicando para outros desenvolvedores que não quero, de maneira alguma, que esse atributo/metodo seja acessado

obs.: atributos sem o(s) underline(s) são publicos, por convenção do python

obs.: Se vc ver uma variavel com uma underline, não a acesse


"""


class BaseDeDados:
    #é um construtor(em python é o q se tem mais próximo de um construtor)
    def __init__(self):
        self.__dados = {}
        #Por convenção do python, se um atributo estiver com um underline(_) na frente do nome, o python recomenda que não acesse o atributo.


    @property
    def dados(self):
        return self.__dados
    #Para obter dados #Estou fazendo um metodo da classe parecer uma propriedade da classe




    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})
            #atualizando o dicionario que foi criado
            #update([other]) -> atualiza o dicionario com os pares chave/valor existente em other, sobrescrevendo chaves existentes.


    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)


    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_cliente(1, 'Rafa')
bd.inserir_cliente(2, 'Brendo')
bd.__dados = 'Outra coisa' #Dessa vez não vai quebrar mminha classe porque ao colorar duas underlines, o python cria um novo atributo com o nome dados
#mas aquele atributo da classe estpa protegido
print(bd.__dados) #Outra coisa
#Criei esse atributo __dados ali em cima e o acessei.
print(bd._BaseDeDados__dados) #{'clientes': {1: 'Rafa', 2: 'Brendo'}}
#Esse é o jeito para acessar o meu atributo da classe
#instancia. + _Nome da classe +__Nome do atributo(real)
#bd.dados = 'Outro valor' #AttributeError: can't set attribute 'dados' #Precisaria do set para mudar esse atributo.
print(bd.dados) #Por causa do getter, eu consigo agora obter os dados assim...


#bd.lista_clientes()



"""bd.inserir_cliente(2, 'Brendo')
bd.inserir_cliente(3, 'Rute')
#print(bd._dados) #Posso acessar o atributo assim... Porque ele é um private mais "fraco"
bd.__dados = 'Um outro valor qualquer' #quebrei de novo"""

"""bd.inserir_cliente(1, 'Rafa')
bd.inserir_cliente(2, 'Brendo')
bd.inserir_cliente(3, 'Rute')
#bd.dados = 'Uma outra coisa' #vai quebrar a classe inteira com isso #o dicionario virou um string assim. Por isso que quebrou
#isso porque o dados eé publico
bd.inserir_cliente(4, 'Rossi')
#bd.apaga_cliente(2)
bd.lista_clientes()"""



