"""
Associação -> Uma classe vai estar relacionada("conversando") a outra mas nenhuma delas vai depender da outra, ou seja,
elas são independentes
-> Uma associação ocorre quando uma classe possui atributos do tipo de outra classe.
"""

from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Rafildes')
#print(escritor.nome) #Para chamar um getter

caneta = Caneta('Bic')
#print(caneta.marca)

maquina = MaquinaDeEscrever()
#print(maquina) #<classe.MaquinaDeEscrever object at 0x00000183FBBBB190>  -> numero na memoria


"""print(escritor.nome)
print(caneta.marca)
maquina.escrever()

nesse caso as três são independentes"""


#Associação:
#ferramenta é um setter da classe escritor
escritor.ferramenta = maquina
escritor.ferramenta.escrever()  #escrever é um metodo da classe MaquinaDeEscrever

#Criamos um escritor, uma maquina de escrever e uma ferramenta.
#escritor.ferramenta = maquina -> estou falando q a ferramenta vai receber o objeto inteiro, nesse caso a maquina
#Estou mandando a classe toda para ferramenta. Obs.: Eu tbm poderia fazer com caneta
#passei o objeto maquina(MaquinaDeEscrever) como atributo


del escritor
#print(escritor) #NameError: name 'escritor' is not defined. Did you mean: 'Escritor'?

#mas a caneta continua existindo e a maquina tbm

print(caneta.marca) #Bic
maquina.escrever() #Maquina está escrevendo...
