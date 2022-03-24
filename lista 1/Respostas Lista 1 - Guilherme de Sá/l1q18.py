n = int(input('Digite o número de termos da série: '))
aux = 1
soma = 0

print('S =',end=' ')
while aux <= n:
    m = 1 if aux == 1 else aux + 2
    soma += aux / n
    print('(',end='')
    print(aux,'/', m, end='')
    print(')',end='')
    
    if aux < n:
        print(' + ', end='')

    aux += 1

print(' =', soma)

