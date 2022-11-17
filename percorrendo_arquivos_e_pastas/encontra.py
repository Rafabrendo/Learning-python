from utils import formata_tamanho
import os

#caminho_procura = 'C:Users/rafal/Desktop/pasta'
caminho_procura = input('Digite um caminho: ')
#termo_procura = ''
termo_procura = input('Digite um termo: ')



#tive que usar as barras invertidas
#Vou utilizar um modulo walk que tem no os para passar por cada sub-pasta dentro da minha pasta.
#Para isso eu tenho que utilizar o for
#no python utiliza-se o barra(/) para caminhos, ao invés de barra invertida(\)
conta = 0
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    #o arquivos retornou uma lista. Daí eu fiz outro for para desempacotar a lista
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo) #Estou mandando a pasta e o nome do arquivo
                #print(caminho_completo) #Ex.: C:Users/rafal/Desktop/pasta\09\texto.txt
                #print(arquivo)
                #nome_arquivo, ext_arquivo = os.path.splitext(caminho_completo)
                #print(nome_arquivo, ext_arquivo) #C:Users/rafal/Desktop/pasta\09\texto .txt
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                #print(nome_arquivo, ext_arquivo, sep='---') #ex.: texto---.txt
                tamanho = os.path.getsize(caminho_completo)
                #print(tamanho) #ex.:4 -> vai retornar o tamanho do arquivo em bits
                #print(arquivo)  #09.txt
                #só vai pegar os arquivos que tem 09 no nome. Independente do formato.

                print()
                print('Encontrei o arquivo: ', arquivo)
                print('Caminho: ', caminho_completo)
                print('Nome: ', nome_arquivo)
                print('Extensão: ', ext_arquivo)
                print('Tamanho: ', formata_tamanho(tamanho))
            except PermissionError as e:
                print("Sem permissão neste arquivo.")
            except FileNotFoundError as e:
                print("Arquivo não encontrado.")
            except Exception as e:
                print("Erro desconhecido: ", e)


print()
print(f'{conta} arquivo(s) enonctrados(s).')