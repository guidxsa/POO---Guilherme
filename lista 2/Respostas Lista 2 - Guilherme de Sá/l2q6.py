def transp(n, m):
    matriz = []
    matriz_t = []


    for i in range (n):
        l = []
        for j in range (m):
            termo = int(input('Digite o termo [{},{}]: '.format(i+1, j+1)))
            l.append(termo)
        matriz.append(l)

    for i in range (n):
        l_t = []
        for j in range (m):
            termo = matriz[j][i]
            l_t.append(termo)
        matriz_t.append(l_t)

    return matriz_t
    
n = int(input('Digite quantas linhas sua matriz tem: '))
m = int(input('Digite quantas colunas sua matriz tem: '))

matriz_t = transp(n,m)

for l in range(n):
    print('[', end = ' ')
    for c in range(m):
        print(matriz_t[l][c], end = ' ')
    print(']', end = '')
    print()