with open ('votos.txt', 'r') as arq:
    linhas = arq.readlines()

dict = {1: 'Goku', 2: 'Vegeta', 3: 'Gohan', 4: 'Broly', 5: 'Freeza'}

for i in range (len(linhas)):
    linhas[i] = linhas[i].replace('\\n', '')
    linhas[i] = int(linhas[i])

lista_modal = [linhas.count(1), linhas.count(2), linhas.count(3), linhas.count(4), linhas.count(5)]
lista_nulo = []

for linha in linhas:
    if linha != 1 and linha != 2 and linha != 3 and linha != 4 and linha != 5:
        lista_nulo.append(linha) 

for i in range (5):
    if lista_modal[i] == max(lista_modal):
        mais_votos = i + 1
    if lista_modal[i] == min(lista_modal):
        menos_votos = i + 1
    
print('Candidato mais votado: {} com {} votos'.format(dict[mais_votos], linhas.count(mais_votos)))
print('Candidato menos votado: {} com {} votos'.format(dict[menos_votos], linhas.count(menos_votos)))
print('Quantidade de votos nulos: {}'.format(len(lista_nulo)))