
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)


    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
        #vai chamar o __init__() e passar nome e idade
        #Essa variavel só vai estar disponivel aqui! Dentro do escopo desse metodo
        #como o parametro é cls, significa que vou ter acesso a variavel ano_atual
        #posso usar cls ou quer outro nome de minha preferencia, menos o self(que faz referencia a instancia)
        #cls se refere a classe Pessoa
    #cls() -> estou chamando a classe(executando)
    #É um metodo de classe que vai retornar a propria classe, com o nome e idade, baseado nos parametros que foram enviados.
    #Estou criando um objeto




"""p1=Pessoa('Rafa', 24)
p1.get_ano_nascimento()
print(Pessoa.ano_atual) #ano_atual é um atributo da classe"""

#p1 = Pessoa('Rafa', 25)
#p1 = Pessoa.por_ano_nascimento('Rafa', 1997) #Estou criando um objeto Pessoa
p1 = Pessoa('Rafa', 32) #Estou instanciando um objeto
print(p1)

print(p1.nome, p1.idade)
p1.get_ano_nascimento()