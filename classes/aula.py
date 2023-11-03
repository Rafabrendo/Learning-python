#Se fosse um nome composto, a primeira letra, do primeiro nome é maiuscula, e a primeiro letra, dos outros nomes tbm

from pessoa import Pessoa

#instanciando
#p1 = Pessoa()
#p2 = Pessoa()

#p1 não é igual a p2. Eu estou instanciando, criando um objeto a partir de uma classe. Estou utilizando apenas um molde
#para criar uma pessoa, que tem os mesmos atributos, mas não é a mesma coisa

"""
#Geralmente não se utiliza assim
p1.nome = 'Rafa' #Eu fiz um atributo aqui 
p2.nome = 'Brendo'
print(p1.nome)"""

#p1.falar() #objeto.função

#p1 = Pessoa('Rafa', 24)
#O self não precisa ser enviado porque ele já enviado automaticamente pelo python
#Isso é a mesma coisa de fazer:
#p1.nome = 'Rafa'
#p1.idade = 24
#p2 = Pessoa('Brendo', 24)
#comendo e falando podem ser mandados, mas não precisam. Porque já se tem valores padrão

#p1.outro_metodo()
#p1.comer('maçã') #Rafa está comendo maçã.
#p1.comer('maçã') #Rafa já está comendo.

#p1.comer('maçã') #Rafa está comendo maçã.
#p1.parar_comer() #Rafa parou de comer.
#p1.parar_comer() #Rafa não está comendo.
#p1.comer('maçã') #Rafa está comendo maçã.


"""p1.comer('maçã') #Rafa está comendo maçã.
p1.falar('POO') #Rafa não pode falar comendo.
p1.parar_comer() #Rafa parou de comer.
p1.falar('POO') #Rafa está falando sobre POO.
p1.comer('alimento') #Rafa não pode comer falando.
p1.parar_falar() #Rafa parou de falar.
p1.falar('Assunto') #Rafa está falando sobre Assunto."""

p1 = Pessoa('Rafa', 25)
p2 = Pessoa('Brendo', 25)

p1.falar('POO')
p2.comer('Sorvete')
p2.falar('Filmes')
p1.comer('churrasco')

print(p1.ano_atual) #Os objetos vão poder ter acesso a variavel da classe #2022
print(p2.ano_atual) #2022
print(Pessoa.ano_atual) #A classe tbm #2022
print(p1.get_ano_nascimento()) #1998
print(p2.get_ano_nascimento()) #1998


