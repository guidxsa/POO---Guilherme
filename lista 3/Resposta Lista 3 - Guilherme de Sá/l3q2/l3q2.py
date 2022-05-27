arq = open('nomes.txt','r')
linhas = arq.readlines()
arq.close()

linhas.sort()

arq_novo = open('nomes_ordenados.txt','w')

i = 0
for i in range (len(linhas)):
    arq_novo.write(linhas[i])
arq_novo.close()

arq_novo = open('nomes_ordenados.txt','r')
conteudo_ordenado = arq_novo.read()
arq_novo.close()

print('O conteudo novo é:\n{}'.format(conteudo_ordenado))