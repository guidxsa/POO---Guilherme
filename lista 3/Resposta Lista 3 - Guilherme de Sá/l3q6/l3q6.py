with open('pontuacoes.csv', 'r') as arq:
    lista_nomes = []
    lista_numeros = []

    linha_1 = arq.readline(5)
    removerl1 = arq.readline()
    linhas = arq.readlines()

    for i in range(len(linhas)):
        
        linha_atual = linhas[i]
        nome_atual = linha_atual[0:linha_atual.find(';')]
        numero_atual = linha_atual[linha_atual.find(';') + 1:]
        numero_atual = int(numero_atual.replace('\\n',''))

        lista_nomes.append(nome_atual)
        lista_numeros.append(numero_atual)

lista = []
lista_list =  []
conjunto = set()

for j in range(len(linhas)):

    for k in range(len(linhas)):
        if lista_nomes[j] == lista_nomes[k]:
            conjunto.add(lista_numeros[j])
            conjunto.add(lista_numeros[k])
    lista.append(conjunto)
    lista_list.append(list(lista[j]))
    conjunto.clear()
        

for l in range(len(lista_list)):
    lista_list[l] = max(lista_list[l])

dict = {}

for m in range(len(lista_list)):
    dict[lista_nomes[m]] = lista_list[m]

tuple_dict = tuple(dict)
valores = []

for n in range (len(tuple_dict)):
    valores.append(dict.get(tuple_dict[n]))

with open('maiores_pontuacoes.csv','w') as arq_novo:
    arq_novo.write(linha_1 + 'maior pontuacao\n')
    for o in range (len(tuple(dict))):
        arq_novo.write(tuple_dict[o] + ';' + str(valores[o]) + '\n')