def copia_texto(texto, texto_cop):
    with open ('texto.txt', 'r') as texto:
        linhas = texto.readlines()
    with open ('texto_cop.txt', 'w') as texto_cop:
        
        conteudo = ''
        for i in range(len(linhas)):
            if linhas[i].find('#') != 0:
                conteudo += linhas[i]
        
        texto_cop.write(conteudo)

with open ('texto.txt', 'r') as texto:
    pass

with open ('texto_cop.txt', 'w') as texto_cop:
    pass

copia_texto(texto, texto_cop)