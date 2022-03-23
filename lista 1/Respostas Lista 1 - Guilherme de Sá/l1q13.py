n = int(input('Digite um número inteiro "n": '))
cont = 0

if n > 0:
    while n > 0:
        if n // 100 >= 1:
            n -= 100

        elif n // 50 >= 1:
            n -= 50

        elif n // 10 >= 1:
            n -= 10

        elif n // 5 >= 1:
            n -= 5

        else:
            n -= 1

        cont += 1

    print('A quantidade mínima de notas é ',cont)

else:
    print('Opção inválida!')