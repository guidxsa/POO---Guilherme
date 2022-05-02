n = int(input('Digite o tamanho da lista: '))

p = []

pont = int(input('Digite a pontuação: '))
p.append(pont)

v_max = pont
v_min = pont

p_max = 0
p_min = 0


for i in range (n - 1):
    pont = int(input('Digite a pontuação: '))
    p.append(pont)

    if v_max < pont:
        v_max = pont
        p_max += 1

    if v_min > pont:
        v_min = pont
        p_min += 1

print('p_max = {} e p_min = {}'.format(p_max, p_min))