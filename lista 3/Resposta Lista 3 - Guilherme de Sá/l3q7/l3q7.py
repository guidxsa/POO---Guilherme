def func(nomes, notas):

    with open ('nomes.txt', 'r') as nomes:
        linhas_nomes = nomes.readlines()
        for i in range (len(linhas_nomes)):
            linhas_nomes[i] = linhas_nomes[i].replace('\n', '')
    with open ('notas.txt', 'r') as notas:
        linhas_notas = notas.readlines()
        lista = []
        media = []
        for i in range (len(linhas_notas)):
            lista.append(linhas_notas[i].split())
            for j in range(len(lista[i])):
                lista[i][j] = int(lista[i][j])
            media.append(sum(lista[i])/len(lista[i]))
    with open ('arquivo_final.txt','w') as arq:
        arq.write('nome;media\n')
        for i in range(len(linhas_nomes)):
            arq.write(linhas_nomes[i] + ';' + str(media[i]) + '\n')


with open ('nomes.txt', 'r') as nomes:
    pass

with open ('notas.txt', 'r') as notas:
    pass

func(nomes, notas)