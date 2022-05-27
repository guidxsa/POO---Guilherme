with open ('votos.txt', 'w') as arq:
    pass

parar = 0
nulo = 0
arq = open ('votos.txt', 'a')
while True:
    if parar != 1:
        ultimo_voto = int(input('\tENQUETE DRAGON BALL\n\n1 - Goku\n2 - Vegeta\n3 - Gohan\n4 - Broly\n5 - Freeza\n\nVote no seu personangem favorito de Dragon Ball: '))
        arq.write(str(ultimo_voto) + '\n')
        parar = int(input('Deseja parar? Caso deseje, digite 1: '))
        if ultimo_voto != 1 and ultimo_voto != 2 and ultimo_voto != 3 and ultimo_voto != 4 and ultimo_voto != 5:
            nulo += 1
    else:
        arq.close()
        break

with open ('votos.txt', 'r') as arq:
    linhas = arq.readlines()

dict = {}
dict[1] = 'Goku'
dict[2] = 'Vegeta'
dict[3] = 'Gohan'
dict[4] = 'Broly'
dict[5] = 'Freeza'

print(linhas)

for i in range (len(linhas)):
    linhas[i] = linhas[i].replace('\\n', '')
    linhas[i] = int(linhas[i])

lista_modal = [linhas.count(1), linhas.count(2), linhas.count(3), linhas.count(4), linhas.count(5)]

print(lista_modal)

for i in range (5):
    if lista_modal[i] == max(lista_modal):
        mais_votos = i + 1
    if lista_modal[i] == min(lista_modal):
        menos_votos = i + 1
    
print('Candidato mais votado: {} com {} votos'.format(dict[mais_votos], linhas.count(mais_votos)))
print('Candidato menos votado: {} com {} votos'.format(dict[menos_votos], linhas.count(menos_votos)))
print('Quantidade de votos nulos: {}'.format(nulo))


