num = int(input('Digite um numero inteiro: '))

if num >= 0:

    fatorial = 1

    #print('{}! = '.format(num), end=' ') Quando digitava 0, printava (0! =  = 1) //
    print('{}!'.format(num), end=' ')
    
    for i in range(num, 0, -1):
        if i == num:
            print('=',end=' ') #Para printar (0! = 1)

        fatorial *= i

        print(i, end=' ')

        if i > 1:
            print('*', end=' ')

    print('= {}'.format(fatorial))

else:
    print('Valor inválido!') 