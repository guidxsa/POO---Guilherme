with open('nomes.txt','r') as arq:
    linhas = arq.readlines()

linhas.sort()

with open('nomes_ordenados.txt','w') as arq_novo:
    for i in range (len(linhas)):
        arq_novo.write(linhas[i])