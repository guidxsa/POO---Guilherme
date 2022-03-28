n = int(input('Digite o número que deseja saber a raiz quadrada: '))
a = int(input('Digite uma aproximção a0 da raiz quadrada desse número: '))

if n < 0:
    print('Valor inválido de n')

elif a <= 0:
    print('Valor inválido de a0')

else:
    x = a ** 2 - n

    if x < 0:
        x = -x


    while x > 0.0001:
        a = (a + (n / a)) / 2
        x = a ** 2 - n
    
        if x < 0:
            x = -x

    print('A raiz quadrada de {} é {}'.format(n, a))