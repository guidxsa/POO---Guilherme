n = int(input('Digite um número inteiro "n": '))
restante = n

minimo = 0

if n > 0:

    while restante > 0:
        if restante // 100 >= 1:
            restante -= 100

        elif restante // 50 >= 1:
            restante -= 50

        elif restante // 10 >= 1:
            restante -= 10

        elif restante // 5 >= 1:
            restante -= 5

        else:
            restante -= 1

        minimo += 1

    print('A quantidade mínima de notas para obter R${} é de {}'.format(n, minimo))

else:
    print('Opção inválida!')