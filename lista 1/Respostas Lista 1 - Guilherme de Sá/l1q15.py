num = int(input('Digite um numero inteiro: '))

if num >= 0:

    aux = num
    fatorial = 1

    print(num, end='')
    print('! =', end=' ')
    
    while aux > 0:
        fatorial *= aux

        print(aux, end=' ')
        
        aux -= 1
        if aux > 0:
            print('*', end=' ')
        else:
            print('=', end= ' ')
            

    print(fatorial)

else:
    print('Valor inválido!') 