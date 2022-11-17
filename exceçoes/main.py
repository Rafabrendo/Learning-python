#Exceções personalizadas -> Criando
#levantando exceção

class TaErradoError(Exception):
    pass
#Essa é uma exceção que eu criei.



def testar():
    raise TaErradoError('Errado!')
    #raise -> levantamento de exceção
    #estou levantando uma exceção que eu criei
    #Ela vai mostrar a mensagem 'Errado!'


try:
    testar()
except TaErradoError as error:
    print(f'Error: {error}')
    #Estou tratando a exceção que eu criei, levantei e estou tratando aqui
    #vai mostrar a msg que eu passei na função