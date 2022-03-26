N1 = float(input('Digite sua nota:'))
N2 = float(input('Digite sua nota:'))

media = (N1 + N2)/2

print('Média =', media,'\n')

if media >= 7:
    if media >= 9.5:
        print('Aprovado com Distinção')
    else:
        print('Aprovado')

else:
    print('Reprovado')