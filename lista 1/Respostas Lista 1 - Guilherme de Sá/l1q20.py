n = int(input('Digite um número de 5 dígitos: '))

for i in range(5, 0, -1):
    if i == 5:
        digito = n // 10 ** (i - 1)
        digito1 = digito
        continue
    
    digito = (n % 10 ** i) // 10 ** (i-1)

    if i == 4:
        digito2 = digito
    
    elif i == 3:
        digito3 = digito
    
    elif i == 2:
        digito4 = digito
    
    elif i == 1:
        digito5 = digito

if digito1 == digito5 and digito2 == digito4:
    print('O número {} é palíndromo!'.format(n))

else:
   print('O número {} não é palíndromo!'.format(n))