n = int(input('Digite o número de termos da série: '))
numerador = 1
soma = 0

print('S =',end=' ')
while numerador <= n:
    m = 2 * numerador - 1

    soma += (numerador / m)

    print('(',end='')
    print(numerador,'/', m, end='')
    print(')',end='')
    
    if numerador < n:
        print(' + ', end='')

    numerador += 1

print(' =', soma)

