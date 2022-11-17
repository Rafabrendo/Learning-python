class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []
        #A lista vai receber objetos da classe endereço
        #"primeiro foi associação, passei Enderecos como atributo. Dps eu fiz metodos que usam a outra classe(agregação)
        #obs.: Esses metodos não existem sem a outra classe, por isso: composição
        # Usei a classe Endereco para compor um Cliente. Se a classe Cliente é apagado da memoria, todos os endereços que pertencem
        # a ele, serão apagados da memoria"


    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))
        #Estou chamando("instanciando") a classe Endereco


    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)


    def __del__(self):
        print(f'{self.nome} FOI APAGADO.')



class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado


    def __del__(self):
        print(f'{self.cidade}/{self.estado} FOI APAGADO')





