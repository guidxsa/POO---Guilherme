def converte(bytes):
    for i in range(len(bytes)):
        bytes[i] = (bytes[i] * 9.537) / 10 ** 7

with open ('usuarios.csv', 'r') as arq:
    arq.readline()
    linhas = arq.readlines()

lista_bytes = []
lista_pessoas = []
for i in range(len(linhas)):
    lista_bytes.append(linhas[i][linhas[i].find(';') + 1:])
    lista_bytes[i] = lista_bytes[i].replace('\n', '')
    lista_bytes[i] = int(lista_bytes[i])
    lista_pessoas.append(linhas[i][0:linhas[i].find(';')])


converte(lista_bytes)

total = sum(lista_bytes)

with open ('relatorio.txt', 'w') as arq_novo:
    arq_novo.write('Usuario\t\t\tEspaco utilizado\t\t% do uso\n')
    for i in range (len(linhas)):
        arq_novo.write('{}\t'.format(i+1) + lista_pessoas[i] + '\t\t\t{:.2f}MB\t\t\t'.format(lista_bytes[i]) + '{:.2f}%\n'.format(100 * lista_bytes[i]/total))
    arq_novo.write('\n\n' + 'Espaco total ocupado: {:.2f}MB\n'.format(total))
    arq_novo.write('Espaco medio ocupado: {:.2f}'.format(total / len(lista_pessoas)))