nome_arquivo = input('Digite o nome do arquivo que deseja abrir: ')
palavra_arquivo = input('Digite a palavra que deseja procurar no arquivo: ')

arquivo = open(nome_arquivo, 'r')
conteudo = arquivo.read()

arquivo.close()

ocorrencia = 0
i = 0

while True:
    if conteudo.find(palavra_arquivo, i) != -1:
        i = conteudo.find(palavra_arquivo, i) + len(palavra_arquivo)
        ocorrencia += 1
    else:
        break
        

print('A palavra aparece no arquivo {} vezes'.format(ocorrencia))