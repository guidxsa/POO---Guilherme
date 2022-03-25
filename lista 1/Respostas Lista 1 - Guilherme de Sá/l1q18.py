n = int(input('Digite o número de termos da série: '))
numerador = 1
soma = 0

print('S =',end=' ')

for numerador in range(1, n + 1):
    m = 2 * numerador - 1

    soma += (numerador / m)

    print('(',end='')
    print(numerador,'/', m, end='')
    print(')',end='')
    
    if numerador < n:
        print(' + ', end='')

print(' =', soma)