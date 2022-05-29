import os

dir = input('Digite o caminho do diretório da pasta:')


'''with open (os.chdir(dir), 'r') as texto:
    pass'''

pasta = os.chdir(dir)
conteudo = os.listdir(pasta)

print('O conteudo é:\n\n{}'.format(conteudo))