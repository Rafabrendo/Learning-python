
#caminho_windows = r'c:\programas\seilá'
#geralmente se coloca um r' atras do string para que não se tenha problemas com as barras invertidas. No windows.
##para que o windows não tente executar as barras

import os
import shutil
#shutil ->é o modulo que vai mover e copiar os arquivos

#é só colocar um r para não executar as barras. Ou posso invertelas.
caminho_original = r'C:\Users\rafal\Desktop\area de trabalho 2'
caminho_novo = r'C:\Users\rafal\Desktop\area de trabalho 3'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta \"{caminho_novo}\' já existe.')
    #Se eu não quiser exibir nada, é só dar um pass

for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        old_file_path = os.path.join(root, file)
        #vou juntar a raiz com o nome do arquivo -> vai me dar o caminho completo de cada arquivo
        new_file_path = os.path.join(caminho_novo, file)
        #vou juntar o caminho_novo(nova pasta) com o arquivo. #É um novo caminho que eu vou mover o arquivo

        # ATENÇÃO!
        # shutil.move(old_file_path, new_file_path)
        # vou mover o arquivo da antiga pasta para a nova pasta
        # print(f'Arquivo {file} movido com sucesso!')

        #if '.txt' in file:
        #Se exister str no final do arquivo, eu o copio
        #    shutil.copy(old_file_path, new_file_path)
        #    print(f'Arquivo {file} copiado com sucesso!')

        #Atenção ao apagar arquivos porque, aqui no python, não tem volta

        if '.txt' in  file:
            os.remove(new_file_path)
            print('Arquivo(s) apagados')

#root(raiz, 'caminho'), dirs(diretorio), file(arquivo)
