n = int(input('Defina o tamanho da lista: '))

pa_1 = 0
pa_2 = 0

l1 = []
l2 = []

for i in range (n):
    nota_1 = int(input('Digite as notas do aluno 1: '))
    l1.append(nota_1)

for i in range (n):
    nota_2 = int(input('Digite as notas do aluno 2: '))
    l2.append(nota_2)

    if l1[i] > l2[i]:
        pa_1 += 1
    
    elif l1[i] < l2[i]:
        pa_2 += 1
    
    else:
        continue

print('O aluno 1 teve {} pontos\nO aluno 2 teve {} pontos'.format(pa_1, pa_2))